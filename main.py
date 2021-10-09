number = int(input())
ss = int(input())
newNumber = ""
delBySs = number // ss
newNumber += str(number % ss)
while delBySs > ss:
    newNumber += str(delBySs % ss)
    delBySs = delBySs // ss
newNumber += str(delBySs % ss)
newNumber += str(delBySs // ss)
print(newNumber[::-1])
