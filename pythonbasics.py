# 🏥 Hospital Management System

# ✅ Data Types and Operations
hospital_name = "CITY CARE HOSPITAL"
total_doctors = 10
consultation_fee = 500.0
emergency_available = True

# ✅ List (Departments in the hospital)
departments = ["Cardiology", "Orthopedics", "Neurology", "Pediatrics"]

# ✅ Tuple (Doctors available)
doctors = ("Dr. Smith", "Dr. Johnson", "Dr. Lee", "Dr. Patel")

# ✅ Dictionary (Patient records)
patients = {
    "Alice": {"age": 30, "disease": "Flu", "doctor": "Dr. Smith"},
    "Bob": {"age": 45, "disease": "Fracture", "doctor": "Dr. Johnson"},
    "Charlie": {"age": 50, "disease": "Migraine", "doctor": "Dr. Lee"},
}

# ✅ Set (Emergency patients)
emergency_patients = {"Bob", "David"}


# ✅ Function to display hospital information
def display_hospital_info():
    info = f"🏥 Welcome to {hospital_name}\n"
    info += f"🔹 Total Doctors: {total_doctors} (Including Specialists)\n"
    info += f"🔹 Consultation Fee: ${consultation_fee:.2f}\n"
    info += f"🔹 Emergency Available: {'Yes' if emergency_available else 'No'}\n"
    info += f"🔹 Total Departments: {len(departments)}\n"
    info += f"🔹 Available Departments: {' '.join(departments)}"
    print(info)
    return info


# ✅ Function to display patient records
def display_patients():
    records = "📋 Patient Records:\n"
    for name, details in patients.items():
        records += f"🧑 {name} (Age: {details['age']}) - {details['disease']} (Doctor: {details['doctor']})\n"
    print(records)
    return records


# ✅ Function to check if a patient is in emergency
def check_emergency(patient_name):
    is_emergency = patient_name in emergency_patients
    if is_emergency:
        print(f"🚨 {patient_name} is an emergency patient!")
    else:
        print(f"✅ {patient_name} is not in emergency.")
    return is_emergency


# ✅ Main function to execute the program
def main():
    display_hospital_info()
    display_patients()

    print("🔎 Checking Emergency Patients...")
    check_emergency("Bob")
    check_emergency("Alice")




# ✅ Run the main function
if __name__ == "__main__":
    main()
