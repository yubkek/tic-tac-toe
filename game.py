import ttkbootstrap as ttk
from PIL import Image, ImageTk

class Game(ttk.Frame):
    def __init__(self, window):
        # setup
        super().__init__(window)
        self.window = window
        self.rowconfigure((0,1,2), weight=1, uniform='a')
        self.columnconfigure((0,1,2), weight=1, uniform='a')

        # state variables

        # matrix
        current_matrix = [[0,0,0],
                          [0,0,0],
                          [0,0,0]]
        
        # button images
        self.empty = ImageTk.PhotoImage((Image.open('images/empty.png')))
        self.x_img = ImageTk.PhotoImage((Image.open('images/x.png')))
        self.o_img = ImageTk.PhotoImage((Image.open('images/o.png')))

        # make boxes
        self.create_boxes()
    
    def create_boxes(self):

        style = ttk.Style()
        style.configure("GameButton.TButton", 
                borderwidth=0,        # Removes border
                padding=0,            # Removes extra padding
                relief="flat",        # Makes it flat
                highlightthickness=0) # Removes focus highlight

        self.top_left = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.top_middle = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.top_right = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.mid_left = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.mid_middle = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.mid_right = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.bot_left = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.bot_middle = ttk.Button(self, image=self.empty, style="GameButton.TButton")
        self.bot_right = ttk.Button(self, image=self.empty, style="GameButton.TButton")

        self.top_left.grid(row = 0, column = 0, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.top_middle.grid(row = 0, column = 1, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.top_right.grid(row = 0, column = 2, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.mid_left.grid(row = 1, column = 0, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.mid_middle.grid(row = 1, column = 1, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.mid_right.grid(row = 1, column = 2, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.bot_left.grid(row = 2, column = 0, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.bot_middle.grid(row = 2, column = 1, rowspan = 1, columnspan = 1, sticky = 'nswe')
        self.bot_right.grid(row = 2, column = 2, rowspan = 1, columnspan = 1, sticky = 'nswe')
        
    def setup_binds(self):
        self.bind()

    def draw_grid(self):
        pass

    def check_win_x(self):
        pass

    def check_win_o(self):
        pass
