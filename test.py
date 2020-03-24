class Solution:
    def exist(self, board, word):   
        result = []
        h = len(board)
        l = len(board[0])
        marked = [[True for _ in range(l)] for _ in range(h)]
  
        for h in range(len(board)):
            for l in range(len(board[0])):
                if board[h][l] ==word[0]:
                      self.dfs(l,h,"",0,word,board,result,marked)
        if result:
            return word==result[0]
        else: return False
    def dfs(self, l,h,path,i,word,board,result,marked):
        # print(path,h,l)
        marked[h][l] =False

        print(path+board[h][l])
        if path +board[h][l]==word:
          
            result.append(path +board[h][l])
            return
        if board[h][l] == word[i]:
            i+=1
            if l>0 and marked[h][l-1] :
                self.dfs(l-1,h,path+board[h][l],i,word,board,result,marked)
            if h>0 and marked[h-1][l] :
                self.dfs(l,h-1,path+board[h][l],i,word,board,result,marked)
            if l<len(board[0])-1 and marked[h][l+1]:
                self.dfs(l+1,h,path+board[h][l],i,word,board,result,marked)
            if h<len(board)-1 and marked[h+1][l]:
                self.dfs(l,h+1,path+board[h][l],i,word,board,result,marked)
        marked[h][l] =True
if __name__ == "__main__":
    s = Solution()
    print(s.exist([["a"]],"a"))
    print(s.exist([["a","b"],["c","d"]],"acdb"))