import json
import os

class ToDoList:
    def _init_(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        """Loads tasks from a file if it exists,otherwise returns ane mpty list."""
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                try:
                    return json.load(file)
                except json.JSONDecodeError:
                    return []
        return []

    def save_tasks(self):
        """Saves tasks to a file for persistence."""
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        """Adds a new task to the list."""
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task added: {task}")

    def mark_completed(self, task_number):
        """Marks a task as completed based on its index."""
        if 0 <= task_number < len(self.tasks):
            self.tasks[task_number]["completed"] = True
            self.save_tasks()
            print(f"Task marked as completed:{self.tasks[task_number]['task']}")
        else:
            print("Invalid task number!")

    def delete_task(self, task_number):
        """Removes a task from the list."""
        if 0 <= task_number < len(self.tasks):
            removed_task = self.tasks.pop(task_number)
            self.save_tasks()
            print(f"Task deleted: {removed_task['task']}")
        else:
            print("Invalid task number!")

    def show_tasks(self):
        """Displays all tasks with their status."""
        if not self.tasks:
            print("No tasks available.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{index + 1}. {task['task']} [{status}]")
            print()


def main():
    todo = ToDoList()

    while True:
        print("\nTo-Do List Menu")
        print("1.Add Task\n2.Mark Task as Completed\n3.Delete Task\n4.View Tasks\n5 Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("Task cannot be empty!")

        elif choice == "2":
            todo.show_tasks()
            try:
                index = int(input("Enter task number to mark as completed:"))-1
                todo.mark_completed(index)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            todo.show_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                todo.delete_task(index)
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            todo.show_tasks()

        elif choice == "5":
            print("Exiting... Your tasks are saved!")
            break

        else:
            print("Invalid choice! Please enter a valid option.")

if _name_ == "_main_":
    main()