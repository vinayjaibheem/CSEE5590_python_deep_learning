class Patient:                 #class Patient
    def __init__(self,fname,lname,age,dob):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.dob = dob

    def getPatientInfo(self):      #Displaying patient info
        print("The first name of patient is",self.fname)
        print("The last name of patient is", self.lname)
        print("The age of patient is", self.age)
        print("The DOB of patient is ", self.dob,"\n")
        #print("\n")

class Doctor:         #class Doctor
    def __init__(self,fname,lname,contact):
        self.fname = fname
        self.lname = lname
        self.cno = contact

    def getDoctorInfo(self):      #Displaying Doctor info
        print("The first name of doctor is",self.fname)
        print("The last name of doctor is", self.lname)
        print("The contact number of doctor is", self.cno)
        print("\n")

class Appointment(Patient,Doctor):   #class Appointment     #Multiple inheritance from Base classes Patient and Doctor classes
    def __init__(self,fname,lname,age,dob,dfname,dlname,contact,time,date):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.dob = dob
        self.fname = dfname
        self.lname = dlname
        self.cno = contact
        self.time = time
        self.date = date
    def takeAppointment(self):   #Displaying time and date of appointment
        print("The time for the appointment is",self.time)
        print("The date of appointment is",self.date)
        print("\n")

class Nurse(Patient):   #class Nurse      #Inheriting Patient class into Nurse class
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact
    def getNurseInfo(self):         #Getting nurse information
        print("Name of Nurse is",self.name)
        print("Contact number of Nurse is",self.contact,"\n")

class HealthProblems(Patient):      #class HealthProblems
    def __init__(self,type,severity):
        super().__init__(fname="Stacy",lname="Mathews",age="56",dob="4th may") #using super function to overrite the init constructor
        self.__type = type  #using private data menbers type and severity
        self.__severity = severity
    def getHealth(self):        #getting health type and severity
        print("Type of disease is",self.__type)
        print("Severity of disease is",self.__severity,"\n")

patient1 = Patient("Fatema","Hasta","26","May")
print("****************************Patient 1*************************")
patient1.getPatientInfo()

patient2 = Patient("Sejal","Kalan","26","May")
print("****************************Patient 2*************************")
patient2.getPatientInfo()

doctor1 = Doctor("Dr Alex","Morrow","123456789")
print("****************************Doctor 1*************************")
doctor1.getDoctorInfo()

doctor2 = Doctor("Dr Rach","Green","63787729")
print("****************************Doctor 2*************************")
doctor2.getDoctorInfo()


appointment1 = Appointment("Fatema","Hasta","26","May","Dr Alex","Morrow","123456789","8:30 am","23rd May")
print("****************************Appointment 1*************************")
appointment1.getPatientInfo()
appointment1.getDoctorInfo()
appointment1.takeAppointment()

appointment2 = Appointment("Sejal","Kalan","26","May","Dr Rach","Green","63787729","8 am","1st May")
print("****************************Appointment 2*************************")
appointment2.getPatientInfo()   #using object of appointment class to call definition of Patient class
appointment2.getDoctorInfo()
appointment2.takeAppointment()

nurse1 = Nurse("Stacia","123456789")
print("****************************Nurse Information during Emergency*************************")
nurse1.getNurseInfo()

health = HealthProblems("Diabetes","type1")
print("****************************Severity of disease of Patient Stacy*************************")
health.getPatientInfo()
health.getHealth()

