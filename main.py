import ttkbootstrap as ttk
from game import Game

class Main(ttk.Window):
    def __init__(self):
        # setup window
        super().__init__()
        self.title('Tic-Tac-Toe')
        self.geometry('600x800')
        self.resizable(height=False, width=False)

        # setup grid
        self.rowconfigure((0,1,2,3), weight=1, uniform='a')
        self.columnconfigure((0,1,2), weight=1, uniform='a')

        # create widgets
        self.create_widgets()

        # run
        self.mainloop()
    
    def create_widgets(self):
        # make
        self.game = Game(self)

        # place 
        self.game.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = 'nswe')

def main():
    app = Main()
    app

if __name__ == "__main__":
    main()