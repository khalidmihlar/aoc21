def part1():
    input = [int(i) for i in open("input.txt").read().split(',')]

    for _ in range(80):
        tmp = []
        for i in input:
            if i == 0:
                tmp.append(8)
                tmp.append(6)
            else:
                tmp.append(i-1)

        input = tmp

    print(len(tmp))

part1()