### Name: Blake Buthod, Ethan Brizendine, Thomas Goodman, & George Wood
### Date: 12-9-2016
### File informedSearchUpdated.py
### Implements the informed search for the unblock me puzzle

from pq import *
from searchUnblock import *
from block import *

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

    
    def __init__(self, initialState, display):
        self.initialState = initialState
        self.fileIDToWrite = -1
        self.display = display
        self.expansions = 0
        self.clearVisitedStates()
        self.q = PriorityQueue()
        self.q.enqueue(InformedNode(initialState, None, 0))
        solution = self.execute()
        if solution == None:
            print("Search failed")
        else:
            self.showPath(solution, display, self.fileIDToWrite)
            print("Expanded", self.expansions, "nodes during search")
    def execute(self):
        #Check if this solution is already in the list of previously played games
        checkID = self.getIDFromGameList()
        
        #If a solution is availible, get it
        solutionMoves = []
        if checkID != -1:
            print("Solution found with id: " + str(checkID))
            solutionMoves = self.getSolution(checkID)
    
        while not self.q.empty():
            current = self.q.dequeue()
            #print(str(current))
            self.expansions += 1
            
            # Checks if the target block is in the exit
            currentState = current.state
            targetBlock = currentState.blockList[currentState.targetInd]
            coordList = targetBlock.getCoords()
            
            if ((targetBlock.getNum() == 1)
                and ((4,2) in coordList) and ((5,2) in coordList)):
                return current
            # Goal state not reached, push new nodes to pq
            else:
                if checkID != -1:
                    #First try the solution's moves before normally applying operators
                    if self.expansions - 1 < len(solutionMoves):
                        solution = solutionMoves[self.expansions - 1]
                        successors = current.state.applyOperatorsKnowledge(int(solution[0]), int(solution[1]), int(solution[2]) )
                    else:
                        successors = current.state.applyOperators()
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

    def getIDFromGameList(self):
        """
        Searches through the list of initial states previously encountered (in games.txt)
          and if the initial state is found, returns the unique ID to that solution.
          If not, the id returned is -1.

          The game state file format goes:
            STATE id
            numberOfBlocks
            (for each block)
            blockNumber orientation size xPosition yPosition
            
        """
        currState = self.initialState #We want to check the initial state
        newBlockList = []
        file = open("games.txt")
        lineCounter = 0 #Keep track of how many lines we are into the current state being read
        numBlocks = 0
        checkID = 0 #The ID of the game state currently being checked
        self.fileIDToWrite = 1 #Keeps track of how many blocks have been encountered to know what id to assign if none are found
        for line in file:
            if lineCounter == 0:
                idInfo = line.split()
                if len(idInfo) == 0: #Empty file or something went wrong, abort
                    return -1
                checkID = int(idInfo[1]) #Grab the second item, which will be the id number
            elif lineCounter == 1:
                numBlocks = int(line)
            else:
                blockInfo = line.split()
                newBlockList.append( Block(int(blockInfo[0]), int(blockInfo[3]), int(blockInfo[4]), int(blockInfo[2]), blockInfo[1]) )
            lineCounter += 1
            #Check if the end of the state has been read
            if lineCounter > 1 + numBlocks:
                #Compare the current blocks with the initial state's blocks
                if len(newBlockList) == len(currState.blockList):
                    blocksAreSame = True
                    for i in range(len(newBlockList)):
                        checkBlock = newBlockList[i]
                        initialBlock = currState.blockList[i]
                        if checkBlock.getSize() != initialBlock.getSize() or checkBlock.getOrientation() != initialBlock.getOrientation() or checkBlock.getCoords() != initialBlock.getCoords():
                            blocksAreSame = False
                            break           
                    if blocksAreSame == True:
                        self.fileIDToWrite = -1
                        return checkID
                #If blocks are not the same, reset to check the next one
                self.fileIDToWrite += 1
                numBlocks = 0
                newBlockList = []
                lineCounter = 0
                
        file.close()

        return -1 #None found

    def getSolution(self, solutionID):
        """
        Searches through the list of game solutions given a particular solutionID.
          Once the solution with the appropriate ID is found, that solution is returned.

          Solutions are a list of tuples with the following format:
            (blocknumber, xMoved, yMoved)

          The solution file format goes:
            SOLUTION id
            numberOfSteps
            (for each step)
            blockNumber, xMoved, yMoved
        """
        solution = []
        file = open("solutions.txt")
        lineCounter = 0
        checkID = 0
        numSteps = 0
        for line in file:
            if lineCounter == 0:
                idInfo = line.split() 
                checkID = int(idInfo[1]) #Grab the second item, which will be the id number
            elif lineCounter == 1:
                numSteps = int(line)
            else:
                #Only populate solution if this is the correct solution
                if solutionID == checkID:
                    solutionStep = line.split()
                    solution.append(( int(solutionStep[0]), int(solutionStep[1]), int(solutionStep[2]) ))

            lineCounter += 1
            #Check if the end of the solution has been read
            if lineCounter > 1 + numSteps:           
                numSteps = 0
                lineCounter = 0
        
        return solution

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
