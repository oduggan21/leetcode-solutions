class TimeMap:

    def __init__(self):
        self.keys = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((value,timestamp))
    #in this function we are attempting to find essentially the value closest to our timestamp
    def get(self, key: str, timestamp: int) -> str:
            if key in self.keys:
                list_new = list(self.keys[key])
            else:
                 return ''
            l = 0
            r = len(list_new) - 1
            best_index= -1
            while(l <= r):
                mid = (l + r) // 2
                if list_new[mid][1] <= timestamp:
                    best_index = mid
                    l = mid + 1
                else: 
                    r = mid -1
            return list_new[best_index][0] if best_index >= 0 else ''

