#from Logic import dbfill
import Database
from Logic import database


def test():
    print('1 - Print Database \0')
    print('2 - Modificate element \0')
    print('3 - Add element \0')
    print('4 - Delete element \0')
    print('5 - Search \0')
    print('6 - Exit \0')
    return  input()

db = database()
db.add_group("kv43", "fam", "spscs")
db.add_student("Vitaliy", 19, 0)
db.add_student("Alexandr", 21, 0)
db.add_student("Yuriy", 21, 0)
db.add_group("kv41", "fam", "spscs")
db.print_groups()
db.print_students()
db.add_student("Innokentiy", 19, 1)

#db.del_student(1)
#db.del_group(0)
db.print_groups()
db.print_students()

