from tkinter import *
import webbrowser
import sqlite3
import os
import re



def callback(url):
    webbrowser.open_new(url)


def ViewSupplier():
    for widget in root.winfo_children():
        widget.destroy()

    def GetToMainMenu(event):
        mainmenu()

    def UpdateSuppliersByUpDown(event):
        for item in suppliers_list.curselection():
            # print("You have selected " + str(item))

            conn = sqlite3.connect("Company_Profile.db")
            c = conn.cursor()

            selected_supplier = str(suppliers_list.get(item))
            # print(selected_supplier)

            supplier_list = c.execute("SELECT *,oid FROM suppliers")
            supplier_name_display = ""
            supplier_business_nature_display = ""
            supplier_email_id_display = ""
            supplier_contact_no_display = ""
            supplier_bank_name_display = ""
            supplier_bank_account_name_display = ""
            supplier_bank_account_no_display = ""
            for unique in supplier_list:
                supplier_name = str(unique[8]) + "- " + unique[1]
                if supplier_name == selected_supplier:
                    supplier_name_display = unique[1]
                    supplier_business_nature_display = unique[2]
                    supplier_email_id_display = unique[3]
                    supplier_contact_no_display = unique[4]
                    supplier_bank_name_display = unique[5]
                    supplier_bank_account_name_display = unique[6]
                    supplier_bank_account_no_display = unique[7]

            space = " "
            supplier_name_label.config(text="supplier / Company Name: " + str(supplier_name_display) + space * 30)
            supplier_name_label.place(x=15, y=480)

            supplier_business_label.config(text="Business Nature: " + str(supplier_business_nature_display) + space * 30)
            supplier_business_label.place(x=15, y=520)

            supplier_email_id_label.config(text="Email ID: " + str(supplier_email_id_display) + space * 30)
            supplier_email_id_label.place(x=15, y=560)

            supplier_contact_no_label.config(text="Contact No: " + str(supplier_contact_no_display) + space * 30)
            supplier_contact_no_label.place(x=15, y=600)

            supplier_bank_name_label.config(text="Bank Name: " + str(supplier_bank_name_display) + space * 30)
            supplier_bank_name_label.place(x=650, y=480)

            supplier_account_name_label.config(text="Account Name: " + str(supplier_bank_account_name_display) + space * 30)
            supplier_account_name_label.place(x=650, y=520)

            supplier_account_no_label.config(text="Account Number: " + str(supplier_bank_account_no_display) + space * 30)
            supplier_account_no_label.place(x=650, y=560)

            conn.commit()
            conn.close()

    supplier_name_label = Label(root, text="" * 30, font=("Roboto", 16), bg="white")
    supplier_name_label.place_forget()

    supplier_business_label = Label(root, text="", font=("Roboto", 16), bg="white")
    supplier_business_label.place_forget()

    supplier_email_id_label = Label(root, text="", font=("Roboto", 16), bg="white")
    supplier_email_id_label.place_forget()

    supplier_contact_no_label = Label(root, text="", font=("Roboto", 16), bg="white")
    supplier_contact_no_label.place_forget()

    supplier_bank_name_label = Label(root, text="", font=("Roboto", 16), bg="white")
    supplier_bank_name_label.place_forget()

    supplier_account_name_label = Label(root, text="", font=("Roboto", 16), bg="white")
    supplier_account_name_label.place_forget()

    supplier_account_no_label = Label(root, text="", font=("Roboto", 16), bg="white")
    supplier_account_no_label.place_forget()

    def DeleteSupplier():
        for item in suppliers_list.curselection():
            conn = sqlite3.connect("Company_Profile.db")
            c = conn.cursor()

            selected_supplier = str(suppliers_list.get(item))

            supplier_list = c.execute("SELECT *,oid FROM suppliers")
            for unique in supplier_list:
                supplier_name = selected_supplier
                if supplier_name == str(unique[8]) + "- " + unique[1]:
                    c.execute("DELETE FROM suppliers WHERE oid=" + str(unique[8]))
                    suppliers_list.delete(0, END)
                    update_supplier_list = c.execute("SELECT supplier_name, oid FROM suppliers")
                    for unique in update_supplier_list:
                        supplier_name = unique[0]
                        supplier_id = unique[1]
                        all_above_values = str(supplier_id) + "- " + supplier_name
                        suppliers_list.insert(END, all_above_values)
                        supplier_name_label.place_forget()
                        supplier_business_label.place_forget()
                        supplier_email_id_label.place_forget()
                        supplier_contact_no_label.place_forget()
                        supplier_bank_name_label.place_forget()
                        supplier_account_name_label.place_forget()
                        supplier_account_no_label.place_forget()


            conn.commit()
            conn.close()

    def ViewSupplier():
        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        selected_supplier = str(suppliers_list.get(ANCHOR))

        supplier_list = c.execute("SELECT *,oid FROM suppliers")
        supplier_name_display = ""
        supplier_business_nature_display = ""
        supplier_email_id_display = ""
        supplier_contact_no_display = ""
        supplier_bank_name_display = ""
        supplier_bank_account_name_display = ""
        supplier_bank_account_no_display = ""
        for unique in supplier_list:
            supplier_name = str(unique[8]) + "- " + unique[1]
            if supplier_name == selected_supplier:
                supplier_name_display = unique[1]
                supplier_business_nature_display = unique[2]
                supplier_email_id_display = unique[3]
                supplier_contact_no_display = unique[4]
                supplier_bank_name_display = unique[5]
                supplier_bank_account_name_display = unique[6]
                supplier_bank_account_no_display = unique[7]

        space = " "
        supplier_name_label = Label(root, text="supplier / Company Name: " + str(supplier_name_display) + space * 30,
                                    font=("Roboto", 16), bg="white")
        supplier_name_label.place(x=15, y=480)

        supplier_business_label = Label(root,
                                        text="Business Nature: " + str(supplier_business_nature_display) + space * 30,
                                        font=("Roboto", 16), bg="white")
        supplier_business_label.place(x=15, y=520)

        supplier_email_id_label = Label(root, text="Email ID: " + str(supplier_email_id_display) + space * 30,
                                        font=("Roboto", 16), bg="white")
        supplier_email_id_label.place(x=15, y=560)

        supplier_contact_no_label = Label(root, text="Contact No: " + str(supplier_contact_no_display) + space * 30,
                                          font=("Roboto", 16), bg="white")
        supplier_contact_no_label.place(x=15, y=600)

        supplier_bank_name_label = Label(root, text="Bank Name: " + str(supplier_bank_name_display) + space * 30,
                                         font=("Roboto", 16), bg="white")
        supplier_bank_name_label.place(x=650, y=480)

        supplier_account_name_label = Label(root, text="Account Name: " + str(
            supplier_bank_account_name_display) + space * 30, font=("Roboto", 16), bg="white")
        supplier_account_name_label.place(x=650, y=520)

        supplier_account_no_label = Label(root,
                                          text="Account Number: " + str(supplier_bank_account_no_display) + space * 30,
                                          font=("Roboto", 16), bg="white")
        supplier_account_no_label.place(x=650, y=560)

        conn.commit()
        conn.close()

    conn = sqlite3.connect("Company_Profile.db")
    c = conn.cursor()
    supplier_list = c.execute("SELECT *,oid FROM suppliers")

    img = PhotoImage(file='managesuppliers_logo.png')
    label = Label(root, image=img)
    label.configure(foreground="black")
    label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    label.place(x=((root.winfo_width() - 657) / 2), y=10)

    suppliers_list = Listbox(root, font=("Roboto", 16, 'bold'), width=75, bg="light blue")
    suppliers_list.place(relx=0.5, y=290, anchor=CENTER)
    suppliers_list.focus_get()
    suppliers_list.select_set(0)

    update_supplier_list = c.execute("SELECT supplier_name, oid FROM suppliers")
    for unique in update_supplier_list:
        supplier_name = unique[0]
        supplier_id = unique[1]
        all_above_values = str(supplier_id) + "- " + supplier_name
        suppliers_list.insert(END, all_above_values)

    view_supplier = Button(root, text="View supplier", font=("Roboto", 20, 'bold'), justify='center',
                           command=ViewSupplier)
    view_supplier.configure(foreground="black")
    view_supplier.configure(bg="light green")
    view_supplier.place_forget()

    delete_supplier = Button(root, text="Delete supplier", font=("Roboto", 20, 'bold'), justify='center',
                             command=DeleteSupplier)
    delete_supplier.configure(foreground="black")
    delete_supplier.configure(bg="light green")
    delete_supplier.place(relx=0.5, y=700, anchor=CENTER)

    main_menu = Button(root, text="MAIN MENU", font=("Roboto", 20, 'bold'), justify='center',
                             command=mainmenu)
    main_menu.configure(foreground="white")
    main_menu.configure(bg="brown")
    main_menu.place(relx=0.5, y=830, anchor=CENTER)

    root.bind('<Down>', UpdateSuppliersByUpDown)
    root.bind('<Up>', UpdateSuppliersByUpDown)
    root.bind('<ButtonRelease-1>', UpdateSuppliersByUpDown)
    root.bind('<Escape>', GetToMainMenu)

    conn.commit()
    conn.close()

    footer()





def Supplier():
    def AddSupplierByEnterKey(event):
        AddSupplier()


    def GetToMainMenu(event):
        mainmenu()

    def SaveEditedSupplier():
        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        selected_supplier = str(suppliers_list.get(ANCHOR))
        s = selected_supplier
        removing_space_from_selected_supplier = re.sub("\s\s+", ",", s)
        selected_supplier_into_list = removing_space_from_selected_supplier.split(",")
        supplier_list = c.execute("SELECT *,oid FROM suppliers")
        for unique in supplier_list:
            if unique[1] == selected_supplier_into_list[0] and unique[3] == selected_supplier_into_list[1] and str(
                    unique[4]) == str(selected_supplier_into_list[2]):

                c.execute("""UPDATE suppliers SET                            
                            supplier_name = :supplier_name,
                            supplier_business = :supplier_business,
                            supplier_email_id = :supplier_email_id,
                            supplier_contact_no = :supplier_contact_no,
                            supplier_bank_name = :supplier_bank_name,
                            supplier_account_name = :supplier_account_name,
                            supplier_account_no = :supplier_account_no

                            WHERE oid = :oid""",
                          {
                              'supplier_name': supplier_name.get(),
                              'supplier_business': supplier_business.get(),
                              'supplier_email_id': supplier_email_id.get(),
                              'supplier_contact_no': supplier_contact_no.get(),
                              'supplier_bank_name': supplier_bank_name.get(),
                              'supplier_account_name': supplier_account_name.get(),
                              'supplier_account_no': supplier_account_no.get(),
                              'oid': unique[8]
                          })
                suppliers_list.delete(0, END)

                update_supplier_list = c.execute(
                    "SELECT supplier_name, supplier_email_id, supplier_contact_no, oid FROM suppliers")
                space = " "

                for unique in update_supplier_list:
                    supplier_name_for_listbox = unique[0]
                    supplier_email_id_for_listbox = unique[1]
                    supplier_contact_no_for_listbox = unique[2]
                    all_above_values = supplier_name_for_listbox + space * (
                            25 - len(str(supplier_name_for_listbox))) + supplier_email_id_for_listbox + space * (
                                               40 - len(str(supplier_email_id_for_listbox))) + str(
                        supplier_contact_no_for_listbox)
                    suppliers_list.insert(0, all_above_values)

        conn.commit()
        conn.close()
        save_edited_supplier.grid_remove()
        edit_supplier.grid(row=10, column=3, padx=25)
        add_supplier_Button.grid(row=5, column=3, padx=50)
        supplier_name.delete(0, END)
        supplier_business.delete(0, END)
        supplier_email_id.delete(0, END)
        supplier_contact_no.delete(0, END)
        supplier_bank_name.delete(0, END)
        supplier_account_name.delete(0, END)
        supplier_account_no.delete(0, END)
        supplier_name.focus()
        root.bind("<Return>", AddSupplierByEnterKey)

    def EditSupplier():
        root.unbind("<Return>")
        supplier_name.delete(0, END)
        supplier_business.delete(0, END)
        supplier_email_id.delete(0, END)
        supplier_contact_no.delete(0, END)
        supplier_bank_name.delete(0, END)
        supplier_account_name.delete(0, END)
        supplier_account_no.delete(0, END)

        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        selected_supplier = str(suppliers_list.get(ANCHOR))
        s = selected_supplier
        removing_space_from_selected_supplier = re.sub("\s\s+", ",", s)
        selected_supplier_into_list = removing_space_from_selected_supplier.split(",")

        supplier_list = c.execute("SELECT *,oid FROM suppliers")
        for unique in supplier_list:
            if unique[1] == selected_supplier_into_list[0] and unique[3] == selected_supplier_into_list[1] and str(
                    unique[4]) == str(selected_supplier_into_list[2]):
                supplier_name.insert(0, unique[1])
                supplier_business.insert(0, unique[2])
                supplier_email_id.insert(0, unique[3])
                supplier_contact_no.insert(0, unique[4])
                supplier_bank_name.insert(0, unique[5])
                supplier_account_name.insert(0, unique[6])
                supplier_account_no.insert(0, unique[7])
                edit_supplier.grid_remove()
                add_supplier_Button.grid_remove()
                save_edited_supplier.grid(row=10, column=3, padx=25)

        conn.commit()
        conn.close()






    def AddSupplier():
        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS suppliers(            
                                supplier_ID INTEGER PRIMARY KEY,
                                supplier_name text,
                                supplier_business text,
                                supplier_email_id text,
                                supplier_contact_no int,
                                supplier_bank_name text,
                                supplier_account_name text,
                                supplier_account_no int           
                        )

                        """)

        serial = c.execute("select count(*) from suppliers")
        # print(serial)
        unique_id = 0
        for unique in serial:
            if unique[0] == '0':
                unique_id = 1
        else:
            serial = c.execute("SELECT supplier_id, oid FROM suppliers")
            for unique in serial:
                unique_id = unique[0]
            unique_id = unique_id + 1


        c.execute(
            "INSERT INTO suppliers VALUES (:supplier_ID, :supplier_name, :supplier_business, :supplier_email_id, :supplier_contact_no, :supplier_bank_name, :supplier_account_name, :supplier_account_no)",
            {
                'supplier_ID': str(unique_id),
                'supplier_name': supplier_name.get(),
                'supplier_business': supplier_business.get(),
                'supplier_email_id': supplier_email_id.get(),
                'supplier_contact_no': supplier_contact_no.get(),
                'supplier_bank_name': supplier_bank_name.get(),
                'supplier_account_name': supplier_account_name.get(),
                'supplier_account_no': supplier_account_no.get()
            })

        suppliers_list.delete(0, END)

        update_supplier_list = c.execute(
            "SELECT supplier_name, supplier_email_id, supplier_contact_no, oid FROM suppliers")
        space = " "

        for unique in update_supplier_list:
            supplier_name_for_listbox = unique[0]
            supplier_email_id_for_listbox = unique[1]
            supplier_contact_no_for_listbox = unique[2]
            all_above_values = supplier_name_for_listbox + space * (
                        25 - len(str(supplier_name_for_listbox))) + supplier_email_id_for_listbox + space * (
                                           40 - len(str(supplier_email_id_for_listbox))) + str(
                supplier_contact_no_for_listbox)
            suppliers_list.insert(0, all_above_values)



        conn.commit()
        conn.close()

        supplier_name.delete(0, END)
        supplier_business.delete(0, END)
        supplier_email_id.delete(0, END)
        supplier_contact_no.delete(0, END)
        supplier_bank_name.delete(0, END)
        supplier_account_name.delete(0, END)
        supplier_account_no.delete(0, END)
        supplier_name.focus()

    for widget in root.winfo_children():
        widget.destroy()

    root.unbind("<Return>")

    img = PhotoImage(file='managesuppliers_logo.png')
    label = Label(root, image=img)
    label.configure(foreground="black")
    label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    label.place(x=((root.winfo_width() - 657) / 2), y=10)


    space_variable = Label(root, text="", font=("Roboto", 16), bg="white")
    space_variable.grid(row=0, column=0, pady=60)

    supplier_name_label = Label(root, text="Supplier / Company Name", font=("Roboto", 16), bg="white")
    supplier_name_label.grid(row=1, column=0, pady=2, padx=20)
    supplier_name = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    supplier_name.grid(row=1, column=1)

    supplier_business_label = Label(root, text="Supplier Of:", font=("Roboto", 16), bg="white")
    supplier_business_label.grid(row=2, column=0, pady=2)
    supplier_business = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    supplier_business.grid(row=2, column=1)

    supplier_email_id_label = Label(root, text="Email ID", font=("Roboto", 16), bg="white")
    supplier_email_id_label.grid(row=3, column=0, pady=2)
    supplier_email_id = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    supplier_email_id.grid(row=3, column=1)

    supplier_contact_no_label = Label(root, text="Contact No", font=("Roboto", 16), bg="white")
    supplier_contact_no_label.grid(row=4, column=0, pady=2, padx=20)
    supplier_contact_no = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    supplier_contact_no.grid(row=4, column=1)

    bank_details_label = Label(root, text="Supplier Bank Details", font=("Roboto", 19), bg="white")
    bank_details_label.grid(row=5, column=1, pady=12)

    supplier_bank_name_label = Label(root, text="Bank Name", font=("Roboto", 16), bg="white")
    supplier_bank_name_label.grid(row=6, column=0, pady=2)
    supplier_bank_name = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    supplier_bank_name.grid(row=6, column=1)

    supplier_account_name_label = Label(root, text="Account Name", font=("Roboto", 16), bg="white")
    supplier_account_name_label.grid(row=7, column=0, pady=2)
    supplier_account_name = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    supplier_account_name.grid(row=7, column=1)

    supplier_account_no_label = Label(root, text="Account Number", font=("Roboto", 16), bg="white")
    supplier_account_no_label.grid(row=8, column=0, pady=2)
    supplier_account_no = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    supplier_account_no.grid(row=8, column=1, pady=2)

    space_variable2 = Label(root, text="", font=("Roboto", 16), bg="white")
    space_variable2.grid(row=9, column=0, pady=30)

    suppliers_list_label = Label(root, text="List Of Suppliers", font=("Roboto", 24), bg="white", fg="Blue")
    suppliers_list_label.grid(row=10, column=1)

    suppliers_list = Listbox(root, font=("Courier", 16, 'bold'), width=82, bg="light blue")
    suppliers_list.grid(row=11, columnspan=2)

    add_supplier_Button = Button(root, text="ADD SUPPLIER", font=("Roboto", 20, 'bold'), justify='center', command=AddSupplier)
    add_supplier_Button.configure(foreground="black")
    add_supplier_Button.configure(bg="light green")
    add_supplier_Button.grid(row=5, column=3, padx=50)

    edit_supplier = Button(root, text="EDIT SUPPLIER", font=("Roboto", 20, 'bold'), justify='center', command=EditSupplier)
    edit_supplier.configure(foreground="black")
    edit_supplier.configure(bg="light green")
    edit_supplier.grid(row=10, column=3, padx=25)

    save_edited_supplier = Button(root, text="SAVE", font=("Roboto", 20, 'bold'), justify='center', command=SaveEditedSupplier)
    save_edited_supplier.configure(foreground="black")
    save_edited_supplier.configure(bg="light green")
    save_edited_supplier.place_forget()

    main_menu_button = Button(root, text="MAIN MENU", font=("Roboto", 20, 'bold'), justify='center',
                              command=mainmenu)
    main_menu_button.configure(foreground="white")
    main_menu_button.configure(bg="brown")
    main_menu_button.grid(row=12, column=3, padx=25)


    conn = sqlite3.connect("Company_Profile.db")
    c = conn.cursor()

    update_supplier_list = c.execute("SELECT supplier_name, supplier_email_id, supplier_contact_no, oid FROM suppliers")
    space = " "

    for unique in update_supplier_list:
        supplier_name_for_listbox = unique[0]
        supplier_email_id_for_listbox = unique[1]
        supplier_contact_no_for_listbox = unique[2]
        all_above_values = supplier_name_for_listbox + space * (25 - len(str(supplier_name_for_listbox))) + supplier_email_id_for_listbox + space * (40 - len(str(supplier_email_id_for_listbox))) + str(supplier_contact_no_for_listbox)
        suppliers_list.insert(0, all_above_values)

    conn.commit()
    conn.close()

    root.bind('<Return>', AddSupplierByEnterKey)
    root.bind('<Escape>', GetToMainMenu)


    supplier_name.focus()

    footer()


def ViewCustomer():
    for widget in root.winfo_children():
        widget.destroy()

    def GetToMainMenu(event):
        mainmenu()

    def UpdateCustomersByUpDown(event):
        for item in customers_list.curselection():
            # print("You have selected " + str(item))

            conn = sqlite3.connect("Company_Profile.db")
            c = conn.cursor()

            selected_customer = str(customers_list.get(item))
            # print(selected_customer)

            customer_list = c.execute("SELECT *,oid FROM customers")
            customer_name_display = ""
            customer_business_nature_display = ""
            customer_email_id_display = ""
            customer_contact_no_display = ""
            customer_bank_name_display = ""
            customer_bank_account_name_display = ""
            customer_bank_account_no_display = ""
            for unique in customer_list:
                customer_name = str(unique[8]) + "- " + unique[1]
                if customer_name == selected_customer:
                    customer_name_display = unique[1]
                    customer_business_nature_display = unique[2]
                    customer_email_id_display = unique[3]
                    customer_contact_no_display = unique[4]
                    customer_bank_name_display = unique[5]
                    customer_bank_account_name_display = unique[6]
                    customer_bank_account_no_display = unique[7]

            space = " "
            customer_name_label.config(text="Customer / Company Name: " + str(customer_name_display) + space * 30)
            customer_name_label.place(x=15, y=480)

            customer_business_label.config(text="Business Nature: " + str(customer_business_nature_display) + space * 30)
            customer_business_label.place(x=15, y=520)

            customer_email_id_label.config(text="Email ID: " + str(customer_email_id_display) + space * 30)
            customer_email_id_label.place(x=15, y=560)

            customer_contact_no_label.config(text="Contact No: " + str(customer_contact_no_display) + space * 30)
            customer_contact_no_label.place(x=15, y=600)

            customer_bank_name_label.config(text="Bank Name: " + str(customer_bank_name_display) + space * 30)
            customer_bank_name_label.place(x=650, y=480)

            customer_account_name_label.config(text="Account Name: " + str(customer_bank_account_name_display) + space * 30)
            customer_account_name_label.place(x=650, y=520)

            customer_account_no_label.config(text="Account Number: " + str(customer_bank_account_no_display) + space * 30)
            customer_account_no_label.place(x=650, y=560)

            conn.commit()
            conn.close()

    customer_name_label = Label(root, text="" * 30, font=("Roboto", 16), bg="white")
    customer_name_label.place_forget()

    customer_business_label = Label(root, text="", font=("Roboto", 16), bg="white")
    customer_business_label.place_forget()

    customer_email_id_label = Label(root, text="", font=("Roboto", 16), bg="white")
    customer_email_id_label.place_forget()

    customer_contact_no_label = Label(root, text="", font=("Roboto", 16), bg="white")
    customer_contact_no_label.place_forget()

    customer_bank_name_label = Label(root, text="", font=("Roboto", 16), bg="white")
    customer_bank_name_label.place_forget()

    customer_account_name_label = Label(root, text="", font=("Roboto", 16), bg="white")
    customer_account_name_label.place_forget()

    customer_account_no_label = Label(root, text="", font=("Roboto", 16), bg="white")
    customer_account_no_label.place_forget()

    def DeleteCustomer():
        for item in customers_list.curselection():
            conn = sqlite3.connect("Company_Profile.db")
            c = conn.cursor()

            selected_customer = str(customers_list.get(item))

            customer_list = c.execute("SELECT *,oid FROM customers")
            for unique in customer_list:
                customer_name = selected_customer
                if customer_name == str(unique[8]) + "- " + unique[1]:
                    c.execute("DELETE FROM customers WHERE oid=" + str(unique[8]))
                    customers_list.delete(0, END)
                    update_customer_list = c.execute("SELECT customer_name, oid FROM customers")
                    for unique in update_customer_list:
                        customer_name = unique[0]
                        customer_id = unique[1]
                        all_above_values = str(customer_id) + "- " + customer_name
                        customers_list.insert(END, all_above_values)
                        customer_name_label.place_forget()
                        customer_business_label.place_forget()
                        customer_email_id_label.place_forget()
                        customer_contact_no_label.place_forget()
                        customer_bank_name_label.place_forget()
                        customer_account_name_label.place_forget()
                        customer_account_no_label.place_forget()


            conn.commit()
            conn.close()

    def ViewCustomer():
        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        selected_customer = str(customers_list.get(ANCHOR))

        customer_list = c.execute("SELECT *,oid FROM customers")
        customer_name_display = ""
        customer_business_nature_display = ""
        customer_email_id_display = ""
        customer_contact_no_display = ""
        customer_bank_name_display = ""
        customer_bank_account_name_display = ""
        customer_bank_account_no_display = ""
        for unique in customer_list:
            customer_name = str(unique[8]) + "- " + unique[1]
            if customer_name == selected_customer:
                customer_name_display = unique[1]
                customer_business_nature_display = unique[2]
                customer_email_id_display = unique[3]
                customer_contact_no_display = unique[4]
                customer_bank_name_display = unique[5]
                customer_bank_account_name_display = unique[6]
                customer_bank_account_no_display = unique[7]

        space = " "
        customer_name_label = Label(root, text="Customer / Company Name: " + str(customer_name_display) + space * 30,
                                    font=("Roboto", 16), bg="white")
        customer_name_label.place(x=15, y=480)

        customer_business_label = Label(root,
                                        text="Business Nature: " + str(customer_business_nature_display) + space * 30,
                                        font=("Roboto", 16), bg="white")
        customer_business_label.place(x=15, y=520)

        customer_email_id_label = Label(root, text="Email ID: " + str(customer_email_id_display) + space * 30,
                                        font=("Roboto", 16), bg="white")
        customer_email_id_label.place(x=15, y=560)

        customer_contact_no_label = Label(root, text="Contact No: " + str(customer_contact_no_display) + space * 30,
                                          font=("Roboto", 16), bg="white")
        customer_contact_no_label.place(x=15, y=600)

        customer_bank_name_label = Label(root, text="Bank Name: " + str(customer_bank_name_display) + space * 30,
                                         font=("Roboto", 16), bg="white")
        customer_bank_name_label.place(x=650, y=480)

        customer_account_name_label = Label(root, text="Account Name: " + str(
            customer_bank_account_name_display) + space * 30, font=("Roboto", 16), bg="white")
        customer_account_name_label.place(x=650, y=520)

        customer_account_no_label = Label(root,
                                          text="Account Number: " + str(customer_bank_account_no_display) + space * 30,
                                          font=("Roboto", 16), bg="white")
        customer_account_no_label.place(x=650, y=560)

        conn.commit()
        conn.close()

    conn = sqlite3.connect("Company_Profile.db")
    c = conn.cursor()
    customer_list = c.execute("SELECT *,oid FROM customers")

    img = PhotoImage(file='manageCustomers_logo.png')
    label = Label(root, image=img)
    label.configure(foreground="black")
    label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    label.place(x=((root.winfo_width() - 657) / 2), y=10)

    customers_list = Listbox(root, font=("Roboto", 16, 'bold'), width=75, bg="light blue")
    customers_list.place(relx=0.5, y=290, anchor=CENTER)
    customers_list.focus_get()
    customers_list.select_set(0)

    update_customer_list = c.execute("SELECT customer_name, oid FROM customers")
    for unique in update_customer_list:
        customer_name = unique[0]
        customer_id = unique[1]
        all_above_values = str(customer_id) + "- " + customer_name
        customers_list.insert(END, all_above_values)

    view_customer = Button(root, text="View Customer", font=("Roboto", 20, 'bold'), justify='center',
                           command=ViewCustomer)
    view_customer.configure(foreground="black")
    view_customer.configure(bg="light green")
    view_customer.place_forget()

    delete_customer = Button(root, text="Delete Customer", font=("Roboto", 20, 'bold'), justify='center',
                             command=DeleteCustomer)
    delete_customer.configure(foreground="black")
    delete_customer.configure(bg="light green")
    delete_customer.place(relx=0.5, y=700, anchor=CENTER)

    main_menu = Button(root, text="MAIN MENU", font=("Roboto", 20, 'bold'), justify='center',
                             command=mainmenu)
    main_menu.configure(foreground="white")
    main_menu.configure(bg="brown")
    main_menu.place(relx=0.5, y=830, anchor=CENTER)

    root.bind('<Down>', UpdateCustomersByUpDown)
    root.bind('<Up>', UpdateCustomersByUpDown)
    root.bind('<ButtonRelease-1>', UpdateCustomersByUpDown)
    root.bind('<Escape>', GetToMainMenu)

    conn.commit()
    conn.close()

    footer()



def Customer():
    def AddCustomerByEnterKey(event):
        AddCustomer()

    def GetToMainMenu(event):
        mainmenu()

    def SaveEditedCustomer():
        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        selected_customer = str(customers_list.get(ANCHOR))
        s = selected_customer
        removing_space_from_selected_customer = re.sub("\s\s+", ",", s)
        selected_customer_into_list = removing_space_from_selected_customer.split(",")
        customer_list = c.execute("SELECT *,oid FROM customers")
        for unique in customer_list:
            if unique[1] == selected_customer_into_list[0] and unique[3] == selected_customer_into_list[1] and str(
                    unique[4]) == str(selected_customer_into_list[2]):

                c.execute("""UPDATE customers SET                            
                            customer_name = :customer_name,
                            customer_business = :customer_business,
                            customer_email_id = :customer_email_id,
                            customer_contact_no = :customer_contact_no,
                            customer_bank_name = :customer_bank_name,
                            customer_account_name = :customer_account_name,
                            customer_account_no = :customer_account_no
    
                            WHERE oid = :oid""",
                          {
                              'customer_name': customer_name.get(),
                              'customer_business': customer_business.get(),
                              'customer_email_id': customer_email_id.get(),
                              'customer_contact_no': customer_contact_no.get(),
                              'customer_bank_name': customer_bank_name.get(),
                              'customer_account_name': customer_account_name.get(),
                              'customer_account_no': customer_account_no.get(),
                              'oid': unique[8]
                          })
                customers_list.delete(0, END)

                update_customer_list = c.execute(
                    "SELECT customer_name, customer_email_id, customer_contact_no, oid FROM customers")
                space = " "

                for unique in update_customer_list:
                    customer_name_for_listbox = unique[0]
                    customer_email_id_for_listbox = unique[1]
                    customer_contact_no_for_listbox = unique[2]
                    all_above_values = customer_name_for_listbox + space * (
                            25 - len(str(customer_name_for_listbox))) + customer_email_id_for_listbox + space * (
                                               40 - len(str(customer_email_id_for_listbox))) + str(
                        customer_contact_no_for_listbox)
                    customers_list.insert(0, all_above_values)

        conn.commit()
        conn.close()
        save_edited_customer.grid_remove()
        edit_customer.grid(row=10, column=3, padx=25)
        add_customer_Button.grid(row=5, column=3, padx=50)
        customer_name.delete(0, END)
        customer_business.delete(0, END)
        customer_email_id.delete(0, END)
        customer_contact_no.delete(0, END)
        customer_bank_name.delete(0, END)
        customer_account_name.delete(0, END)
        customer_account_no.delete(0, END)
        customer_name.focus()
        root.bind("<Return>", AddCustomerByEnterKey)


    def EditCustomer():
        root.unbind("<Return>")
        customer_name.delete(0, END)
        customer_business.delete(0, END)
        customer_email_id.delete(0, END)
        customer_contact_no.delete(0, END)
        customer_bank_name.delete(0, END)
        customer_account_name.delete(0, END)
        customer_account_no.delete(0, END)

        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        selected_customer = str(customers_list.get(ANCHOR))
        s = selected_customer
        removing_space_from_selected_customer = re.sub("\s\s+", ",", s)
        selected_customer_into_list = removing_space_from_selected_customer.split(",")

        customer_list = c.execute("SELECT *,oid FROM customers")
        for unique in customer_list:
            if unique[1] == selected_customer_into_list[0] and unique[3] == selected_customer_into_list[1] and str(unique[4]) == str(selected_customer_into_list[2]):
                customer_name.insert(0, unique[1])
                customer_business.insert(0, unique[2])
                customer_email_id.insert(0, unique[3])
                customer_contact_no.insert(0, unique[4])
                customer_bank_name.insert(0, unique[5])
                customer_account_name.insert(0, unique[6])
                customer_account_no.insert(0, unique[7])
                edit_customer.grid_remove()
                add_customer_Button.grid_remove()
                save_edited_customer.grid(row=10, column=3, padx=25)


        conn.commit()
        conn.close()

    def AddCustomer():
        conn = sqlite3.connect("Company_Profile.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS customers(            
                                customer_ID INTEGER PRIMARY KEY,
                                customer_name text,
                                customer_business text,
                                customer_email_id text,
                                customer_contact_no int,
                                customer_bank_name text,
                                customer_account_name text,
                                customer_account_no int           
                        )

                        """)

        serial = c.execute("select count(*) from customers")
        # print(serial)
        unique_id = 0
        for unique in serial:
            if unique[0] == '0':
                unique_id = 1
        else:
            serial = c.execute("SELECT customer_id, oid FROM customers")
            for unique in serial:
                unique_id = unique[0]
            unique_id = unique_id + 1


        c.execute(
            "INSERT INTO customers VALUES (:customer_ID, :customer_name, :customer_business, :customer_email_id, :customer_contact_no, :customer_bank_name, :customer_account_name, :customer_account_no)",
            {
                'customer_ID': str(unique_id),
                'customer_name': customer_name.get(),
                'customer_business': customer_business.get(),
                'customer_email_id': customer_email_id.get(),
                'customer_contact_no': customer_contact_no.get(),
                'customer_bank_name': customer_bank_name.get(),
                'customer_account_name': customer_account_name.get(),
                'customer_account_no': customer_account_no.get()
            })

        customers_list.delete(0, END)

        update_customer_list = c.execute(
            "SELECT customer_name, customer_email_id, customer_contact_no, oid FROM customers")
        space = " "

        for unique in update_customer_list:
            customer_name_for_listbox = unique[0]
            customer_email_id_for_listbox = unique[1]
            customer_contact_no_for_listbox = unique[2]
            all_above_values = customer_name_for_listbox + space * (
                        25 - len(str(customer_name_for_listbox))) + customer_email_id_for_listbox + space * (
                                           40 - len(str(customer_email_id_for_listbox))) + str(
                customer_contact_no_for_listbox)
            customers_list.insert(0, all_above_values)



        conn.commit()
        conn.close()

        customer_name.delete(0, END)
        customer_business.delete(0, END)
        customer_email_id.delete(0, END)
        customer_contact_no.delete(0, END)
        customer_bank_name.delete(0, END)
        customer_account_name.delete(0, END)
        customer_account_no.delete(0, END)
        customer_name.focus()

    for widget in root.winfo_children():
        widget.destroy()

    img = PhotoImage(file='manageCustomers_logo.png')
    label = Label(root, image=img)
    label.configure(foreground="black")
    label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    label.place(x=((root.winfo_width() - 657) / 2), y=10)


    space_variable = Label(root, text="", font=("Roboto", 16), bg="white")
    space_variable.grid(row=0, column=0, pady=60)

    customer_name_label = Label(root, text="Customer / Company Name", font=("Roboto", 16), bg="white")
    customer_name_label.grid(row=1, column=0, pady=2, padx=20)
    customer_name = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    customer_name.grid(row=1, column=1)

    customer_business_label = Label(root, text="Business", font=("Roboto", 16), bg="white")
    customer_business_label.grid(row=2, column=0, pady=2)
    customer_business = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    customer_business.grid(row=2, column=1)

    customer_email_id_label = Label(root, text="Email ID", font=("Roboto", 16), bg="white")
    customer_email_id_label.grid(row=3, column=0, pady=2)
    customer_email_id = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    customer_email_id.grid(row=3, column=1)

    customer_contact_no_label = Label(root, text="Contact No", font=("Roboto", 16), bg="white")
    customer_contact_no_label.grid(row=4, column=0, pady=2, padx=20)
    customer_contact_no = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    customer_contact_no.grid(row=4, column=1)

    bank_details_label = Label(root, text="Customer Bank Details", font=("Roboto", 19), bg="white")
    bank_details_label.grid(row=5, column=1, pady=12)

    customer_bank_name_label = Label(root, text="Bank Name", font=("Roboto", 16), bg="white")
    customer_bank_name_label.grid(row=6, column=0, pady=2)
    customer_bank_name = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    customer_bank_name.grid(row=6, column=1)

    customer_account_name_label = Label(root, text="Account Name", font=("Roboto", 16), bg="white")
    customer_account_name_label.grid(row=7, column=0, pady=2)
    customer_account_name = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    customer_account_name.grid(row=7, column=1)

    customer_account_no_label = Label(root, text="Account Number", font=("Roboto", 16), bg="white")
    customer_account_no_label.grid(row=8, column=0, pady=2)
    customer_account_no = Entry(root, width=60, font=("Roboto", 16), bg='light blue')
    customer_account_no.grid(row=8, column=1, pady=2)

    space_variable2 = Label(root, text="", font=("Roboto", 16), bg="white")
    space_variable2.grid(row=9, column=0, pady=30)

    customers_list_label = Label(root, text="List Of Customers", font=("Roboto", 24), bg="white", fg="Blue")
    customers_list_label.grid(row=10, column=1)

    customers_list = Listbox(root, font=("Courier", 16, 'bold'), width=82, bg="light blue")
    customers_list.grid(row=11, columnspan=2)

    add_customer_Button = Button(root, text="ADD CUSTOMER", font=("Roboto", 20, 'bold'), justify='center', command=AddCustomer)
    add_customer_Button.configure(foreground="black")
    add_customer_Button.configure(bg="light green")
    add_customer_Button.grid(row=5, column=3, padx=50)

    edit_customer = Button(root, text="EDIT CUSTOMER", font=("Roboto", 20, 'bold'), justify='center',
                                 command=EditCustomer)
    edit_customer.configure(foreground="black")
    edit_customer.configure(bg="light green")
    edit_customer.grid(row=10, column=3, padx=25)

    save_edited_customer = Button(root, text="SAVE", font=("Roboto", 20, 'bold'), justify='center',
                           command=SaveEditedCustomer)
    save_edited_customer.configure(foreground="black")
    save_edited_customer.configure(bg="light green")
    save_edited_customer.place_forget()

    main_menu_button = Button(root, text="MAIN MENU", font=("Roboto", 20, 'bold'), justify='center',
                              command=mainmenu)
    main_menu_button.configure(foreground="white")
    main_menu_button.configure(bg="brown")
    main_menu_button.grid(row=12, column=3, padx=25)


    conn = sqlite3.connect("Company_Profile.db")
    c = conn.cursor()

    update_customer_list = c.execute("SELECT customer_name, customer_email_id, customer_contact_no, oid FROM customers")
    space = " "

    for unique in update_customer_list:
        customer_name_for_listbox = unique[0]
        customer_email_id_for_listbox = unique[1]
        customer_contact_no_for_listbox = unique[2]
        all_above_values = customer_name_for_listbox + space * (25 - len(str(customer_name_for_listbox))) + customer_email_id_for_listbox + space * (40 - len(str(customer_email_id_for_listbox))) + str(customer_contact_no_for_listbox)
        customers_list.insert(0, all_above_values)

    conn.commit()
    conn.close()

    root.bind('<Return>', AddCustomerByEnterKey)
    root.bind('<Escape>', GetToMainMenu)


    customer_name.focus()

    footer()


def mainmenu():
    root.unbind_all('<Return>')
    for widget in root.winfo_children():
        widget.destroy()
    inventory_label_img = PhotoImage(file='inventory_logo.png')
    inventory_label = Label(root, image=inventory_label_img)
    inventory_label.configure(foreground="black")
    inventory_label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    inventory_label.grid(row=1, column=2, pady=40)
    #

    addCustomer = Button(root, text="ADD CUSTOMER", font=("Roboto", 20, 'bold'), justify='center', command=Customer)
    addCustomer.configure(foreground="black")
    addCustomer.configure(bg="light blue")
    addCustomer.grid(row=2, column=1, padx=40)

    viewCustomer = Button(root, text="VIEW CUSTOMER", font=("Roboto", 20, 'bold'), justify='center', command=ViewCustomer)
    viewCustomer.configure(foreground="black")
    viewCustomer.configure(bg="light blue")
    viewCustomer.grid(row=2, column=2, padx=2)

    addSupplier = Button(root, text="ADD SUPPLIER", font=("Roboto", 20, 'bold'), justify='center', command=Supplier)
    addSupplier.configure(foreground="black")
    addSupplier.configure(bg="light blue")
    addSupplier.grid(row=2, column=3, padx=2)

    viewSupplier = Button(root, text="VIEW SUPPLIER", font=("Roboto", 20, 'bold'), justify='center', command=ViewSupplier)
    viewSupplier.configure(foreground="black")
    viewSupplier.configure(bg="light blue")
    viewSupplier.grid(row=2, column=4, padx=85, pady=40)

    account_label_img = PhotoImage(file='accounts_logo.png')
    account_label = Label(root, image=account_label_img)
    account_label.configure(foreground="black")
    account_label.configure(bg="white")
    account_label.grid(row=3, column=2, pady=25)

    makeTransaction = Button(root, text="Make Transaction", font=("Roboto", 20, 'bold'), justify='center')
    makeTransaction.configure(foreground="black")
    makeTransaction.configure(bg="light green")
    makeTransaction.grid(row=4, column=1, padx=2)

    generalLedger = Button(root, text="General Ledger", font=("Roboto", 20, 'bold'), justify='center')
    generalLedger.configure(foreground="black")
    generalLedger.configure(bg="light green")
    generalLedger.grid(row=4, column=2, padx=2)

    trialBalance = Button(root, text="Trial Balance", font=("Roboto", 20, 'bold'), justify='center')
    trialBalance.configure(foreground="black")
    trialBalance.configure(bg="light green")
    trialBalance.grid(row=4, column=3, padx=2)

    profitAndLoss = Button(root, text="Profit & Loss", font=("Roboto", 20, 'bold'), justify='center')
    profitAndLoss.configure(foreground="black")
    profitAndLoss.configure(bg="light green")
    profitAndLoss.grid(row=4, column=4, padx=2, pady=40)

    administration_label_img = PhotoImage(file='administration_logo.png')
    administration_label = Label(root, image=administration_label_img)
    administration_label.configure(foreground="black")
    administration_label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    administration_label.grid(row=5, column=2, pady=40)

    createUser = Button(root, text="Create User", font=("Roboto", 20, 'bold'), justify='center')
    createUser.configure(foreground="black")
    createUser.configure(bg="light pink")
    createUser.grid(row=6, column=1)

    editUser = Button(root, text="Edit User", font=("Roboto", 20, 'bold'), justify='center')
    editUser.configure(foreground="black")
    editUser.configure(bg="light pink")
    editUser.grid(row=6, column=2)

    deleteUser = Button(root, text="Delete User", font=("Roboto", 20, 'bold'), justify='center')
    deleteUser.configure(foreground="black")
    deleteUser.configure(bg="light pink")
    deleteUser.grid(row=6, column=3)

    changeRights = Button(root, text="Change Rights", font=("Roboto", 20, 'bold'), justify='center')
    changeRights.configure(foreground="black")
    changeRights.configure(bg="light pink")
    changeRights.grid(row=6, column=4)

    footer()


def signin():

    def callback(event):
        authenticate()

    def authenticate():
        conn = sqlite3.connect("Company_Profile.db")

        c = conn.cursor()

        c.execute("SELECT user_id, user_password, oid FROM login")
        users = c.fetchall()
        # print(records)
        users_allowed = []
        for user in users:
            users_allowed.append(str(user[0]) + str(user[1]))

        login = user_id.get()+user_password.get()

        if login in users_allowed:
            mainmenu()
        else:
            c.execute("SELECT company_name, oid FROM company")
            company_name = c.fetchone()
            companyName = company_name[0]

            # for company in company_name:
            #     print(str(company[0]))

        conn.commit()
        conn.close()

    for widget in root.winfo_children():
        widget.destroy()
    img = PhotoImage(file='signin_logo.png')
    label = Label(root, image=img)
    label.configure(foreground="black")
    label.configure(bg="white")
    label.grid(row=0, column=0, pady=20)
    label.place(x=((root.winfo_width() - 351) / 2), y=100)

    space_variable = Label(root, text="", font=("Roboto", 18), bg="white")
    space_variable.grid(row=0, column=0, pady=160, padx=270)

    user_id_label = Label(root, text="User ID: ", font=("Roboto", 28), bg="white")
    user_id_label.grid(row=1, column=0, sticky='e')
    user_id = Entry(root, width=30, font=("Roboto", 28), bg='light blue')
    user_id.grid(row=1, column=1, sticky='w', pady=50)

    user_password_label = Label(root, text="Password: ", font=("Roboto", 28), bg="white")
    user_password_label.grid(row=2, column=0, pady=7, sticky='e')
    user_password = Entry(root, width=30, font=("Roboto", 28), bg='light blue', show="*")
    user_password.grid(row=2, column=1, sticky='w')

    startButton = Button(root, text="SIGN IN", font=("Roboto", 20, 'bold'), justify='center', command=authenticate)
    startButton.configure(foreground="white")
    startButton.configure(bg="blue")
    startButton.grid(row=3, column=1, pady=160)

    user_id.focus()
    root.bind('<Return>', callback)
    footer()






def GetToAdminUser():
    def createUserAndSignin():
        create_user()
        signin()


    def create_user():
        conn = sqlite3.connect("Company_Profile.db")

        c = conn.cursor()

        c.execute("""CREATE TABLE user_profile(            
                        user_ID INTEGER PRIMARY KEY,
                        user_name text,
                        education text,
                        email_id text,
                        contact_no int            
                )

                """)
        c.execute("""CREATE TABLE login(            
                            login_ID INTEGER PRIMARY KEY,
                            user_id text,
                            user_password text                                               
                    )

                    """)

        c.execute(
            "INSERT INTO user_profile VALUES (:user_ID, :user_name, :education, :email_id, :contact_no)",
            {
                'user_ID': 1,
                'user_name': user_name.get(),
                'education': user_education.get(),
                'email_id': email_id.get(),
                'contact_no': contact_no.get()
            })

        c.execute("INSERT INTO login VALUES (:login_ID, :user_id, :user_password)",
                  {
                      'login_ID': 1,
                      'user_id': user_id.get(),
                      'user_password': user_password.get()
                  })

        conn.commit()
        conn.close()


    conn = sqlite3.connect("Company_Profile.db")

    c = conn.cursor()

    c.execute("INSERT INTO company VALUES (:company_ID, :company_name, :nature_of_business, :ntn, :year_established)",
              {
                  'company_ID':1,
                  'company_name': company_name.get(),
                  'nature_of_business': business_nautre.get(),
                  'ntn': ntn.get(),
                  'year_established': year_of_establishment.get()
              })

    c.execute("INSERT INTO banks VALUES (:bank_ID, :bank_name, :account_name, :account_number, :IBAN)",
              {
                  'bank_ID': 1,
                  'bank_name': bank_name.get(),
                  'account_name': account_name.get(),
                  'account_number': account_number.get(),
                  'IBAN': ""
              })


    conn.commit()
    conn.close()

    for widget in root.winfo_children():
        widget.destroy()
    img = PhotoImage(file='adminuser_logo.png')
    label = Label(root, image=img)
    label.configure(foreground="black")
    label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    label.place(x=((root.winfo_width() - 657) / 2), y=10)
    #

    space_variable = Label(root, text="", font=("Roboto", 18), bg="white")
    space_variable.grid(row=0, column=0, pady=75)

    user_name_label = Label(root, text="User Name", font=("Roboto", 18), bg="white")
    user_name_label.grid(row=1, column=0, pady=7, padx=((root.winfo_width() - 1141) / 2))
    user_name = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    user_name.grid(row=1, column=1)

    user_education_label = Label(root, text="Education", font=("Roboto", 18), bg="white")
    user_education_label.grid(row=2, column=0, pady=7)
    user_education = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    user_education.grid(row=2, column=1)

    email_id_label = Label(root, text="Email ID", font=("Roboto", 18), bg="white")
    email_id_label.grid(row=3, column=0, pady=7)
    email_id = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    email_id.grid(row=3, column=1)

    contact_no_label = Label(root, text="Contact No", font=("Roboto", 18), bg="white")
    contact_no_label.grid(row=4, column=0, pady=12, padx=20)
    contact_no = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    contact_no.grid(row=4, column=1)

    bank_details_label = Label(root, text="User Log-in Details", font=("Roboto", 22), bg="white")
    bank_details_label.grid(row=5, column=1, pady=12)

    user_id_label = Label(root, text="User ID", font=("Roboto", 18), bg="white")
    user_id_label.grid(row=6, column=0, pady=7)
    user_id = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    user_id.grid(row=6, column=1)

    user_password_label = Label(root, text="Password", font=("Roboto", 18), bg="white")
    user_password_label.grid(row=7, column=0, pady=7)
    user_password = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    user_password.grid(row=7, column=1)

    space_variable2 = Label(root, text="", font=("Roboto", 18), bg="white")
    space_variable2.grid(row=9, column=0, pady=50)

    startButton = Button(root, text="N E X T", font=("Roboto", 20, 'bold'), justify='center', command=createUserAndSignin)
    startButton.configure(foreground="black")
    startButton.configure(bg="light green")
    startButton.grid(row=10, column=1)

    footer()


def footer():
    footer = Label(root, text="softwares.rubick.org", font=(14), cursor="hand2")
    footer.bind("<Button-1>", lambda e: callback("http://softwares.rubick.org"))
    footer.configure(foreground="white")
    footer.configure(bg="black")
    footer.place(x=((root.winfo_width() - 150) / 2), y=(root.winfo_height() - 30))
    root.mainloop()




root = Tk()
root.resizable(0,0)
root.iconbitmap('icon.ico')
if os.path.exists("Company_Profile.db"):
    conn = sqlite3.connect("Company_Profile.db")
    c = conn.cursor()
    c.execute("SELECT company_name, oid FROM company")
    company_name = c.fetchone()
    companyName = company_name[0]
    root.title(companyName + " - DBMS")
else:
    root.title('Database Management System')
# root.geometry("440x630")
root.configure(bg="white")
root.state("zoomed")

if os.path.exists("Company_Profile.db"):
    conn = sqlite3.connect("Company_Profile.db")
    c = conn.cursor()
    signin()
else:
    img = PhotoImage(file='companyProfile_logo.png')
    label = Label(root, image=img, anchor="se")
    label.configure(foreground="black")
    label.configure(bg="white")
    # label.grid(row=0, column=0, pady=20)
    label.place(x=((root.winfo_width() - 576) / 2), y=10)
    #

    space_variable = Label(root, text="", font=("Roboto", 18), bg="white")
    space_variable.grid(row=0, column=0, pady=75)

    company_name_label = Label(root, text="Company Name", font=("Roboto", 18), bg="white")
    company_name_label.grid(row=1, column=0, pady=7, padx=((root.winfo_width() - 1141) / 2))
    company_name = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    company_name.grid(row=1, column=1)

    business_nautre_label = Label(root, text="Nature Of Bussiness", font=("Roboto", 18), bg="white")
    business_nautre_label.grid(row=2, column=0, pady=7)
    business_nautre = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    business_nautre.grid(row=2, column=1)

    ntn_label = Label(root, text="NTN", font=("Roboto", 18), bg="white")
    ntn_label.grid(row=3, column=0, pady=7)
    ntn = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    ntn.grid(row=3, column=1)

    year_of_establishment_label = Label(root, text="Year Estabished", font=("Roboto", 18), bg="white")
    year_of_establishment_label.grid(row=4, column=0, pady=12, padx=20)
    year_of_establishment = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    year_of_establishment.grid(row=4, column=1)

    bank_details_label = Label(root, text="Bank Details", font=("Roboto", 22), bg="white")
    bank_details_label.grid(row=5, column=1, pady=12)

    bank_name_label = Label(root, text="Bank Name", font=("Roboto", 18), bg="white")
    bank_name_label.grid(row=6, column=0, pady=7)
    bank_name = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    bank_name.grid(row=6, column=1)

    account_name_label = Label(root, text="Account Name", font=("Roboto", 18), bg="white")
    account_name_label.grid(row=7, column=0, pady=7)
    account_name = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    account_name.grid(row=7, column=1)

    account_number_label = Label(root, text="Account Number", font=("Roboto", 18), bg="white")
    account_number_label.grid(row=8, column=0, pady=7)
    account_number = Entry(root, width=60, font=("Roboto", 18), bg='light blue')
    account_number.grid(row=8, column=1)

    space_variable2 = Label(root, text="", font=("Roboto", 18), bg="white")
    space_variable2.grid(row=9, column=0, pady=50)

    startButton = Button(root, text="N E X T", font=("Roboto", 20, 'bold'), justify='center', command=GetToAdminUser)
    startButton.configure(foreground="black")
    startButton.configure(bg="light green")
    startButton.grid(row=10, column=1)

    conn = sqlite3.connect("Company_Profile.db")
    c = conn.cursor()


    c.execute("""CREATE TABLE company(            
            company_ID INTEGER PRIMARY KEY,
            company_name text,
            nature_of_business text,
            ntn int,
            year_established            
    )
    
    """)
    c.execute("""CREATE TABLE banks(            
                bank_ID INTEGER PRIMARY KEY,
                bank_name text,
                account_name text,
                account_number text,
                IBAN text                            
        )

        """)
    conn.commit()
    conn.close()


    footer()



