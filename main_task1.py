#first enter the field size
#then indicate the places where there are mines with stars and empty cells with dots
idx = 1
while True:
    n, m = map(int, input("set the field size like 4 4: ").split())
    print("indicate the places where there are mines with stars and empty cells with dots.")
    if n == m == 0:
        break
    field = []
    for i in range(n):
        field.append([])
        for j in input():
            field[i].append(0 if j == "." else "*")
    for i in range(n):
        for j in range(m):
            if field[i][j] == "*":
                if i > 0 and field[i-1][j] != "*":
                    field[i-1][j] += 1

                if i < n - 1 and field[i+1][j] != "*":
                    field[i+1][j] += 1


                if j > 0 and field[i][j-1] != "*":
                    field[i][j-1] += 1


                if j < m - 1 and field[i][j+1] != "*":
                    field[i][j+1] += 1

                if i > 0 and j > 0 and field[i - 1][j - 1] != '*':
                    field[i - 1][j - 1] += 1

                if i < n - 1 and j < m - 1 and field[i + 1][j + 1] != '*':
                    field[i + 1][j + 1] += 1

                if i > 0 and j < m - 1 and field[i - 1][j + 1] != '*':
                    field[i - 1][j + 1] += 1

                if i < n - 1 and j > 0 and field[i + 1][j - 1] != '*':
                    field[i + 1][j - 1] += 1

    print(f"Field #{idx}")
    for i in range(n):
        for j in range(m):
            print(field[i][j], sep='', end='')
        print()
    idx += 1