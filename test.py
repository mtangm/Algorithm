class Solution:
    def permute(self, nums) :
        if not nums:
            return []
        
        res = []
        
        def helper(path, nums_left):
            if not nums_left:
                res.append(path)
                return 
                
            for i in range(len(nums_left)):
                helper(path + [nums_left[i]], nums_left[:i]+nums_left[i+1:])
            
        helper([], nums)
        return res 
    
    
        
    
nums = [1,2,3]
s = Solution()
print(s.permute(nums))        