#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
# class Solution:
#     def exist(self, board, word):   
#         result = []
#         h = len(board)
#         l = len(board[0])
#         marked = [[True for _ in range(l)] for _ in range(h)]
  
#         for h in range(len(board)):
#             for l in range(len(board[0])):
#                 if board[h][l] ==word[0]:
#                       self.dfs(l,h,"",0,word,board,result,marked)
#         if result:
#             return word==result[0]
#         else: return False
#     def dfs(self, l,h,path,i,word,board,result,marked):
#         # print(path,h,l)
#         marked[h][l] =False
#         # print(path+board[h][l])
#         if path +board[h][l]==word:
#             result.append(path +board[h][l])
#             return True
#         else:
#             if board[h][l] == word[i]:
#                 i+=1
#                 if l>0 and marked[h][l-1] :
#                     self.dfs(l-1,h,path+board[h][l],i,word,board,result,marked)
#                 if h>0 and marked[h-1][l] :
#                     self.dfs(l,h-1,path+board[h][l],i,word,board,result,marked)
#                 if l<len(board[0])-1 and marked[h][l+1]:
#                     self.dfs(l+1,h,path+board[h][l],i,word,board,result,marked)
#                 if h<len(board)-1 and marked[h+1][l]:
#                     self.dfs(l,h+1,path+board[h][l],i,word,board,result,marked)
#             marked[h][l] =True
class Solution:
    #         (x-1,y)
    # (x,y-1) (x,y) (x,y+1)
    #         (x+1,y)

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 对每一个格子都从头开始搜索
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def __search_word(self, board, word, index,
                      start_x, start_y, marked, m, n):
        # 先写递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]

        # 中间匹配了，再继续搜索
        if board[start_x][start_y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m and 0 <= new_y < n and \
                        not marked[new_x][new_y] and \
                        self.__search_word(board, word,
                                           index + 1,
                                           new_x, new_y,
                                           marked, m, n):
                    return True
            marked[start_x][start_y] = False
        return False

# @lc code=end

