class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty
        self.available_slots = []

    def add_slot(self, date, time):
        self.available_slots.append((date, time))

    def show_slots(self):
        return self.available_slots

    def remove_slot(self, date, time):
        if (date, time) in self.available_slots:
            self.available_slots.remove((date, time))
