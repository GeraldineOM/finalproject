class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

    def show_details(self):
        return f"Appointment with Dr. {self.doctor.name} ({self.doctor.specialty}) on {self.date} at {self.time} for {self.patient.name}"
