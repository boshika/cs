'''Game Theory Application
Wendy and Bob are playing a game. They are given a string and have to pull chars based on what they are assigned.
Wendy has white chars and bob has black chars.
They each have to pull the assigned char, based on if thta char has left same char and right same char
Wendy always goes first
Example
'wwwbwwbbbb'
After Wendy moves: 'wwbwwbbbb'
Bob moves: 'wwbwwbbb'
Wendy loses as there are no more 'w' surrounded by other 'w
Return: Bob
'''

def findWinner(s):
    b_char = [i for i in s.split('w') if i]
    w_char = [i for i in s.split('b') if i]

    wendys_points = 0
    bobs_points = 0

    print(b_char)
    print(w_char)

    for i in w_char:
        print(i)
        counter = len(i)
        if len(i) > 2:
            print(counter)
            while counter > 2:
                wendys_points += 1
                counter -= 1

    for i in b_char:
        print(i)
        counter = len(i)
        if len(i) > 2:
            print(counter)
            while counter > 2:
                bobs_points += 1
                counter -= 1
    print(wendys_points, bobs_points)

    if wendys_points > bobs_points:
        return "Wendy"
    return "Bob"


print(findWinner('wwwbbbb'))
