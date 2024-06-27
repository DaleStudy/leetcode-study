"""
207. Course Schedule
https://leetcode.com/problems/course-schedule/

Solution: 
    If there is a cycle in the graph, it is impossible to finish all courses.
    We can detect a cycle by using DFS and keeping track of the state of each node.
    
    - We can create an adjacency list to represent the graph.
    - We can use a state array to keep track of the state of each node.
        - 0: unvisited, 1: visiting, 2: visited
    - We can create a helper function to check if there is a cycle starting from a node.
        - If the node is being visited, we have a cycle.
        - If the node has been visited, there is no cycle.
        - If not, we mark the node as visiting and explore its neighbors.
        - After exploring all neighbors, we mark the node as visited.
    - We can iterate through all nodes and check for cycles.
    - If we find a cycle, we return False.
    - If no cycle is found, we return True.

Time complexity: O(m + n)
    - m is the number of prerequisites.
    - n is the number of courses.
    - We explore all prerequisites and courses once.

Space complexity: O(m + n)
    - We use an adjacency list to represent the graph.
    - We use a state array to keep track of the state of each node.
"""

from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        # State: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses

        def has_cycle(v):
            if state[v] == 1:  # Node is being visited, so we have a cycle
                return True
            if state[v] == 2:  # Node has been visited, no cycle here
                return False
            
            state[v] = 1
            for neighbor in adj_list[v]:
                if has_cycle(neighbor):
                    return True
            
            state[v] = 2
            return False

        for course in range(numCourses):
            if state[course] == 0:
                if has_cycle(course):
                    return False
        
        return True