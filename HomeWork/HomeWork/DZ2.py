print(sum(filter(lambda j: sum(map(int, str(j))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])))
print(sum(filter(lambda j: sum(map(int, str(j + 17))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])))