# Importing the tkinter module for creating GUI applications
from tkinter import *

# Importing the socket module for network communication
import socket

# Importing the filedialog module from tkinter for opening file dialogs
from tkinter import filedialog

# Importing the os module for interacting with the operating system
import os

# Creates a window instance
root = Tk()

# Setting the title of the window
root.title("Share it")

# Setting the initial size and position of the window
root.geometry("450x560+500+200")

# Setting the background color of the window
root.config(bg="#f4fdfe")

# Disabling the ability to resize the window
root.resizable(False, False)

def send():
    # Creating a new window
    window = Toplevel(root)
    window.title('Send')
    window.geometry("450x560+500+200")
    window.config(bg='#f4fdfe')
    window.resizable(False, False)

    def select_file():
        global filename
        filename = filedialog.askopenfile(initialdir=os.getcwd(),title="Select file")

    def sender():
        s = socket.socket()
        host = socket.socket()
        port = 9090
        s.bind((host,port))
        s.listen(1)
        print(host)

        print("Waiting for any incoming connections...")
        conn ,addr = s.accept()

        file = open(filename,'rb')
        file_data = file.read(1024)

        conn.send(file_data)

        print("Data has been succesfully sent")



    # Setting the icon for the new window
    image_icon1 = PhotoImage(file='fileimages/send.png')
    window.iconphoto(False, image_icon1)

    # Setting background images
    Sbackground = PhotoImage(file='fileimages/sender.png')
    Label(window, image=Sbackground).place(x=-10, y=0)

    Mbackground = PhotoImage(file='fileimages/id.png')
    Label(window, image=Mbackground).place(x=-10, y=170)

    # Getting host name
    host = socket.gethostname()
    Label(window, text=f"ID: {host}", bg='white', fg='#000000').place(x=140, y=290)

    # Buttons for file selection and sending
    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg='#ffffff', fg='#000000',
           compound=CENTER,command = select_file).place(x=160, y=150)

    Button(window, text='SEND', width=8, height=1, font='arial 14 bold', bg='#ffffff', fg='#000000',
           compound=CENTER,command=sender).place(x=300, y=150)

    # Running the main event loop for the new window
    window.mainloop()





def recieve():
    window2 = Toplevel(root)
    window2.title('Recieve')
    window2.geometry("450x560+500+200")
    window2.config(bg='#f4fdfe')
    window2.resizable(False,False)

    def reciever():
        ID = SenderID.get()
        filename1 = incoming_file.get()

        s = socket.socket()
        port = 9090
        s.connect((ID,port))
        file = open(filename1,'wb')
        file_data = s.recv(1024)
        file.write(file_data)
        file.close()

        print("File has been recieved succesfully!")


    image_icon2 = PhotoImage(file='fileimages/recieve.png')
    window2.iconphoto(False,image_icon2)

    Sbackground = PhotoImage(file='fileimages/sender.png')
    Label(window2,image=Sbackground).place(x=-10,y=0)

    Mbackground = PhotoImage(file='fileimages/id.png')
    Label(window2,image=Mbackground).place(x=-10,y=170)

    Label(window2,text='Introduce senders ID:',font=('arial',10,'bold'),bg='#f4fdfe').place(x=20,y=340)

    SenderID = Entry(window2,width=25,fg='#000000',border=2,bg='#ffffff',font=('arial',15))
    SenderID.place(x=20,y=370)

    SenderID.focus()

    Label(window2,text='filename for the incoming file',font=('arial',10,'bold'),bg="#f4fdfe").place(x=20,y=420)
    incoming_file = Entry(window2,width=25,fg='#000000',border=2,bg='#ffffff',font=('arial',15))
    incoming_file.place(x=20,y=450)

    image_icon3 = PhotoImage(file='fileimages/recieve.png')
    rr = Button(window2,text = 'Recieve', compound=LEFT,image=image_icon3,width=130,bg='#39c790',font=('arial',14,'bold'),command=reciever)
    rr.place(x=20,y=500)



    window2.mainloop()



# icon
image_icon = PhotoImage(file="fileimages/logo.png")

# to apply it
root.iconphoto(False, image_icon)

# Label for the title
Label(root, text="File Transfer", font=("Acumin Variable Concept", 20,'bold'), bg='#f4fdfe').place(x=20, y=30)

# Separator frame
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

# Send button image
send_image = PhotoImage(file='fileimages/send.png')

# Creating the Send button
send = Button(root, image=send_image, bg="#f4fdfe", bd=0, command=send)

# Adjusting the position of the Send button
send.place(x=75, y=100)

# Receive button image
recieve_image = PhotoImage(file='fileimages/recieve.png')

# Creating the Receive button
recieve = Button(root, image=recieve_image, bg="#f4fdfe", bd=0,command=recieve)

# Adjusting the position of the Receive button
recieve.place(x=300, y=100)

# Label for Send File
Label(root, text='Send File', font=("Acumin Variable Concept", 17, 'bold'), bg='#f4fdfe').place(x=50, y=180)

# Label for Receive File
Label(root, text='Receive File', font=("Acumin Variable Concept", 17, 'bold'), bg='#f4fdfe').place(x=250, y=180)

background = PhotoImage(file='fileimages/background.png')
Label(root,image=background).place(x=-2,y=220)


# Running the main event loop to display the window
root.mainloop()

