# BFS-DFS_Search_Python

Created By : - Galang Rambu Anarqi - M. Wahyu Kuncoro

BFS and DFS Algorithm

1. Make a graph 
    - Ex : - A -> B,C,D 
           - B -> A,C,E,F,G 
           - C -> A,B,D 
           - etc.

2. First set start node and goal 
    - Ex : rute_dfs/bfs(graph, 'start', 'goal')

3. Initiate Queue (FIFO) for BFS or Stack (LIFO) for DFS
    - Ex : queue/stack = [(start, [start])]

4. Visit all nodes using loop by taking a node on the queue/stack and check wheter its not empty 
    - Ex : queue/stack.pop[n] , n=0 -> BFS n=-1 -> DFS

5. Select the nodes and its path which has difference value 
    - Ex : node[A,B,C] different [A,C] (this part to avoid visited node being taken) node = B

6. Check the node wheter is a GOAL
   - if TRUE, return route (edge + node)
   - if False, append the current edge and node to the queue or stack

7. Record all route that has been found on the list 
    - Ex : List(rute_dfs/bfs(graph, 'start', 'goal'))

8. Check List
   - if not empty, Show the priority routes of BFS or DFS process from the list Ex : list_route[0]
   - if empty, Show message that routes has not been found
