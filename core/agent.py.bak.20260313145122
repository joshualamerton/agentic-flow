```python
class Task:
    """Represents a task that can be executed by an Agent."""
    def __init__(self, name, func):
        """
        Initializes a Task instance.

        Args:
            name (str): The name of the task.
            func (callable): The function to be executed when the task is run.
        """
        self.name = name
        self.func = func

class Agent:
    """Represents an agent that can execute tasks."""
    def __init__(self, name, capabilities):
        """
        Initializes an Agent instance.

        Args:
            name (str): The name of the agent.
            capabilities (list[str]): A list of task names that the agent can execute.
        """
        self.name = name
        self.capabilities = set(capabilities)

    def can_run(self, task_name):
        """
        Checks if the agent can execute a task.

        Args:
            task_name (str): The name of the task to check.

        Returns:
            bool: True if the agent can execute the task, False otherwise.
        """
        return task_name in self.capabilities

    def run(self, task):
        """
        Executes a task.

        Args:
            task (Task): The task to be executed.
        """
        print(f"{self.name} executing task: {task.name}")
        task.func()


# Example usage:
def greet():
    print("Hello!")

def farewell():
    print("Goodbye!")

task1 = Task("Greet", greet)
task2 = Task("Farewell", farewell)

agent = Agent("John", ["Greet", "Farewell"])

print(agent.can_run("Greet"))  # Output: True
print(agent.can_run("Unknown"))  # Output: False

agent.run(task1)  # Output: John executing task: Greet
agent.run(task2)  # Output: John executing task: Farewell
```