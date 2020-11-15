#!/usr/bin/python3
# Matthew Spohrer
# Monopoles Solved with via SAT
# Problem: m number of Monopoles need to be put into n number
#          of rooms. No two monopoles can add up to another
#          monopole in the same room. i.e. 1 and 2 can be in
#          the same room but not with 3 because 1 + 2 = 3 (in
#          case you didn't know)
# This program converts the monopole constraints to DIMACS format
# by minisat.

import sys
import math

# monos = number of monopoles, first arg passed by user
# rooms = number of rooms, second arg passed by user
monos = int(sys.argv[1])
rooms = int(sys.argv[2])


def one_room(clauses):
    # creates the atoms responsible for ensuring no monopole can be
    # rooms at once.
    # clauses is a list of all clauses to be passed to miniSAT
    # monos is the number of monopoles to be processed
    # rooms is an upper bound to the number of rooms to be checked

    not_clauses = []

    for m in range(1, monos + 1):
        clause = []
        not_clause = []
        for r in range(0, rooms):
            clause.append((monos * r) + m)
            not_clause.append(-((monos * r) + m))
        clauses.append(clause)
        not_clauses.append(not_clause)

    for c in not_clauses:
        clauses.append(c)


def monopole(clauses):
    # divides the monopoles so no two monopoles can be added
    # together to equal a third in the same room
    # clauses is a list of all clauses to be passed to miniSAT
    # monos is the number of monopoles to be processed
    # rooms is an upper bound to the number of rooms to be checked

    if monos % 2 == 0:
        mono_stop = monos//2
    else:
        mono_stop = math.ceil(monos/2)

    print(mono_stop)
    for m in range(1, mono_stop):
        for r in range(0, rooms):
            new_room_start = (monos * r) + m
            new_room_stop = monos * r + monos - m + 1

            print(m, "start=", new_room_start, "stop=", new_room_stop)
            for i in range(new_room_start + 1, new_room_stop):
                clauses.append([-new_room_start, -i, -(m+i)])


def p_a(clauses):
    for c in clauses:
        print(*c, '0')


def main():
    clauses = []
    num_atoms = monos * rooms
    atoms = []
    for r in range(0, rooms):
        for m in range(1, monos + 1):
            atoms.append((monos * r) + m)

    one_room(clauses)
    monopole(clauses)

    print(*atoms)
    print("p cnf", num_atoms, len(clauses))
    #   p_a(clauses)
    print("p cnf", num_atoms, len(clauses))


if __name__ == '__main__':
    main()
