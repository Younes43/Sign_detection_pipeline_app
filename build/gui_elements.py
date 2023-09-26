from tkinter import Canvas, Entry, Button, PhotoImage
from helper_functions import relative_to_assets, upload_video, download_video, download_map, run_pipeline

def setup_gui_elements(window):
        
    window.geometry("1190x629")
    window.configure(bg = "#3A7FF6")


    canvas = Canvas(
        window,
        bg = "#3A7FF6",
        height = 629,
        width = 1190,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_rectangle(
        348.0,
        0.0,
        1190.0,
        629.0,
        fill="#FCFCFC",
        outline="")

    canvas.create_text(
        384.0,
        170.0,
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
        command=lambda : run_pipeline(window,directory_path_widget),
        relief="flat"
    )
    run_pipeline_btn.place(
        x=75.0,
        y=545.0,
        width=180.0,
        height=55.0
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
        x=480.0,
        y=575.0,
        width=180.0,
        height=24.0
    )

    canvas.button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    download_map_btn = Button(
        image=canvas.button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=download_map,
        relief="flat"
    )
    download_map_btn.place(
        x=885.0,
        y=575.0,
        width=180.0,
        height=24.00006103515625
    )

    canvas.create_text(
        31.0,
        20.0,
        anchor="nw",
        text="Curve Sign Pipeline",
        fill="#FCFCFC",
        font=("Roboto Bold", 32 * -1)
    )

    canvas.create_text(
        20.0,
        114.20878601074219,
        anchor="nw",
        text="Upload Video",
        fill="#FCFCFC",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_text(
        702.0,
        20.0,
        anchor="nw",
        text="Results",
        fill="#505485",
        font=("Roboto Bold", 24 * -1)
    )

    canvas.create_text(
        380.0,
        58.0,
        anchor="nw",
        text="Logs",
        fill="#505485",
        font=("Roboto Bold", 16 * -1)
    )

    canvas.create_rectangle(
        27.0,
        215.0,
        328.0,
        220.0,
        fill="#FCFCFC",
        outline="")

    canvas.entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        768.5,
        123.5,
        image=canvas.entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D6DAE6",
        fg="#000716",
        highlightthickness=0
    )
    entry_1.place(
        x=386.0,
        y=85.0,
        width=765.0,
        height=75.0
    )

    canvas.entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        174.0,
        164.0,
        image=canvas.entry_image_2
    )
    directory_path_widget = Entry(
        bd=0,
        bg="#F1F5FF",
        fg="#000716",
        highlightthickness=0
    )
    directory_path_widget.place(
        x=32.0,
        y=146.0,
        width=284.0,
        height=34.0
    )

    canvas.button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    upload_video_btn = Button(
        image=canvas.button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: upload_video(directory_path_widget),
        relief="flat"
    )
    upload_video_btn.place(
        x=286.0,
        y=153.0,
        width=24.0,
        height=22.0
    )

    # canvas.create_text(
    #     20.0,
    #     242.0,
    #     anchor="nw",
    #     text="Upload GPS Coordinates",
    #     fill="#FCFCFC",
    #     font=("Roboto Bold", 16 * -1)
    # )

    # canvas.entry_image_3 = PhotoImage(
    #     file=relative_to_assets("entry_3.png"))
    # entry_bg_3 = canvas.create_image(
    #     174.0,
    #     299.0,
    #     image=canvas.entry_image_3
    # )
    # gps_path = Entry(
    #     bd=0,
    #     bg="#F1F5FF",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # gps_path.place(
    #     x=32.0,
    #     y=281.0,
    #     width=284.0,
    #     height=34.0
    # )

    # canvas.button_image_5 = PhotoImage(
    #     file=relative_to_assets("button_5.png"))
    # upload_gps_btn = Button(
    #     image=canvas.button_image_5,
    #     borderwidth=0,
    #     highlightthickness=0,
    #     command=lambda: upload_gps(gps_path),
    #     relief="flat"
    # )
    # upload_gps_btn.place(
    #     x=286.0,
    #     y=288.0,
    #     width=24.0,
    #     height=22.0
    # )

    canvas.create_rectangle(
        480.0,
        195.0,
        1065.0,
        550.0,
        fill="#D9D9D9",
        outline="")