# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
from game import Directions
from typing import List


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    w = Directions.WEST
    return [w, w, w]


def depthFirstSearchRecursive(problem: SearchProblem, actualState, alreadyVisited, directions) -> List[Directions]:
    if problem.isGoalState(actualState):
        return directions
    
    alreadyVisited.append(actualState)  
    successors = problem.getSuccessors(actualState)

    for nodo in successors:
        nextState, action, cost = nodo
        
        if nextState not in alreadyVisited:
            directions.append(action)
            result = depthFirstSearchRecursive(problem, nextState, alreadyVisited, directions)

            if result:
                return result
            
            directions.pop()

    return []



def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    actualState = problem.getStartState()
    alreadyVisited = [actualState]
    directions = []
    return depthFirstSearchRecursive(problem, actualState, alreadyVisited, directions)
    
'''
def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    actualState = problem.getStartState()
    pila = [actualState]
    alreadyVisited = [actualState]
    directions = []
    i = 0
    while 1:
        justDeleted = False
        if problem.isGoalState(actualState):
            break
        successors = problem.getSuccessors(actualState)
        if len(successors) != 0: # Si tiene hijos
            try:
                i = 0
                nodo = successors[i]
                while nodo[0] in alreadyVisited:
                    i += 1
                    nodo = successors[i]
                actualState = nodo[0]
                directions.append(nodo[1])
            except IndexError:
                directions.pop()
                pila.pop()
                actualState = pila[-1]
                i = 0
        else: # Si no tiene hijos
            pila.pop()
            justDeleted = True
            directions.pop()
            actualState = pila[-1]
            i += 1
        if actualState not in pila and not justDeleted:
            pila.append(actualState)
        if actualState not in alreadyVisited:
            alreadyVisited.append(actualState)
        
    return directions
'''


def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # la mejor opcion es coste + distancia
    util.raiseNotDefined()


def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearchRecursive(problem, actualState, alreadyVisited, directions, heuristic, queue) -> List:
    alreadyVisited.add(actualState)
    if problem.isGoalState(actualState):
        return directions
    
    for nextState, action, _ in problem.getSuccessors(actualState):
        if nextState not in alreadyVisited:
            new_directions = directions + [action]  # Crear nueva lista en vez de modificar
            priority = problem.getCostOfActions(new_directions) + heuristic(nextState, problem)
            queue.push((nextState, new_directions), priority)

    if queue.isEmpty():
        return None  

    nextState, new_directions = queue.pop()
    return aStarSearchRecursive(problem, nextState, alreadyVisited, new_directions, heuristic, queue)


def aStarSearch(problem, heuristic=nullHeuristic) -> List:
    """Search the node that has the lowest combined cost and heuristic first."""
    actualState = problem.getStartState()
    alreadyVisited = set()  # Usar set para mejor eficiencia
    queue = util.PriorityQueue()
    
    return aStarSearchRecursive(problem, actualState, alreadyVisited, [], heuristic, queue) or []  # Evitar None



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
