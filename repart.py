"""Dispatch teachers on classes"""

import constraint

class Teacher:
    """The person always on holidays"""

    def __init__(self, name, mini, maxi):
        self.name = name
        self.mini = mini
        self.maxi = maxi
        self.time = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Repart(constraint.Problem):
    """Problem about teachers dispatching"""

    timeAmount = {}

    def __init__(self, teachersList):
        super().__init__()
        self.teachersList = teachersList


    def addClass(self, name, time):
        self.addVariable(name, self.teachersList)
        self.timeAmount[name] = time

    def prettySolutions(self):
        for s in self.getSolutions():
            print(s)
            for t in self.teachersList:
                t.time = 0
            for c, t in s.items():
                t.time += self.timeAmount[c]
            for t in self.teachersList:
                print(t.name.ljust(3, ' '), t.time)
            print()
