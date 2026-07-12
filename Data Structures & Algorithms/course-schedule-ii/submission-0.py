class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # If the directed graph contains a cycle, you cannot finish all courses.

        graph = [[] for _ in range(numCourses)]
        # prerequisite -> course
        for course, prerequisite in prerequisites:
            # graph[prerequisite].append(course)
            # directed graph changed from 1->0 to 0->1
            graph[course].append(prerequisite)

        # 0 = unvisited, 1 = visiting, 2 = processed
        state = [0] * numCourses
        result = []

        def dfs(course):
            # We returned to a node in the current DFS path
            if state[course] == 1:
                return False
            
            # This course was already fully checked
            if state[course] == 2:
                return True
            
            # currently exploring course i, haven't finished checking all of its prerequisites/dependents yet."
            # course changes from 1 to 2 before DFS returns:
            # So 1 is temporary.
            # But 1 has not finished yet. That means:1 → 2 → 1. It comes back to state = 1.

            state[course] = 1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # Remove from current path; mark fully processed
            state[course] = 2
            result.append(course)
            return True

        # The graph may have disconnected components
        for course in range(numCourses):
            if not dfs(course):
                return []

        return result

              