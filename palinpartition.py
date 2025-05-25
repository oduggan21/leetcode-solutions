class Solution:
    def partition(self, s: str) -> List[List[str]]:
        final_list = []

        def backtracking(start: int, path: List[str]):
            if start == len(s):
                final_list.append(list(path))
                return
            
            for end in range(start, len(s)):
                substr = s[start:end+1]
                if substr == substr[::-1]:
                    path.append(substr)
                    backtracking(end+1,path)
                    path.pop()
        backtracking(0,[])
        return final_list
