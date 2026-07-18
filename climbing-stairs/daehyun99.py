class Solution:
    def climbStairs(self, n: int) -> int:
        one_count = n
        two_count = 0
        total_count = 0

        while one_count >=0 and two_count >=0:
            # 조합
            total = one_count + two_count

            count = 1
            for i in range(two_count):
                count *= total - i
            for i in range(two_count, 0, -1):
                count /= i
            total_count += count

            one_count -=2
            two_count +=1
        return int(total_count)
