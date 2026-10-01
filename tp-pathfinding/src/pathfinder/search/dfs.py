from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

class Pila:
    def __init__(self):
        self.items = []
    
    def apilar(self,dato):
        self.items.append(dato)
        
    def desapilar(self):
        return self.items.pop()
        
    def esta_vacia(self):
        if len(self.items) == 0:
            return True
        else:
            return False
        
class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

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

        # Initialize expanded with the empty dictionary
        expanded = dict()

        frontera = Pila()
        frontera.apilar(root)
        
        while not frontera.esta_vacia():
            nodo = frontera.desapilar()
            
            if nodo.state in expanded:
                continue
            
            expanded[nodo.state] = True
            
            if grid.objective_test(nodo.state):
                return Solution(nodo, expanded) 
            
            for accion in grid.actions(nodo.state): 
                sucesor = grid.result(nodo.state, accion)
                
                if sucesor not in expanded:

                    son = Node(
                        "",
                        state=sucesor,
                        cost=nodo.cost + grid.individual_cost(
                            nodo.state, accion
                        ),
                        parent=nodo,
                        action=accion
                    )

                    frontera.apilar(son)                      
        

        return NoSolution(expanded)
