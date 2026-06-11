class TTBRule:

    def __init__(self, rule_id, description, severity):

        self.rule_id = rule_id
        self.description = description
        self.severity = severity

    def evaluate(self, text, product):

        raise NotImplementedError
