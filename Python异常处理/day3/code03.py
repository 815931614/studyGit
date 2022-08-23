

def fun01():

    a = 1

    def fun02():
        b =2
        # nonlocal a
        print(a)

        # a = 2222
        # print(a)

    fun02()

fun01()