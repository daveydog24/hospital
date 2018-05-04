class Patient(object):
    patient_count = 0
    def __init__(self, name, allergies, hospital):
        self.name = name
        self.allergies = allergies
        self.hospital = hospital
        self.id = Patient.patient_count
        self.bed_num = None
        Patient.patient_count += 1

class Hospital(object):
    def __init__(self, hospital_name, capacity):
        self.hospital_name = hospital_name
        self.capacity = capacity
        self.patients = []
        self.beds = self.initialize_beds()

    def initialize_beds(self):
        beds = []
        for i in range(0, self.capacity):
            beds.append({
                "bed_id": i,
                "Available": True
            })
        return beds

    # def display_patients(self):
    #     for i in stored_patients:
    #         print "\n" + ("#" * 50)
    #         for key in i:
    #             if key == "hospital_name":
    #                 print "Hospital_name: {}".format(val)
    #             elif key == "capacity":
    #                 print "Capacity: {}".format(val)
    #             elif key == "name":
    #                 print "Patients Name: {}".format(val)
    #             elif key == "patient.name":
    #                 print "Patients ID: {}".format(val)                
    #             elif key == "allergies":
    #                 print "Patients allergies: {}".format(val)
    #         prints to end the block of information for seperation
    #         print "#" * 50
    #         print ""
    #     return self
        
    def admit_patient(self, patient):
        # if stored_patients == null:
        #     stored_patients = []
        if len(self.patients) <= self.capacity:
            self.patients.append(patient)
            for i in range(0, len(self.beds)):
                if self.beds[i]["Available"]:
                    patient.bed_num = self.beds[i]["bed_id"]
                    self.beds[i]["Available"] = False
                    break
            print "Patient #{} admitted to bed #{}".format(patient.id, patient.bed_num)
            # print "Patient Name: {}".format(patient.name)
            # print "Patient allergies: {}".format(patient.allergies)
            # print "Patient Hospital: {}".format(patient.hospital)
            # stored_patients[patient['id']].append(patient)
            # return stored_patients
        else:
            print "The Hospital is full, Sorry!"

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break
                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"
    
    def display_info(self):
        print "\n" + ("#" * 25)
        for key, val in self.__dict__.iteritems():
            if key == "hospital_name":
                print "Hospital_name: {}".format(val)
            elif key == "capacity":
                print "Capacity: {}".format(val)
            elif key == "name":
                print "Patients Name: {}".format(val)
            elif key == "patient.name":
                print "Patients ID: {}".format(val)                
            elif key == "allergies":
                print "Patients allergies: {}".format(val)
        print "#" * 25
        print ""

def handle_call():
    print "Would You like to make a call?"
    print "Type [1] for YES and [0] for NO and press return/enter"
    ans = raw_input()
    print ""
    return int(ans)
    
def take_call():
    print "What is your Name?"
    name = raw_input()
    print "What allergies do you have?"
    allergies = raw_input()
    print "What hospital would you like to go to?"
    hospital = raw_input()
    print "Please stay on the line while we proccess your call"
    print ""
    if hospital == "Northwest Hospital":
        patient = Patient(name, allergies, hospital)
        Northwest.admit_patient(patient)
    elif hospital == "Swedish":
        patient = Patient(name, allergies, hospital)
        Swedish.admit_patient(patient)
    elif hospital == "Fred Hutch":
        patient = Patient(name, allergies, hospital)
        Fred_Hutch.admit_patient(patient)
    print "you will have to call the other hospital sorry" 
Northwest = Hospital("Northwest Hospital", 500)
Swedish = Hospital("Swedish", 1000)
Fred_Hutch = Hospital("Fred Hutch", 2000)
game_on = True
while game_on:
    ring =  handle_call()
    if ring == 1:
       take_call()
    else:
        game_on = False
        print Northwest.display_info()
        print Swedish.display_info()
        print Fred_Hutch.display_info()