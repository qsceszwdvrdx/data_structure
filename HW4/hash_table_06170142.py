from Crypto.Hash import MD5
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyHashSet:
    def __init__(self, capacity):             #如果capacity=n 0.1.2.3...n-1
        self.capacity = capacity
        self.data = [None] * self.capacity

    def add(self, key):
        h=MD5.new()
        h.update(key.encode("utf-8"))           #使用 MD5用 utf-8編碼 再轉成10進位>>>area
        area = int(h.hexdigest(),16)            
        idx =  area % self.capacity             #用餘數分類 分成不同的 node
        node = self.data[idx]
        
        while node:
            if node.val == area:                 
                return         
            node = node.next                    #不管if成不成立 都移動 node>>>node.next
            
        new_node = ListNode(area)               #把值放進去           
        new_node.next = self.data[idx] 
        self.data[idx] = new_node
        
    def remove(self, key):
        
        h=MD5.new()
        h.update(key.encode("utf-8"))
        area = int(h.hexdigest(),16)
        idx =  area % self.capacity
        node = self.data[idx]
        
        if node and node.val == area:       
            self.data[idx] = node.next
            return
        pre = None                               #leetcode概念
        while node:
            if node.val == area:                 #移動 node.next>>>node 
                pre.next = node.next
                return                           #用pre連接
            pre = node
            node = node.next

    def contains(self, key):
        
        h=MD5.new()
        h.update(key.encode("utf-8"))
        area = int(h.hexdigest(),16)
        idx =  area % self.capacity
        node = self.data[idx]
        
        while node:
            if node.val == area:            
                return True
            node = node.next                      #通通測過一輪
        return False

#參考:https://www.youtube.com/watch?v=oqzStHk36PI&feature=youtu.be
