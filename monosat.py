#!/usr/bin/python3
# Matthew Spohrer
# Monopoles Solved with via SAT
# Problem: m number of Monopoles need to be put into n number
#          of rooms. No two monopoles can add up to another
#          monopole in the same room. i.e. 1 and 2 can be in
#          the same room but not with 3 because 1 + 2 = 3 (in
#          case you didn't know)
# This program converts the monopole constraints to DIMACS CNF format
# to be used by minisat.

import sys

# monos = number of monopoles, first arg passed by user
monos = int(sys.argv[1])
# rooms = number of rooms, second arg passed by user
rooms = int(sys.argv[2])


def one_room(clauses):
    # creates the atoms responsible for ensuring every monopole is in exactly
    # one room.
    # TODO: make function more streamlined. It's pretty dirty
    # clauses is a list of all CNF clauses to be passed to miniSAT
    # monos is the number of monopoles to be processed
    # rooms is an upper bound to the number of rooms to be checked

    for mono in range(1, monos + 1):
        # ensures each monopole is in a room.
        clause = []
        for room in range(0, rooms):
            clause.append((room * monos) + mono)
        clauses.append(clause)

    for room1 in range(0, rooms):
        # ensures each monopole is only in 1 room
        # room1 is the first room being checked against
        for mono in range(1, monos + 1):
            current_room = room1 * monos + mono
            for room2 in range(room1 + 1, rooms):
                other_room = (room2 * monos + current_room)
                clauses.append([-current_room, -other_room])


def monopole(clauses):
    # divides the monopoles so no two monopoles can be added
    # together to equal a third in the same room
    # clauses is a list of all clauses to be passed to miniSAT
    # monos is the number of monopoles to be processed
    # rooms is an upper bound to the number of rooms to be checked

    monos_stop = monos // 2
    if monos % 2 == 1:
        monos_stop += 1
    print("m_stop:", monos_stop)

    for m in range(1, monos_stop):
        for r in range(0, rooms):
            i_start = (monos * r) + m + 1
            i_stop = (monos * r) + monos - m + 1
#            print("m:", m, "r:", r, "i_start:", i_start, "i_stop:", i_stop)
            for i in range (i_start, i_stop):
                clauses.append([-(i_start - 1), -i, -(m + i)])




def main():
    clauses = []
    num_atoms = monos * rooms
    atoms = []
    for r in range(0, rooms):
        for m in range(1, monos + 1):
            atoms.append((monos * r) + m)

    one_room(clauses)
    monopole(clauses)

    print("p cnf", num_atoms, len(clauses))
    for c in clauses:
        print(*c, '0')


if __name__ == '__main__':
    main()
