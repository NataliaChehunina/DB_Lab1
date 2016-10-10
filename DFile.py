from pickle import dump
from pickle import load

class dumper:

    @staticmethod
    def dump_to_file(list,filename):
        file = open(filename, 'wb')
        try:
            dump(list,file)
        except:
            print "Error while dumping file"
        file.close()

    @staticmethod
    def load_from_file(filename):
        try:
            file = open(filename, 'rb')
        except:
            file = open(filename, 'wb')
            file.close()
            return []
        try:
            return load(file)
        except:
            return []
        file.close()

    def clean_file(self, fname):
        file = open(fname, 'wb')
        file.close()