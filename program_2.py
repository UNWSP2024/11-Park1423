##
# --Program 2--
# By Parker Jolly
# Desc: A program to make a simple window where you can push a button to quit or see some info
# Notes: Not giving my real address.
##

import tkinter as tk


def main():
    # Create GUI
    quoteGUI = GUI("""
    Name: Parker Jolly
    Address: 221b Baker St """)

class GUI:

    def __init__(self,info):
        # Create main window
        self.main_window = tk.Tk()
        self.main_window.title("Quote")
        
        # Create and pack frames
        self.top_frame = tk.Frame(self.main_window)
        self.bottom_frame = tk.Frame(self.main_window)
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        # Create info variable and info label
        self.info = info
        self.infoLabelValue = tk.StringVar()
        self.info_label = tk.Label(self.top_frame, textvariable=self.infoLabelValue)

        # Create info and quit buttons
        self.show_info_button = tk.Button(self.bottom_frame, text="Show Info", command=self.show_info)
        self.quit_button = tk.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the label and buttons
        self.info_label.pack(side="top")
        self.show_info_button.pack(side="left")
        self.quit_button.pack(side="left")

        tk.mainloop()
    
    # Set our label variable to the info supplied
    def show_info(self):
        self.infoLabelValue.set(self.info)

if __name__ == "__main__":
    main()
