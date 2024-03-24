import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")
        self.master.geometry("400x300")  # Setting initial window size

        # Colorful background
        self.master.config(bg="#f0f0f0")

        # Initialize tasks list
        self.tasks = []

        # Task input field
        self.task_entry = tk.Entry(master, width=30, bd=2, relief="groove")
        self.task_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="ew")

        # Add Task button
        self.add_button = tk.Button(master, text="Add Task", command=self.add_task, bg="#77dd77", bd=2, relief="raised")
        self.add_button.grid(row=0, column=2, padx=5, pady=10, sticky="ew")

        # Task list
        self.task_listbox = tk.Listbox(master, width=50, height=10, bd=2, relief="groove")
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=5, sticky="nsew")

        # Delete Task button
        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task, bg="#ff6961", bd=2, relief="raised")
        self.delete_button.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        # Update Task button
        self.update_button = tk.Button(master, text="Update Task", command=self.update_task, bg="#aec6cf", bd=2, relief="raised")
        self.update_button.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        # Exit button
        self.exit_button = tk.Button(master, text="Exit", command=self.exit_app, bg="#f8d6ff", bd=2, relief="raised")
        self.exit_button.grid(row=2, column=2, padx=10, pady=5, sticky="ew")

        # Configure row and column weights
        master.grid_rowconfigure(1, weight=1)
        master.grid_columnconfigure(0, weight=1)
        master.grid_columnconfigure(1, weight=1)
        master.grid_columnconfigure(2, weight=1)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task field cannot be empty!")

    def delete_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            del self.tasks[index]
            self.task_listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def update_task(self):
        try:
            index = self.task_listbox.curselection()[0]
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[index] = updated_task
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task field cannot be empty!")
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")

    def exit_app(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
