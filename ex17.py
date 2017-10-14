from sys import argv
from os.path import exists

script, from_file, to_file = argv

print('Copying from %s to %s...' %(from_file,to_file))

indata = open(from_file).read()

print('The input file is %d bytes long.' % len(indata))

print('Does the coutput file exists? %r' % exists(to_file))

print('Ready, hit RETURN to continue, CTRL-C to abort.')
input()

output = open(to_file,'w')
output.write(indata)

print('Alright, all done.')

output.close()
open(from_file).close()