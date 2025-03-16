""""
Started learning DP and Greedy approach 
Difference between DP and GReedy:
Both are used for solving optimization problems
Greedy : We use predefined procedure to find out the solution
DP     :  We will try to find all the possible solutions and find the best approach

feasible solutions , optimal solutions

Questions list in Greedy:

   1 . Knapsack problem
   2 . Job sequencing with deadlines
   3 . Single source shortest path
   4 . Minimum cost spanning tree

"""
"""
1 . fiboannci in DP
    we can use both recursive and iterative approaches

"""

Iterative approach
def fib(n):
    l = [0] * (n + 1)
    l[0], l[1] = 0, 1  
    for i in range(2,n+1):
        l[i]=l[i-1]+l[i-2]
    return l[n]
print("enter the value which you want:")
n=int(input())
print(fib(n))

Recursive approach:

def fib(n):
    if n<=1:
        return n 
    return fib(n-1)+fib(n-2)
print("enter the value which you want:")
n=int(input())
print(fib(n))

#Minimum cost spanning tree
"""
2 methods(prims and krushkal)

spanning tree properties: A spanning tree is subgraph of given graph
If graph contains n vertices , then spanning tree should have n vertices
If graph contains n edges , then spanning tree should have n-1 edges
should not contain cycle.

1 .prims algorithm:
      
    A. Start with any vertex in the given graph
    B. Find the edges associated with that vertex , and add minimum cost edge to the spanning tree if it is not 
    forming any cycle . If it is forming a cycle then discard that edge.
    C. Repeat 2nd step until all the vertices are covered.

2 . Krushkals Algorithm:
   
    A. Arrange all the edges in ascending order based upon the cost
    B. Select Minimim cost edge and add thet edge to spanning tree if it is not forming any cycle
    C. Repeat second step until all the vertices are covered.


JOB SEQUENCING WITH DEADLINES:

 1. Arrange all the jobs in decreading order based on the profit
 2. select first job and execute it by assigning  slot.
    
   if deadline is r, then we have to assign the slot [r-1,r]
   if that sort is already assigned , then we have to assign to [r-2,r-1]
   and so on----
   

Dijkstra algorithm: (Directed and weighted graphs)
 - Mark all nodes as unvisited
 - Take source node
 - Set the distance of souce node to 0 and all othe nodes to infinity
 1. Start from souce node
    - keep it as current
    - check all unvisited neighbors
    - Calculate the tentative distances
    - If the tentative distance is smaller than the currently recorded distace, the update for it
2. Mark Node as visited
    - Add the current node to visited set(visited nodes are never checked again)
    - Select the vunvisisted nodes with the smallest tentaive distance and keep as new current node
3. Repeat step 2 and step 3 untill all nodes are visited.
 
"""
#Disadvantages
#Dijkstra algorithm may or may not work for negative weights







