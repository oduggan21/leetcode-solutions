class Solution:
    def foreignDictionary(self, words: List[str]) -> str:

        chars = set(''.join(words))
        
        adj = defaultdict(list) #what letters depend on this one
        count = {c: 0 for c in chars}

        for i in range(len(words)-1):
            w1,w2 = words[i], words[i+1]
            min_length = min(len(w1), len(w2))
            found_diff = False
            for j in range(min_length):
                if w1[j] != w2[j]:
                    adj[w1[j]].append(w2[j])
                    count[w2[j]] += 1
                    found_diff = True
                    break
            if not found_diff and len(w1) > len(w2):
                return ''
            
        queue = deque([c for c in count if count[c] == 0])
        string_final = ''
        while queue:
            c = queue.popleft()
            string_final+=c
            for val in adj[c]:
                count[val] -=1
                if count[val] == 0:
                    queue.append(val)
        if len(string_final) != len(chars):
            return ''

        return string_final

                
