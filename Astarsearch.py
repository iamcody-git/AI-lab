inputGraph = {
'A': [('B', 7, 8), ('D', 9, 5)],
'B': [('A', 7, 10), ('C', 11, 3)],
'C': [('D', 5, 12), ('B', 13, 4)],
'D': [('A', 5, 14), ('C', 15, 3)],
}
goal='C'
def gbfs(graph, start):
    rootToParentCost = 0 # Keeps track of cumulative cost
    queue = [start + (rootToParentCost, )] # Append cost to start tuple
    visitedNodes = [] # Stores visited nodes
    
    while queue:
        queue = sorted(queue, key=lambda x: x[1] + x[2] + x[3]) # The queue is sorted based on the
#sum of: Edge cost (x[1]),Heuristic value (x[2]),Cumulative cost (x[3]

        node = queue.pop(0)
        rootToParentCost = node[1] + node[3] # Update cost
        if node not in visitedNodes:
            visitedNodes.append(node)
            
        if node[0] == goal: # Stop if goal is found
            break
        
        neighbours = graph[node[0]]
        
        for neighbour in neighbours:
            queue.append(neighbour + (rootToParentCost, )) # Append new cost
    return visitedNodes
    
visitedNodes = gbfs(inputGraph, ('A', 5, 16))
print(visitedNodes)