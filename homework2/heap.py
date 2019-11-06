{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    基本上都是參考老師的寫法：https://github.com/pecu/DSA/blob/master/06_HeapSort/heapSort.py\n",
    "    但是也沒完全看懂 所以細節觀念參考:http://alrightchiu.github.io/SecondRound/comparison-sort-heap-sortdui-ji-pai-xu-fa.html\n",
    "    range寫法:https://www.runoob.com/python/python-func-range.html"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    我有自己寫過很多次 還錯蠻多次的 雖然沒辦法從0創造code 但是每發現錯一次 感覺細節觀念就有慢慢被導正\n",
    "    錯的太亂了所以我把最後 正確的放在前面"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "正確的code"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heap(alist,n,i):\n",
    "     \n",
    "    top=i       #序數的大小關係\n",
    "    left=2*i+1\n",
    "    right=2*i+2\n",
    "    \n",
    "    if left<n and alist[top]<alist[left]:   #比大小 先比左邊/在比右邊\n",
    "        top=left                            #所以比左邊的code寫在前面\n",
    "\n",
    "    if right<n and alist[top]<alist[right]:\n",
    "        top=right\n",
    "\n",
    "    if top != i: \n",
    "        alist[i],alist[top] = alist[top],alist[i]  #top有可能會變化不只一次 所以交換的code分開寫        \n",
    "        heap(alist,n,top)                          #確定每個條件都有執行過\n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heapsort(alist):\n",
    "    n=len(alist)\n",
    "    for i in range(n,-1,-1):                      #每個位置都執行heap\n",
    "        heap(alist, n, i)\n",
    "        \n",
    "    for i in range(n-1,-1,-1):                    #比完一次就把 top(最大的)移到最後面\n",
    "        alist[i],alist[0] = alist[0], alist[i] \n",
    "        heap(alist, i, 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "     range(起點,終點正負1,多少為一個單位)     \n",
    "     終點要多設一個位置 range 語法中終點不包括自己 而是自已以內"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "A=[9,3,8,1,2,0,4,5,6,3,5,7,8,9,0]\n",
    "heapsort(A)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[0, 0, 1, 2, 3, 3, 4, 5, 5, 6, 7, 8, 8, 9, 9]"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Ａ"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "錯誤的code "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "第1個"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heap(alist,n,i):\n",
    "    n=len(alist)         #錯在這行\n",
    "        \n",
    "    top=i       \n",
    "    left=2*i+1\n",
    "    right=2*i+2\n",
    "    \n",
    "    if left<n and alist[top]<alist[left]:   \n",
    "        top=left                            \n",
    "\n",
    "    if right<n and alist[top]<alist[right]:\n",
    "        top=right\n",
    "\n",
    "    if top != i: \n",
    "        alist[i],alist[top] = alist[top],alist[i]        \n",
    "        heap(alist,n,top)                   "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    這樣會卡死 n 後面再使用 heap(alist,n,i)時 n會動不了"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "第2個"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heap(alist,n,i):\n",
    "    top=i       \n",
    "    left=2*i+1\n",
    "    right=2*i+2\n",
    "    \n",
    "    if left<n and alist[i]<alist[left]:           #沒錯 但把 i改成 top比較好 \n",
    "        top=left                            \n",
    "\n",
    "    if right<n and alist[i]<alist[right]:         #錯在這行 i一定要改成 top \n",
    "        top=right\n",
    "\n",
    "    if top != i: \n",
    "        alist[i],alist[top] = alist[top],alist[i]        \n",
    "        heap(alist,n,top)                   "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    如果左邊有先換過的情況下 用i的話會換錯 應該要跟現在的 top換 而不是原本的 top  "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "第3個"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heap(alist,n,i):\n",
    "    top=i       \n",
    "    left=2*i+1\n",
    "    right=2*i+2\n",
    "    \n",
    "    if left<n and alist[top]<alist[left]:            \n",
    "        top=left                            \n",
    "\n",
    "    if right<n and alist[top]<alist[right]:       \n",
    "        top=right\n",
    "\n",
    "    if top != i: \n",
    "        alist[i],alist[top] = alist[top],alist[i]        \n",
    "                                                        #少了heap(alist,n,top)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    少了確認全部是否都有測試過3個if"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "第4個"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heap(alist,n,i):\n",
    "     \n",
    "    top=i       \n",
    "    left=2*i+1\n",
    "    right=2*i+2\n",
    "    \n",
    "    if left<n and alist[top]<alist[left]:   \n",
    "        top=left                            \n",
    "        alist[i],alist[top] = alist[top],alist[i]     #錯在這行\n",
    "        \n",
    "    if right<n and alist[top]<alist[right]:\n",
    "        top=right\n",
    "        alist[i],alist[top] = alist[top],alist[i]     #錯在這行\n",
    "              \n",
    "        heap(alist,n,top)                          \n",
    "        "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    這樣看來起來比較精簡 但卻忽略了一個問題 如果if不符合 即使交換的code都寫對 也部會執行"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "第5個"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "def heapsort(alist):\n",
    "    n=len(alist)\n",
    "    for i in range(0,n+1,1):                      \n",
    "        heap(alist, n, i)\n",
    "        \n",
    "    for i in range(0,n,1):                    \n",
    "        alist[i],alist[0] = alist[0], alist[i] \n",
    "        heap(alist, i, 0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "    如果要改變順序 不只heapsort要改 前面的heap也要改"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
