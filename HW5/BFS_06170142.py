# Python3 Program to print BFS traversal 
# from a given source vertex. BFS(int s) 
# traverses vertices reachable from s. 
from collections import defaultdict 
  
# This class represents a directed graph 
# using adjacency list representation 
class Graph:
    # Constructor 
    def __init__(self): 
        # default dictionary to store graph 
        self.graph = defaultdict(list) 

    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    # Function to print a BFS of graph 
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """                                              
        visited = [False] * (len(self.graph))  #把還沒查訪果的點標記False
        queue = []                             #把輸入的數字加入 並把加入的標記改成True
        queue.append(s)       
        visited[s] = True
  
        while queue:        #while會跑很多次  if只會跑一次
  
            s = queue.pop(0)                   #把第一個(取出不放回)取出來
            print (s, end = " ") 
  
            for i in self.graph[s]:            #其餘還沒檢測的 push進pop的這個迴圈
                if visited[i] == False: 
                    queue.append(i) 
                    visited[i] = True        
            
    def DFSUtil(self, v, visited): 
  
        visited[v] = True
        print(v, end = ' ') 
   
        for i in self.graph[v]: 
            if visited[i] == False: 
                self.DFSUtil(i, visited) 
  
    def DFS(self, v): 
        """
        :type s: int
        :rtype: list
        """
  
        visited = [False] * (len(self.graph)) 
  
        self.DFSUtil(v, visited)        
