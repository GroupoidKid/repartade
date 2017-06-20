"Repart pour 2017-2018"

from repart import Repart
from repart import Teacher as T

cb  = T("CB",  14, 16)
mc  = T("MC",  14, 16)
cg  = T("CG",  14, 16)
nr  = T("NR",  14, 16)
sr  = T("SR",  17, 19)
jpr = T("JPR", 14, 15)
pv  = T("PV",  14, 18)
bmp = T("BMP", 10, 18)

teachersList = [cb, mc, cg, nr, sr, jpr, pv, bmp]

r = Repart(teachersList)

for i in range(1, 7):
    r.addClass("2GT{}".format(i), 4)
    r.addClass("2GT{} AP".format(i), 1)

r.addConstraint(lambda x: x.name == "CG",  ("2GT1",))
r.addConstraint(lambda x: x.name == "CG",  ("2GT1 AP",))
r.addConstraint(lambda x: x.name == "JPR", ("2GT2",))
r.addConstraint(lambda x: x.name == "JPR", ("2GT2 AP",))
r.addConstraint(lambda x: x.name == "JPR", ("2GT3",))
r.addConstraint(lambda x: x.name == "JPR", ("2GT3 AP",))
r.addConstraint(lambda x: x.name == "MC",  ("2GT4",))
r.addConstraint(lambda x: x.name == "MC",  ("2GT4 AP",))
r.addConstraint(lambda x: x.name == "CB",  ("2GT5",))
r.addConstraint(lambda x: x.name == "CB",  ("2GT5 AP",))
r.addConstraint(lambda x: x.name == "SR",  ("2GT6",))
r.addConstraint(lambda x: x.name == "SR",  ("2GT6 AP",))

#r.addConstraint(
r.prettySolutions()
