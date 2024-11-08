# write = "Hey bro this code like good"

f = open('wr.txt')

# f.write(write)
# f.close()

line = f.readline()

while(line != ''):
    print(line)
    line = f.readline()
    
f.close()