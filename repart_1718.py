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
r.addClass("MPS", 1.50)
r.addClass("ICN", 0.75)
r.addClass("1ES.L", 3.30)
r.addClass("1ES", 3.30)
r.addClass("1ES.SES", 3.30)
r.addClass("1S.+AP", 5.50)
r.addClass("1S.SES+AP", 5.50)
r.addClass("1S.TPE", 0.55)
r.addClass("1S.ES.TPE", 0.55)
r.addClass("1ST2S", 3.30)
r.addClass("1STMG.1", 3.30)
r.addClass("1STMG.2", 3.30)
r.addClass("TES.1+AP", 4.77)
r.addClass("TES.2+AP", 5.13)
r.addClass("TES.SpéM", 1.65)
r.addClass("TS.1+AP", 8.07)
r.addClass("TS.2+AP", 8.07)
r.addClass("TS.SpéM", 2.20)
r.addClass("TS.ISN", 1.10)
r.addClass("TST2S", 3.30)
r.addClass("TSTMG.1", 2.20)
r.addClass("TSTMG.2", 2.20)
r.addClass("SIO.1.1.Algo", 2.50)
r.addClass("SIO.1.2.Algo", 2.50)
r.addClass("SIO.1.1", 5.00)
r.addClass("SIO.1.2", 5.00)
r.addClass("SIO.2.1.UF", 5.00)
r.addClass("SIO.2.2.UF", 2.50)
r.addClass("Prépa", 3.00)

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
