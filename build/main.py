import tkinter as tk
from gui_elements import setup_gui_elements

if __name__ == "__main__":
    window = tk.Tk()
    setup_gui_elements(window)
    window.resizable(False, False)
    window.mainloop()
