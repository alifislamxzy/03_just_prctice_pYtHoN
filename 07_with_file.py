# f = open('wr.txt', 'r')
# print(f.read())
# f.close()

# Output is :
# Hello World
# Hi Alif
# Go Alif
# Good Bye Alif

with open('wr.txt', 'r') as f:
    print(f.read())
    f.close()

for i in range(50):
    print(i)
    i+=1

i = 0
while(i<11):
    print(i)
    i+=1