class Task:
    def __init__(self, name, func, depends_on=None):
        self.name = name
        self.func = func
        self.depends_on = depends_on or []
        self.completed = False


class Workflow:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, func, depends_on=None):
        self.tasks[name] = Task(name, func, depends_on)

    def ready_tasks(self):
        ready = []
        for task in self.tasks.values():
            if task.completed:
                continue
            if all(self.tasks[dep].completed for dep in task.depends_on):
                ready.append(task)
        return ready

    def mark_complete(self, task_name):
        self.tasks[task_name].completed = True
