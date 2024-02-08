import tkinter as tk
from tkinter import messagebox
import webbrowser

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.todo_list = self.load_todo_list()

        self.task_entry = tk.Entry(root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=30)
        self.task_listbox.pack(pady=10)

        self.scrollbar = tk.Scrollbar(root, command=self.task_listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)

        self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
        self.remove_button.pack(side=tk.BOTTOM, fill=tk.X, pady=10)

        github_label = tk.Label(
            root,
            text="GitHub",
            cursor="hand2",  
            foreground="blue",
            underline=True
        )
        github_label.pack(pady=5)
        github_label.bind("<Button-1>", lambda event: webbrowser.open("https://github.com/iW3ll"))

        self.update_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
            self.save_todo_list()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            self.todo_list.pop(selected_index[0])
            self.update_task_list()
            self.save_todo_list()

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.todo_list:
            self.task_listbox.insert(tk.END, task)

        self.task_listbox.yview(tk.END)

    def save_todo_list(self):
        with open("todo_list.txt", "w") as file:
            for task in self.todo_list:
                file.write(task + "\n")

    def load_todo_list(self):
        todo_list = []
        try:
            with open("todo_list.txt", "r") as file:
                todo_list = [line.strip() for line in file.readlines()]
        except FileNotFoundError:
            pass
        return todo_list

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(300, 300)
    app = TodoApp(root)
    root.mainloop()
