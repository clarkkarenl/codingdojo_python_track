# Assignment: Hospital
# Karen Clark
# 2018-07-06

# ================================================================
# NOTE:
# I struggled with this one quite a bit. I finally gave up and...
# 1. watched Minh's code review for Hospital
# 2. looked at the solution
# 3. realized I needed to invoke the Hospital functions 
#  differently than I was
# ================================================================

# You're going to build a hospital with patients in it! Create a hospital class.
# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?
# Patient:
# Attributes:
# * Id: an id number
# * Name
# * Allergies
# * Bed number: should be none by default
class Patient(object):
    PATIENT_COUNT = 0
    def __init__(self, name, allergies):
        self.name = name
        self.allergies = allergies
        self.id = Patient.PATIENT_COUNT
        self.bed_num = None
        Patient.PATIENT_COUNT += 1

    def patient_info(self):
        print "Patient id:", self.id
        print "Patient name:", self.name
        print "Allergies:", self.allergies
        print "Bed id:", self.bed_num

# Hospital
# Attributes:
# * Patients: an empty array
# * Name: hospital name
# * Capacity: an integer indicating the maximum number of patients the hospital can hold.
class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "bed_id": i,
                "available" : True
            })
        return beds

# * Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
    def admit(self, patient):
        if len(self.patients) <= self.capacity:
            self.patients.append(patient) 
            for i in range(0, len(self.beds)):
                if self.beds[i]['available']:
                    patient.bed_num = self.beds[i]['bed_id']
                    self.beds[i]['available'] = False
                    break
            print "Patient {} admitted to bed {}".format(patient.id, patient.bed_num)
        else:
            print "Hospital", self.name, " is full."


    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.beds:
                    if bed['bed_id'] == patient.bed_num:
                        bed['available'] = True
                        break

                self.patients.remove(patient)
                print "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)


    def hospital_info(self):
        print "Hospital name:", self.name
        print "Patient capacity:", self.capacity
        print "Patient list:"
        for p in self.patients:
            print "* Patient", p.name, "- bed", p.bed_num
        return self


p1 = Patient("John Smith", "Penicillin")
p2 = Patient("Mary Johnson", "None")
p3 = Patient("Allen Wrench", "Iron")
p4 = Patient("M'baku", "None")

h1 = Hospital("St. John", 3)
h1.admit(p1)
h1.admit(p4)
h1.admit(p2)
print "discharging p2 (p2.id = 2)"
h1.discharge(p2.id)
h1.admit(p3)
h1.hospital_info()