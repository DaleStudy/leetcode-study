'''
1차시도 : 시간 복잡도 O(n)으로 해결 실패..;;
Approach 
- nums 리스트가 비어있는 경우 0을 반환합니다.
- nums 리스트의 중복을 제거하고 정렬합니다.
- 정렬된 리스트를 순회하며 이전 숫자와 현재 숫자가 연속되는지 확인합니다.
- 연속된다면 count를 증가시키고, 연속되지 않는다면 max_count와 비교하여 갱신 후 count를 1로 초기화합니다.
- 최종적으로 max_count를 반환합니다.

Time Complexity: O(n log n)
- 중복 제거 및 정렬에 O(n log n) 발생

Space Complexity: O(n)
- 중복 제거된 리스트 저장 공간으로 인해 O(n) 발생
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 리스트에 값이 없는 경우는 0 반환
        if len(nums) == 0:
            return 0
        
        # 정렬 
        new_nums = list(set(nums))
        new_nums.sort()
        # 변수 생성 : 배열의 길이가 1이상인 경우 연속되는 숫자는 무조건 1개 포함된다고 가정
        count = 1
        max_count = 1

        for idx, val in enumerate(new_nums):
                # 첫 번째 인덱트(idx == 0)는 비교할 이전 값이 없으므로 그냥 건너뛰기
                if idx == 0:
                    continue
                if new_nums[idx-1] +1 == val:
                    count+=1
                    # 마지막 값인 경우
                    if idx == len(new_nums)-1:
                        if max_count <= count:
                            max_count = count
                else:
                    # 이전갑과 연속되지 않는 경우
                    if max_count <= count:
                        max_count = count
                        count = 1
                    else:
                        count = 1

        return max_count

'''
2차시도 : Set 자료구조 활용
Approach
- Set 자료구조로 중복 값을 제거하고, Set을 활용한 존재 여부 확인 시간은 O(1)이기 때문에 이를 활용했습니다.
- nums 리스트가 비어이는 경우 0을 반환합니다.
- Set으로 중복된 값을 제거합니다.
- Set을 순회하며 각 값에 대해 val-1이 Set에 없는 경우 새로운 연속 수열의 시작점으로 간주합니다.
- 시작점 이후로 While문을 사용해서 val+1, val+2,... 가 Set에 존재하는지 확인하며 count를 증가시킵니다.
- 최종적으로 max_count를 반환합니다.

Time Complexity: O(n)
- Array를 Set으로 변환: O(n)
- 각 원소에 대해:
  - 시작점이 아닌 경우: if (val - 1) not in num_set → O(1) 후 바로 넘어감
  - 시작점인 경우: while로 연속 구간을 끝까지 탐색: 각 숫자는 연속되는 숫자 내에서 최대 한 번씩만 방문되므로,
  전체 while 반복 횟수의 합은 O(n)을 넘지 않음.

Space Complexity: O(n)
- Set 자료구조에 중복 제거된 값들을 저장하는데 O(n) 발생
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 값이 없는 경우 0 반환
        if len(nums) == 0:
            return 0
        
        # set으로 중복된 값 제거 
        num_set = set(nums)
        max_count = 1 

        for val in num_set:
            # val-1 이 없다면, val은 새로운 연속 수열의 시작점
            if (val - 1) not in num_set:
                current = val   
                count = 1   

                # 시작점 이후 연속되는 숫자가 set안에 있는지 검증
                while (current + 1) in num_set:
                    current += 1
                    count += 1
                # while문 탈출 (=연속되는 숫자가 없는 경우) 최대 연속된 숫자 길이와 비교함        
                if count > max_count:
                    max_count = count 

        return max_count
