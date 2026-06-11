class NISTControl:

    def __init__(self, control_id, family, description):

        self.control_id = control_id
        self.family = family
        self.description = description


NIST_CONTROLS = [

    NISTControl(
        "AC-2",
        "Access Control",
        "Account Management"
    ),

    NISTControl(
        "AU-2",
        "Audit and Accountability",
        "Event Logging"
    ),

    NISTControl(
        "SC-8",
        "System and Communications Protection",
        "Transmission Protection"
    ),

    NISTControl(
        "SI-4",
        "System Monitoring",
        "Threat Detection"
    )
]
