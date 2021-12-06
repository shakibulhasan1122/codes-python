
def organizedList(list):
    m=len(list)
    n=len(list[0])
    for i in range(0,n):
        for j in range(0,m):
            print(list[j][i],end='') 
        print("\n")     

grid = [['.', '.', '.', '.', '.', '.'],        ['.', 'O', 'O', '.', '.', '.'],        ['O', 'O', 'O', 'O', '.', '.'],        ['O', 'O', 'O', 'O', 'O', '.'],        ['.', 'O', 'O', 'O', 'O', 'O'],        ['O', 'O', 'O', 'O', 'O', '.'],        ['O', 'O', 'O', 'O', '.', '.'],        ['.', 'O', 'O', '.', '.', '.'],        ['.', '.', '.', '.', '.', '.']]

organizedList(grid)        