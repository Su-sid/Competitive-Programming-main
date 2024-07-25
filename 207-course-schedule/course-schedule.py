class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build up the graph
        graph = defaultdict(set)
        for (course, prereq) in prerequisites:
            graph[course].add(prereq)
        
        # add courses without prereqs
        for course in range(numCourses):
            if course not in graph:
                graph[course] = set()
        
        count = 0
        no_prereqs = [course for course in graph if not len(graph[course])]
        while len(no_prereqs) and count < numCourses:
            # get a course with no prereqs
            curr = no_prereqs.pop()
            # increment count
            count += 1
            # 'take' the course by removing it from graph
            # and from the prereqs of other courses
            graph.pop(curr)
            for course in graph:
                graph[course].discard(curr)
            
            # recompute no_prereqs
            no_prereqs = [course for course in graph if not len(graph[course])]
        
        return count == numCourses