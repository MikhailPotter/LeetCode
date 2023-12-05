class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        parsed_matrix = [[] for i in range(n)]
        for conn_start, conn_end in connections:
            parsed_matrix[conn_start].append([conn_end, 1])
            parsed_matrix[conn_end].append([conn_start, 0])
            
        passed = set()
        passed.add(0)
        def go_deep(parsed_matrix, curr):
            nonlocal passed

            res = 0
            for i, v in parsed_matrix[curr]:
                if i in passed:
                    continue

                passed.add(i)
                res += v + go_deep(parsed_matrix, i)

            return res

        return go_deep(parsed_matrix, 0)