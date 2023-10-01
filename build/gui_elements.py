from tkinter import Canvas, Entry, Button, PhotoImage
from helper_functions import relative_to_assets, displayFolderPath, download_video, plot_map, process_video

def setup_gui_elements(window):
        
    window.geometry("1485x752")
    window.configure(bg = "#3A7FF6")


    canvas = Canvas(
        window,
        bg = "#3A7FF6",
        height = 752,
        width = 1485,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        363.0,
        0.0,
        1485.0,
        752.0,
        fill="#FCFCFC",
        outline="")

    canvas.create_text(
        404.0,
        205.0,
        anchor="nw",
        text="Map",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )
    
    canvas.button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    run_pipeline_btn = Button(
        image=canvas.button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda : process_video(directory_path_widget),
        relief="flat"
    )
    run_pipeline_btn.place(
        x=59.0,
        y=650.0,
        width=225.0,
        height=66.0
    )

    canvas.button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    download_video_btn = Button(
        image=canvas.button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=download_video,
        relief="flat"
    )
    download_video_btn.place(
        x=1027.0,
        y=683.0,
        width=280.0,
        height=45.0
    )

    canvas.button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    download_map_btn = Button(
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda :plot_map(window),
        relief="flat"
    )
    download_map_btn.place(
        x=514.0,
        y=683.0,
        width=283.18170166015625,
        height=45.054443359375
    )

    canvas.create_text(
        38.68487548828125,
        23.910972595214844,
        anchor="nw",
        text="Curve Sign Pipeline",
        fill="#FCFCFC",
        font=("Roboto Bold", 32 * -1)
    )

    canvas.create_text(
        24.957977294921875,
        136.63723754882812,
        anchor="nw",
        text="Upload Video",
        fill="#FCFCFC",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        876.0252075195312,
        23.910972595214844,
        anchor="nw",
        text="Results",
        fill="#505485",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_text(
        404.0,
        69.0,
        anchor="nw",
        text="Logs",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_rectangle(
        34.0,
        257.0,
        309.0,
        263.0,
        fill="#FCFCFC",
        outline="")

    canvas.entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        927.5,
        148.0,
        image=canvas.entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D6DAE6",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=416.0,
        y=102.0,
        width=1023.0,
        height=90.0
    )

    canvas.entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        178.0,
        196.5,
        image=canvas.entry_image_2
    )
    directory_path_widget = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    directory_path_widget.place(
        x=37.0,
        y=175.0,
        width=282.0,
        height=41.0
    )

    canvas.button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    upload_video_btn = Button(
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: displayFolderPath(directory_path_widget),
        relief="flat"
    )
    upload_video_btn.place(
       x=288.0,
        y=184.0,
        width=29.9495849609375,
        height=26.30206298828125
    )

    canvas.create_rectangle(
        404.0,
        242.0,
        1451.0,
        672.0,
        fill="#D9D9D9",
        outline="")
    
