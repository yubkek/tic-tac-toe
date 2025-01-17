import ttkbootstrap as ttk

class Main(ttk.Window):
    def __init__(self):
        # setup window
        super().__init__(themename='journal')
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
        pass

def main():
    app = Main()
    app

if __name__ == "__main__":
    main()