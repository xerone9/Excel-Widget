


def add_teacher():
    for widget in root.winfo_children():
        widget.destroy()

    manage_teachers_logo = PhotoImage(file='manageTeachers_logo.png')
    manage_teachers_label = Label(root, image=manage_teachers_logo)
    manage_teachers_label.configure(foreground="black")
    manage_teachers_label.configure(bg="white")
    manage_teachers_label.place(relx=0.5, rely=0.1, anchor=CENTER)

    space_variable = Label(root, text="", font=("Roboto", 18), bg="white")
    space_variable.grid(row=0, column=0, pady=75)

    teacher_name_label = Label(root, text="Teacher Name: ", font=("Roboto", 18), bg="white")
    teacher_name_label.grid(row=1, column=0, pady=7)
    teacher_name = Entry(root, width=30, font=("Roboto", 18), bg='light blue')
    teacher_name.grid(row=1, column=1)

    teacher_subject_label = Label(root, text="Teacher Subject: ", font=("Roboto", 18), bg="white")
    teacher_subject_label.grid(row=2, column=0, pady=7)
    teacher_subject = Entry(root, width=30, font=("Roboto", 18), bg='light blue')
    teacher_subject.grid(row=2, column=1)

    teacher_time_slot_label = Label(root, text="Teacher Reserved Time: ", font=("Roboto", 18), bg="white")
    teacher_time_slot_label.grid(row=3, column=0, pady=7)
    teacher_time_slot = Entry(root, width=30, font=("Roboto", 18), bg='light blue')
    teacher_time_slot.grid(row=3, column=1)

    teacher_room_label = Label(root, text="Teacher Reserved Room", font=("Roboto", 18), bg="white")
    teacher_room_label.grid(row=4, column=0, pady=12, padx=20)
    teacher_room = Entry(root, width=30, font=("Roboto", 18), bg='light blue')
    teacher_room.grid(row=4, column=1)