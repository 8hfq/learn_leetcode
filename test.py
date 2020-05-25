class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        list1 = version1.split('.')
        list2 = version2.split('.')
        print(list1, list2)
        minlen = min(len(list1), len(list2))
        for i in range(minlen):
            if int(list1[i]) < int(list2[i]):
                return -1
            elif int(list1[i]) > int(list2[i]):
                return 1
            else: continue



if __name__ == "__main__":
    s = Solution()
    print(s.compareVersion("1","0"))