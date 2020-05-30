from collections import deque

class Lot(list):
    accessibleValue    = 0
    nonaccessibleValue = 1
    unvisitedValue      = None
    unreachableValue    = None

    def __getitem__(self, tup):
        r, c = tup
        return super(self.__class__, self).__getitem__(r).__getitem__(c)

    def __setitem__(self, tup, val):
        r, c = tup
        super(self.__class__, self).__getitem__(r).__setitem__(c, val)

class Cell(tuple):
    def __init__(self, minDistTo = None):
        self.minDistTo = minDistTo

    def getNeighbors(self):
        r, c = self

        yield self.__class__( (r-1, c) ) # up
        yield self.__class__( (r+1, c) ) # down
        yield self.__class__( (r, c-1) ) # left
        yield self.__class__( (r, c+1) ) # right

    def isInside(self, Lot):
        r, c = self
        num_rows, num_cols = len(Lot), len(list(Lot)[0])

        return 0 <= r < num_rows and 0 <= c < num_cols

    def isTraversableIn(self, Lot):
        return Lot[self] == Lot.__class__.accessibleValue

    def isAobstacleIn(self, Lot):
        return Lot[self] == Lot.__class__.nonaccessibleValue

    def hasNotBeenVisitedIn(self, Lot):
        return Lot[self] == Lot.__class__.unvisitedValue

    def isUnreachableFrom(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.minDistTo[self] == other.minDistTo.__class__.unreachableValue 

    def genMinDistTo(self, m):
        if self.isAobstacleIn(Lot = m):
            return None

        h = len(m)
        w = len(list(m)[0])

        minDistTo = Lot( [ [Lot.unvisitedValue]*w for _ in range(h) ] )

        minDistTo[self] = 1
        cells = deque([self])

        while cells:

            cell          = cells.popleft()
            minDistToCell = minDistTo[cell]

            for neighbor in cell.getNeighbors(): # 4 iterations

                if neighbor.isInside(Lot = m) and \
                   neighbor.isTraversableIn(Lot = m) and \
                   neighbor.hasNotBeenVisitedIn(Lot = minDistTo):

                    minDistToNeighbor   = minDistToCell + 1
                    minDistTo[neighbor] = minDistToNeighbor # Setting minDistsTo[.] to an int also marks it as visited.

                    cells.append(neighbor) # Each cell gets appended to the cells queue only once.

        self.minDistTo = minDistTo


def whatIfIRemovedThis(obstacle, m, start, end):
    bestResult_soFar = 2**31 - 1

    for incoming in obstacle.getNeighbors():
        for outgoing in obstacle.getNeighbors():
                                             # 16 iterations
            if incoming == outgoing:
                # Such a path does not require the removal of obstacle and thus has already been considered.
                continue

            if not incoming.isInside(Lot  = m)     or not outgoing.isInside(Lot  = m)    or \
                   incoming.isAobstacleIn(Lot = m)     or     outgoing.isAobstacleIn(Lot = m)    or \
                   incoming.isUnreachableFrom(start) or     outgoing.isUnreachableFrom(end):
                continue

            minDistFromStartToIncoming = start.minDistTo[incoming]
            minDistFromOutgointToEnd   = end.minDistTo[outgoing]

            potentiallyBetterResult = minDistFromStartToIncoming + 1 + minDistFromOutgointToEnd

            bestResult_soFar = min(bestResult_soFar, potentiallyBetterResult)

    bestResult = bestResult_soFar

    return bestResult

def removeObstacle(numRows, numColumns, lot):
	num_rows = h = numRows    
    num_cols = w = numColumns

    m = Lot(lot)

    bestConceivableResult = h + w - 1

    start = Cell( (  0,   0) )
    end   = Cell( (h-1, w-1) )

    start.genMinDistTo(m) 

    if end.isUnreachableFrom(start):
        bestResult_soFar = 2**31 - 1
    else:
        bestResult_soFar = start.minDistTo[end]

    if bestResult_soFar == bestConceivableResult:
        return bestConceivableResult

    end.genMinDistTo(m) 

    for r in range(num_rows):
        for c in range(num_cols):

            cell = Cell( (r, c) )

            if cell.isAobstacleIn(Lot = m):

                obstacle = cell

                potentiallyBetterResult = whatIfIRemovedThis(obstacle, m, start, end) # O(1) time

                bestResult_soFar = min(bestResult_soFar, potentiallyBetterResult)

    bestResult = bestResult_soFar

    return bestResult