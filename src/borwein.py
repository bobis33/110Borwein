##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-110borwein-elliot.masina
## File description:
## borwein
##


from math import pi

from src.calcul import midpoint_method
from src.calcul import trapezoidal_method
from src.calcul import simpson_method


def borwein(integral):

    result  = float (0.0)
    x       = int   (integral)

    result = midpoint_method(x)
    print("Simpson:\nI" + str (x) + " = " + ("%.10f" % result))
    if ((result - (pi / 2)) < 0):
        print("diff = " + ("%.10f" % ( -1 * (result - (pi / 2)))) + "\n")
    else:
        print("diff = " + ("%.10f" % (result - (pi / 2))) + "\n")

    result = trapezoidal_method(x)
    print("Trapezoidal:\nI" + str (x) + " = " + ("%.10f" % result))
    if ((result - (pi / 2)) < 0):
        print("diff = " + ("%.10f" % ( -1 * (result - (pi / 2)))) + "\n")
    else:
        print("diff = " + ("%.10f" % (result - (pi / 2))) + "\n")

    result = simpson_method(x)
    print("Simpson:\nI" + str (x) + " = " + ("%.10f" % result))
    if ((result - (pi / 2)) < 0):
        print("diff = " + ("%.10f" % ( -1 * (result - (pi / 2)))))
    else:
        print("diff = " + ("%.10f" % (result - (pi / 2))))
