from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """

        root = Node("",
                    state=grid.initial,
                    cost=0,
                    parent=None,
                    action=None)

        # Initialize reached with the initial state 
        reached = {}
        reached[root.state] = root.cost

        # Initialize frontier with the root node 
        frontera = PriorityQueueFrontier()
        frontera.add(root, root.cost + grid.h(root))

        # TODO Complete the rest!!
        while True:
            if frontera.is_empty():
                return NoSolution(reached)
            nodo = frontera.pop()
            if grid.objective_test(nodo.state):
                return Solution(nodo, reached)
            for a in grid.actions(nodo.state):

                estadoResult = grid.result(nodo.state, a)
                costoResult = nodo.cost + grid.individual_cost(nodo.state, a)

                if estadoResult not in reached or costoResult < reached[estadoResult]:            
                    son = Node(
                                value = "", 
                                state = estadoResult, 
                                cost = costoResult, 
                                parent = nodo, 
                                action = a
                                )
                    reached[estadoResult] = costoResult
                    frontera.add(son, son.cost + grid.h(son))


