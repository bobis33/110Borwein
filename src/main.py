#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-106bombyx-elliot.masina
## File description:
## main
##


from sys import argv

from src.error import error_case
from src.borwein import borwein


def main():


    error_case(argv)

    borwein(argv[1])

    exit(0)


if __name__ == '__main__':
    exit(main())
