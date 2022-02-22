class Solution:
    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]
    def partition2(self, s: str) :
        
        # python 双指针
        def check(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        # 递归+回溯
        def dfs(start, path):

            if start == len(s):
                res.append(path.copy())
                return

            for i in range(start, len(s)):

                if not check(start, i):
                    continue

                path.append(s[start:i + 1])
                dfs(i + 1, path)
                path.pop(-1)# 弹出最后一个

        res = []
        dfs(0, [])
        return res

    def partition(self, s: str):

        def DFS(s, start, end, dp):
            if(start > end):
                l = []
                l.append(path_list)
                res_list.append(l)
                return
            # n叉树遍历
            for i in range(1, end-start+1):
                if not dp[start][start+i-1]:
                    continue
                path_list.append(s[start:start+i])
                DFS(s, start+i, end, dp)
                path_list.pop(-1)

        
        res_list = []
        path_list = []
        arr  = list(s)
        dp = [[False for col in range(len(s))] for row in range(len(s))]
        for i in range(0,len(s)):
            dp[i][i] = True
        for j in range(1,len(s)):
            for i in range(0,j):
                if (j-i)>=2:
                    dp[i][j] = arr[i]==arr[j] and dp[i+1][j-1]
                else:
                    dp[i][j] = arr[i] == arr[j]

        
        DFS(s, 0, len(s), dp)
        return res_list
        
print(Solution().partition("aab"))
