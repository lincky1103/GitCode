from sys import argv

script, filename = argv

print('Going to ease: %r.' %(filename))
print('If u don\'t want that, hit CTRL-C (^C).')
print('Else hit RETURN')

input('?')

print('Openning the file...')
target = open(filename, 'w')

print('Truncating the file. Goodbye!')
target.truncate()

print('Ask u 3 questions for 3 lines:')

line1 =input('line1: ')
line2 =input('line2: ')
line3 =input('line3: ')

print('And write these to the file.')

target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print('And finally, we close it.')
target.close()