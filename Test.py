
import Database
from Logic import database


def printmenu():
    print('1 - Print Database \0')
    print('2 - Modificate element \0')
    print('3 - Add element \0')
    print('4 - Delete element \0')
    print('5 - Search \0')
    print('6 - Exit \0')

def autofill(db):
    db.add_group("kv41", "fam", "spscs")
    db.add_group("kv42", "fam", "spscs")
    db.add_group("kv43", "fam", "spscs")
    db.add_student("Alexandr", 19, 2)
    db.add_student("Leoid", 20, 2)
    db.add_student("Ivan", 19, 2)
    db.add_student("Vladislav", 19, 2)

    db.add_student("Oleg", 20, 1)
    db.add_student("Anna", 19, 1)
    db.add_student("Valentin", 18, 1)

    db.add_student("Alexandr", 21, 0)
    db.add_student("yuriy", 19, 0)
    db.add_student("bogdan", 23, 0)
    db.add_student("mariya", 19, 0)

def menu(auto = False):
    db = database()
    if auto:
        autofill(db)
    #printmenu()
    flag = True
    while True:
        printmenu()
        key = input()
        if key == 1:
            db.print_groups()
            db.print_students()
        elif key == 2:
            print('1 - Modify student \0')
            print('2 - Modify group \0')
            key1 = input()
            if key1 == 1:
                print "student's id:"
                id = input()
                print "field:"
                field = input()
                print "value:"
                value = input()
                db.modify_student(id, field, value)
            elif key1 == 2:
                print "group id"
                id = input()
                print "field:"
                field = input()
                print "value:"
                value = input()
                db.modify_group(id, field, value)
            else:
                print "Wrong key!"
        elif key == 3:
            print('1 - Add group \0')
            print('2 - Add student \0')
            key1 = input()
            if key1 == 1:
                print "name:"
                name = input()
                print "faculty:"
                fac = input()
                print "department:"
                dep = input()
                db.add_group(name,fac,dep)
            elif key1 == 2:
                print "fullname:"
                name = input()
                print "age:"
                age = input()
                print "group:"
                grp = input()
                db.add_student(name, age, grp)
            else:
                print"Wrong key!"
        elif key == 4:
            print('1 - Delete group \0')
            print('2 - Delete student \0')
            key1 = input()
            if key1 == 1:
                print('Group id \0')
                id = input()
                db.del_group(id)
               # printmenu()
            elif key1 == 2:
                print('Student id \0')
                id = input()
                db.del_student(id)
            else:
                print"Wrong key!"
        elif key == 5:
            lst = db. find_youngest()
            for i in lst:
                i.print_student()
        elif key == 6:
            break;
        else:
            print "Wrong key!"

menu(True)


# db = database()
# db.add_group("kv43", "fam", "spscs")
# db.add_student("Vitaliy", 19, 0)
# db.add_student("Alexandr", 21, 0)
# db.add_student("Yuriy", 21, 0)
# db.add_group("kv41", "fam", "spscs")
# db.print_groups()
# db.print_students()
# db.add_student("Innokentiy", 19, 1)
#
# #db.del_student(1)
# #db.del_group(0)
# db.print_groups()
# db.print_students()






