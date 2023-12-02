import sys

# get bags may contain 12 red, 13 green, 14 blue
def part1(filename):
    total = 0
    bluem = 14
    greenm = 13
    redm = 12
    with open(filename) as f:
        for line in f:
            possible = True
            gameid = line.split(':')[0].split(' ')[-1]
            picks = line.split(':')[1].split(';')
            print(gameid)
            for pick in picks:
                balls = map(lambda x: x.strip(), pick.split(','))
                for b in balls:
                    ball_count = b.split(' ')[0]
                    ball_name = b.split(' ')[1]
                    print(ball_count, ball_name)
                    if ball_name == 'green':
                        if int(ball_count) > greenm:
                            possible = False
                    elif ball_name == 'blue':
                        if int(ball_count) > bluem:
                            possible = False
                    elif ball_name == 'red':
                        if int(ball_count) > redm:
                            possible = False

                    if not possible:
                        break
                if not possible:
                    break

            if possible:
                total += int(gameid)

    return total

# get the minimum number of balls per color per game. Per each game, multiply the minimums together as "power", return sum of all "powers"
def part2(filename):
    total = 0
    with open(filename) as f:
        for line in f:
            redm = 0
            greenm = 0
            bluem = 0
            gameid = line.split(':')[0].split(' ')[-1]
            picks = line.split(':')[1].split(';')
            for pick in picks:
                balls = map(lambda x: x.strip(), pick.split(','))
                for b in balls:
                    ball_count = b.split(' ')[0]
                    ball_name = b.split(' ')[1]

                    if ball_name == 'green':
                        if int(ball_count) > greenm:
                            greenm = int(ball_count)
                    elif ball_name == 'blue':
                        if int(ball_count) > bluem:
                            bluem = int(ball_count)
                    elif ball_name == 'red':
                        if int(ball_count) > redm:
                            redm = int(ball_count)

            total += redm * greenm * bluem

    return total

ans = part2(sys.argv[1])
print(ans)