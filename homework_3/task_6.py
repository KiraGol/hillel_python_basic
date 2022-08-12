x1 = int(input("Enter the cell number on the x-axis: "))
y1 = int(input("Enter the cell number on the y-axis: "))
x2 = int(input("Enter the number of the second cell along the x-axis: "))
y2 = int(input("Enter the number of the second cell along the y-axis: "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
if dx == 1 and dy == 2 or dx == 2 and dy == 1:
    print('YES')
else:
    print('NO')
