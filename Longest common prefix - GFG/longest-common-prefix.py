#User function Template for python3

class Solution:
    def longestCommonPrefix(self, str1, str2):
        # code here
        longest=[-1,-1]
        for i in range(len(str1)):
            if str1[0:i+1] in str2:
                #it checks characters in str1 are present in str2
                #one by one index and increase the index
                longest=[0,i]
            else:
                break
        return longest
        
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        str1 = input()
        str2 = input()
        ob = Solution()
        ans = ob.longestCommonPrefix(str1, str2)
        if ans[0] == -1:
            print(-1)
        else:
            print(ans[0], ans[1])

# } Driver Code Ends