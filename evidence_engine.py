import time


class EvidenceEngine:

    def __init__(self):

        self.evidence_store = []

    def record(self, control_id, event, metadata):

        self.evidence_store.append({

            "timestamp": time.time(),

            "control_id": control_id,

            "event": event,

            "metadata": metadata
        })

    def get_evidence(self):

        return self.evidence_store