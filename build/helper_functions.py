from tkinter import filedialog
from pathlib import Path
import tkintermapview
import tkinter as tk
import shutil
import time
import requests
import os
import zipfile
import pandas as pd
from PIL import Image, ImageTk

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame0"

BASE_URL = "http://128.61.129.196:8004"
images_dict={}
output_folder='2022_10_20_16_08_11_578'

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def displayFolderPath(directory_path_widget):
    directory = filedialog.askdirectory(title="Select a Directory")
    if directory:
        directory_path_widget.delete(0, 'end')
        directory_path_widget.insert(0, directory)


def format_size(bytes_size):
    """Format bytes size to string."""
    if bytes_size < 1024:
        return f"{bytes_size}B"
    elif bytes_size < 1024 * 1024:
        return f"{bytes_size / 1024:.2f}KB"
    elif bytes_size < 1024 * 1024 * 1024:
        return f"{bytes_size / (1024 * 1024):.2f}MB"
    else:
        return f"{bytes_size / (1024 * 1024 * 1024):.2f}GB"

def download_with_progress(response, filename):
    total_size = int(response.headers.get('content-length', 0))
    block_size = 1024  # 1 Kibibyte
    wrote = 0
    with open(filename, 'wb') as f:
        for data in response.iter_content(block_size):
            wrote += len(data)
            f.write(data)
            print(f"Downloaded {format_size(wrote)} of {format_size(total_size)} - {round((wrote / total_size) * 100, 2)}%", end='\r')
    print()  # Go to the next line after the download completes
    
def unzip_with_progress(zip_filename):
    # Extract the directory name from the zip filename (removing .zip)
    output_directory = os.path.splitext(zip_filename)[0]
    
    # Create the directory
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with zipfile.ZipFile(zip_filename, 'r') as zip_ref:
        total_files = len(zip_ref.namelist())
        for i, member in enumerate(zip_ref.infolist(), start=1):
            zip_ref.extract(member, path=output_directory)
            print(f"Extracting {i}/{total_files}: {member.filename}")
               
def process_video(folder_path):
    global output_folder
    print('Started Uploading data to Server')
    
    directory = folder_path.get()

    # Prepare the data for the /upload_folder endpoint
    folder_name = os.path.basename(directory)
    all_files = [os.path.join(dp, f) for dp, dn, filenames in os.walk(directory) for f in filenames if os.path.isfile(os.path.join(dp, f))]
    
    # Prepare files for upload
    upload_files = []
    file_paths_list = []
    for i, file in enumerate(all_files):
        relative_path = os.path.join(folder_name,os.path.relpath(file, directory))  # Get the relative path
        upload_files.append(('files', (relative_path, open(file, 'rb'))))  # Tuple ('name', (filename, fileobj))
        file_paths_list.append(relative_path)
        
    data = {'inputFolder': folder_name, 'filePaths': file_paths_list}

    # Send request
    response = requests.post(f"{BASE_URL}/upload_folder", data=data, files=upload_files)

    # Close all the opened files
    for _, (_, file_obj) in upload_files:
        file_obj.close()

    if response.status_code != 200:
        raise Exception(f"Failed to upload folder: {response.text}")

    data = response.json()

    # Call the /process_video endpoint
    print("Sending dataset_path:", data["folderPath"])
    response = requests.post(f"{BASE_URL}/process_video", json={"dataset_path": data["folderPath"]})
    print('Started Processing Video')
    # print(response.content)
    if not response.ok:
        raise Exception(f"Failed to trigger processing: {response.text}")
    task_data = response.json()

    task_id = task_data["task_id"]
    dataset_name = task_data["dataset_name"]
    output_folder=dataset_name
    # Check task status every few seconds
    while True:
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        task_status_data = response.json()

        if task_status_data["task_status"] == "SUCCESS":
            # Download zip
            print('Pipeline task finnished')
            # tk.messagebox.showinfo("Info", "Pipeline processing task finished")
            print('Started Downloading data from Server')
            print('...')
            zip_filename = f"{dataset_name}.zip"
            extracted_folder = os.path.splitext(zip_filename)[0]

            # Download zip with progress
            if not os.path.exists(zip_filename):
                print("Downloading ZIP file:")
                response = requests.get(f"{BASE_URL}/download_results/{dataset_name}", stream=True)
                download_with_progress(response, zip_filename)
            else:
                print("ZIP file already exists. Skipping download.")

            # Unzip the file in place
            if not os.path.exists(extracted_folder):
                print("Unzipping the file:")
                unzip_with_progress(zip_filename)
            else:
                print("Files already extracted. Skipping unzip step.")
            
            tk.messagebox.showinfo("Info", "Pipeline finished and results downloaded!")
            break
        elif task_status_data["task_status"] in ["FAILURE", "REVOKED"]:
            tk.messagebox.showerror("Error", "Processing failed!")
            break
        time.sleep(5)
    
    

    
    return response.json()


def download_video():
    source_path = output_folder+"results/demo.mp4"
    # TO BE COMPLETED
    #
    #
    #
    #
    filetypes = [("Video files", ".mp4 .avi .mov .mkv"), ("All files", "*.*")]
    destination_path = filedialog.asksaveasfilename(title="Save Video As", defaultextension=".mp4", filetypes=filetypes)
    
    if destination_path:
        shutil.copy2(source_path, destination_path)
        
        
def update_canvas_text(canvas, item, message):
    """
    Update the text of a canvas item.
    """
    canvas.itemconfig(item, text=message)
    canvas.update()  # Refresh the canvas to reflect changes immediately



# Map Plot
# 
# 
# 
# 
# 
# 
# 
# 


def create_map_markers(map_view, data_path, icon_folder_path):
    data = pd.read_csv(data_path)

    for _, row in data.iterrows():
        sign_type = row['sign_class']
        icon_path = f"{icon_folder_path}/{sign_type}.png"
        if not os.path.exists(icon_path):
            # print(icon_path, ' Not found')
            icon_path = "../icons/Default.png"
            
        if icon_path in images_dict:
            icon_image = images_dict[icon_path]
        else:
            icon_image = ImageTk.PhotoImage(Image.open(icon_path).resize((30, 30)))
            images_dict[icon_path] = icon_image  # Add image to global dictionary
        
        map_view.set_marker(row['latitude'], row['longitude'], icon=icon_image)
        
def compute_avg_coords(data_path):
    data = pd.read_csv(data_path)
    avg_lat = data['latitude'].mean()
    avg_lon = data['longitude'].mean()
    return avg_lat, avg_lon

def plot_map(window):
    print('Started Ploting Map')
    icon_path = "../icons"
    result_table= output_folder+"/result_table.csv"
    
    avg_lat, avg_lon = compute_avg_coords(result_table)
    # Create a map view
    map_view = tkintermapview.TkinterMapView(window, width=1047, height=430)
    map_view.place(x=404, y=242)

    map_view.set_position(avg_lat, avg_lon)  #  Atlanta's coordinates
    map_view.set_zoom(12)# Adjust zoom as needed
    
    # Add traffic sign markers
    create_map_markers(map_view, result_table, icon_path)

    
def check_task_status(task_id):
    while True:
        response = requests.get(f"http://128.61.129.196:8004/tasks/{task_id}")
        if response.status_code == 200:
            status_info = response.json()
            if status_info["task_status"] in ["SUCCESS", "FAILURE"]:
                return status_info
            time.sleep(10)  # wait for 10 seconds before checking again
        else:
            print("Error checking status:", response.text)
            return None 