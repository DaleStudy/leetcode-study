# 시간 복잡도 O(n): 2로 반복해서 나눠야함
# 공간 복잡도 O(n): result 생성

class Solution:
    def devide_by_2 (self, n, temp):
        global val
        if n > 1 :
            val = n // 2
            remain = n % 2
            temp.append(remain)
            return self.devide_by_2(val, temp)
        temp.append(val)
        return val, temp

    def hammingWeight(self, n: int) -> int:
        result = []
        n, result = self.devide_by_2(n, result)
        return result.count(1)
        