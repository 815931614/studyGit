


class Skill:
    def __init__(self):
        pass
class SkillNext:
    def __init__(self, skill):
        self.skill = skill
        self.start = -1
    def __next__(self):
        self.start += 1
        if self.start >= len(self.skill):
            raise StopIteration
        return self.skill[self.start]
class SkillManager:
    def __init__(self,skill):
        self.skill = skill

    def __iter__(self):
       for item in self.skill:
           yield item

manager = SkillManager([Skill(),Skill(),Skill(),Skill()])


manageri = manager.__iter__()
while True:
    try:
        print(manageri.__next__())
    except Exception as e:
        break