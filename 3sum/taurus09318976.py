# 이 문제는 1)정렬을 통해 중복을 처리, 2)투 포인터를 사용하여 효율적으로 탐색, 
#3) 합이 0보다 작으면 left를 +1, 크면 right를 -1이동, 4)중복된

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  #중복된 숫자를 쉽게 처리하고, 투 포인터 기법을 사용하기 위해 배열을 정렬
        result = []
        
        #첫번째 숫자를 선택하는 루프
        #마지막 두 숫자는 left와 right가 사용하므로 len(nums)-2해야 함
        #예: len(nums) = 4라면, range(2)=[0,1]
        for i in range(len(nums) - 2):
            #첫번째 숫자가 이전과 같으면 건너뜀
            if i > 0 and nums[i] == nums[i-1]:
                continue

            #투 포인터 설정 : left는 첫번째 숫자 다음부터, right는 배열의 끝부터 설정  
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                #합이 0보다 작으면 left를 +1
                if total < 0:
                    left += 1
                #합이 0보다 크면 right를 -1이동    
                elif total > 0:
                    right -= 1               
                else:
                    #합이 0인 경우 처리
                    result.append([nums[i], nums[left], nums[right]])               
                    #중복된 숫자 건너뛰기
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    #다음 가능한 조합을 찾기 위해 포인터를 이동
                    left += 1
                    right -= 1
        
        return result


        #시간 복잡도: O(n²)
            #정렬: O(n log n)
            #메인 루프: O(n²)
        #공간 복잡도: O(1) (출력 배열 제외하고 추가적인 공간을 사용하지 않음)



