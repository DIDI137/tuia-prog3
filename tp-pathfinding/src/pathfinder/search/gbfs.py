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
                    action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = root.cost
        
        frontera = PriorityQueueFrontier()
        
        fila, columna = root.state
        fila_objetivo, columna_objetivo = grid.end
        
        heuristica = abs(fila - fila_objetivo) + abs(columna - columna_objetivo)
        
        frontera.add(root, heuristica)
        while not frontera.is_empty():
     
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
  
                    fila, columna = state
                    fila_objetivo, columna_objetivo = grid.end

                    heuristica = abs(fila - fila_objetivo) + abs(columna - columna_objetivo)

                    frontera.add(son, heuristica)
        

        return NoSolution(reached)
