```python
class Task:
    """
    Represents a task in a workflow.

    Attributes:
        name (str): The name of the task.
        func (callable): The function to be executed when the task is completed.
        depends_on (list[str], optional): The names of tasks that must be completed before this task. Defaults to an empty list.
        completed (bool): Whether the task has been completed.
    """

    def __init__(self, name: str, func: callable, depends_on: list[str] = None):
        """
        Initializes a new Task instance.

        Args:
            name (str): The name of the task.
            func (callable): The function to be executed when the task is completed.
            depends_on (list[str], optional): The names of tasks that must be completed before this task. Defaults to an empty list.
        """
        self.name = name
        self.func = func
        self.depends_on = depends_on or []
        self.completed = False


class Workflow:
    """
    Represents a workflow consisting of tasks.

    Attributes:
        tasks (dict[str, Task]): A dictionary of tasks in the workflow, keyed by task name.
    """

    def __init__(self):
        """
        Initializes a new Workflow instance.
        """
        self.tasks = {}

    def add_task(self, name: str, func: callable, depends_on: list[str] = None):
        """
        Adds a new task to the workflow.

        Args:
            name (str): The name of the task.
            func (callable): The function to be executed when the task is completed.
            depends_on (list[str], optional): The names of tasks that must be completed before this task. Defaults to an empty list.
        """
        self.tasks[name] = Task(name, func, depends_on)

    def get_ready_tasks(self) -> list[Task]:
        """
        Returns a list of tasks that are ready to be completed, i.e., all dependencies have been completed.

        Returns:
            list[Task]: A list of ready tasks.
        """
        ready = []
        for task in self.tasks.values():
            if task.completed:
                continue
            if all(self.tasks[dep].completed for dep in task.depends_on):
                ready.append(task)
        return ready

    def mark_task_complete(self, task_name: str):
        """
        Marks a task as completed.

        Args:
            task_name (str): The name of the task to mark as completed.
        """
        self.tasks[task_name].completed = True
```

```python
# Example usage:
def task1():
    print("Task 1 completed")

def task2():
    print("Task 2 completed")

def task3():
    print("Task 3 completed")

workflow = Workflow()
workflow.add_task("task1", task1)
workflow.add_task("task2", task2, ["task1"])
workflow.add_task("task3", task3, ["task1", "task2"])

ready_tasks = workflow.get_ready_tasks()
for task in ready_tasks:
    print(f"Ready to complete: {task.name}")

workflow.mark_task_complete("task1")
workflow.mark_task_complete("task2")

ready_tasks = workflow.get_ready_tasks()
for task in ready_tasks:
    print(f"Ready to complete: {task.name}")
```