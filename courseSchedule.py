from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        adj = defaultdict(list)
        prereqs = [0] * numCourses

        for a , b in prerequisites:
            adj[b].append(a)
            prereqs[a] += 1
        
        queue = deque([course for course in range(numCourses) if prereqs[course] == 0])
        taken = 0 

        while queue:
            course = queue.popleft()
            taken += 1
            for edge in adj[course]:
                prereqs[edge] -=1
                if prereqs[edge] == 0:
                    queue.append(edge)
        
        return taken == numCourses



        
