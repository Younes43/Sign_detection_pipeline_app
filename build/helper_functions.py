from tkinter import filedialog
from pathlib import Path
import tkintermapview
import tkinter
import shutil

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = Path(__file__).resolve().parent / "assets" / "frame0"

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def upload_video(video_path):
    filetypes = [("Video files", ".mp4 .avi .mov .mkv"), ("All files", "*.*")]
    filepath = filedialog.askopenfilename(title="Select a Video", filetypes=filetypes)
    if filepath:
        video_path.delete(0, 'end')
        video_path.insert(0, filepath)

def upload_gps(gps_path):
    filetypes = [("CSV files", "*.csv"), ("All files", "*.*")]
    filepath = filedialog.askopenfilename(title="Select a CSV", filetypes=filetypes)
    if filepath:
        gps_path.delete(0, 'end')
        gps_path.insert(0, filepath)

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
    
    
def run_pipeline(window):
    """
    Placeholder function for running the processing pipeline.
    This function will be responsible for processing the data and producing results.
    For now, it will simply print a statement.
    """
    print("Running the processing pipeline...")
    plot_folium_map_embedded(window)
