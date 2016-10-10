import Database
from DFile import dumper
from Database import group
from Database import student

def printlist (list):
    if isinstance(list[0], Database.student):
        for elem in list:
            elem.print_student()
    elif isinstance(list[0], Database.group):
        for elem in list:
            elem.print_group()
    else:
        print "Wrong type!"

class database:

    def __init__(self, fgroups = None, fstudents = None):
        if fgroups is None or fstudents is None:
            self.fgroups = "groups.txt"
            self.fstudents = "students.txt"
            self.groups = []
            self.students = []
        else:
            self.fgroups = fgroups
            self.fstudents = fstudents
            self.groups = dumper.load_from_file(fgroups)
            group.counter = self.groups.pop(0)
            self.students = dumper.load_from_file(fstudents)
            student.counter = self.students.pop(0)

    def __del__(self):
        self.groups.insert(0, group.counter)
        self.students.insert(0, student.counter)
        dumper.dump_to_file(self.groups, self.fgroups)
        dumper.dump_to_file(self.students, self.fstudents)

    def force_dump(self):
        self.groups.insert(0, group.counter)
        self.students.insert(0, student.counter)
        dumper.dump_to_file(self.groups, self.fgroups)
        dumper.dump_to_file(self.students, self.fstudents)
        self.groups.pop(0)
        self.groups.pop(0)

    def print_groups(self):
        print "GROUPS : "
        for elem in self.groups:
            elem.print_group()

    def print_students(self):
        print "STUDENTS : "
        for elem in self.students:
            elem.print_student()

    def add_group(self, name, faculty, department):
        self.groups.append(group(name, faculty, department))

    def find_group(self, test, field = "id"):
        if field == "name":
            for el in self.groups:
                if el.name == test:
                    return el
        elif field == "faculty":
            for el in self.groups:
                if el.faculty == test:
                    return el
        elif field == "department":
            for el in self.groups:
                if el.department == test:
                    return el
        elif field == "id":
            for el in self.groups:
                if el.id == test:
                    return el
        else:
            print "No such field in groups!"
        print "No group was founded."
        return None

    def find_student(self, test, field = "id"):
        if field == "id":
            for el in self.students:
                if el.id == test:
                    return el
        if field == "fullname":
            for el in self.students:
                if el.fullname == test:
                    return el
        if field == "age":
            for el in self.students:
                if el.age == test:
                    return el
        else:
            print "No such field in student"
        print "No student was founded"
        return None

    def add_student(self, fullname, age, group_id):
        buff_group = self.find_group(group_id)
        print buff_group
        if buff_group is None:
            return
        else:
            stud = Database.student(fullname, age, buff_group.name)
            self.students.append(stud)
            self.groups[self.groups.index(buff_group)].studid.append(stud.id)

    def del_student(self, id):
        el = self.find_student(id)
        self.find_group(el.group, "name").studid.remove(id)
        self.students.remove(el)

    def del_group(self, id):
        el = self.find_group(id)
        stud = list(el.studid)
        for i in stud:
            self.del_student(i)
        self.groups.remove(el)

    def modify_student(self, id, field, value):
        el = self.find_student(id)
        if el is None:
            print "Wrong id"
        else:
            if field == "fullname":
                el.fullname = value
            elif field == "age":
                el.age = value
            elif field == "group":
                st = self.find_student(id)
                gr = self.find_group(st.group, "name")
                if gr is None:
                    print "Wrong group id!"
                    return
                else:
                    gr.studid.remove(id)
                gr = self.find_group(value)
                el.group = gr.name
                gr.studid.append(id)
            else:
                print "wrong field"

    def modify_group(self, id, field, value):
        el = self.find_group(id)
        if el is None:
            print "Wrong id"
        else:
            if field == "name":
                el.name = value;
            elif field == "faculty":
                el.faculty = value
            elif field == "department":
                el.department = value
            else:
                print "wrong field"
        return

    def find_youngest(self):
        res = []
        for group in self.groups:
            youngest = self.find_student(group.studid[0])
            for id in group.studid:
                stud = self.find_student(id)
                if stud.age < youngest.age:
                    youngest = stud
            res.append(youngest)
        return res