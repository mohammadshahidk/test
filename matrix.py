
row = int(input("Enter the number of rows:")) 
col = int(input("Enter the number of coloumns:"))

matrix = [[0 for i in range(row)]
              for j in range(col)]
              

value = 1

for i in range(row+col-1):
    for j in range(row):
        for k in range(col):
            if j+k == i:
                matrix[k][j] = value
                value += 1

if row < col:
    row = col

if col < row:
    col = row

for i in range(row):
    for j in range(col):
        try:
            print(matrix[i][j], end = " ")
        except IndexError:
            pass  
    print()
                      