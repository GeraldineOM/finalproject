from system import AppointmentSystem

if __name__ == "__main__":
    system = AppointmentSystem()

    print("=== Medical Appointment Scheduling System ===")

    doctor1 = system.register_doctor("Laura Gómez", "Pediatrics")
    doctor1.add_slot("2024-04-20", "09:00")
    doctor1.add_slot("2024-04-20", "10:00")

    patient1 = system.register_patient("Andrés Pérez", "123456789", "3100000000")

    system.schedule_appointment(patient1, doctor1, "2024-04-20", "09:00")

    system.show_appointments()
