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
        return self.items.pop(0)

    def vacia(self):
        if len(self.items) == 0:
            return True
        else:
            return False

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
        root = Node("",
                    state=grid.initial,
                    cost=0, 
                    parent=None, 
                    action=None)

        # Initialize reached with the initial state
        reached = {}
        reached[root.state] = True

        if grid.objective_test(root.state):
            return Solution(root, reached)
        
        
        frontera = Cola()  
        frontera.encolar(root)
        
        while not frontera.vacia():
            
            node = frontera.pop()
            
            for accion in grid.actions(node.state):
                sucesor = grid.result(node.state, accion)
                
                if sucesor not in reached:
                    son = Node(
                        "",
                        state=sucesor,
                        cost=node.cost + grid.individual_cost(
                            node.state, accion
                        ),
                        parent= node,
                        action=accion
                    )
                    
                    reached[sucesor] = True
                    
                    if grid.objective_test(sucesor):
                        return Solution(son, reached)
                    
                    frontera.encolar(son)
        return NoSolution(reached)
    
        