from prettytable import PrettyTable

class Registration:
    def __init__(self, name, fname, age, sid, surname, std, add, dob):
        self.name = name
        self.surname = surname
        self.fname = fname
        self.age = age
        self.sid = sid
        self.std = std
        self.add = add
        self.dob = dob

    def write_file(self):
        file = open("School.txt", 'a')
        file.writelines('%-9s %-9s %-9s %-9s %-9s %-9s %-9s %-10s \n' %(self.sid, self.name, self.surname, self.fname, self.age, self.std, self.add, self.dob))
        file.close()
        print("Student %s %sregistered successfully" %(self.sid, self.name))
        print("Student %d deleted" %(self.sid))

    def read_file(self, display = False):
        file = open("School.txt", 'r')
        data = file.readlines()
        if not display:
            if len(data) == 0:
                return 'SID_1'
            else:
                return 'SID_%s' % str(len(data)+1)
        column_names = ["SID", "Name", "Surname", "Father Name", "Age", "Class", "Address", "DOB"]
        i = PrettyTable()
        i.field_names = column_names
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

    def delete_record(self, sid):
        file = open("School.txt", 'r')

        data = file.readlines()
        flag = False
        new_data = " "
        for line in data:
            words = line.split()
            if words[0] == sid:
               flag = True
            else:
                new_data = new_data + line
        if not flag:
           print("Student record not found")
        else:
            print("Deleted", sid)
        file.close()
        print(new_data)
        file = open("School.txt", 'w')
        file.writelines('%s' % (new_data))
        file.close()

while True:
    print("Student Management System")
    print("1. Registration")
    print("2. Student Details")
    print("3. Fee Details")
    print("4. Delete Student Record")
    choice = int(input("Enter your choice : "))
    print("\n  ********* SCHOOL MANAGEMENT SYSTEM *********")
    if choice == 1:
        name = input("Enter Student Name: ")
        surname = input("Enter Surname: ")
        fname = input("Enter Father Name: ")
        age = int(input("Enter Age: "))
        std = input("Enter Class: ")
        add = input("Enter Address: ")
        dob = input("Enter DOB: ")
        reg = Registration(name, fname, age, '', surname, std, add, dob)
        reg.sid = reg.read_file(False)
        reg.write_file()
    elif choice == 2:
        reg_1 = Registration('', '', '', '', '', '', '', '')
        reg_1.read_file(True)
    elif choice == 3:
        reg_2 = Registration('', '', '', '', '', '', '', '')
        reg_2.read_file_fee()
    elif choice == 4:
        sid = input("Enter Student ID to be deleted: ")
        reg_3 = Registration('', '', '', '', '', '', '', '')
        reg_3.delete_record(sid)
    else:
        print("Invalid choice")
        break
