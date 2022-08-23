

list01 = [23,3,4,556,677,68,8,98,98]

def getos():
    for num in list01:
        if num % 2 == 0:
            yield num


oushu = getos()

for o in oushu:
    print(o)
print(2 ** 2.2)
# while True:
#     try:
#         print(oushu.__next__())
#     except:
#         break
#
#
#
#
# class Student:
#     def __init__(self):
