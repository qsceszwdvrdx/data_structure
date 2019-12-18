
## bfs  Breadth-First Search(廣度優先搜尋)

    是一種圖形搜尋演算法。簡單的說，BFS是從根節點開始，沿著樹的寬度遍歷樹的節點。如果所有節點均被存取，則演算法中止。
    廣度優先搜尋的實現一般採用open-closed表。 
    
    時間複雜度：O(|V|+|E|)= O(b^d) b的d次方
    空間複雜度：O(|V|+|E|)= O(b^d) b的d次方
    
    BFS是一種盲目搜尋法，目的是系統地展開並檢查圖中的所有節點，以找尋結果。換句話說，它並不考慮結果的可能位址，徹底地搜尋整張圖，
    直到找到結果為止。BFS並不使用經驗法則演算法。
    
### bfs 核心想法
    從圖的某一節點(vertex, node)開始走訪，接著走訪此一節點所有相鄰且未拜訪過的節點，由走訪過的節點繼續進行先廣後深的搜尋。
    以樹(tree)來說即把同一深度(level)的節點走訪完，再繼續向下一個深度搜尋，直到找到目的節點或遍尋全部節點。
  
### dfs Depth-First-Search(深度優先搜尋)

    是一種用於遍歷或搜尋樹或圖的演算法。沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支。當節點v的所在邊都己被探尋過，
    搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止。如果還存在未被發現的節點
    
    時間複雜度：O(b^m) b的m次方
    空間複雜度：O(bm)
    
    則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止。屬於盲目搜尋。
    因發明「深度優先搜尋演算法」，約翰·霍普克洛夫特與羅伯特·塔揚在1986年共同獲得電腦領域的最高獎：圖靈獎。

### 資料參考
  
    https://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
    https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2
    http://simonsays-tw.com/web/DFS-BFS/BreadthFirstSearch.html
    
    https://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
    https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2
    
    
    
    
    
    
    
    
