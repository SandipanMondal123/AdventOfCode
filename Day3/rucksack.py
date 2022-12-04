#Divide each line by 2
#put everything in a set and find the intersection
#ord(number) and add it sum


totalSum = 0
for line in open('input.txt'):
    left, right = line[0: int(len(line)/2)] , line[int(len(line)/2): len(line)]
    #print(left, right)
    letterASCII = ord(list(set(left) & set(right))[0])
    if letterASCII >= ord('a'):
        totalSum += letterASCII - ord('a') + 1
    else:
        totalSum += letterASCII - ord('A') + 27
print(totalSum)

totalSum = 0
x=1
set1 = set()
set2 = set()
set3 = set()       
with open('input.txt') as file1:
    while True:
        if x == 4:
            print((set1 & set2 & set3))
            
            letterASCII = ord(list(set1 & set2 & set3)[0])
            if letterASCII >= ord('a'):
                totalSum += letterASCII - ord('a') + 1
            else:
                totalSum += letterASCII - ord('A') + 27
            
            x=1
            set1 = set()
            set2 = set()
            set3 = set()
        else:
            line = file1.readline()
            if line == '':
                break
            if x == 1:
                set1.update(line.strip('\n'))
                print(set1)
            elif x == 2:
                set2.update(line.strip('\n'))
            else:
                set3.update(line.strip('\n'))
            x+=1
        

        

    #totalSum += ord(list(set(left) & set(right))[0]) - ord('A') + 1
    
print(totalSum)
