class Solution(object):
    def productExceptSelf(self, nums):
        # 시간복잡도 = O(N)
        n = 1
        arr = []
        cnt = nums.count(0)
        for i in nums : # 0을 제외한 값들의 곱
            if i != 0 :
                n *= i
        for i in nums :
            if i == 0 and cnt == 1: # nums에 0이 한개인 경우 나머지의 곱
                arr.append(n)
            elif cnt >= 1 : # nums에 0이 여러개인 경우 무조건 0
                arr.append(0)
            else : # 그 외의 경우
                arr.append(n // i)
        return(arr)

