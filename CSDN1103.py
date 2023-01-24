class Solution:
    def __init__(self) -> None:
        pass
    def solution(self, n, M, vector):
        result = None
        # TODO: 请在此编写代码
        dp=[[0]*(M+1) for i in range(n)]
        for i in range(n):
            for j in range(M,vector[i][0]-1,-1):
                dp[i][j]=max(dp[i][j],dp[j-vector[i][0]+vector[i][1]])
        result=dp
        return result



if __name__ == "__main__":
    arr_temp = [int(item) for item in input().strip().split()]
    n = int(arr_temp[0])
    M = int(arr_temp[1])
    vector = []
    for i in range(n):
        vector.append([int(item) for item in input().strip().split()])
    sol = Solution()
    result = sol.solution(n, M, vector)
    print(result)