from math import pi


def area_calc(r):
    try:
        return pi * (r ** 2)
    except TypeError:
        print("Tani werey, shey eye dey pain you? Enter integer jareh")


area_calc(4)
