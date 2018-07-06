# Assignment: Hospital
# Karen Clark
# 2018-07-06

# You're going to build a hospital with patients in it! Create a hospital class.
# Before looking at the requirements below, think about the potential characteristics of each patient and hospital. How would you design each?
# Patient:
# Attributes:
# * Id: an id number
# * Name
# * Allergies
# * Bed number: should be none by default
class Patient(object):
    def __init__(self, name, allergies, bed_num=None):
        self.name = name
        self.allergies = allergies
        self.bed_num = bed_num

    def patient_info(self):
        print self.name
        print self.allergies
        print self.bed_num

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
        self.beds = []


    # def assign_bed(self, bed_num):
    #     Patient.bed_num = bed_num
    #     return self

    def bed_list(self):
        for bed in self.beds:
            print bed
        return self

    def admit(self, patient):
        
        # keep a list of beds
        # if beds full, reject request
        # else give the patient a bed num
        # update bed_num value on patient
        # Patient.bed_num = bed_num
        # if that is successful, add patient to list
        self.patients.append(patient) 


# Methods:
# * Admit: add a patient to the list of patients. Assign the patient a bed number. If the length of the list is >= the capacity do not admit the patient. Return a message either confirming that admission is complete or saying the hospital is full.
# * Discharge: look up and remove a patient from the list of patients. Change bed number for that patient back to none.
# This is a challenging assignment. Ask yourself what input each method requires and what output you will need.

p1 = Patient("John", "Penicillin")
p1.assign_bed(2).patient_info()