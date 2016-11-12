### Name: Blake Buthod
### Date: 9-30-2016
### File missionary.py
### Implements the missionary and cannibals problem for state space search

from search import *

class MissionaryState(ProblemState):
    """
    The missionary and cannibals problem: Three cannibals and three
    missionaries need to cross a river. They have a boat that can
    hold one or two people. At no point can the cannibals on either
    side outnumber the missionaries, or they'll get eaten. The goal
    is to get all three cannibals and missionaries to the other side
    without anyone getting eaten.

    Each operator returns a new instance of this class representing
    the successor state.
    """
    def __init__(self, lCann, lMiss, rCann, rMiss, boat):
        self.lCann = lCann
        self.lMiss = lMiss
        self.rCann = rCann
        self.rMiss = rMiss
        self.boat = boat
    def __str__(self):
        """
        Required method for use with the Search class.
        Returns a string representation of the state.
        """
        return "("+str(self.lCann)+","+str(self.lMiss)+","+str(self.rCann)+","+str(self.rMiss)+","+str(self.boat)+")"    
    def illegal(self):
        """
        Required method for use with the Search class.
        Tests whether the state is illegal.
        """
        if self.lCann > 3 or self.lCann < 0: return 1
        if self.rCann > 3 or self.rCann < 0: return 1

        if self.lMiss > 3 or self.lMiss < 0: return 1
        if self.rMiss > 3 or self.rMiss < 0: return 1

        if self.boat > 1 or self.boat < 0: return 1
                                                               
        if self.lCann > self.lMiss and self.lMiss != 0: return 1
        if self.rCann > self.rMiss and self.rMiss != 0: return 1
        
        return 0
    def equals(self, state):
        """
        Required method for use with the Search class.
        Determines whether the state instance and the given
        state are equal.
        """
        return self.lCann==state.lCann and self.lMiss==state.lMiss and self.rCann==state.rCann and self.rMiss==state.rMiss and self.boat==state.boat
    def sendOneCannAcross(self):
        """
        Sends one cannibal across the river.
        """
        return MissionaryState(self.lCann-1, self.lMiss, self.rCann+1, self.rMiss, self.boat+1)
    def sendOneCannBack(self):
        """
        Sends one cannibal back.
        """
        return MissionaryState(self.lCann+1, self.lMiss, self.rCann-1, self.rMiss, self.boat-1)

    def sendOneMissAcross(self):
        """
        Sends one missionary across the river.
        """
        return MissionaryState(self.lCann, self.lMiss-1, self.rCann, self.rMiss+1, self.boat+1)
    def sendOneMissBack(self):
        """
        Sends one missionary back.
        """
        return MissionaryState(self.lCann, self.lMiss+1, self.rCann, self.rMiss-1, self.boat-1)

    def sendTwoCannAcross(self):
        """
        Sends two cannibals across the river.
        """
        return MissionaryState(self.lCann-2, self.lMiss, self.rCann+2, self.rMiss, self.boat+1)
    def sendTwoCannBack(self):
        """
        Sends two cannibals back.
        """
        return MissionaryState(self.lCann+2, self.lMiss, self.rCann-2, self.rMiss, self.boat-1)

    def sendTwoMissAcross(self):
        """
        Sends two missionaries across the river.
        """
        return MissionaryState(self.lCann, self.lMiss-2, self.rCann, self.rMiss+2, self.boat+1)
    def sendTwoMissBack(self):
        """
        Sends two missionaries back.
        """
        return MissionaryState(self.lCann, self.lMiss+2, self.rCann, self.rMiss-2, self.boat-1)

    def sendOneOfEachAcross(self):
        """
        Sends one cannibal and one missionary across the river.
        """
        return MissionaryState(self.lCann-1, self.lMiss-1, self.rCann-1, self.rMiss-1, self.boat+1)
    def sendOneOfEachBack(self):
        """
        Sends one cannibal and one missionary back.
        """
        return MissionaryState(self.lCann+1, self.lMiss+1, self.rCann-1, self.rMiss-1, self.boat-1)
                                                               
    def operatorNames(self):
        """
        Required method for use with the Search class.
        Returns a list of the operator names in the
        same order as the applyOperators method.
        """
        return ["sendOneCannAcross", "sendOneCannBack",
                "sendOneMissAcross", "sendOneMissBack",
                "sendTwoCannAcross", "sendTwoCannBack",
                "sendTwoMissAcross", "sendTwoMissBack",
                "sendOneOfEachAcross", "sendOneOfEachBack"]
    def applyOperators(self):
        """
        Required method for use with the Search class.
        Returns a list of possible successors to the current
        state, some of which may be illegal.  
        """
        return [self.sendOneCannAcross(), self.sendOneCannBack(),
                self.sendOneMissAcross(), self.sendOneMissBack(),
                self.sendTwoCannAcross(), self.sendTwoCannBack(),
                self.sendTwoMissAcross(), self.sendTwoMissBack(),
                self.sendOneOfEachAcross(), self.sendOneOfEachBack()]

Search(MissionaryState(3,3,0,0,0), MissionaryState(0,0,3,3,1))
