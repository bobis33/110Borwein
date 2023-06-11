##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-110borwein-elliot.masina
## File description:
## calcul
##

from math import sin




#     void midpoint(double n, double pi)
#     {
#         double res = 0;
#         double res1 = 0;
#     
#         for (double a = 0, b = 0.5; b <= 5000; a += 0.5, b += 0.5) {
#             res1 = borwein(n, ((a + b) / 2));
#             res1 *= b - a;
#             res += res1;
#         }
#         pi = diff_pi(pi, res);
#         printf("Midpoint:\nI%.0f = %.10f\n", n, res);
#         printf("diff = %.10f\n\n", pi);
#     }
#     


def midpoint_method(x):
    result          = float (0.0)
    final_result    = float (0.0)
    a               = float (0.0)
    b               = float (0.5)

    while (b <= 5000):
        result = (calcul_sin(x, (a + b) / 2))
        result = result * (b - a)
        a += 0.5
        b += 0.5
        final_result += result


    return (final_result)


def     calcul_sin(x, y):

    z       = int       (0)
    result  = float     (1.0)

    while (z <= x):

        if (y != 0):
            result = result * (sin(y / (2 * z + 1)) / (y / (2 * z + 1)))

        z += 1

    return (result)


def     trapezoidal_method(x):
    result      = float (0.0)
    h           = float (0.5)
    i           = int   (1)

    while (i < 10000):
        result += calcul_sin(x, i * h)
        i += 1

    result = result * 2
    result += (calcul_sin(x, 5000) + calcul_sin(x, 0))
    result = result * (h / 2)

    return (result)


def     simpson_method(x):
    final_result    = float (0.0)
    result_1        = float (0.0)
    result_2        = float (0.0)
    h               = float (0.5)
    i               = int   (1)

    while (i < 10000):
        result_1 += calcul_sin(x, i * h)
        i += 1

    i = 0
    while (i < 10000):
        result_2 += calcul_sin(x, (i * h) + (h / 2))
        i += 1

    final_result = (calcul_sin(x, 5000) + calcul_sin(x, 0))
    final_result += ((2 * result_1) + (4 * result_2))
    final_result = final_result * (5000 / (6 * 10000))

    return (final_result)
