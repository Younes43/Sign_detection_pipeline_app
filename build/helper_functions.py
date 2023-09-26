from tkinter import filedialog
from pathlib import Path
import tkintermapview
import tkinter
import shutil
import time
import requests
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame0"

BASE_URL = "http://128.61.129.196:8004"



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)



def upload_files_to_gpu(input_folder, filepaths):
    """Upload files to the server using FastAPI endpoint."""
    
    url = BASE_URL+"/upload_folder"
    file_objects = []

    relative_paths = [os.path.relpath(filepath, input_folder) for filepath in filepaths if os.path.isfile(filepath) and not os.path.basename(filepath).startswith('.')]

    for filepath in filepaths:
        if not os.path.isfile(filepath):  # Make sure it's a file and not a directory or other entity
            continue
        # Exclude certain files like .python_history or other hidden/system files
        if os.path.basename(filepath).startswith('.'):
            continue

        # Prepare file path and name for sending without opening it yet
        file_objects.append((filepath, os.path.relpath(filepath, input_folder)))

    # Prepare the files to send with the request
    send_files = [("files", (rel_path, open(filepath, "rb"))) for filepath, rel_path in file_objects]

    # Adding input folder name
    data = {
        "inputFolder": os.path.basename(input_folder),
        "filePaths": relative_paths
    }
    
    response = requests.post(url, files=send_files, data=data)

    # Close the files after sending the request
    for _, file in send_files:
        file[1].close()

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to upload files with status code {response.status_code}: {response.text}")
        return None

def upload_video(directory_path_widget):
    directory = filedialog.askdirectory(title="Select a Directory")
    if directory:
        directory_path_widget.delete(0, 'end')
        directory_path_widget.insert(0, directory)

        # Get a list of all files in the directory and subdirectories
        all_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                all_files.append(os.path.join(root, file))
        
        if all_files:
            uploaded_folder = upload_files_to_gpu(directory, all_files)
            return uploaded_folder

# def upload_gps(gps_path):
#     filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
#     filepath = filedialog.askopenfilename(title="Select a CSV", filetypes=filetypes)
#     if filepath:
#         gps_path.delete(0, 'end')
#         gps_path.insert(0, filepath)

def download_video():
    source_path = "path/to/your/video.mp4"
    # TO BE COMPLETED
    #
    #
    #
    #
    filetypes = [("Video files", ".mp4 .avi .mov .mkv"), ("All files", "*.*")]
    destination_path = filedialog.asksaveasfilename(title="Save Video As", defaultextension=".mp4", filetypes=filetypes)
    
    if destination_path:
        shutil.copy2(source_path, destination_path)

def download_map():
    # Path of the map image you want to download
    source_path = "path/to/your/map_image.png"  # or .jpg/.jpeg, etc.
    # To Be completed
    #
    #
    #
    #
    filetypes = [("Image files", ".png .jpg .jpeg"), ("All files", "*.*")]
    destination_path = filedialog.asksaveasfilename(title="Save Map Image As", defaultextension=".png", filetypes=filetypes)
    
    if destination_path:
        shutil.copy2(source_path, destination_path)

def plot_folium_map_embedded(window):
    map_widget  = tkintermapview.TkinterMapView(window, width=585, height=355)
    map_widget.place(x=480, y=195)
    map_widget.set_position(33.774657428070974, - 84.3973542372711)  #  Atlanta's coordinates
    map_widget.set_zoom(15)
    
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
 
def trigger_video_processing(dataset_path):
    response = requests.post("http://128.61.129.196:8004/process_video", json={"dataset_path": dataset_path})
    
    if response.status_code == 201:
        task_info = response.json()
        return task_info["task_id"]
    else:
        print("Error triggering processing:", response.text)
        return None

   
def run_pipeline(window,directory_path_widget):
    print("Running the processing pipeline...")

    directory = directory_path_widget.get()  # Assuming this widget holds the directory path
    dataset_name = os.path.basename(directory)  # Get the name of the folder

    # Trigger the pipeline and get the task_id
    task_id = trigger_video_processing(directory)
    if not task_id:
        print("Failed to trigger processing")
        return

    # Check the status of the task. Here, we're blocking until the task is done.
    # In a more advanced version, you might want to do this check periodically in the background.
    status_info = check_task_status(task_id)
    if status_info["task_status"] == "SUCCESS":
        print("Processing completed successfully!")
        plot_folium_map_embedded(window)  # If you want to display the map after processing is done
    elif status_info["task_status"] == "FAILURE":
        print("Processing failed:", status_info["task_result"])