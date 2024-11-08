# single inheritence
class first:
    print("This is A")

class second(first):
    print("This is B")

c = second()
print(c)

# multiple inheritance
class first:
    print("This is A")

class second:
    print("This is B")

class theird(first, second):
    print("This is c")

c = theird()
print(c)