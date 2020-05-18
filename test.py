class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        res = []
        self.dfs(beginWord,endWord,wordList,[beginWord],res)
        if not res:
            return 0
        minlen = len(min(res,key=len))
        result = []
        print(res,minlen)
        for  x in res:
            if len(x) ==minlen:
                result.append(x)
        return result

    def isOnlyOneChange(self,a,b):
        n = len(a)
        j =0
        for i in range(n):
            if a[i]!=b[i]:
                j+=1
        return j==1
    
    def dfs(self,word,endWord,wordList,path,res):
        if res and len(path) > len(min(res)):
            return
        if word ==endWord:
            res.append(path)
        if not wordList:
            return
        
        for i,x in enumerate(wordList):
            if self.isOnlyOneChange(word,x):
                self.dfs(x,endWord,wordList[:i]+wordList[i+1:],path+[x],res)




if __name__ == "__main__":
    s = Solution()
    print(s.findLadders("a","c",["a","b","c"]))
 