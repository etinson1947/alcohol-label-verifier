import hashlib
import json
import time


class ImmutableAuditLog:

    def __init__(self):

        self.chain = []

    def _hash(self, data: str) -> str:

        return hashlib.sha256(
            data.encode("utf-8")
        ).hexdigest()

    def write_event(self, event: dict):

        previous_hash = (
            self.chain[-1]["hash"]
            if self.chain else "GENESIS"
        )

        payload = {
            "timestamp": time.time(),
            "event": event,
            "previous_hash": previous_hash
        }

        block_string = json.dumps(payload, sort_keys=True)

        block_hash = self._hash(block_string)

        block = {
            "payload": payload,
            "hash": block_hash
        }

        self.chain.append(block)

        return block