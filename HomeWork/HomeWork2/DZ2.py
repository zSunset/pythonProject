def Weather(x):
    if x[0] in '+-':
        return x[0]

may_Weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < len(may_Weather):
    sign = Weather(may_Weather[i])
    if may_Weather[i].isdigit() or (sign and may_Weather[i][1:].isdigit()):
        if sign:
            may_Weather[i] = sign + may_Weather[i][1:].zfill(2)
        else:
            may_Weather[i] = may_Weather[i].zfill(2)

        may_Weather.insert(i, '"')
        may_Weather.insert(i + 2, '"')
        i += 2

    i += 1
Weather = ' '.join(may_Weather)
print(Weather)
