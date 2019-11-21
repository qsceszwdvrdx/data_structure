class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution(object):
    def insert(self, root, val):
#         """
#         :type root: TreeNode
#         :type val: int
#         :rtype: TreeNode(inserted node)
#         """
        newnode = TreeNode(val)      #連接到TreeNode

        if root is None:
            return newnode

        else:
            if root.val > val:
                if root.right is None:
                    root.right= newnode
                    return root.right

                else:
    #                 insert(root.right,val)
    #             return root.right
                    return self.insert(root.left,val)


            else:
                if root.left is None:
                    root.left= newnode
                    return root.left
                else:
    #                 insert(root.left,val)
    #             return root.left
                    return self.insert(root.left,val)
    
    def minValueNode(root):  #算出最小
        current = root

        while(current.left is not None): 
            current = current.left  

        return current 


    def delete(self, root, target):
    
        if root is None: 
            return root  

        if target < root.val:                 #不是root的時候 移動root
            root.left = delete(root.left,target) 

        if target > root.val: 
            root.right = delete(root.right,target) 

        else:               
                                        #root = target
            if root.left is None : 
                temp = root.right  
                root = None 
                return temp  

            elif root.right is None : 
                temp = root.left  
                root = None
                return temp 

            temp = minValueNode(root.right) 

            root.val = temp.val 

            root.right = delete(root.right , temp.val) 


        return root  
    
    def search(self,root,target): 
        if root:              
                                            # 3種不同的狀況
            if  root.val == target: 
                return root 

            if root.val < target: 
                if root.left:

                    if root.left.val == target:
                        return root.left
                                            # 移動root
                    else:
                        return self(root.left,target)

                else:
                    return None


            if root.val > target:
                if root.right:

                    if root.right.val == target:
                        return root.right
                                            # 移動root
                    else:
                        return self(root.right,target)

                else:
                    return None

        else:
            return None

    def modify(self, root, target, new_val):
        if target == new_val:
            return root
        else:
            Solution().delete(root,target)
            return Solution().insert(root,new_val)
        
        
        
#參考資料

  #insert寫法：
  #https://www.runoob.com/python/att-list-insert.html

  #BST寫法：
  #https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
  #https://buptldy.github.io/2016/05/09/2016-05-09-Python%20BST/
  #https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9  
  #https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/
