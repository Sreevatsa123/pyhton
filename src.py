from sys import argv

from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file=open(from_file)
indata=in_file.read()
outfile=open(to_file,'w')
outfile.write(indata)

