### Name: Blake Buthod, Ethan Brizendine, Thomas Goodman, & George Wood
### Date: 12-9-2016
### File informedSearchUpdated.py
### Implements the informed search for the unblock me puzzle

from pq import *
from searchUnblock import *

class InformedNode(Node):
    """
    Added the goal state as a parameter to the constructor.  Also
    added a new method to be used in conjunction with a priority
    queue.
    """
    def __init__(self, state, parent, depth):
        Node.__init__(self, state, parent, depth)
    def priority(self):
        """
        Needed to determine where the node should be placed in the
        priority queue.  Depends on the current depth of the node as
        well as the estimate of the distance from the current state to
        the goal state.
        """
        return self.depth + self.state.heuristic()

class InformedSearchUnblock(Search):
    """
    A general informed search class that uses a priority queue and
    traverses a search tree containing instances of the InformedNode
    class.  The problem domain should be based on the
    InformedProblemState class.  
    """

    
    def __init__(self, initialState):
        self.expansions = 0
        self.clearVisitedStates()
        self.q = PriorityQueue()
        self.q.enqueue(InformedNode(initialState, None, 0))
        solution = self.execute()
        if solution == None:
            print("Search failed")
        else:
            self.showPath(solution)
            print("Expanded", self.expansions, "nodes during search")
    def execute(self):
        while not self.q.empty():
            current = self.q.dequeue()
            self.expansions += 1
            
            # Checks if the target block is in the exit
            currentState = current.state
            targetBlock = currentState.blockList[currentState.targetInd]
            coordList = targetBlock.getCoords()
            if ((targetBlock.getNum == 1)
                and ((2,6) in coordList) and ((2,7) in coordList)):
                return current
            # Goal state not reached, push new nodes to pq
            else:
                successors = current.state.applyOperators()
                for i in range(len(successors)):
                    if not successors[i].illegal():
                        n = InformedNode(successors[i],
                                         current,
                                         current.depth+1)
                        if n.repeatedState():
                            del(n)
                        else:
                            self.q.enqueue(n)
        return None
            

class InformedProblemState(ProblemState):
    """
    An interface class for problem domains used with informed search.
    """
    def heuristic(self):
        """
        For use with informed search.  Returns the estimated
        cost of reaching the goal from this state.
        """
        abstract()

