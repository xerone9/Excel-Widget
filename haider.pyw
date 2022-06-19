from tkinter import *
import webbrowser
from excel import *
from datetime import date
import os


def window_event(event):


def callback(url):
    webbrowser.open_new(url)


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
        status_label = Label(root, text="Recepie Name Empty", font=("Roboto", 20), bg="white", fg="red")
        status_label.place(relx=0.5, rely=0.85, anchor=CENTER)
        root.after(2000, status_label.destroy)
    else:
        if str(excel_entry(str(today.strftime("%d/%m/%Y")), str(recepie_name.get()), selections, rates)) != "Excel Open":
            # excel_entry(str(today.strftime("%d/%m/%Y")), str(recepie_name.get()), selections, rates)
            status_label = Label(root, text="Entry Saved Successfully", font=("Roboto", 20), bg="white", fg="green")
            status_label.place(relx=0.5, rely=0.85, anchor=CENTER)
            youtube_selected.set("YouTube")
            instagram_selected.set("0")
            reel_selected.set("Reel")
            photo_selected.set("Photo")
            recepie_name.delete(0, 'end')
            root.after(2000, status_label.destroy)
        else:
            status_label = Label(root, text="Close Excel File", font=("Roboto", 20), bg="white", fg="red")
            status_label.place(relx=0.5, rely=0.85, anchor=CENTER)
            root.after(2000, status_label.destroy)


root = Tk()
root.title('Client Excel Entry')
# root.resizable(0,0)
root.iconbitmap('icon.ico')
root.configure(bg="white")
root.geometry('500x500')
root.bind("<Configure>", window_event)

hello = int(root.winfo_screenwidth()) - 500


root.geometry('500x200+' + str(hello) + '+0')
recepie_name = Entry(root, width=25, font=("Roboto", 20), bg='light blue')
recepie_name.place(relx=0.5, rely=0.15, anchor=CENTER)

websites = ["YouTube", "Instagram", "Reel", "Photo"]

youtube_selected = StringVar()
instagram_selected = StringVar()
reel_selected = StringVar()
photo_selected = StringVar()

youtube_selected.set("YouTube")
instagram_selected.set("0")
reel_selected.set("Reel")
photo_selected.set("Photo")


youtube_checkbox = Checkbutton(root, text=websites[0], variable=youtube_selected, onvalue=websites[0],
                               font=("Roboto", 10), bg="white").place(relx=0.15, rely=0.36, anchor="w")
instagram_checkbox = Checkbutton(root, text=websites[1], variable=instagram_selected, onvalue=websites[1],
                                 font=("Roboto", 10), bg="white").place(relx=0.35, rely=0.36, anchor="w")
reel_checkbox = Checkbutton(root, text=websites[2], variable=reel_selected, onvalue=websites[2],
                            font=("Roboto", 10), bg="white").place(relx=0.55, rely=0.36, anchor="w")
photo_checkbox = Checkbutton(root, text=websites[3], variable=photo_selected, onvalue=websites[3],
                             font=("Roboto", 10), bg="white").place(relx=0.70, rely=0.36, anchor="w")

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
save.place(relx=0.5, rely=0.625, anchor=CENTER)

root.mainloop()
