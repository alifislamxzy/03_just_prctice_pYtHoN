# f = open('modes.txt') # Open file

# lines = f.readlines() # readlines wacth print like a list

# print(lines, type(lines)) # print this modes

# f.close() # close this file

f = open('modes.txt')

line1 = f.readline() # This is open like a String 
print(line1, type(line1))

line2 = f.readline()
print(line2, type(line2))

line3 = f.readline()
print(line3, type(line3))

line4 = f.readline()
print(line4, type(line4))

line5 = f.readline()
print(line5 == '') # This a String

f.close()