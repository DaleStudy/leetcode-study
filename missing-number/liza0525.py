# 7기 풀이
# 시간 복잡도: O(n)
# - nums의 전체 합을 계산할 때 nums의 길이 만큼 시간 소요 
# 공간 복잡도: O(1)
# - 계산에 필요한 변수 몇 개만 사용
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums에서 빠진 값까지 함께 더했을 때의 값
        # 최소값(0) + 최대값(len(nums))을 2로 나눈 후, nums의 개수 + 1(0 포함)의 개수만큼 곱한 값
        # 등차수열의 전체 합
        all_sum_nums = int(len(nums) / 2 * (len(nums) + 1))
        
        # nums 리스트의 전체 합
        sum_nums = sum(nums)

        # 두 값의 차이가 곧 누락된 값
        return all_sum_nums - sum_nums
