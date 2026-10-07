class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k=[]
        for num in nums:
            if num==val:
                continue
            k.append(num)
        for i in range(len(k)):
            nums[i]=k[i]
        return len(k)

        
