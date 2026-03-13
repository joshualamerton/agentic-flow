from core.workflow import Workflow


def test_add_task():
    workflow = Workflow()
    workflow.add_task("analysis", lambda: None)
    assert "analysis" in workflow.tasks
