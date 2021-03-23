"""
Advent of Code 2020
Mission 5 Part 1:
The point of this mission is to find the highest ID in all seats, ID = Row*8+Column. To get column and Row you have to decode some letters

For example, consider just the first seven characters of FBFBBFFRLR:
    Start by considering the whole range, rows 0 through 127.
    F means to take the lower half, keeping rows 0 through 63.
    B means to take the upper half, keeping rows 32 through 63.
    F means to take the lower half, keeping rows 32 through 47.
    B means to take the upper half, keeping rows 40 through 47.
    B keeps rows 44 through 47.
    F keeps rows 44 through 45.
    The final F keeps the lower of the two, row 44.
    
and.For example, consider just the last 3 characters of FBFBBFFRLR:

    Start by considering the whole range, columns 0 through 7.
    R means to take the upper half, keeping columns 4 through 7.
    L means to take the lower half, keeping columns 4 through 5.
    The final R keeps the upper of the two, column 5.
"""

file = open("input.txt").read().split("\n")
print(file)
ID = []
for i in range(len(file)):
    
    up_r = 127
    down_r = 0
    up_c = 7
    down_c = 0
    for j in range(len(file[i])):#Turn letters of the code into row and colums by finding the upper or lower half.
        #Row
        if file[i][j]=="F":
            #If the dif of the up and down row is equal to 1, row = down row
            if up_r-down_r == 1:
                row = down_r
            else:
                up_r -= round((up_r-down_r)/2)
        elif file[i][j]=="B":
            #If the dif of the up and down row is equal to 1, row = up row
            if up_r-down_r == 1:
                row = up_r
            else:
                down_r += round((up_r-down_r)/2)
        #Column
        elif file[i][j]=="L":
            if up_c-down_c == 1:
                column = down_c
            else:
                up_c -= round((up_c-down_c)/2)
        elif file[i][j]=="R":
            if up_c-down_c == 1:
                column = up_c
            else:
                down_c += round((up_c-down_c)/2)
    #Array of every ID
    ID.append(row*8+up_c)

#Pass throught every Id to get the higher one
win = ID[0]
for i in range(0,len(ID)):
    if win<ID[i]:
        win=ID[i]
        
print(win)