##### heap_sort_ID.py

class Solution(object):
        """
        :type nums: List[int] ex:[3,2,-4,6,4,2,19],[5,1,1,2,0,0]
        :rtype: List[int] ex:[-4,2,2,3,4,6,19],[0,0,1,1,2,5]
        """
  def heap(alist,n,i):
     
        top=i       #序數的大小關係
        left=2*i+1
        right=2*i+2
    
    if left<n and alist[top]<alist[left]:   #比大小 先比左邊/在比右邊
        top=left                            #所以比左邊的code寫在前面

    if right<n and alist[top]<alist[right]:
        top=right

    if top != i: 
        alist[i],alist[top] = alist[top],alist[i]  #top有可能會變化不只一次 所以交換的code分開寫        
        heap(alist,n,top)                          #確定每個條件都有執行過
        
        
  def heap_sort(alist):
            n=len(alist)
            for i in range(n,-1,-1):                      #每個位置都執行heap
        heap(alist, n, i)
        
            for i in range(n-1,-1,-1):                    #比完一次就把 top(最大的)移到最後面
            alist[i],alist[0] = alist[0], alist[i] 
            heap(alist, i, 0)
