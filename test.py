class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        res = []
        self.dfs(beginWord,endWord,wordList,1,res)
        return min(res)
    def isOnlyOneChange(self,a,b):
        n = len(a)
        j =0
        for i in range(n):
            if a[i]!=b[i]:
                j+=1
        return j==1
    def dfs(self,word,endWord,list,index,res):
        if res and index>= min(res):
            return
        if word ==endWord:
            res.append(index)
            return
        if not list:
            return
        for i,x in enumerate(list):
            if self.isOnlyOneChange(word,x):
                self.dfs(x,endWord,list[:i]+list[i+1:],index+1,res)
        
if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("qa","sq",["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
 