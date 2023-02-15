// https://leetcode.com/problems/find-target-indices-after-sorting-array

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count=0
        same_num=0
        for i in nums:
            if i<target:
                count+=1
            elif i==target:
                same_num+=1
        arr=[0]*same_num
        for i in range(same_num):
            arr[i]=count
            count+=1
        
        return arr