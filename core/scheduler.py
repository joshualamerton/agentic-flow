class Scheduler:
    def __init__(self, workflow):
        self.workflow = workflow
        self.agents = []

    def register_agent(self, agent):
        self.agents.append(agent)

    def run(self):
        while True:
            ready = self.workflow.ready_tasks()
            if not ready:
                break

            progress = False

            for task in ready:
                for agent in self.agents:
                    if agent.can_run(task.name):
                        agent.run(task)
                        self.workflow.mark_complete(task.name)
                        progress = True
                        break

            if not progress:
                print("No compatible agent found for remaining ready tasks.")
                break
