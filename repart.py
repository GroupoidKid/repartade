"""Dispatch teachers on classes"""

import constraint

class Teacher:
    """The person always on holidays"""

    def __init__(self, name, mini, maxi):
        self.name = name
        self.mini = mini
        self.maxi = maxi
        self.time = 0

class Repart(constraint.Problem):
    """Problem about teachers dispatching"""
    
    timeAmount = {}

    def __init__(self, teachersList):
        super().__init__()
        self.teachersList = teachersList

    def getTeacherByName(self, name):
        for teacher in self.teachersList:
            if teacher.name == name:
                return teacher

    def addClass(self, name, time):
        self.addVariable(name, [t.name for t in self.teachersList])
        self.timeAmount[name] = time

    def prettySolutions(self):
        for s in self.getSolutions():
            print(s)
            for t in self.teachersList:
                t.time = 0
            for c, t in s.items():
                self.getTeacherByName(t).time += self.timeAmount[c]
            for t in self.teachersList:
                print(t.name.ljust(3, ' '), t.time)
            print()
