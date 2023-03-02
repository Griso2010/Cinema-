from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
class Hall():
        
    def __init__(self) -> None:
        global root
        root = Tk()
        root.resizable(False, False)
        root.title("Main window")
        
        self.button_login = Button(text="LOG IN", font=('Comic Sans MS', 25, 'bold'), command=self.create_window)
        self.button_login.grid(padx=50, pady=5)
        self.book_ticket_btn = Button(text="Book ticket", font=('Comic Sans MS', 15, 'bold'), command=self.book_ticket)

    def create_new_window(self):
        self.button_login.destroy()

        self.controls_frame = Frame(bg="#F5F5DC", padx=100, pady=100)
        self.hall_frame = Frame(bg="#F5F5DC", padx=100, pady=50)
        self.controls_frame.grid()
        self.hall_frame.grid()
        hall_size_lbl = Label(self.controls_frame,bg="#F5F5DC", text='Select hall size:' ,font=('Comic Sans MS', 25, 'bold'), fg="black")
        hall_size_lbl.grid(column=1, row=0)
        self.button_hall_1 = Button(self.controls_frame, text="30 seats", command=self.first_hall)
        self.button_hall_1.grid(column=1, row=2)
        self.button_hall_2 = Button(self.controls_frame, text="60 seats", command=self.second_hall)
        self.button_hall_2.grid(column=1, row=3)
        self.button_hall_3 = Button(self.controls_frame, text="90 seats", command=self.third_hall)
        self.button_hall_3.grid(column=1, row=4)

    def create_hall(self, size):
        self.controls_frame.destroy()
        self.hall_boxes = []
        hall_size = size
        for i in range(hall_size):
            
            row = []
            for j in range(hall_size):
                btn = Checkbutton(self.hall_frame,
                    indicatoron=0,
                    text=f"{i}_{j}",
                    selectcolor='blue',
                    background='green',
                    width=5,
                    foreground="#FFF",
                    justify=CENTER)
                
                btn.grid(column=j, row=i)
                row.append(btn)        
    
            self.hall_boxes.append(row)     
        self.book_ticket_btn.grid()

    def book_ticket(self):

        pass

    def resize(self):    
        self.hall_frame.update_idletasks()
        self.hall_frame.update()
        self.root.update_idletasks()
        self.root.update()

    def create_window(self):
        self.tplvl = Toplevel()
        self.tplvl.title("Second window")
        
        self.control_frame = Frame(self.tplvl, bg = "#FBEC5D")
        self.control_frame.pack()
        self.entry_1 = Entry(self.control_frame, width=15)
        self.entry_2 = Entry(self.control_frame, width=15)
        self.login_lbl = Label(self.control_frame,text="Login", bg = "#FBEC5D",fg="black", font=('Comic Sans MS', 25, 'bold',))
        self.password_lbl = Label(self.control_frame,text="Password", bg = "#FBEC5D",fg="black", font=('Comic Sans MS', 25, 'bold'))
        self.login_lbl.grid(column=0, row=0)
        self.password_lbl.grid(column=0, row=1)
        self.entry_1.grid(column=1, row=0)
        self.entry_2.grid(column=1, row=1)
        self.button = Button(self.control_frame, text = 'LOG IN', font=('Comic Sans MS', 20, "bold"), command=self.check_admin)
        self.button.grid(column=0, row=2, columnspan=2, ipadx=100, ipady=10)

    def check_admin(self):
        USER = "Grisha"
        PASSWORD = "12345"
        self.login = self.entry_1.get()
        self.password = self.entry_2.get()
        if self.login == USER :
            if self.password == PASSWORD:
                self.tplvl.destroy()
                self.create_new_window()
            else:
                messagebox.showinfo("Information window", "INCORRECT PASSWORD")
        else:
            messagebox.showinfo("Information window", "INCORRECT LOGIN")

    def first_hall(self):
        self.create_hall(10)

    def second_hall(self):
        self.create_hall(15)

    def third_hall(self):
        self.create_hall(20)
    
hall = Hall()
root.mainloop()
