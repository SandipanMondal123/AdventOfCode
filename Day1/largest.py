
"""
     Learned how to use readLine. This returns an empty string when it as reach EOF
"""
calorieList = []
with open('input.txt') as file1:
    tempSum = 0
    while True:
        line = file1.readline()
        if line == '':
            calorieList.append(tempSum)
            break
        elif line == '\n':
            calorieList.append(tempSum)
            tempSum = 0
        else:
            line = line.strip('\n')
            tempSum += int(line)

calorieList.sort()
print('Part 1 ->', calorieList[-1])
print('Part 2 ->', sum(calorieList[-3:]))