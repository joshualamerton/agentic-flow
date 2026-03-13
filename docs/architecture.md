# AgentFlow Architecture

AgentFlow is a lightweight execution layer for multi-agent workflows.

## Core components

### Workflow
Defines tasks and dependency relationships between tasks.

### Agent
Represents a worker with a set of capabilities.

### Scheduler
Determines which tasks are ready to run and assigns them to compatible agents.

## Execution model

1. Tasks are added to a workflow.
2. Each task may depend on one or more prior tasks.
3. Agents register their capabilities.
4. The scheduler selects tasks whose dependencies are satisfied.
5. Compatible agents execute the task.
6. Completed tasks unlock downstream tasks.

## Goal

The system is designed to explore workflow orchestration for agent systems rather than simple prompt-based execution.
