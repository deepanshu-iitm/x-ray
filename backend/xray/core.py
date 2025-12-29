from datetime import datetime
import uuid

class XRayStep:
    def __init__(self, step_name, input_data=None):
        self.step_id = str(uuid.uuid4())
        self.step_name = step_name
        self.timestamp = datetime.utcnow().isoformat()

        self.input = input_data or {}
        self.rules = {}
        self.evaluations = []
        self.output = {}
        self.reasoning = ""

    def add_rule(self, name, value):
        self.rules[name] = value

    def evaluate(self, item_id, passed, reason):
        self.evaluations.append({
            "item_id": item_id,
            "passed": passed,
            "reason": reason
        })

    def set_output(self, output):
        self.output = output

    def set_reasoning(self, reasoning):
        self.reasoning = reasoning

    def to_dict(self):
        return {
            "step_id": self.step_id,
            "step_name": self.step_name,
            "timestamp": self.timestamp,
            "input": self.input,
            "rules": self.rules,
            "evaluations": self.evaluations,
            "output": self.output,
            "reasoning": self.reasoning
        }


class XRayExecution:
    def __init__(self):
        self.execution_id = str(uuid.uuid4())
        self.start_time = datetime.utcnow().isoformat()
        self.steps = []

    def add_step(self, step: XRayStep):
        self.steps.append(step)

    def finish(self):
        self.end_time = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "execution_id": self.execution_id,
            "start_time": self.start_time,
            "end_time": getattr(self, "end_time", None),
            "steps": [s.to_dict() for s in self.steps]
        }
