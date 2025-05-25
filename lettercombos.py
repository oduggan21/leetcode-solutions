class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        final_list = []
        mapping = {
        2:['a','b','c'],
        3: ['d','e','f'],
        4: ['g','h','i'],
        5: ['j','k','l'],
        6: ['m','n','o'],
        7: ['p','q','r','s'],
        8: ['t','u','v'],
        9: ['w','x','y','z']
        }

        def backtracking(index, path):
            
            if index == len(digits):
                final_list.append(path)
                return
            if index > len(digits):
                return
        
            list_letters = mapping[int(digits[index])]
            for letter in list_letters:
                path+= letter
                backtracking(index+1,path)
                path = path[:-1]
        backtracking(0,'')
        if not digits:
            return []
        return final_list

