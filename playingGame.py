import heapq
from math import sqrt

def heuristic(a, b):
    return sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

def get_neighbors(pos, grid_size):
    x, y = pos
    neighbors = []
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
            neighbors.append((new_x, new_y))
    return neighbors

def astar(grid_size, start, goal):
   
    open_set = []
    closed_set = set()
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    
    heapq.heappush(open_set, (f_score[start], start))
    
    while open_set:
        current = heapq.heappop(open_set)[1]
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        closed_set.add(current)
        
        for neighbor in get_neighbors(current, grid_size):
            if neighbor in closed_set:
                continue
                
            tentative_g_score = g_score[current] + 1  
            
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                
                if neighbor not in [item[1] for item in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None  

if __name__ == "__main__":
    grid_size = 4
    start_pos = (0, 0)
    goal_pos = (3,3)
    
    print(f"Finding path from {start_pos} to {goal_pos} in a {grid_size}x{grid_size} grid")
    
    # Find path using A*
    path = astar(grid_size, start_pos, goal_pos)
    
    if path:
        print("\nPath found:")
        print(" -> ".join(str(pos) for pos in path))
        print(f"Path length: {len(path)-1} steps")
    else:
        print("\nNo path found!")
    
    # Print path
    print("\nPath:")
    print(" -> ".join(str(pos) for pos in path))
