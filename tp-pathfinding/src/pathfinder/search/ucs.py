from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("", 
                    state=grid.initial,
                    cost = 0,
                    parent = None,
                    action = None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost

 
        # Initialize frontier with the root node
        frontera = PriorityQueueFrontier()
        frontera.add(root, root.cost)

        # TODO Complete the rest!!
        while True:
            if frontera.is_empty():
                return NoSolution(reached)
            n = frontera.pop()
            if grid.objective_test(n.state):
                return Solution(n, reached)
            for a in grid.actions(n.state):
                s = grid.result(n.state, a)
                c = n.cost + grid.individual_cost(n.state, a)

                if s not in reached or c < reached[s]:
                    np = Node("", state= s, cost = c, parent = n, action = a)
                    reached[s] = c
                    frontera.add(np, c)

        return NoSolution(reached)
