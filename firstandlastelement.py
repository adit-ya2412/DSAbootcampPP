from re import M
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        firsele=self.findfirst(nums,target,True)
        lasele=self.findfirst(nums,target,False)
        return [firsele,lasele]

    def findfirst(self,nums:List[int],target:int,first:bool)->int:
        l=0
        h=len(nums)-1
        while(l<=h):
            mid=l+(h-l)//2
            if(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                h=mid-1
            else:
                if(first):
                    if(mid==0):
                        return mid
                    elif(nums[mid-1]==target):
                        h=mid-1
                    else:
                        return mid
                else:
                    if(mid==len(nums)-1):
                        return mid
                    elif (nums[mid+1]==target):
                        l=mid+1
                    else :
                        return mid        
        return -1


ans=Solution()

print(ans.searchRange([5,7,7,8,8,10],8))