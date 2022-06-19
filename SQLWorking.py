import sqlite3

# CREATE ALL TABLES

def create_main_table():
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE Institution ( 
        Institution_Name     varchar(100)     ,
        Department_Name      varchar(100)     
     );
                    """)

    c.execute("""CREATE TABLE License ( 
            Till_Date            date     ,
            Key_1                integer     ,
            Key_2                integer     
         );
                        """)

    c.execute("""CREATE TABLE Rooms ( 
            Room_Number          varchar(15)     
         );
                        """)

    c.execute("""CREATE TABLE Teachers ( 
            Teacher_Name         varchar(100)     ,
            Subject_Name         varchar(100)     ,
            Teacher_Reserved_Time_Slot         varchar(25)     ,
            Teacher_Reserved_Room         varchar(25)     
         );
                        """)

    c.execute("""CREATE TABLE Time_Slots ( 
            TIme_Slots           varchar(25)     
         );
                        """)

    c.execute("""CREATE TABLE Time_Table ( 
            Date                 date     ,
            Teacher_Name         varchar(100)     ,
            Teacher_Subject      varchar(100)     ,
            Teacher_Time_Slot    varchar(25)     ,
            Teacher_Room         varchar(25)     
         );
                        """)



    conn.commit()
    conn.close()






# Adding Values in Institution Table

def entry_in_institution_table(institution_name, department_name):
    conn = sqlite3.connect("Class_Scheduler.db")

    c = conn.cursor()

    c.execute("INSERT INTO Institution VALUES (:institution_name, :department_name)",
              {
                  'institution_name': institution_name,
                  'department_name': department_name

              })

    conn.commit()
    conn.close()







# Adding, Removing and Fetching Values From Rooms Table

def entry_in_rooms_table(room_number):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    c.execute("INSERT INTO Rooms VALUES (:Room_Number)",
              {
                  'Room_Number': room_number

              })

    conn.commit()
    conn.close()


def fetch_values_from_rooms_table():
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    fetch_values = c.execute("SELECT Room_Number, oid FROM Rooms")

    rooms = []
    for value in fetch_values:
        room_number = value[0]
        rooms.append(room_number)
    return rooms

    conn.commit()
    conn.close()


def delete_values_from_rooms_table(room_selected):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    rooms = c.execute("SELECT *,oid FROM Rooms")
    for room in rooms:
        room_name = room[0]
        if room_name == room_selected:
            c.execute("DELETE FROM Rooms WHERE oid=" + str(room[1]))

    conn.commit()
    conn.close()
    validate(room_selected)




# Adding, Removing and Fetching Values For Time Slots Table

def entry_in_time_slots_table(time_slot):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    c.execute("INSERT INTO Time_Slots VALUES (:Time_Slots)",
              {
                  'Time_Slots': time_slot

              })

    conn.commit()
    conn.close()


def fetch_values_from_time_slots_table():
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    fetch_values = c.execute("SELECT Time_Slots, oid FROM Time_Slots ORDER BY Time_Slots")

    Time_Slots = []
    for value in fetch_values:
        Time_Slots_number = value[0]
        Time_Slots.append(Time_Slots_number)
    return Time_Slots

    conn.commit()
    conn.close()


def delete_values_from_time_slots_table(time_slot_selected):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    Time_Slots = c.execute("SELECT *,oid FROM Time_Slots")
    for time in Time_Slots:
        time_slot = time[0]
        if time_slot == time_slot_selected:
            c.execute("DELETE FROM Time_Slots WHERE oid=" + str(time[1]))

    conn.commit()
    conn.close()

    validate(time_slot_selected)


# Adding, Removing, Modifying and Fetching Values For Teachers Table

def entry_in_teachers_table(name, subject, time, room):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    c.execute("INSERT INTO Teachers VALUES (:Teacher_Name, :Subject_Name, :Teacher_Reserved_Time_Slot, :Teacher_Reserved_Room)",
              {
                  'Teacher_Name': name,
                  'Subject_Name': subject,
                  'Teacher_Reserved_Time_Slot': time,
                  'Teacher_Reserved_Room': room

              })

    conn.commit()
    conn.close()


def fetch_values_from_teachers_table():
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    fetch_values = c.execute("SELECT *, oid FROM Teachers ORDER BY Teacher_Name")

    Teachers = []
    for value in fetch_values:
        name = value[0]
        subject = value[1]
        time = value[2]
        room = value[3]
        All_Values = name + " - " + subject + " - " + time + " - " + room
        Teachers.append(All_Values)
    return Teachers

    conn.commit()
    conn.close()


def fetch_values_from_teachers_table_with_oid():
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    fetch_values = c.execute("SELECT *, oid FROM Teachers")

    Teachers = []
    for value in fetch_values:
        name = value[0]
        subject = value[1]
        time = value[2]
        room = value[3]
        oid = value[4]
        All_Values = name + " - " + subject + " - " + time + " - " + room + " - " + str(oid)
        Teachers.append(All_Values)
    return Teachers

    conn.commit()
    conn.close()


def delete_values_from_teachers_table(teacher_selected):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    Teachers = c.execute("SELECT *,oid FROM Teachers")
    for teacher in Teachers:
        name = teacher[0]
        subject = teacher[1]
        time = teacher[2]
        room = teacher[3]

        if name == teacher_selected[0] and subject == teacher_selected[1] and time == teacher_selected[2] and room == teacher_selected[3]:
            c.execute("DELETE FROM Teachers WHERE oid=" + str(teacher[4]))


    conn.commit()
    conn.close()


def modify_values_from_teachers_table(teacher_selected):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()
    # teacher_selected_converted = teacher_selected.replace(" - ", "")

    Teachers = c.execute("SELECT *,oid FROM Teachers")
    for teacher in Teachers:
        name = teacher[0]
        subject = teacher[1]
        time = teacher[2]
        room = teacher[3]
        oid = teacher[4]
        # All_Values = name + subject + time + room

        if name == teacher_selected[0] and subject == teacher_selected[1] and time == teacher_selected[2] and room == teacher_selected[3]:
            return [name, subject, time, room, oid]


def save_modified_values_from_teachers_table(name, subject, time, room, oid):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    c.execute("""UPDATE Teachers SET                            
                        Teacher_Name = :name,
                        Subject_Name = :subject,
                        Teacher_Reserved_Time_Slot = :time,
                        Teacher_Reserved_Room = :room
                        

                        WHERE oid = :oid""",
              {
                  'name': name,
                  'subject': subject,
                  'time': time,
                  'room': room,
                  'oid': oid
              })


    conn.commit()
    conn.close()





# Adding, Clearing Values For Time Table

def entry_in_time_table(date, name, subject, time, room):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    c.execute(
        "INSERT INTO Time_Table VALUES (:Date, :Teacher_Name, :Subject_Name, :Teacher_Reserved_Time_Slot, :Teacher_Reserved_Room)",
        {
            'Date': date,
            'Teacher_Name': name,
            'Subject_Name': subject,
            'Teacher_Reserved_Time_Slot': time,
            'Teacher_Reserved_Room': room

        })

    conn.commit()
    conn.close()


def fetch_values_from_time_table(date):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()


    fetch_values = c.execute("SELECT * FROM Time_Table WHERE Date='" + date + "'" + "ORDER BY Teacher_Time_Slot")

    Teachers = []
    for value in fetch_values:
        date = value[0]
        name = value[1]
        subject = value[2]
        time = value[3]
        room = value[4]
        All_Values = name + " - " + subject + " - " + time + " - " + room
        Teachers.append(All_Values)
    return Teachers

    conn.commit()
    conn.close()


def delete_values_from_time_table(date_selected):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()
    c2 = conn.cursor()

    date = c.execute("SELECT *,oid FROM Time_Table")
    # result = c.fetchall()
    for value in date:
        dates = value[0]
        if dates == date_selected:
            c2.execute("DELETE FROM Time_Table WHERE oid=" + str(value[5]))

    conn.commit()
    conn.close()


def delete_values2_from_time_table(date, name, subject, time, room):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    Teachers = c.execute("SELECT *,oid FROM Time_Table")
    for teacher in Teachers:
        date_in_table = teacher[0]
        name_in_table = teacher[1]
        subject_in_table = teacher[2]
        time_in_table = teacher[3]
        room_in_table = teacher[4]

        if date_in_table == date and name == name_in_table and subject == subject_in_table and time == time_in_table and room == room_in_table:
            c.execute("DELETE FROM Time_Table WHERE oid=" + str(teacher[5]))

    conn.commit()
    conn.close()


def verify_rooms_available_from_Time_table(time_room):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    list = time_room.split(" - ")
    fetch_values = c.execute("SELECT *, oid FROM Time_Table")

    Teachers = ""
    for value in fetch_values:
        name = value[1]
        subject = value[2]
        time = value[3]
        room = value[4]
        if list[0] == time and list[1] == room:
            Teachers = value[1] + " - " + value[2]
    return Teachers

    conn.commit()
    conn.close()


def verify_teacher_available_from_Time_table(teacher_time):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    list = teacher_time.split(" - ")
    fetch_values = c.execute("SELECT *, oid FROM Time_Table")

    Teachers = ""
    for value in fetch_values:
        name = value[1]
        subject = value[2]
        time = value[3]
        room = value[4]
        if list[0] == name and list[1] == time:
            Teachers = value[1] + " - " + value[2]
    return Teachers

    conn.commit()
    conn.close()


def max_room():
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    total = fetch_values_from_rooms_table()
    count = 0

    for room in total:
        count += 1

    return count


    conn.commit()
    conn.close()


def max_time():
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()

    total = fetch_values_from_time_slots_table()
    count = 0

    for time in total:
        count += 1

    return count

    conn.commit()
    conn.close()




def validate(value):
    conn = sqlite3.connect("Class_Scheduler.db")
    c = conn.cursor()
    c2 = conn.cursor()

    acid = fetch_values_from_teachers_table_with_oid()
    for game in acid:
        list = game.split(" - ")
        name = list[0]
        subject = list[1]
        time = list[2]
        room = list[3]
        oid = list[4]
        if value == time:
            c2.execute("""UPDATE Teachers SET
                                    Teacher_Name = :name,
                                    Subject_Name = :subject,
                                    Teacher_Reserved_Time_Slot = :time,
                                    Teacher_Reserved_Room = :room
        
        
                                    WHERE oid = :oid""",
                      {
                          'name': name,
                          'subject': subject,
                          'time': "",
                          'room': room,
                          'oid': oid
                      })

        elif value == room:
            c2.execute("""UPDATE Teachers SET
                                    Teacher_Name = :name,
                                    Subject_Name = :subject,
                                    Teacher_Reserved_Time_Slot = :time,
                                    Teacher_Reserved_Room = :room


                                    WHERE oid = :oid""",
                       {
                           'name': name,
                           'subject': subject,
                           'time': time,
                           'room': "",
                           'oid': oid
                       })


    conn.commit()
    conn.close()

