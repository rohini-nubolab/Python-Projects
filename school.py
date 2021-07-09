from prettytable import PrettyTable

class Registration:
    def __init__(self, name, fname, age, cid, surname, std, add, dob, fee):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.age = age
        self.cid = cid
        self.std = std
        self.add = add
        self.dob = dob
        self.fee = fee

    def write_file(self):
        file = open("School.txt", 'a')
        file.writelines('%-9s %-9s %-9s %-9s %-9s %-9s %-10s \n'%(self.name, self.surname, self.fname, self.age, self.std, self.add, self.dob))
        file.close()
        print("Student %s registered successfully" %(self.name))

    def read_file(self):
        file = open("School.txt", 'r')
        column_names = ["Name", "Surname", "Father Name", "Age", "Class", "Address", "DOB"]
        i = PrettyTable()
        i.field_names = column_names # ["Name", "Surname", "Father Name", "Age", "Class" , "Address", "DOB"])
        data = file.readlines()
        for line in data:
            words = line.split()
            i.add_row(words)
        file.close()
        print(i)


    def read_file_fee(self):
        file = open("Fee.txt", 'r')
        print("\n** FEES DETAILS **")
        column_names = ["Class", "Fees"]
        x = PrettyTable()
        x.field_names = column_names
        data = file.readlines()
        for line in data:
            words = line.split()
            x.add_row(words)
        file.close()
        print(x)

while True:
    print("=======================================")
    print("Student Management System")
    print("=======================================")
    print("1. Registration")
    print("2. Student Details")
    print("3. Fee Details")
    choice = int(input("Enter your choice : "))
    print("\n    ********* SCHOOL MANAGEMENT SYSTEM *********")
    if choice == 1:
        name = input("Enter Student Name: ")
        surname = input("Enter Surname: ")
        fname = input("Enter Father Name: ")
        age = int(input("Enter Age: "))
        std = input("Enter Class: ")
        add = input("Enter Address: ")
        dob = input("Enter DOB: ")
        print("=======================================")
        reg = Registration(name, fname, age, '', surname, std, add, dob)
        print(reg.name, reg.fname, reg.age, reg.surname, reg.std, reg.add, reg.dob)
        print("=======================================")

        reg.write_file()


    elif choice == 2:
        reg_1 = Registration('', '', '', '', '', '', '', '', '')
        reg_1.read_file()
    elif choice == 3:
        reg_2 = Registration('', '', '', '', '', '', '', '', '')
        reg_2.read_file_fee()
    else:
        print("Invalid choice")
        break
