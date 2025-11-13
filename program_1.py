##
# --Program 1--
# By Parker Jolly
# 11/13/2025
# Desc: A program to make a simple window with an Albert Einstein quote come up.
# Notes: Not sure if he actually said this, but the random website I found said he did.
##

import tkinter as tk


def main():
    # Make GUI
    quoteGUI = GUI("Artificial intellegance is no match for natural stupidity.","-Albert Einstein (Supposedly)")

class GUI:

    def __init__(self,quote,quoted):
        # Create Window and title
        self.main_window = tk.Tk()
        self.main_window.title("Quote")

        # Create the two labels
        self.quote = tk.Label(self.main_window, text=quote)
        self.quoted = tk.Label(self.main_window, text=quoted)

        # Pack the labels
        self.quote.pack(side="top")
        self.quoted.pack(side="bottom")

        tk.mainloop()

if __name__ == "__main__":
    main()
