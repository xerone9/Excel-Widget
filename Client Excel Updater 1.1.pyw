from tkinter import *
import webbrowser
import os
from excel import *
from datetime import date


def window_event(event):
    if root.state() == 'zoomed':
        label.place(relx=0.5, rely=0.1, anchor=CENTER)
        recepie_name.config(width=25, font=("Roboto", 30), bg='light blue')
        recepie_name_label.place(relx=0.43, rely=0.3, anchor="se")
        recepie_name.place(relx=0.65, rely=0.27, anchor=CENTER)
        youtube_checkbox.config(font=("Roboto", 20))
        youtube_checkbox.place(relx=0.24, rely=0.36, anchor="w")
        instagram_checkbox.config(font=("Roboto", 20))
        instagram_checkbox.place(relx=0.24, rely=0.42, anchor="w")
        reel_checkbox.config(font=("Roboto", 20))
        reel_checkbox.place(relx=0.24, rely=0.48, anchor="w")
        photo_checkbox.config(font=("Roboto", 20))
        photo_checkbox.place(relx=0.24, rely=0.54, anchor="w")
        youtube_amount.config(font=("Roboto", 25), bg='light blue')
        youtube_amount.place(relx=0.463, rely=0.36, anchor=CENTER)
        instagram_amount.config(font=("Roboto", 25), bg='light blue')
        instagram_amount.place(relx=0.463, rely=0.42, anchor=CENTER)
        reel_amount.config(font=("Roboto", 25), bg='light blue')
        reel_amount.place(relx=0.463, rely=0.48, anchor=CENTER)
        photo_amount.config(font=("Roboto", 25), bg='light blue')
        photo_amount.place(relx=0.463, rely=0.54, anchor=CENTER)
        save.config(font=("Roboto", 20, 'bold'), justify='center')
        save.place(relx=0.25, rely=0.77, anchor=CENTER)
        open_excel.config(font=("Roboto", 20, 'bold'), justify='center')
        open_excel.place(relx=0.75, rely=0.77, anchor=CENTER)
        footer.place(relx=0.5, y=(root.winfo_height() - 30))
    if root.state() == 'normal':
        label.place_forget()
        recepie_name_label.place_forget()
        recepie_name.config(width=25, font=("Roboto", 20), bg='light blue')
        recepie_name.place(relx=0.5, rely=0.15, anchor=CENTER)
        youtube_checkbox.config(font=("Roboto", 10))
        youtube_checkbox.place(relx=0.15, rely=0.36, anchor="w")
        instagram_checkbox.config(font=("Roboto", 10))
        instagram_checkbox.place(relx=0.35, rely=0.36, anchor="w")
        reel_checkbox.config(font=("Roboto", 10))
        reel_checkbox.place(relx=0.55, rely=0.36, anchor="w")
        photo_checkbox.config(font=("Roboto", 10))
        photo_checkbox.place(relx=0.70, rely=0.36, anchor="w")
        youtube_amount.config(font=("Roboto", 25), bg='light blue')
        youtube_amount.place_forget()
        instagram_amount.config(font=("Roboto", 25), bg='light blue')
        instagram_amount.place_forget()
        reel_amount.config(font=("Roboto", 25), bg='light blue')
        reel_amount.place_forget()
        photo_amount.config(font=("Roboto", 25), bg='light blue')
        photo_amount.place_forget()
        save.config(font=("Roboto", 15, 'bold'))
        save.place(relx=0.25, rely=0.625, anchor=CENTER)
        open_excel.config(font=("Roboto", 15, 'bold'))
        open_excel.place(relx=0.75, rely=0.625, anchor=CENTER)
        footer.place_forget()


def callback(url):
    webbrowser.open_new(url)


def openexcelfile():
    os.startfile('data.xlsx')


def selected_radio_button():
    selections = []
    rates = []
    if youtube_selected.get() != "0":
        selections.append(youtube_selected.get())
        rates.append(youtube_amount.get())
    if instagram_selected.get() != "0":
        selections.append(instagram_selected.get())
        rates.append(instagram_amount.get())
    if reel_selected.get() != "0":
        selections.append(reel_selected.get())
        rates.append(reel_amount.get())
    if photo_selected.get() != "0":
        selections.append(photo_selected.get())
        rates.append(photo_amount.get())
    today = date.today()
    if len(recepie_name.get()) == 0:
        if root.state() == "normal":
            status_label = Label(root, text="Recepie Name Empty", font=("Roboto", 20), bg="white", fg="red")
            status_label.place(relx=0.5, rely=0.85, anchor=CENTER)
            root.after(2000, status_label.destroy)
        if root.state() == "zoomed":
            status_label = Label(root, text="Recepie Name Empty", font=("Roboto", 30), bg="white", fg="red")
            status_label.place(relx=0.5, rely=0.9, anchor=CENTER)
            root.after(2000, status_label.destroy)
    elif youtube_selected.get() == "0" and instagram_selected.get() == "0" and reel_selected.get() == "0" and photo_selected.get() == "0":
        if root.state() == "normal":
            status_label = Label(root, text="Checkmark Atleast One Option", font=("Roboto", 20), bg="white", fg="red")
            status_label.place(relx=0.5, rely=0.85, anchor=CENTER)
            root.after(2000, status_label.destroy)
        if root.state() == "zoomed":
            status_label = Label(root, text="Checkmark Atleast One Option", font=("Roboto", 30), bg="white", fg="red")
            status_label.place(relx=0.5, rely=0.9, anchor=CENTER)
            root.after(2000, status_label.destroy)
    else:
        if str(excel_entry(str(today.strftime("%d/%m/%Y")), str(recepie_name.get()), selections, rates)) != "Excel Open":
            # excel_entry(str(today.strftime("%d/%m/%Y")), str(recepie_name.get()), selections, rates)
            if root.state() == "normal":
                status_label = Label(root, text="Entry Saved Successfully", font=("Roboto", 20), bg="white", fg="green")
                status_label.place(relx=0.5, rely=0.85, anchor=CENTER)
            if root.state() == "zoomed":
                status_label = Label(root, text="Entry Saved Successfully", font=("Roboto", 30), bg="white", fg="green")
                status_label.place(relx=0.5, rely=0.9, anchor=CENTER)
            youtube_selected.set("0")
            instagram_selected.set("0")
            reel_selected.set("0")
            photo_selected.set("0")
            recepie_name.delete(0, 'end')
            root.after(2000, status_label.destroy)
        else:
            if root.state() == "normal":
                status_label = Label(root, text="Close Excel File", font=("Roboto", 20), bg="white", fg="red")
                status_label.place(relx=0.5, rely=0.85, anchor=CENTER)
                root.after(2000, status_label.destroy)
            if root.state() == "zoomed":
                status_label = Label(root, text="Close Excel File", font=("Roboto", 30), bg="white", fg="red")
                status_label.place(relx=0.5, rely=0.9, anchor=CENTER)
                root.after(2000, status_label.destroy)


root = Tk()
root.title('Client Excel Entry')
# root.resizable(0,0)
root.iconbitmap('icon.ico')
root.configure(bg="white")
root.bind("<Configure>", window_event)

xaxis = int(int(root.winfo_screenwidth()) / 2)
yaxis = int(int(root.winfo_screenheight()) / 2)


root.geometry('500x200+' + str(xaxis - 250) + '+' + str(yaxis - 100))


welcome_logo = PhotoImage(file='images\\welcome_logo.png')
label = Label(root, image=welcome_logo)
label.configure(foreground="black")
label.configure(bg="white")
label.place()

recepie_name_label = Label(root, text="Recepie Name: ", font=("Roboto", 30), bg="white")
recepie_name_label.place()


recepie_name = Entry(root, width=25, font=("Roboto", 20), bg='light blue')
recepie_name.place(relx=0.5, rely=0.15, anchor=CENTER)

websites = ["YouTube", "Instagram", "Reel", "Photo"]

youtube_selected = StringVar()
instagram_selected = StringVar()
reel_selected = StringVar()
photo_selected = StringVar()

youtube_selected.set("0")
instagram_selected.set("0")
reel_selected.set("0")
photo_selected.set("0")


youtube_checkbox = Checkbutton(root, text=websites[0], variable=youtube_selected, onvalue=websites[0],
                               font=("Roboto", 10), bg="white")
youtube_checkbox.place(relx=0.15, rely=0.36, anchor="w")
instagram_checkbox = Checkbutton(root, text=websites[1], variable=instagram_selected, onvalue=websites[1],
                                 font=("Roboto", 10), bg="white")
instagram_checkbox.place(relx=0.35, rely=0.36, anchor="w")
reel_checkbox = Checkbutton(root, text=websites[2], variable=reel_selected, onvalue=websites[2],
                            font=("Roboto", 10), bg="white")
reel_checkbox.place(relx=0.55, rely=0.36, anchor="w")
photo_checkbox = Checkbutton(root, text=websites[3], variable=photo_selected, onvalue=websites[3],
                             font=("Roboto", 10), bg="white")
photo_checkbox.place(relx=0.70, rely=0.36, anchor="w")

rates = []

f = open("default_rates.ini", "r")
for x in f:
    k = x.split(" = ")
    j = k[1].rstrip('\n')
    rates.append(j)
f.close()

youtube_amount = Entry(root, textvariable=StringVar(root, value=rates[0]), width=4, font=("Roboto", 25),
                       bg='light blue')
youtube_amount.place()
instagram_amount = Entry(root, textvariable=StringVar(root, value=rates[1]), width=4, font=("Roboto", 25),
                         bg='light blue')
instagram_amount.place()
reel_amount = Entry(root, textvariable=StringVar(root, value=rates[2]), width=4, font=("Roboto", 25),
                    bg='light blue')
reel_amount.place()
photo_amount = Entry(root, textvariable=StringVar(root, value=rates[3]), width=4, font=("Roboto", 25),
                     bg='light blue')
photo_amount.place()

save = Button(root, text="S A V E", font=("Roboto", 15, 'bold'), justify='center', command=selected_radio_button)
save.configure(foreground="black")
save.configure(bg="light green")
save.place(relx=0.25, rely=0.625, anchor=CENTER)

open_excel = Button(root, text="O P E N", font=("Roboto", 15, 'bold'), justify='center', command=openexcelfile)
open_excel.configure(foreground="black")
open_excel.configure(bg="light green")
open_excel.place(relx=0.75, rely=0.625, anchor=CENTER)

footer = Label(root, text="softwares.rubick.org", font=(14), cursor="hand2")
footer.bind("<Button-1>", lambda e: callback("http://softwares.rubick.org"))
footer.configure(foreground="white")
footer.configure(bg="black")
footer.place()

root.mainloop()
