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
        self.current_matrix = [[0,0,0], 
                               [0,0,0], 
                               [0,0,0]]
        
        # buttons
        self.buttons = []
        
        # button images
        self.empty = ImageTk.PhotoImage((Image.open('images/empty.png')))
        self.x_img = ImageTk.PhotoImage((Image.open('images/x.png')))
        self.o_img = ImageTk.PhotoImage((Image.open('images/o.png')))

        # make boxes
        self.create_boxes()

        # setup binds
        self.setup_binds()
    
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

        self.buttons.append(self.top_left)
        self.buttons.append(self.top_middle)
        self.buttons.append(self.top_right)
        self.buttons.append(self.mid_left)
        self.buttons.append(self.mid_middle)
        self.buttons.append(self.mid_right)
        self.buttons.append(self.bot_left)
        self.buttons.append(self.bot_middle)
        self.buttons.append(self.bot_right)
        
    def setup_binds(self):
        self.bind('<Button-3>', lambda event: self.clear_board)
        self.top_left.bind('<Button-1>', lambda event: self.draw_x(self.top_left), self.draw_x_board(0,0))
        self.top_middle.bind('<Button-1>', lambda event: self.draw_x(self.top_middle), self.draw_x_board(0,1))
        self.top_right.bind('<Button-1>', lambda event: self.draw_x(self.top_right), self.draw_x_board(0,2))
        self.mid_left.bind('<Button-1>', lambda event: self.draw_x(self.mid_left), self.draw_x_board(1,0))
        self.mid_middle.bind('<Button-1>', lambda event: self.draw_x(self.mid_middle), self.draw_x_board(1,1))
        self.mid_right.bind('<Button-1>', lambda event: self.draw_x(self.mid_right), self.draw_x_board(1,2))
        self.bot_left.bind('<Button-1>', lambda event: self.draw_x(self.bot_left), self.draw_x_board(2,0))
        self.bot_middle.bind('<Button-1>', lambda event: self.draw_x(self.bot_middle), self.draw_x_board(2,1))
        self.bot_right.bind('<Button-1>', lambda event: self.draw_x(self.bot_right), self.draw_x_board(2,2))

        self.top_left.bind('<Button-3>', lambda event: self.draw_o(self.top_left), self.draw_y_board(0,0))
        self.top_middle.bind('<Button-3>', lambda event: self.draw_o(self.top_middle), self.draw_y_board(0,1))
        self.top_right.bind('<Button-3>', lambda event: self.draw_o(self.top_right), self.draw_y_board(0,2))
        self.mid_left.bind('<Button-3>', lambda event: self.draw_o(self.mid_left), self.draw_y_board(1,0))
        self.mid_middle.bind('<Button-3>', lambda event: self.draw_o(self.mid_middle), self.draw_y_board(1,1))
        self.mid_right.bind('<Button-3>', lambda event: self.draw_o(self.mid_right), self.draw_y_board(1,2))
        self.bot_left.bind('<Button-3>', lambda event: self.draw_o(self.bot_left), self.draw_y_board(2,0))
        self.bot_middle.bind('<Button-3>', lambda event: self.draw_o(self.bot_middle), self.draw_y_board(2,1))
        self.bot_right.bind('<Button-3>', lambda event: self.draw_o(self.bot_right), self.draw_y_board(2,2))

    def draw_x_board(self, x, y):
        self.current_matrix[x][y] = 1

    def draw_y_board(self, x, y):
        self.current_matrix[x][y] = 2

    def draw_x(self, button):
        button.config(image=self.x_img)

    def draw_o(self, button):
        button.config(image=self.o_img)

    def draw_grid(self):
        pass

    def check_win_x(self):
        pass

    def check_win_o(self):
        pass

    def clear_board(self):
        print("test")
        self.current_matrix = [[0,0,0], 
                               [0,0,0], 
                               [0,0,0]]
        