class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # target = desination mile to be reached
        # cars cannot cross each other XX [4, 1 ] 00 [ 3, 3 ]
        # fleet = [ 2, 2 ] OR [ 1, 2, 3 ]
        desc = []
        res = []

        for index in range(len(position)):
            desc.append((position[index], speed[index]))
        
        desc.sort(key = lambda item: item[0], reverse=True)
        for item in desc:
            p = item[0]
            s = item[1]
            time = ((target - p) / s)
            if not res:
                res.append(time)
            elif time <= res[-1]:
                continue
            else:
                res.append(time)
        
        return len(res)
