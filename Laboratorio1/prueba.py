from PIL import Image
from collections import deque

class Problem:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.width, self.height = self.image.size
        self.start = None
        self.goals = []
        self.walkable = set()
        self.load_image()
        
    def load_image(self):
        for x in range(self.width):
            for y in range(self.height):
                pixel = self.image.getpixel((x, y))
                if pixel == (255, 255, 255):
                    self.walkable.add((x, y))
                elif pixel == (255, 0, 0):
                    self.start = (x, y)
                elif pixel == (0, 255, 0):
                    self.goals.append((x, y))

    def actions(self, state):
        if state is None:
            return []
        actions = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = state
            next_x, next_y = x + dx, y + dy
            if (next_x, next_y) in self.walkable:
                actions.append((next_x, next_y))
        return actions

    def result(self, state, action):
        return action

    def goalTest(self, state):
        if state is None:
            return False
        return state in self.goals

    def stepCost(self, state, action, next_state):
        return 1

    def pathCost(self, states):
        return len(states) - 1


def BFS(problem):
    queue = deque([(problem.start, [problem.start])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if problem.goalTest(state):
            return path
        for next_state in problem.actions(state):
            queue.append((next_state, path + [next_state]))
    return None


problem = Problem("sharpened.bmp")
path = BFS(problem)
if path is not None:
    print("Path found:", path)
else:
    print("No path found.")