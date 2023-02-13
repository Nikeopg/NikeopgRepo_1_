games_amount = int(input())
team = []
table = []
teams = {}
points, match_amount, wp, draw, gg = 0, 0, 0, 0, 0

cnter = 0

while cnter < games_amount:
    match = str(input())
    table.append(match.split(";"))
    cnter += 1

for i in range(len(table)):
    teams[table[i][0]] = [match_amount, wp, draw, gg, points]
    teams[table[i][2]] = [match_amount, wp, draw, gg, points]

for i in range(len((table))):
    table[i][1] = int(table[i][1])
    table[i][3] = int(table[i][3])
    if table[i][1] > table[i][3]:
        teams[table[i][0]][0] += 1
        teams[table[i][0]][1] += 1
        teams[table[i][0]][4] += 3
        teams[table[i][2]][0] += 1
        teams[table[i][2]][3] += 1
    elif table[i][1] < table[i][3]:
        teams[table[i][2]][0] += 1
        teams[table[i][2]][1] += 1
        teams[table[i][2]][4] += 3
        teams[table[i][0]][0] += 1
        teams[table[i][0]][3] += 1
    else:
        teams[table[i][0]][0] += 1
        teams[table[i][0]][2] += 1
        teams[table[i][0]][4] += 1
        teams[table[i][2]][0] += 1
        teams[table[i][2]][2] += 1
        teams[table[i][2]][4] += 3

for club, res in teams.items():
    print(club, *res)

""" Напишите программу, которая принимает на стандартный вход список игр футбольных команд
с результатом матча и выводит на стандартный вывод сводную таблицу результатов всех матчей.
За победу команде начисляется 3 очка, за поражение — 0, за ничью — 1.

Формат ввода следующий:
В первой строке указано целое число  n — количество завершенных игр.
После этого идет n строк, в которых записаны результаты игры в следующем формате:
Первая_команда;Забито_первой_командой;Вторая_команда;Забито_второй_командой
Вывод программы необходимо оформить следующим образом:
Команда:Всего_игр Побед Ничьих Поражений Всего_очков
Конкретный пример ввода-вывода приведён ниже.
Порядок вывода команд произвольный.

Sample Input:
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
Sample Output:

Спартак:2 0 0 2 0
Зенит:2 1 0 1 3
Локомотив:2 2 0 0 6 """
