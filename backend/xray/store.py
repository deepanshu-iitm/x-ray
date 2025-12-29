EXECUTIONS = {}

def save_execution(execution):
    EXECUTIONS[execution.execution_id] = execution

def get_execution(execution_id):
    return EXECUTIONS.get(execution_id)

def get_all_executions():
    return EXECUTIONS
