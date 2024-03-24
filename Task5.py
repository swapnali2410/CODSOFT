from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg='#d1e7f5') 
root.title('Contact Book')
root.resizable(0, 0)

# Sample contact list
contactlist = [
    ['Sreeja mhatre', '369854712'],
    ['Gauresh Patil', '521155222'],
    ['Abhimanyu shukla', '78945614'],
    ['Sakshi Gaikwad', '58745246'],
    ['Mohit Patil', '5846975'],
]

Name = StringVar()
Number = StringVar()

frame = Frame(root)
frame.pack(side=RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Arial', 14), bg="#f2f2f2", width=20, height=20,
                 borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
    else:
        return int(select.curselection()[0])


def AddContact():
    if Name.get() != "" and Number.get() != "":
        contactlist.append([Name.get(), Number.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill in all the information")


def UpdateDetail():
    if Name.get() and Number.get():
        contactlist[Selected()] = [Name.get(), Number.get()]
        messagebox.showinfo("Confirmation", "Contact Updated Successfully")
        EntryReset()
        Select_set()
    elif not (Name.get()) and not (Number.get()) and not (len(select.curselection()) == 0):
        messagebox.showerror("Error", "Please fill in the information")
    else:
        if len(select.curselection()) == 0:
            messagebox.showerror("Error", "Please Select the Name and press Load button")
        else:
            messagebox.showerror("Error", "To load all information of the selected row, press Load button.")


def EntryReset():
    Name.set('')
    Number.set('')


def Delete_Entry():
    if len(select.curselection()) != 0:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result == True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the contact')


def VIEW():
    if len(select.curselection()) != 0:
        NAME, PHONE = contactlist[Selected()]
        Name.set(NAME)
        Number.set(PHONE)
    else:
        messagebox.showerror("Error", 'Please select the contact')


def EXIT():
    root.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone in contactlist:
        select.insert(END, name)


Select_set()

Label(root, text='Name', font=("Arial", 18, "bold"), bg='#d1e7f5').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Arial", 18, "bold"), bg='#d1e7f5').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)

Button(root, text="Add", font='Arial 16 bold', bg='#a5d8f3', command=AddContact, padx=20).place(x=50, y=140)
Button(root, text="Edit", font='Arial 16 bold', bg='#a5d8f3', command=UpdateDetail, padx=20).place(x=50, y=200)
Button(root, text="Delete", font='Arial 16 bold', bg='#a5d8f3', command=Delete_Entry, padx=20).place(x=50, y=260)
Button(root, text="View", font='Arial 16 bold', bg='#a5d8f3', command=VIEW, padx=20).place(x=50, y=320)
Button(root, text="Reset", font='Arial 16 bold', bg='#a5d8f3', command=EntryReset, padx=20).place(x=50, y=380)
Button(root, text="Exit", font='Arial 20 bold', bg='#fa5765', command=EXIT).place(x=250, y=470)

root.mainloop()
