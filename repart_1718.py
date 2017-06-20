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

r.addClass("2GT1", 4)
r.addClass("2GT1 AP", 1)

#r.addConstraint(
r.prettySolutions()
