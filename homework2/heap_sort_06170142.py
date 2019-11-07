##### heap_sort_ID.py

class Solution(object):
    
    def heap(self,nums,i,n):
        
        self.nums=nums
        top=i                                   #序數的大小關係
        left=2*i+1
        right=2*i+2

        if left<n and nums[top]<nums[left]:   #比大小 先比左邊/在比右邊
            top=left                            #所以比左邊的code寫在前面

        if right<n and nums[top]<nums[right]:
            top=right

        if top != i: 
            nums[i],nums[top] = nums[top],nums[i]  #top有可能會變化不只一次 所以交換的code分開寫        
            Solution().heap(nums,n,top) 
    
    def heap_sort(self,nums):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """    
    
        n=len(nums)
        for i in range(n,-1,-1):                      #每個位置都執行heap
            Solution().heap(nums, n, i)
        return nums    

    
        maxheap=Solution().maxheap(nums)
        for i in range(n-1,-1,-1):                    #比完一次就把 top(最大的)移到最後面
            nums[i],nums[0] = nums[0], nums[i] 
            Solution().heap(maxheap, i, 0)     
        return nums
   
#失敗了 失敗了
        #失敗了 失敗了
                #失敗了 失敗了
                        #失敗了 失敗了
                                #失敗了 失敗了
                                        #失敗了 失敗了
                                                #失敗了 失敗了
                                                        #失敗了 失敗了
                                                                #失敗了 失敗了
                                                                        #失敗了 失敗了
                                                                                #失敗了 失敗了
                                                                                        #失敗了 失敗了
                                                                                                #失敗了 失敗了
                                                                                                        #失敗了 失敗了
        
