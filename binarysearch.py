
from typing import List
class Solution:
    def binarysearch(self,nums:List[int],target:int)->int:
         l=0
         h=len(nums)-1
         while(l<=h):
            mid=l+(h-l)//2
            if(nums[mid]<target):
                l=mid+1
            elif(nums[mid]>target):
                h=mid-1
            else:
                return mid
         return -1
ans=Solution()
print(ans.binarysearch([1,3,5,7,12,15],13))