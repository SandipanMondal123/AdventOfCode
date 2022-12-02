#Rock A  X-> 1, paper B Y -> 2, sizzor C Z -> 3, win = 8, tie = 3, loss = 1

        
book = {'A': 'X', 'B': 'Y', 'C': 'Z'}
value = {'X': 1, 'Y': 2, 'Z': 3}

def check(opp, you) -> int:
    score = 0
    if book[opp] == you:
        score = 3
    else:
        temp = book[opp]
        if temp == 'X':
            if you == 'Y':
                score = 6
            else:
                score = 0
        elif temp == 'Y':
            if you == 'Z':
                score = 6
            else:
                score = 0
        else:
            if you == 'X':
                score = 6
            else:
                score = 0
    score += value[you]
    #print(score)
    return score

def check2(opp, you) -> int:
    score = 6
    win = True
    if you == 'Y': #tie
        score = 3
        predicted = book[opp] 
    else:
        if you == 'X':
            win = False
            score = 0
        temp = book[opp]
        
        if temp == 'X':
            if win:
                predicted = 'Y'
            else:
                predicted = 'Z'
                
        elif temp == 'Y':
            if win:
                predicted = 'Z'
            else:
                predicted = 'X'
        elif temp == 'Z':
            if win:
                predicted = 'X'
            else:
                predicted = 'Y'            
                
   # if predicted == 'B':
      #  print()
    score += value[predicted]
    #print(score)
    return score
        
        
ts = 0
temp1 = 0
temp2 = 0
for line in open('input.txt'):
        
        opp , you = line.strip('\n').split()
        temp2+=  check2(opp, you)
        temp1 +=  check(opp, you)
        #print(line.strip('\n'), ' ', temp)
        
print("Part 1 -> ", temp1) # why is this console.log unreachable?
print("Part 2 -> ", temp2)


        
    