def maxPassengers(grid):
    if not grid or not grid[0]:
        return 0

    n = len(grid)
    m = len(grid[0])

    def is_valid(x, y):
        return 0 <= x < n and 0 <= y < m and grid[x][y] != -1

    def dfs(x, y):
        if (x, y) == (n - 1, n - 1):
            return 0

        original_value = grid[x][y]
        grid[x][y] = -1  

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        max_passengers = 0

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                max_passengers = max(max_passengers, dfs(new_x, new_y))

        grid[x][y] = original_value  

        if original_value == 1:
            return 1 + max_passengers
        return max_passengers

    max_passengers = dfs(0, 0)
    return max_passengers

def get_user_input():
    n = int(input())
    m = n  
    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            print("Invalid input. Please enter exactly", m, "values.")
            return None

        grid.append(row)

    return grid


    
grid = get_user_input()
max_passengers = maxPassengers(grid)
print(max_passengers)

