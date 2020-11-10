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

def main():
    # m: number of monopole
    # n: number of rooms
    m = int(sys.argv[1])
    n = int(sys.argv[2])

    ms = range(1, m + 1)
    rs = [[] for i in range(n)]
    todo = [*ms]

    rs = dfs(rs, todo, n, 0)
    if rs == 0:
        print("unsat")
    else:
        pretty_print(rs)

    check(rs)


if __name__ == '__main__':
    main()
