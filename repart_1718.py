"Repart pour 2017-2018"

from repart import Repart
from repart import Teacher

cb  = Teacher("CB",  15, 16)
mc  = Teacher("MC",  15, 16.5)
cg  = Teacher("CG",  15, 17)
nr  = Teacher("NR",  15, 17)
sr  = Teacher("SR",  18, 19)
jpr = Teacher("JPR", 14, 15) # hu?
pv  = Teacher("PV",  15, 17)
bmp = Teacher("BMP", 10, 18)

teachersList = [cb, mc, cg, nr, sr, jpr, pv, bmp]

r = Repart(teachersList)

# Re-export with untrucated names (& 3-digit precision)
r.addClass("TS.1+AP",8.067)
r.addClass("TS.2+AP",8.067)
r.addClass("1S.+AP",5.500)
r.addClass("1S.SES+AP",5.500)
r.addClass("TES.2+AP",5.133)
for i in range(1, 7):
    r.addClass("2GT{}+AP".format(i), 5)
r.addClass("SIO.1.1",5.000)
r.addClass("SIO.1.2",5.000)
r.addClass("SIO.2.1.UF2",5.000)
r.addClass("TES.1+AP",4.767)
r.addClass("1ES",3.300)
r.addClass("1ES.L",3.300)
r.addClass("1ES.SES",3.300)
r.addClass("1ST2S",3.300)
r.addClass("1STMG.1",3.300)
r.addClass("1STMG.2",3.300)
r.addClass("TST2S",3.300)
r.addClass("Prépa",3.000)
r.addClass("SIO.1.1.Algo",2.500)
r.addClass("SIO.1.2.Algo",2.500)
r.addClass("SIO.2.2.UF2",2.500)
r.addClass("TS.SpéM",2.200)
r.addClass("TSTMG.1",2.200)
r.addClass("TSTMG.2",2.200)
r.addClass("TES.SpéM",1.650)
r.addClass("2nde.MPS",1.500)
r.addClass("TS.ISN",1.100)
r.addClass("2nde.ICN",0.750)
r.addClass("1S.ES.TPE",0.550)
r.addClass("1S.TPE",0.550)

# Assign some teachers-value to some classes-variables
r.addConstraint(lambda x: x.name == "CB",  ["2GT5+AP"])
r.addConstraint(lambda x: x.name == "CB",  ["TS.2+AP"])
r.addConstraint(lambda x: x.name == "MC",  ["2GT4+AP"])
r.addConstraint(lambda x: x.name == "MC",  ["TS.1+AP"])
r.addConstraint(lambda x: x.name == "CG",  ["2GT1+AP"])
r.addConstraint(lambda x: x.name == "NR",  ["SIO.1.1"])
r.addConstraint(lambda x: x.name == "JPR", ["2GT2+AP"])
r.addConstraint(lambda x: x.name == "JPR", ["2GT3+AP"])
r.addConstraint(lambda x: x.name == "PV",  ["SIO.1.2"])
r.addConstraint(lambda x: x.name == "SR",  ["2GT6+AP"])




r.addConstraint(r.totalTimeOK, r.variables)

print("Let's roll")

#r.prettySolutions()

# r.getSolution() => nothing found in 30 minutes...
