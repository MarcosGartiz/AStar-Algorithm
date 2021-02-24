from copy import deepcopy
#Create a class named puzzle with all the parameters it will use
class puzzle:
    def __init__ (self, starting, parent):
        self.board = starting
        self.parent = parent
        self.f = 0
        self.g = 0
        self.h = 0
#Def of my heuristic function Manhattan distance
    def manhattan(self):
        inc = 0
        h = 0
        for i in range(3):
            for j in range(3):
                h += abs(inc-self.board[i][j])
            inc += 1
        return h

#Def function to compare the actual node to the goal node
    def goal(self):
        inc = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] != inc:
                    return False
                inc += 1
        return True
#Create a temporal node
    def __eq__(self, other):
        return self.board == other.board
#Def expand function
def Expand(u):
    u = u.board
    for i in range(3):
        for j in range(3):
            if u[i][j] == 0:
                x, y = i, j
                break
    q = []
    if x-1 >= 0:
        b = deepcopy(u)
        b[x][y]=b[x-1][y]
        b[x-1][y]=0
        succ = puzzle(b, u)
        q.append(succ)
    if x+1 < 3:
        b = deepcopy(u)
        b[x][y]=b[x+1][y]
        b[x+1][y]=0
        succ = puzzle(b, u)
        q.append(succ)
    if y-1 >= 0:
        b = deepcopy(u)
        b[x][y]=b[x][y-1]
        b[x][y-1]=0
        succ = puzzle(b, u)
        q.append(succ)
    if y+1 < 3:
        b = deepcopy(u)
        b[x][y]=b[x][y+1]
        b[x][y+1]=0
        succ = puzzle(b, u)
        q.append(succ)

    return q

def fvalue(openList):
    f = openList[0].f
    index = 0
    for i, item in enumerate(openList):
        if i == 0:
            continue
        if(item.f < f):
            f = item.f
            index  = i

    return openList[index], index
#Def A* algorithm
def AStar(start):
    openList = []
    closedList = []
    openList.append(start)

    while openList:
        current, index = fvalue(openList)
        if current.goal():
            return current
        openList.pop(index)
        closedList.append(current)

        X = Expand(current)
        for move in X:
            ok = False   #checking in closedList
            for i, item in enumerate(closedList):
                if item == move:
                    ok = True
                    break
            if not ok:              #not in closed list
                newG = current.g + 1
                present = False

                #openList includes move
                for j, item in enumerate(openList):
                    if item == move:
                        present = True
                        if newG < openList[j].g:
                            openList[j].g = newG
                            openList[j].f = openList[j].g + openList[j].h
                            openList[j].parent = current
                if not present:
                    move.g = newG
                    move.h = move.manhattan()
                    move.f = move.g + move.h
                    move.parent = current
                    openList.append(move)

    return None


#start = puzzle([[5,2,8],[4,1,7],[0,3,6]], None)
start = puzzle([[1,4,2],[0,7,5],[3,6,8]], None)
#start = puzzle([[1,2,0],[3,4,5],[6,7,8]], None)
# End state = [0,1,2],[3,4,5],[6,7,8]
result = AStar(start)
noofMoves = 0

if(not result):
    print ("No solution")
else:
    print(result.board)
    t=result.parent
    while t:
        noofMoves += 1
        print(t.board)
        t=t.parent
print ("Length: " + str(noofMoves))