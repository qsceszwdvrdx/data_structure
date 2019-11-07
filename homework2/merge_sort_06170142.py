###### merge_sort_ID.py

class Solution(object):
    def merge_sort(self,nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
        self.nums=nums
        
        n=len(nums)
        if n<= 1:
            return nums
        else:
            m=n//2                #切割方法
            left=nums[0:m]
            right=nums[m:]  

            Solution().merge_sort(left)                 
            Solution().merge_sort(right)     #切到不能再切           

            i=0
            l=0
            r=0

            while l<len(left) and r<len(right):      #比較方法小的先放
                if left[l]<right[r]:                 #放好往下移一個位置
                    nums[i]=left[l]
                    l=l+1 
                else:
                    nums[i]=right[r]
                    r=r+1
                i=i+1
                
            while l < len(left):           #要再檢查一次 不然落單的沒執行到
                nums[i] = left[l]          #原本測試的資料都沒這種狀況 所以差點漏掉 
                l = l+1
                i = i+1

            while r < len(right):
                nums[i]=right[r]
                r = r+1
                i = i+1

                
            return nums
