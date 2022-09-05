import re
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot=self.findpivot(nums,target)
        part1=self.binarysearch(nums,target,0,pivot)
        if(part1==-1):
            part2=self.binarysearch(nums,target,pivot+1,len(nums)-1)
            return part2
        else :return part1
    
    def binarysearch(self,nums:List[int],target:int,st:int,end:int)->int:
        l=st
        h=end
        while(l<=h):
            mid=l+(h-l)//2
            if(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                h=mid-1
            else:
                return mid
        return -1

    
    
    def findpivot(self,nums:List[int],target:int)->int:
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=l+(h-l)//2
            if(nums[mid]<=nums[len(nums)-1]):
                h=mid-1
            else:
                if(nums[mid]>nums[mid+1]):
                    return mid
                else:
                    l=mid+1
        return -1


ans=Solution()
print(ans.search([4,5,6,7,0,1,2],0))