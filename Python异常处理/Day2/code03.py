

def SkillManager(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

manager = SkillManager(5)
while True:
    try:
        print(manager.__next__())
    except Exception as e:
        break