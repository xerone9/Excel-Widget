from tkinter import *

class GenerateClassSchedule:
    def __init__(self, master):
        self.room_name_label = Label(master, text="Room Name: ", font=("Roboto", 18), bg="white")
        self.room_name_label.place(relx=0.30, y=220)
        self.room_name = Entry(master, width=30, font=("Roboto", 18), bg='light blue')
        self.room_name.place(relx=0.45, y=220)

        self.addRoom = Button(master, text="ADD ROOM", font=("Roboto", 15, 'bold'), justify='center')
        self.addRoom.configure(foreground="black")
        self.addRoom.configure(bg="light green")
        self.addRoom.place(relx=0.38, y=320)

        self.deleteRoom = Button(master, text="DELETE ROOM", font=("Roboto", 15, 'bold'), justify='center')
        self.deleteRoom.configure(foreground="black")
        self.deleteRoom.configure(bg="red")
        self.deleteRoom.place(relx=0.50, y=320)

        self.rooms_list = Listbox(master, font=("Courier", 16, 'bold'), width=50, height=20, bg="light blue")
        self.rooms_list.place(relx=0.5, y=650, anchor=CENTER)