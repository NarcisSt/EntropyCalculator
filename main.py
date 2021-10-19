import math


def getSumOfPartition(partition):
    a = partition[0]
    b = partition[1]
    s = a + b

    return s


def simpleEntropy(partition):
    a = partition[0]
    b = partition[1]
    s = getSumOfPartition(partition)

    if a == 0 or b == 0:
        entropy = 0
    else:
        entropy = a / s * math.log2(s / a) + b / s * math.log2(s / b)

    return entropy


def conditionalEntropy(root, first_partition, second_partition):
    s_part1 = getSumOfPartition(first_partition)
    s_part2 = getSumOfPartition(second_partition)
    s_root = getSumOfPartition(root)

    conditional_entropy = s_part1 / s_root * simpleEntropy(first_partition) + s_part2 / s_root * simpleEntropy(
        second_partition)

    return conditional_entropy


if __name__ == '__main__':
    while True:
        print("\nIntroduceti prima partitie descendenta: ")
        a1 = int(input("+: "))
        b1 = int(input("-: "))
        partition1 = [a1, b1]

        print("\nIntroduceti a doua partitie descendenta: ")
        a2 = int(input("+: "))
        b2 = int(input("-: "))
        partition2 = [a2, b2]

        r1 = a1 + a2
        r2 = b1 + b2
        root = [r1, r2]

        print("\nCompasul de decizie rezultat este:")
        print("\n           [" + str(r1) + "+, " + str(r2) + "-]            ")
        print("\n   [" + str(a1) + "+, " + str(b1) + "-]" + "        " + "[" + str(a2) + "+, " + str(b2) + "-]")

        print("\nEntropia atributului de iesire este : " + str(simpleEntropy(root)))
        print("\nEntropia specifica primei partitii este : " + str(simpleEntropy(partition1)))
        print("\nEntropia specifica celei de-a doua partitii este : " + str(simpleEntropy(partition2)))
        print("\nEntropia conditionala a atributului de iesire este : " + str(
            conditionalEntropy(root, partition1, partition2)))
        print("\nCastigul de informatie al atributului de iesire este : " + str(
            simpleEntropy(root) - conditionalEntropy(root, partition1, partition2)))
        print("\n")
