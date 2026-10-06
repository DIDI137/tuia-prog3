from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class GreedyBestFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Greedy Best First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize root node
        root = Node("",
                    state=grid.initial,
                    cost=0,
                    parent=None,
                    action=None
                    )

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost
        
        frontera = PriorityQueueFrontier()

        root.estimated_distance = grid.h(root)
        frontera.add(root, root.estimated_distance)

        while True:
            if frontera.is_empty():
                return NoSolution(reached)
            
            nodo = frontera.pop()

            if nodo.state == grid.end:
                return Solution(nodo, reached)
   
            for accion in grid.actions(nodo.state):
                state = grid.result(nodo.state, accion)

                cost = nodo.cost + grid.individual_cost(nodo.state,accion)
                
                if state not in reached or cost < reached[state]:

                    # Crear nuevo nodo
                    son = Node(
                        accion,
                        state=state,
                        cost=cost,
                        parent=nodo
                    )

                    reached[state] = cost
                    son.estimated_distance = grid.h(son)
                    frontera.add(son, son.estimated_distance)
        
