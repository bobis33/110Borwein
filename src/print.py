#!/usr/bin/env python3
##
## EPITECH PROJECT, 2023
## B-MAT-200-BDX-2-1-106bombyx-elliot.masina
## File description:
## print
##


from sys import stderr


def print_error():

    print("Error: bad arguments.\nRetry with ./110borwein -h.", file=stderr)


def print_help():


    print("USAGE\n",
          "   ./110borwein n\n\nDESCRPTION\n",
          "   n     constant defining the integral to be computed\n")

