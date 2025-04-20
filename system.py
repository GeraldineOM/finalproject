from patient import Patient
from doctor import Doctor
from appointment import Appointment

class AppointmentSystem:
    def __init__(self):
        self.patients = []
        self.doctors = []
        self.appointments = []

    def register_patient(self, name, document, phone):
        patient = Patient(name, document, phone)
        self.patients.append(patient)
        return patient

    def register_doctor(self, name, specialty):
        doctor = Doctor(name, specialty)
        self.doctors.append(doctor)
        return doctor

    def schedule_appointment(self, patient, doctor, date, time):
        if (date, time) in doctor.available_slots:
            appointment = Appointment(patient, doctor, date, time)
            self.appointments.append(appointment)
            patient.add_appointment(appointment)
            doctor.remove_slot(date, time)
            print("\n✅ Appointment successfully scheduled.")
            return appointment
        else:
            print("\n⚠️  Selected time slot is not available.")
            return None

    def show_appointments(self):
        if not self.appointments:
            print("\nNo appointments scheduled.")
        else:
            print("\n📋 List of Scheduled Appointments:")
            for appointment in self.appointments:
                print("-", appointment.show_details())
