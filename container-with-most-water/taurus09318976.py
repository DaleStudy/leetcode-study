'''
이 문제는 주어진 높이 배열에서 두 개의 수직선을 선택해 최대 물의 양을 구하는 문제임 

조건 : 1) 두 선 사이의 거리(너비) * 두 선 중 낮은 높이 = 물의 양
      2) 물은 기울일 수 없으므로 높이는 낮은 선 기준임

해결 방법 : 
    two pointers 접근법을 사용해서 
    왼쪽과 오른쪽 포인터를 배열의 시작과 끝에 배치함
    더 낮은 높이를 가진 포인터를 안쪽으로 이동시키며 최대 물의 양을 계산함

'''

class Solution:
    def maxArea(self, height: List[int]):
        # two pointers 초기화
        left = 0
        right = len(height) - 1
        # 최대 물의 양을 저장할 변수
        max_water = 0
        
        # 포인터가 교차하기 전까지 반복
        while left < right:
            # 두 선 사이의 거리 계산
            width = right - left
            # 두 선 중 낮은 높이 계산
            current_height = min(height[left], height[right])
            # 현재 물의 양 계산
            current_water = width * current_height
            
            # 최대 물의 양 계산
            if current_water > max_water:
                max_water = current_water
            
            # 더 낮은 높이의 포인터 이동
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_water
