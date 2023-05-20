class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print("Task added successfully.")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print("Task marked as complete.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else " "
                print(f"{i}. [{status}] {task['description']}")
        else:
            print("No tasks found.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Complete Task")
        print("3. Display Tasks")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            description = input("Enter task description: ")
            todo_list.add_task({"description": description, "completed": False})
        elif choice == "2":
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.complete_task(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
