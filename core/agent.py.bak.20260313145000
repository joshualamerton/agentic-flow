class Agent:
    def __init__(self, name, capabilities):
        self.name = name
        self.capabilities = set(capabilities)

    def can_run(self, task_name):
        return task_name in self.capabilities

    def run(self, task):
        print(f"{self.name} executing task: {task.name}")
        task.func()
