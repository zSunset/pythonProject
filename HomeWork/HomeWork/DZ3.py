numbs = {11,12,13,14}
for i in range(100):
    i = i + 1
    if i in numbs:
        print(i, "процентов")
    elif i % 10 == 1:
        print(i, "процент")
    elif i % 10 > 1 and i % 10 <5:
        print(i, "процента")
    else:
        print(i, "процентов")