part1 = part2 = 0
#part 1
with open('input.txt') as file1:
    while True:
        line = file1.readline()
        if line == '':
            break
        
        left , right = line.strip('\n').split(',')
        l1, l2 = left.split('-')
        r1, r2 = right.split('-')
        
        setLeft = set([i for i in range(int(l1), int(l2) + 1)])
        setRight = set([i for i in range(int(r1), int(r2) + 1)])
        
        #print(setLeft)
        #print(setRight)
        
        if setLeft <= setRight or setRight <= setLeft:
            part1 +=1
        if len(list(setLeft & setRight)) > 0:
            part2 +=1   

print("Part 1 -> ", part1)
print("Part 2 -> ", part2)
        
        
