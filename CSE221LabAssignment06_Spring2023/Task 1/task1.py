# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eHrSIL-yDqFaP5C9755ZGq08Srlg_fJN
"""

import math
from queue import PriorityQueue

def dijsktra(s,graph,c):
    dis_lst = [math.inf]*(n+1)
    queue = PriorityQueue()
    queue.put((c,s))
    while queue.empty()!= True:
        cost,src = queue.get()
        if dis_lst[int(src)] > cost:
            dis_lst[int(src)] = cost
            if graph[int(src)] != None:
                for i in graph[int(src)]:
                    src,up_cost = i
                    queue.put((up_cost+cost,src))
    return dis_lst


       
inp = open('/content/input1.txt','r')
out = open('/content/output1.txt','w')
n,m = list(map(int,inp.readline().split(" ")))
adj = [None]*(n+1)
for i in range(m):
    u,v,w = list(map(int,inp.readline().split(" ")))
    if adj[u]==None:
        adj[u] = [(str(v),w)]
    else:
        adj[u].append((str(v),w))
read = int(inp.readline())
obj = dijsktra(read,adj,0)
for i in range(1,len(obj)):
    if obj[i] == math.inf:
        print(-1,file = out, end=" ")
    else:
        print(obj[i], file = out, end=" ")

inp.close()
out.close()