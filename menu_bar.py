# @authors Brynn
# @date 4/13/21
# @brief Houses all components and functions of the top menu
# @todo fill in functions

import tkinter as tk
import sys


# Creates a new window with helpful information
def about():
    about_window = tk.Tk()
    about_window.title("About")
    about_window.geometry("400x300")

    tk.Label(about_window,
             text="Our team proposes to build an accurate visible and NIR (near-Infrared light) spectrum (or\n "
                  "Color-Infrared) mapping software specifically for STELLA (Science and Technology Education for\n "
                  "Land/Life Assessment), that will cartographically include and/or display STELLA’s other sensor\n "
                  "readings in a user friendly and visually appealing GUI (Graphical User Interface).\n "
             ).pack()


class MenuBar(tk.Menu):
    # MenuBar constructor
    def __init__(self, master):
        tk.Menu.__init__(self, master)

        # Dropdown menu of file options: open, save, exit
        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="File", underline=0, menu=file_menu)
        file_menu.add_command(label="Open File", underline=1, command=self.quit)
        file_menu.add_command(label="Save File", underline=1, command=self.quit)
        file_menu.add_command(label="Exit", underline=1, command=self.quit)

        # Dropdown menu of view options: vis, nir, temp
        view_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="View", underline=0, menu=view_menu)
        view_menu.add_command(label="Visual Map", underline=1, command=self.quit)
        view_menu.add_command(label="NIR Map", underline=1, command=self.quit)
        view_menu.add_command(label="Temp Map", underline=1, command=self.quit)

        # Dropdown menu of annotation options
        annotate_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Annotate", underline=0, menu=annotate_menu)
        annotate_menu.add_command(label="New Annotation", underline=1, command=self.quit)
        annotate_menu.add_command(label="Clear Annotations", underline=1, command=self.quit)

        # Help Menu
        help_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Help", underline=0, menu=help_menu)
        help_menu.add_command(label="About", underline=1, command=about)

    # Closes the window
    def quit(self):
        sys.exit(0)


# Window for testing purposes only. Shows how to create a MenuBar object.
class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        # menu_bar = MenuBar(parent/master/root)
        menu_bar = MenuBar(self)
        # I think the root window needs to do this to add the menu
        self.config(menu=menu_bar)


if __name__ == "__main__":
    app = App()
    app.mainloop()
