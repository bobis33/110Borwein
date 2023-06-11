#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-106bombyx-elliot.masina
## File description:
## error
##


from src.print import print_help
from src.print import print_error



def error_case(argv):

    i           = int (0)
    len_argv    = int (len(argv))

    if (len_argv == 2 and (argv[1] == "-h" or argv[1] == "--help")):

        print_help()
        exit(0)

    if (len_argv != 2 or argv[1].isdigit() == False):
        print_error()
        exit(84)


