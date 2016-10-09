class group:
    counter = 0

    def __init__(self, name, faculty, department):
        self.id = group.counter
        self.studid = []
        self.name = name
        self.faculty = faculty
        self.department = department
        group.counter += 1

    def print_group(self):
        print str(self.id)+ ': ' + self.name + ': ' + self.faculty + ' : ' + self.department \
              + ': ' + str(self.studid)

class student:
    counter = 0

    def __init__(self, fullname, age, group):
        self.fullname = fullname
        self.age = age
        self.id = student.counter
        self.group = group
        student.counter += 1

    def print_student(self):
        print str(self.id) + ': ' + self.fullname + ' : ' + str(self.age)+': '+ self.group


