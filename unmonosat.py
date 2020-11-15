import sys
import fileinput

# monos = number of monopoles, first arg passed by user
monos = int(sys.argv[1])
# rooms = number of rooms, second arg passed by user
rooms = int(sys.argv[2])

soln = []
for line in sys.stdin:
    soln.append(line.strip())

print(soln_list)
for room in range(0, rooms):
    i = room * monos
    while i < ((room + 1) * monos):
        if soln_list[i] > 0:
            print(soln_list[i] - (monos * room), end=' ')
        i += 1
    print()