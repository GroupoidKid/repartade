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


# Objective:
# Repart may be considered a map from {Classes} to {Teachers}
# The objective si to build up such a map with extra constraints

class Repart(constraint.Problem):
    """Problem about teachers dispatching"""

    timeAmount = {}
    variables = []

    def __init__(self, teachersList):
        super().__init__()
        self.teachersList = teachersList

    def totalTimeOK(self, *x):
        for t in self.teachersList:
            t.time = 0
        for c, t in zip(self.variables, x):
            t.time += self.timeAmount[c]
        for t in self.teachersList:
            if not t.mini <= t.time <= t.maxi:
                return False
        return True

    def addClass(self, name, time):
        self.variables.append(name)  # r.variables = {Classes}
        self.addVariable(name, self.teachersList)
        self.timeAmount[name] = time  # timeAmount ob = {Class.name=>Class.hours}

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
