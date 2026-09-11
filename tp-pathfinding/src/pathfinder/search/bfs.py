from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class Cola:
    def __init__(self) -> None:
        self.items = []        
    
    def encolar(self,x):
        self.items.append(x)

    def pop(self):
        self.items.remove(0)

    def vacia(self):
        if len(self.items) == 0:
            return True

class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", state=grid.initial, cost=0, parent=None, action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        if grid.objective_test(root.state):
            return Solution(root, reached)
        
        alcanzados = root.state
        frontera = Cola()  
        frontera.encolar(root)
        if frontera.vacia():
            return NoSolution(reached, 0)
        
        
        # Initialize frontier with te root node
        # TODO Complete the rest!!
        # ...

        return NoSolution(reached)
