
class Solution:
    """
    1. 브루트포스와 같이 전부 길이를 대조해보고 하면 시간복잡도가 터질 것.
    투포인터 방식을 활용하면 됨. 투포인터에 대한 문제가 코딩테스트로 많이 나올 것 같음.
    확실하게 공부 필요.
    """
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        start, end = 0, len(height) - 1
        while start < end:
            area = (end - start) * min(height[start], height[end])
            max_area = max(area, max_area)

            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1

        return max_area
