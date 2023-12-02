import sys

def part1(fileName):
    total = 0
    with open(fileName) as f:
        for line in f:
            digit1 = ''
            digit2 = ''
            for i in line:
                if ord(i) >= 48 and ord(i) <= 57:
                    if digit1 == '':
                        digit1 = i
                    digit2 = i
            total += int(digit1 + digit2)

    return total

def part2(fileName):
    total = 0
    numsDict = {
        "one": "1", 
        "two": "2", 
        "three": "3", 
        "four": "4", 
        "five": "5", 
        "six": "6", 
        "seven":"7", 
        "eight": "8",
        "nine": "9"
        }     
        
    with open(fileName) as f:
        for line in f:
            digit1 = ''
            digit2 = ''
            tmp = ''
            l = line
            while l != '':
                if l[0] == 'o':
                    if l[0:3] == 'one':
                        tmp = '1'
                        l = l[2:]
                    else:
                        l = l[1:]
                elif l[0] == 't':
                    if l[0:3] == 'two':
                        tmp = '2'
                        l = l[2:]
                    elif l[0:5] == 'three':
                        tmp = '3'
                        l = l[4:]
                    else:
                        l = l[1:]
                elif l[0] == 'f':
                    if l[0:4] == 'four':
                        tmp = '4'
                        l = l[3:]
                    elif l[0:4] == 'five':
                        tmp = '5'
                        l = l[3:]
                    else:
                        l = l[1:]
                elif l[0] == 's':
                    if l[0:3] == 'six':
                        tmp = '6'
                        l = l[2:]
                    elif l[0:5] == 'seven':
                        tmp = '7'
                        l = l[4:]
                    else:
                        l = l[1:]
                elif l[0] == 'e':
                    if l[0:5] == 'eight':
                        tmp = '8'
                        l = l[4:]
                    else:
                        l = l[1:]
                elif l[0] == 'n':
                    if l[0:4] == 'nine':
                        tmp = '9'
                        l = l[3:]
                    else:
                        l = l[1:]
                elif ord(l[0]) >= 48 and ord(l[0]) <= 57:
                    tmp = l[0]
                    l = l[1:]
                else:
                    l = l[1:]
        
                if digit1 == '':
                    digit1 = tmp
                digit2 = tmp

                print(l, digit1, digit2, tmp)


            total += int(digit1 + digit2)
    
    return total



ans = part2(sys.argv[1])
print(ans)