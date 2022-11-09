from tkinter import *
import time
import ttkthemes
from tkinter import ttk #additional module, this helps us in applying theme on button, just write "ttk." to the label or button
from tkinter import messagebox, filedialog
import pymysql
import pandas as pd


def exitbtn():
    msgbx=messagebox.askyesno("Exit Screen",'Do you want to close this window?')
    if msgbx:
        root.destroy()
    else:
        pass



def export_data():
    # url=filedialog.asksaveasfile(defaultextension='.csv')
    url = filedialog.asksaveasfile(defaultextension='.csv')
    # print(url)
    indexing=studdentTable.get_children()
    # print(indexing)
    newlist=[]
    for index in indexing:
        content=studdentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)


    #pandas is for converting a datalist into a row or tabular form. first install panda in the python package or terminal
    # example=['faizan', 'khan', 'is', 'a', 'good', 'boy']
    table=pd.DataFrame(newlist, columns=['Id','Name', 'Mobile No','Email', 'Address', 'Gender', 'DOB','Added Date', 'Added Time']) #pd is panda module. ensure to spell 'DataFrame' correctly when using it
    table.to_csv(url, index=False) #index=False is to remove the index values attached to the data. this line is to convert the table to csv file which is the xcel format
    messagebox.showinfo('', 'Data is saved successfully')
    # print(table)




def clear_screen():
    # messagebox.askyesno('?','Do you want to clear the screen?')

    for item in studdentTable.get_children():
        studdentTable.delete(item)

def update_student():

    def update_data():

            query='update student set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
            mycursor.execute(query,(idEntryName.get(),idEntryPhone.get(),idEntryEmail.get(),idEntryAddress.get(),idEntryGender.get(),idEntryDOB.get(),date,currenttime, idEntry.get()))
            conect.commit() #make changes
            messagebox.showinfo('SUCCESS', 'ID No {0} is modified successfully'.format(idEntry.get()),parent=Update_Window)
            Update_Window.destroy()
            show_student()


    Update_Window = Toplevel()
    Update_Window.title('UPDATE DATA')
    Update_Window.grab_set()  # this widget is for disabling every other buttons on other window when it's visibly in use. in other words, you won't be able to click on other button
    Update_Window.resizable(False, False)
    Update_Window.iconbitmap('C:\\Users\Igbon Ifijeh\Downloads\\favicon (3).ico')

    idLabel = Label(Update_Window, text='Id', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabel.grid(row=0, column=0)

    idEntry = Entry(Update_Window, font=('ariel', 15, 'bold'), width=22)
    idEntry.grid(row=0, column=1, pady=15, padx=10, sticky=W)

    idLabelName = Label(Update_Window, text='Name', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelName.grid(row=1, column=0)
    idEntryName = Entry(Update_Window, font=('ariel', 15, 'bold'), width=22)
    idEntryName.grid(row=1, column=1, pady=15, padx=10, sticky=W)

    idLabelPhone = Label(Update_Window, text='Mobile', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelPhone.grid(row=2, column=0)
    idEntryPhone = Entry(Update_Window, font=('ariel', 15, 'bold'), width=22)
    idEntryPhone.grid(row=2, column=1, pady=15, padx=10, sticky=W)

    idLabelEmail = Label(Update_Window, text='Email', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelEmail.grid(row=3, column=0)
    idEntryEmail = Entry(Update_Window, font=('ariel', 15, 'bold'), width=22)
    idEntryEmail.grid(row=3, column=1, pady=15, padx=10, sticky=W)

    idLabelAddress = Label(Update_Window, text='Address', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelAddress.grid(row=4, column=0)
    idEntryAddress = Entry(Update_Window, font=('ariel', 15, 'bold'), width=22)
    idEntryAddress.grid(row=4, column=1, pady=15, padx=10, sticky=W)

    idLabelGender = Label(Update_Window, text='Gender', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelGender.grid(row=5, column=0)
    idEntryGender = Entry(Update_Window, font=('ariel', 15, 'bold'), width=22)
    idEntryGender.grid(row=5, column=1, pady=15, padx=10, sticky=W)

    idLabelDOB = Label(Update_Window, text='D.O.B', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelDOB.grid(row=6, column=0)
    idEntryDOB = Entry(Update_Window, font=('ariel', 15, 'bold'), width=22)
    idEntryDOB.grid(row=6, column=1, pady=15, padx=10, sticky=W)

    update_student_button = ttk.Button(Update_Window, text='UPDATE DATA',
                                       command=update_data)  # after typing all the details, this command btn would be used to store the data on the database
    update_student_button.grid(row=7, columnspan=2, pady=15)

    indexing = studdentTable.focus()  # which ever roll you select would go into this focus
    # print(indexing) #with the help of this indexing, you can get the complete role
    content = studdentTable.item(
        indexing)  # this will give a complete content corresponding to the index, that's to see what's inside it
    listData=content['values']
    idEntry.insert(0, listData[0])
    idEntryName.insert(0, listData[1])
    idEntryPhone.insert(0, listData[2])
    idEntryEmail.insert(0,listData[3])
    idEntryAddress.insert(0,listData[4])
    idEntryGender.insert(0,listData[5])
    idEntryDOB.insert(0,listData[6])



def show_student():
    query = 'select * from student'
    mycursor.execute(query)  # to execute the initial instruction from top 'query='select * from student'
    fetched_data = mycursor.fetchall()  # to fetch the data
    for data in fetched_data:
        studdentTable.insert('', END,
                             values=data)  # this is to show the updated data in my treeview after a successful delete


def delete_student():
    indexing=studdentTable.focus() #which ever roll you select would go into this focus
    # print(indexing) #with the help of this indexing, you can get the complete role
    content=studdentTable.item(indexing) #this will give a complete content corresponding to the index, that's to see what's inside it
    # print(content)
    content_id=content['values'][0] #content-id would be getting the content of the values
    query='delete from student where id=%s' #from db, this is the instruction for delete a content id or roll from the database
    mycursor.execute(query, content_id) #for executing the command for db
    conect.commit() #for updating/making changes
    messagebox.showinfo('Deleted', 'ID {0} was deleted Sucessfully'.format(content_id)) #this is to show that this id has been deleted successfully on a msgbox
    query='select * from student'
    mycursor.execute(query) #to execute the initial instruction from top 'query='select * from student'
    fetched_data=mycursor.fetchall() #to fetch the data
    studdentTable.delete(*studdentTable.get_children()) #this is to delete and would not appear on the treeview after being deleted
    for data in fetched_data:
        studdentTable.insert('', END, values=data) #this is to show the updated data in my treeview after a successful delete



def search_Student():
    def search_data():

        # if idEntry.get()=='' or idEntryName.get()=='' or idEntryGender.get()=='' or idEntryAddress.get()=='':
        #     messagebox.showerror('Error', 'Entry field must not be empty')
        #
        # else:

            query='select * from student where id=%s or name=%s or mobile=%s or gender=%s or address=%s '
            mycursor.execute(query,(idEntry.get(),idEntryName.get(), idEntryPhone.get(), idEntryGender.get(),idEntryAddress.get()))
            studdentTable.delete(*studdentTable.get_children())
            fetched_data=mycursor.fetchall() #for fetching all the rows on where the data falls to display on the treeview
            for data in fetched_data:
                studdentTable.insert('', END, values=data)




    searchWindow = Toplevel()
    searchWindow.title('SEARCH DATA')
    searchWindow.grab_set()  # this widget is for disabling every other buttons on other window when it's visibly in use. in other words, you won't be able to click on other button
    searchWindow.resizable(False, False)
    searchWindow.iconbitmap('C:\\Users\Igbon Ifijeh\Downloads\\favicon (3).ico')

    idLabel = Label(searchWindow, text='Id', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabel.grid(row=0, column=0)

    idEntry = Entry(searchWindow, font=('ariel', 15, 'bold'), width=22)
    idEntry.grid(row=0, column=1, pady=15, padx=10, sticky=W)

    idLabelName = Label(searchWindow, text='Name', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelName.grid(row=1, column=0)
    idEntryName = Entry(searchWindow, font=('ariel', 15, 'bold'), width=22)
    idEntryName.grid(row=1, column=1, pady=15, padx=10, sticky=W)

    idLabelPhone = Label(searchWindow, text='Mobile', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelPhone.grid(row=2, column=0)
    idEntryPhone = Entry(searchWindow, font=('ariel', 15, 'bold'), width=22)
    idEntryPhone.grid(row=2, column=1, pady=15, padx=10, sticky=W)

    idLabelEmail = Label(searchWindow, text='Email', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelEmail.grid(row=3, column=0)
    idEntryEmail = Entry(searchWindow, font=('ariel', 15, 'bold'), width=22)
    idEntryEmail.grid(row=3, column=1, pady=15, padx=10, sticky=W)

    idLabelAddress = Label(searchWindow, text='Address', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelAddress.grid(row=4, column=0)
    idEntryAddress = Entry(searchWindow, font=('ariel', 15, 'bold'), width=22)
    idEntryAddress.grid(row=4, column=1, pady=15, padx=10, sticky=W)

    idLabelGender = Label(searchWindow, text='Gender', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelGender.grid(row=5, column=0)
    idEntryGender = Entry(searchWindow, font=('ariel', 15, 'bold'), width=22)
    idEntryGender.grid(row=5, column=1, pady=15, padx=10, sticky=W)

    idLabelDOB = Label(searchWindow, text='D.O.B', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelDOB.grid(row=6, column=0)
    idEntryDOB = Entry(searchWindow, font=('ariel', 15, 'bold'), width=22)
    idEntryDOB.grid(row=6, column=1, pady=15, padx=10, sticky=W)

    search_student_button = ttk.Button(searchWindow, text='SEARCH STUDENT',
                                    command=search_data)  # after typing all the details, this command btn would be used to store the data on the database
    search_student_button.grid(row=7, columnspan=2, pady=15)

#add student funtionality part
def add_student():
    # def add_data(): #second stage
    def add_data():
        if idEntry.get()=='' or idEntryName.get()=='' or idEntryPhone.get()=='' or idEntryEmail.get()=='' or idEntryAddress.get()=='' or idEntryGender.get()=='' or idEntryDOB.get()=='':
            messagebox.showerror('Error', 'Data field must be entered', parent=add_window) #this is to check if all the entry fields are empty if it is true it'll show a msgbox error

        else:
            # currentdate = time.strftime('%d/%m/%Y')  # this gives us time or day
            # currenttime = time.strftime('%H:%M/%S/%p')
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                mycursor.execute(query,(idEntry.get(),idEntryName.get(), idEntryPhone.get(), idEntryEmail.get(),idEntryAddress.get(), idEntryGender.get(), idEntryDOB.get(),
                                        date, currenttime))#else if the entry fields are not empty it will simple put them to the database and show a msg 'Confirm' on the msgbox
                conect.commit() #for updating/making changes
                result=messagebox.askyesno('Confirm',"Data added successfully. Do you want to clean the form?", parent=add_window)#tis msgbx asks yes or no to clear or update the entry
                # print(result)
                if result: #this result gives back a yes command after being clicked if i want to clear the entries and do other things if not it'll pass
                    idEntry.delete(0, END)
                    idEntryName.delete(0, END)
                    idEntryPhone.delete(0, END)
                    idEntryEmail.delete(0, END)
                    idEntryAddress.delete(0, END)
                    idEntryGender.delete(0, END)
                    idEntryDOB.delete(0, END)
                else:
                    pass #this would pass if I do not want to do anything
            except:
                messagebox.showerror('Error', "ID cannot be repeated", parent=add_window)
                return #i do not want it to display at the bottom run

            #this is for fetching the entered/existing data from the database and display on our left frame display board
            query='select * from student'
            mycursor.execute(query)
            fetchded_data=mycursor.fetchall()
            print(fetchded_data)
            studdentTable.delete(*studdentTable.get_children())#for deleting the studenttable to avoid repetition of previous data
            for data in fetchded_data:
                datalist=list(data)#this is for converting my data to a list to display on my student table
                studdentTable.insert('',END, values=datalist)


    add_window=Toplevel()
    add_window.title('ADD STUDENT')
    add_window.grab_set() #this widget is for disabling every other buttons on other window when it's visibly in use. in other words, you won't be able to click on other button
    add_window.resizable(False, False)
    add_window.iconbitmap('C:\\Users\Igbon Ifijeh\Downloads\\favicon (3).ico')

    idLabel=Label(add_window, text='Id', font=('ariel', 20, 'bold'), padx= 20, pady=15, fg='brown1')
    idLabel.grid(row=0, column=0)
    idEntry=Entry(add_window, font=('ariel', 15, 'bold'), width=22)
    idEntry.grid(row=0, column=1, pady=15, padx=10, sticky=W)

    idLabelName = Label(add_window, text='Name', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelName.grid(row=1, column=0)
    idEntryName = Entry(add_window, font=('ariel', 15, 'bold'), width=22)
    idEntryName.grid(row=1, column=1, pady=15, padx=10, sticky=W)

    idLabelPhone = Label(add_window, text='Mobile', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelPhone.grid(row=2, column=0)
    idEntryPhone = Entry(add_window, font=('ariel', 15, 'bold'), width=22)
    idEntryPhone.grid(row=2, column=1, pady=15, padx=10, sticky=W)

    idLabelEmail = Label(add_window, text='Email', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelEmail.grid(row=3, column=0)
    idEntryEmail = Entry(add_window, font=('ariel', 15, 'bold'), width=22)
    idEntryEmail.grid(row=3, column=1, pady=15, padx=10, sticky=W)

    idLabelAddress = Label(add_window, text='Address', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelAddress.grid(row=4, column=0)
    idEntryAddress = Entry(add_window, font=('ariel', 15, 'bold'), width=22)
    idEntryAddress.grid(row=4, column=1, pady=15, padx=10, sticky=W)

    idLabelGender = Label(add_window, text='Gender', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelGender.grid(row=5, column=0)
    idEntryGender = Entry(add_window, font=('ariel', 15, 'bold'), width=22)
    idEntryGender.grid(row=5, column=1, pady=15, padx=10, sticky=W)

    idLabelDOB = Label(add_window, text='D.O.B', font=('ariel', 20, 'bold'), padx=20, pady=15, fg='brown1')
    idLabelDOB.grid(row=6, column=0)
    idEntryDOB = Entry(add_window, font=('ariel', 15, 'bold'), width=22)
    idEntryDOB.grid(row=6, column=1, pady=15, padx=10, sticky=W)


    add_student_button=ttk.Button(add_window, text='ADD STUDENT', command=add_data) #after typing all the details, this command btn would be used to store the data on the database
    add_student_button.grid(row=7, columnspan=2,pady=15)



#slider functionality part
count=0
text=''
def slider():
    global text, count
    if count==len(s): #if the countdown is up to the length of the t variable, then it should start from zero
        count=0
        text="" #means text should be empty else it'll count continously
    text=text+s[count] #t first letter comes into this value
    sliderLabel.config(text=text)
    count+=1 #for looping in 1s
    sliderLabel.after(300,slider) #next letter comes in after 300nano secs


def clock():
    global date,  currenttime
    date=time.strftime('%d/%m/%Y') #this gives us time or day
    currenttime=time.strftime('%H:%M/%S/%p')
    datetimeLabel.config(text=f'Date: {date}\nTime: {currenttime}', pady=3) #is for updating something on this label ('f' is used to concatenate string and variable
    datetimeLabel.after(1000, clock)#for updating something after sometime


#Button Definition, Labels and Entries for connecting window andCreating database
def connect_database():
    def connect():
        global mycursor, conect #when it is global means this particular function can be used elsewhere: for insert student values %s
        try:
            # conect=pymysql.connect(host=hostEntry.get(), user=usernamehostEntry.get(), password=passwordhostEntry.get()) #this will help to connect to mysql database
            conect = pymysql.connect(host='localhost', user='root', password='1234')  # this will help to connect to mysql database
            mycursor=conect.cursor()

        except: # if the hostname or password is not correct it'll display a msgbox bellow
            messagebox.showerror('Error', 'Invalid Deatils', parent=connectWindow) #the parent is for placing the msgbox on the parent window
            return #this is to go back to accept another entry and check if the password, userame and hostEntry are correct
        # create datebase
        try:
            query='create database studentmanagementsystem' # this is the command for creating database,it'll be stored in query variable
            mycursor.execute(query) #this is to execute the name
            query='use studentmanagementsystem'
            mycursor.execute(query)
            #to create a table, use command 'create table and the name of the table 'student' followed by the tables below
            query='create table student(id int not null primary key, name varchar(30), mobile varchar(14), email varchar(30),' \
              'address varchar(100), gender varchar(20), dob varchar(20), date varchar(50), time varchar(50))'
            mycursor.execute(query)
        except: #the line of code below is for creating a DB again after its been created initially to add a table, after that on the cmd type show databses enter then type use studentmanagementsystem; enter, then to show if the tables have been created type
            query='use studentmanagementsystem'
            mycursor.execute(query)
        messagebox.showinfo('Successful', 'Database updated',parent=connectWindow)  # if the details are entered correct, it'll show this successful messagebox
        # messagebox.iconbitmap('C:\\Users\Igbon Ifijeh\Downloads\\favicon (3).ico')
        connectWindow.destroy()
        addStudent.config(state=NORMAL)
        searchStudent.config(state=NORMAL)
        deleteStudent.config(state=NORMAL)
        updateStudent.config(state=NORMAL)
        showStudent.config(state=NORMAL)
        exportStudent.config(state=NORMAL)
        ClearScreen.config(state=NORMAL)
        exitbutton.config(state=NORMAL)

#database connection section
    connectWindow=Toplevel() #for connecting and creating another window
    connectWindow.grab_set() #this will make the host window to minimize after entry
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(False,False)


    hostnameLabel=Label(connectWindow, text="Host Name", font=('ariel', 14, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=10)

    hostEntry=Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=10, pady=20)

    usernameHostLabel = Label(connectWindow, text="User Name", font=('ariel', 14, 'bold'))
    usernameHostLabel.grid(row=1, column=0, padx=10)

    usernamehostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernamehostEntry.grid(row=1, column=1, padx=10, pady=20)

    passwordHostLabel = Label(connectWindow, text="Password", font=('ariel', 14, 'bold'))
    passwordHostLabel.grid(row=2, column=0, padx=10)

    passwordhostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordhostEntry.grid(row=2, column=1, padx=10, pady=20)

    connectButton=ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, column=1)





#Window
root=ttkthemes.ThemedTk() #this class of tk comes with beautiful themes
# root=Tk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x650+15+0')
root.title('Student Management System')
# root.ttkcolumn('Student Management System', width=50, anchor=CENTER)
# root.resizable(False, False) #todisable the window, making it unanble to modify
root.iconbitmap('C:\\Users\Igbon Ifijeh\Downloads\\favicon (3).ico')

datetimeLabel=Label(root, fg='darkblue', font=('Calibre',14,'bold'))
datetimeLabel.place(x=5,y=5)
clock() #calling this function after creating a Label for it and the define it

s='Student Management System'
sliderLabel=Label(root, text=s, font=('Calibre', 20, 'italic bold'))
sliderLabel.place(x=430, y=0)

slider()

#database button
connectButton=ttk.Button(root, text='Connect Database', command=connect_database)
connectButton.place(x=1000, y=0)




#frame
leftframe=Frame(root, pady=10)
leftframe.place(x=60, y=50, width=450, height=600)

logo_image=PhotoImage(file='students (2).png')
logo_imagelabel=Label(leftframe, image=logo_image, anchor='center')
logo_imagelabel.grid(row=0, column=2, pady=15)

addStudent=ttk.Button(leftframe, text='Add Student', width=25, state=DISABLED, command=add_student)
addStudent.grid(row=1, column=2, pady=12)

searchStudent=ttk.Button(leftframe, text='Search Student', width=25, state=DISABLED, command=search_Student)
searchStudent.grid(row=2, column=2, pady=12)

deleteStudent=ttk.Button(leftframe, text='Delete Student', width=25, state=DISABLED, command=delete_student)
deleteStudent.grid(row=3, column=2, pady=12)

updateStudent=ttk.Button(leftframe, text='Update database', width=25, state=DISABLED, command=update_student)
updateStudent.grid(row=4, column=2, pady=12)

showStudent=ttk.Button(leftframe, text='Show Student', width=25, state=DISABLED, command=show_student)
showStudent.grid(row=5, column=2, pady=12)

exportStudent=ttk.Button(leftframe, text='Export Data', width=25, state=DISABLED, command=export_data)
exportStudent.grid(row=6, column=2, pady=12)

ClearScreen=ttk.Button(leftframe, text='Clear Screen', width=25, state=DISABLED, command=clear_screen)
ClearScreen.grid(row=7, column=2, pady=12)

exitbutton=ttk.Button(leftframe, text='Exit', width=25, command=exitbtn)
exitbutton.grid(row=9, column=2, pady=12)





#right frame
rightframe=Frame(root)
rightframe.place(x=320, y=80, width=850, height=570)

scrollbarX=Scrollbar(rightframe, orient=HORIZONTAL)
scrollbaY=Scrollbar(rightframe, orient=VERTICAL)

studdentTable=ttk.Treeview(rightframe, columns=('ID', 'Name', 'Mobile No', 'Email', 'Address', 'Gender',
                                                'D.O.B', 'Added Date', 'Added Time'), xscrollcommand=scrollbarX.set, yscrollcommand=scrollbaY.set)

#in order to see the scrollbarX X View moving, we'll have to configure it
scrollbarX.config(command=studdentTable.xview)
scrollbaY.config(command=studdentTable.yview)

#this is to pack all the scroll in the frame due to complex codes
scrollbarX.pack(side=BOTTOM, fill=X) #scrollbar at the bottom
scrollbaY.pack(side=RIGHT, fill=Y) #scrollbar at the righthand side


studdentTable.pack(fill=BOTH, expand=1) #for filling the scroll screen and below

#in order to add heading to the student table for the treeview
studdentTable.heading('ID', text='ID')
studdentTable.heading('Name', text='Name')
studdentTable.heading('Mobile No', text='Mobile No')
studdentTable.heading('Email', text='Email')
studdentTable.heading('Address', text='Address')
studdentTable.heading('Gender', text='Gender')
studdentTable.heading('D.O.B', text='D.O.B')
studdentTable.heading('Added Date', text='Added Date')
studdentTable.heading('Added Time', text='Added Time')

studdentTable.column('ID', width=50, anchor=CENTER)
studdentTable.column('Name', width=400, anchor=CENTER)
studdentTable.column('Mobile No', width=300, anchor=CENTER)
studdentTable.column('Email', width=300, anchor=CENTER)
studdentTable.column('Address', width=300, anchor=CENTER)
studdentTable.column('Gender', width=100, anchor=CENTER)
studdentTable.column('D.O.B', width=300, anchor=CENTER)
studdentTable.column('Added Date', width=200, anchor=CENTER)
studdentTable.column('Added Time', width=200, anchor=CENTER)

#this is to provide style to our treeview
style=ttk.Style()

style.configure('Treeview', rowheight=40, font=('ariel', 12, 'bold'),foreground='red4', background='floral white') #for providin' gapping or height btw my roll in the treeview
style.configure('Treeview.Heading', font=('ariel', 15,'bold'))



studdentTable.config(show='headings')


root.mainloop()