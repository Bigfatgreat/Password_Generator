from tkinter import *
from random import randint
def passGenerator():
    root = Tk()
    root.title('Password Generator')

    root.geometry("500x300")

#Open https://www.asciitable.com/ and you'll see that 32 stands for space which we don't want that in password

    my_password = chr(randint(33,126))

    def new_rand():
        """ Clear the entry box """
        pw_entry.delete(0,END)

        #Get PW length
        pw_length = int(my_entry.get())
        #random letters loop
        my_password = ''
        for x in range(pw_length):
            my_password += chr(randint(33,126))
    
        pw_entry.insert(0,my_password)


    def clipper():
    #clear the Clipboard
        root.clipboard_clear()
    #Copy to clipboard
        root.clipboard_append(pw_entry.get())

    lf = LabelFrame(root, text = " How many characters? ")
    lf.pack(pady=20)

        #TODO Create Entry Box to disignate the number of character
    my_entry = Entry(lf,font = ('Helvetica',24) )
    my_entry.pack(pady=20,padx = 20) #Padding for more space in entry box

#? After create a password I want to get the value and copy paste it
    #TODO Create Entry Box for the returned password
    pw_entry = Entry(root, text= '', font=('Helvetica',24),bd=0,)
    pw_entry.pack(pady=20)

    #TODO Create Frame for the buttons
    my_frame = Frame(root)
    my_frame.pack(pady=20)

    #TODO Create buttons
    my_button = Button(my_frame, text = 'Generate Password',command = new_rand)
    my_button.grid(row=0, column=0, padx=10)

    clip_button = Button(my_frame,text= 'Copy To Clipboard', command = clipper)
    clip_button.grid(row=0, column=1, padx=10)



    root.mainloop()