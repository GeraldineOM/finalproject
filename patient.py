class Patient:
    def __init__(self, name, document, phone):
        self.name = name
        self.document = document
        self.phone = phone
        self.scheduled_appointments = []

    def add_appointment(self, appointment):
        self.scheduled_appointments.append(appointment)

    def cancel_appointment(self, appointment):
        if appointment in self.scheduled_appointments:
            self.scheduled_appointments.remove(appointment)
