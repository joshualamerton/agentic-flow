from core.workflow import Workflow
from core.agent import Agent
from core.scheduler import Scheduler


def analyze_data():
    print("Analyzing market data...")


def generate_report():
    print("Generating investment report...")


def send_email():
    print("Sending report to stakeholders...")


def main():
    workflow = Workflow()

    workflow.add_task("analysis", analyze_data)
    workflow.add_task("report", generate_report, depends_on=["analysis"])
    workflow.add_task("email", send_email, depends_on=["report"])

    analysis_agent = Agent("analysis_agent", capabilities=["analysis"])
    report_agent = Agent("report_agent", capabilities=["report", "email"])

    scheduler = Scheduler(workflow)
    scheduler.register_agent(analysis_agent)
    scheduler.register_agent(report_agent)

    scheduler.run()


if __name__ == "__main__":
    main()
