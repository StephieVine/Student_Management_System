from tkinter import* #import all the files in tkinter to work with
from PIL import Image, ImageTk
from tkinter import messagebox



#window

window=Tk()
#attaching the class to a variable to work with along the project
window.geometry('1280x700+0+0')
width=window.winfo_screenwidth()
blank_space=(" "*(int(width)//8))
# window.title(160*blank_space+'Registration Form')
window.title(blank_space+'REGISTRATION FORM')

window.resizable(0,0) #means the maximize button on the window is going to disabled by leaving the actualized values on default
window.iconbitmap('C:\\Users\Igbon Ifijeh\Downloads\\favicon (3).ico')

# backgroundImage=ImageTk.PhotoImage(file='bg1.jpg')
backgroundImage=Image.open('C:\\Users\Igbon Ifijeh\Desktop\pixels\\pexels-andrea-piacquadio-3769021.jpg')
bck_pic=ImageTk.PhotoImage(backgroundImage.resize((1280,700)))

lbl=Label(window, image=bck_pic)
lbl.place(x=0, y=0)

LoginFrame=Frame(window,  bg='floral white')
LoginFrame.place(x=850, y=150)
# LoginFrame.place(x=400, y=150) #real

LogoImage=PhotoImage(file='logoblack.png')
lblLogo=Label(LoginFrame, image=LogoImage)
lblLogo.grid(row=0, column=0, columnspan=2, pady=10)

usernameImage=PhotoImage(file='usernamelogo.png')
usernameLabel=Label(LoginFrame, image=usernameImage, text='Username', compound=LEFT, bg='floral white',  font=('Harrington', 14, 'bold'))
usernameLabel.grid(row=1, column=0, pady=10)

#Button Definition process
def Login():
    if UsernameEntry.get()=='' or PasswordEntry.get()=='': #if this condition is true it'll show an error box
        messagebox.showerror('Error', 'Empty Entry Field!')
         #to check if the user has entered a correct detail or not
    elif UsernameEntry.get()=='steph' or PasswordEntry.get()=='1111':
        messagebox.showinfo('Success!', 'Welcome {0}!'.format(UsernameEntry.get()))
        window.destroy() #for closing the previous window after a successful login
        import StudentManagementSystemGUI

    else:
        messagebox.showerror('Error','Please enter the correct details')






#Entry Class
UsernameEntry=Entry(LoginFrame, font=('Harrington', 14, 'bold'), bd=5, fg='#8470FF')
UsernameEntry.grid(row=1, column=1, padx=10)


#password entryand Labelfield
passwordImage=PhotoImage(file='padlock.png')
passwordLabelField=Label(LoginFrame,  image=passwordImage, text='Password', compound=LEFT, bg='floral white',  font=('Harrington', 14, 'bold'))
passwordLabelField.grid(row=2, column=0, pady=10)

PasswordEntry=Entry(LoginFrame, font=('Harrington', 14, 'bold'), bd=5, fg='#8470FF')
PasswordEntry.grid(row=2, column=1, padx=10)

#Button

Loginbutton=Button(LoginFrame, text='Login', font=('ariel', 14, 'bold'), width=8, padx=5, bg='cornflowerblue', fg='black', activebackground='cornflowerblue', activeforeground='black', cursor='hand2',
                   command=Login)
Loginbutton.grid(row=3, column=1)

window.mainloop()