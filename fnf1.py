from sys import argv

script,fname = argv

def disp(f):
    print f.read()

def rewind(f):
    f.seek(0)
cf=open(fname)
print "Display file contents"

disp(open(fname))

print "Lets rewind"

rewind(open(fname))

print "3 lines"

print cf.readline()
print cf.readline()
print cf.readline()


