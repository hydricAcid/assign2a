import random as r
import os
import time as t
import tracemalloc as tr
from node import Node
from edge import Edge

def generateGraph(nodeCount,minX,maxX,minY,maxY,minEdge,maxEdge,maxCost,minCost,destNum):
    print("Generating...")
    lines = []

    nodeList = []
    edgeList = []
    destList = []

    XcoordList = []
    YcoordList = []

    i = 1
    while i <= nodecount:
        validCoords = False
        while not validCoords:
            randomX = r.randint(minX,maxX)
            randomY = r.randint(minY,maxY)
            validCoords = True
            
            if len(XcoordList) != 0:
                coordCount = 0
                currentCoordAmt = len(XcoordList)
                while coordCount < currentCoordAmt:
                    currentX = XcoordList[coordCount]
                    currentY = YcoordList[coordCount]

                    if currentX == randomX and currentY == randomY: # checks if coords are already occupied
                        validCoords = False
                    coordCount += 1
                    
                if validCoords:
                    XcoordList.append(randomX)
                    YcoordList.append(randomY)
                    nodeList.append(Node(i,randomX,randomY))
                    
            else:
                XcoordList.append(randomX)
                YcoordList.append(randomY)
                nodeList.append(Node(i,randomX,randomY))
        i += 1

    lines.append("Nodes:")
    for obj in nodeList:
        lines.append(f"{obj.number}: ({obj.x},{obj.y})")

    '''
    print("Nodes:")
    for obj in nodeList:
        print(f"{obj.number}: ({obj.x},{obj.y})")
    '''

    for obj in nodeList:
        edgeAmt = r.randint(minEdge,maxEdge)
        edgeCurrent = 0
        while edgeCurrent < edgeAmt:
            validEdge = False
            while not validEdge:
                if len(edgeList) != 0:

                    randomNode = nodeList[r.randint(0,(len(nodeList) - 1 ))]
                    if obj.number != randomNode.number: # checks if the start and end are the same node
                        validEdge = True

                    for edge in edgeList:
                        if edge.start == obj.number and edge.end == randomNode.number: # checks if edge already exists
                            validEdge = False
                        
                    if validEdge:
                        edgeList.append(Edge(obj.number,randomNode.number))
                else:
                    randomNode = nodeList[r.randint(0,(len(nodeList) - 1 ))]
                    if obj.number != randomNode.number:
                        validEdge = True
                        edgeList.append(Edge(obj.number,randomNode.number))
            edgeCurrent += 1
    
    lines.append("Edges:")
    for obj in edgeList:
        randCost = r.randint(minCost,maxCost)
        obj.cost = randCost
        lines.append(f"({obj.start},{obj.end}): {obj.cost}")

    '''
    print("Edges: ")
    for obj in edgeList:
        print(f"({obj.start},{obj.end}): {obj.cost}")
    '''

    lines.append("Origin:")
    origin = r.randint(1,len(nodeList) - 1)
    lines.append(origin)
    lines.append("Destinations:")
    i = 0
    while i < destNum:
        dest = r.randint(1,len(nodeList) - 1)
        if dest != origin and not str(dest) in destList:
            destList.append(str(dest))
            i += 1
    dests = ";".join(destList)
    lines.append(dests)

    return lines



if __name__ == "__main__":
    fileName = input("name of file: ")
    nodecount = int(input("number of nodes: "))

    minx = int(input("min x: "))
    maxx = int(input("max x: "))
    miny = int(input("mix y: "))
    maxy = int(input("max y: "))

    if ((maxx-minx)*(maxy-miny)) < nodecount: # checks if total size is large enough to fit the graph
        print("plane too small")
        exit()

    minCost = int(input("min edge cost: ")) 
    maxCost = int(input("max edge cost: "))
    
    minEdge = int(input("min edge amount per node: "))
    maxEdge = int(input("max edge amount per node: "))

    if maxEdge > nodecount: # checks if the number of edges could be greater than the number of nodes
        print("too many possible edges for a node")
        exit()

    destNum = int(input("number of destinations: "))

    startTime = t.time() # runtime and memory measuring
    tr.start()


    lines = generateGraph(nodecount,minx,maxx,miny,maxy,minEdge,maxEdge,maxCost,minCost,destNum)
    
    endTime = t.time()
    print("Done")
    print(f"Memory usage: {tr.get_traced_memory()}")
    print(f"execution time: {(endTime-startTime) * 10**3} ms")
    tr.stop()

    f = open(f"autoTestCases/{fileName}.txt", "w")
    for c in lines:
        f.write(str(c))
        f.write("\n")
    f.close()

        

