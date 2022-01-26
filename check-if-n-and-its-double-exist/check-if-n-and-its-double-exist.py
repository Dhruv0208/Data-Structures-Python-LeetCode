class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        dict_number = collections.defaultdict(int)
        for i in range(len(arr)):
            if 2*arr[i] in dict_number or arr[i]/2 in dict_number:
                return True
            else:
                dict_number[arr[i]] = i
        return False
        
        