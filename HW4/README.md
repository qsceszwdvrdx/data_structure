
## Hash Table

    若直接把Key當作Array的index，並將Value存放進Array，這樣的實作稱為Direct Access Table
    若關鍵字為k，則其值存放在f(k)的存儲位置上 由此，不需比較便可直接取得所查記錄。
    對不同的關鍵字可能得到同一雜湊地址 即 k1!= k2，而 f(k1)=f(k2) 
    
    1.add:增加新的data
    2.delete:刪除data
    3.search:尋找data

### 期望目標

    如果能在時間複雜度為常數的O(1)完成完成查詢的Hash Table那該有多好

### 資料參考

    http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html
    https://zh.wikipedia.org/wiki/%E5%93%88%E5%B8%8C%E8%A1%A8
    
