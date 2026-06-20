import heapq

# Define the grid dimensions
GRID_SIZE = 5

# Define the possible movements (up, down, left, right)
MOVEMENTS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Define the heuristic function (Manhattan distance)
def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

# Define the A* pathfinding algorithm
def astar(grid, start, goal):
    # Create a priority queue to hold nodes to be processed
    queue = []
    heapq.heappush(queue, (0, start))
    came_from = {start: None}
    cost_so_far = {start: 0}

    while queue:
        # Extract the node with the lowest cost from the queue
        _, current = heapq.heappop(queue)

        # If we've reached the goal, reconstruct the path
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        # Explore neighbors
        for movement in MOVEMENTS:
            neighbor = (current[0] + movement[0], current[1] + movement[1])

            # Skip if the neighbor is out of bounds or blocked
            if (neighbor[0] < 0 or neighbor[0] >= GRID_SIZE or
                    neighbor[1] < 0 or neighbor[1] >= GRID_SIZE or
                    grid[neighbor[0]][neighbor[1]] == 1):
                continue

            # Calculate the new cost and push the neighbor to the queue
            new_cost = cost_so_far[current] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(queue, (priority, neighbor))
                came_from[neighbor] = current

    # If there's no path to the goal, return None
    return None

# Define the grid with blocked cells (represented by 1)
grid = [[0]*GRID_SIZE for _ in range(GRID_SIZE)]
grid[1][1] = 1
grid[2][2] = 1

# Define the main function
def main():
    start = (0, 0)
    goal = (GRID_SIZE-1, GRID_SIZE-1)
    path = astar(grid, start, goal)

    if path:
        print("Path found:", path)
    else:
        print("No path found")

# Run the main function
if __name__ == "__main__":
    main()