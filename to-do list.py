import tkinter as tk;
from tkinter import messagebox as msg;
from tkinter import ttk;


def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END,task)
        entry.delete(0,tk.END)
    else:
        msg.showwarning("Warning","please enter task")

def upd_task():
    try:
        index = listbox.curselection()[0]
        task = entry.get()
        if task:
            listbox.delete(index)
            listbox.insert(index,task)
            entry.delete(0,tk.END)
        else:
            msg.showwarning("Warning","Please enter a task")
    except IndexError:
        msg.showwarning("Warning","Please select a task to update")

def del_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
    except IndexError:
        msg.showwarning("Warning","Please select a task to delete")

def del_all():
    mb = msg.askyesno("Delete all","Are you sure?")
    if mb==True:
        listbox.delete(0,'end')

def mark():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(tk.END, f"{task} (Done)")
    except IndexError:
        msg.showwarning("Warning", "No task selected.")
        
window  = tk.Tk()
window.title("To-do list")
window.configure(bg="black")
window.geometry(newGeometry="500x670+1000+50")

listbox = tk.Listbox(window,width=35,font=('Arial 17'))
listbox.pack(pady=10)

entry = tk.Entry(window,width=38,font=('Arial 15'))
entry.pack(pady=10,padx=10)

add = tk.Button(window,text="Add Task",font=('Arial 10'),height="2",width="20", command=add_task)
add.pack(pady=10)

update = tk.Button(window,text="Update Task",font=('Arial 10'),height="2",width="20", command=upd_task)
update.pack(pady=10) 

delete = tk.Button(window,text="Delete Task", font=('Arial 10'),height="2",width="20",command=del_task)
delete.pack(pady=10)

del_all = tk.Button(window,text="Delete all",font=('Arial 10'),height="2",width="20",command = del_all)
del_all.pack(pady=10)

mark = del_all = tk.Button(window,text="Mark as done",font=('Arial 10'),height="2",width="20",command = mark)
mark.pack(pady=10)

window.mainloop()