from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

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
        
        
        frontier = QueueFrontier()  
        frontier.add(root)
        
        while not frontier.is_empty():
            
            nodo = frontier.remove()
            
            for action in grid.actions(nodo.state):
                sucesor = grid.result(nodo.state, action)
                
                if sucesor not in reached:
                    son = Node(
                        "",
                        state=sucesor,
                        cost=nodo.cost + grid.individual_cost(
                            nodo.state, action
                        ),
                        parent= nodo,
                        action=action
                    )
                    
                    reached[sucesor] = True
                    
                    if grid.objective_test(sucesor):
                        return Solution(son, reached)
                    
                    frontier.add(son)
                    
        return NoSolution(reached)
    
        