# load file
with open('key.txt') as f:
    lines = f.readlines()

# PART 1
score = 0
for i in range(len(lines)):
    plays = lines[i].split()
    if plays[0] == 'A':  # OPP: ROCK
        if plays[1] == 'X':  # YOU: ROCK
            score += 1  # +1 for rock
            score += 3  # +3 for draw
        elif plays[1] == 'Y':  # YOU: PAPER
            score += 2  # +2 for paper
            score += 6  # +6 for win
        elif plays[1] == 'Z':  # YOU: SCISSORS
            score += 3  # +3 for scissors
            score += 0  # +0 for win
    elif plays[0] == 'B':  # OPP: PAPER
        if plays[1] == 'X':  # YOU: ROCK
            score += 1  # +1 for rock
            score += 0  # +0 for lose
        elif plays[1] == 'Y':  # YOU: PAPER
            score += 2  # +2 for paper
            score += 3  # +3 for draw
        elif plays[1] == 'Z':  # YOU: SCISSORS
            score += 3  # +3 for scissors
            score += 6  # +6 for win
    elif plays[0] == 'C':  # OPP: SCISSORS
        if plays[1] == 'X':  # YOU: ROCK
            score += 1  # +1 for rock
            score += 6  # +6 for win
        elif plays[1] == 'Y':  # YOU: PAPER
            score += 2  # +2 for paper
            score += 0  # +0 for lose
        elif plays[1] == 'Z':  # YOU: SCISSORS
            score += 3  # +3 for scissors
            score += 3  # +3 for draw
    print(score)

# PART 2
# "X" means need to lose, "Y" means you need to draw, "Z" means you need to win
score = 0
for i in range(len(lines)):
    plays = lines[i].split()
    if plays[1] == 'X':  # NEED TO LOSE
        score += 0
        if plays[0] == 'A': # OPP: ROCK, you play scissors to lose
            score += 3
        elif plays[0] == 'B':  # OPP: PAPER, you play rock to lose
            score += 1
        elif plays[0] == 'C':  # OPP: SCISSORS, you play paper to lose
            score += 2
    elif plays[1] == 'Y':  # NEED TO DRAW
        score += 3
        if plays[0] == 'A': # OPP: ROCK, need rock to draw
            score += 1
        elif plays[0] == 'B':  # OPP: PAPER, need paper to draw
            score += 2
        elif plays[0] == 'C':  # OPP: SCISSORS, need scissors to draw
            score += 3
    elif plays[1] == 'Z':  # NEED TO WIN
        score += 6
        if plays[0] == 'A': # OPP: ROCK, need paper to win
            score += 2
        elif plays[0] == 'B':  # OPP: PAPER, need scissors to win
            score += 3
        elif plays[0] == 'C':  # OPP: SCISSORS, need rock to win
            score += 1
    print(score)
