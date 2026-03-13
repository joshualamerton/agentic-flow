```python
from core.workflow import Workflow

def test_add_task():
    """
    Test adding a task to the workflow.

    This test case checks if a task can be successfully added to the workflow.
    """
    # Create a new workflow instance
    workflow = Workflow()
    
    # Add a task with a name and a function that does nothing
    workflow.add_task("analysis", lambda: None)
    
    # Assert that the task is present in the workflow's tasks
    assert "analysis" in workflow.tasks
```