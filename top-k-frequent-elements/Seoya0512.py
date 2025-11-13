from typing import List

'''
[1차 시도]
Approach: nums 리스트의 각 원소의 빈도수를 hash_map에 저장후, 빈도수 기준으로 정렬을 하고 상위 k개를 반환
count 함수를 사용해서 간견할게 코드를 완성하고자 했습니다.

Time Complexity: O(n²)
- for num in nums 순환과 nums.count(num) 의 중첩으로 인해 O(n²) 발생

Space Complexity: O(n)
- hash_map 저장 공간과 sorted_hash_map 저장 공간으로 인해 O(n) 발생

- 
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = nums.count(num)

        # hash_map 정렬 
        sorted_hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        # 상위 k개 반환 
        return [x[0] for x in sorted_hash_map[:k]]

'''
[2차 시도]
Approach: 위의 방식에서 count 함수를 제거하고, hash_map에 빈도수를 직접 카운팅 하도록 수정하도록 해서
Time Complexity를 개선하기 위해 노력했습니다. 

Time Complexity: O(n log n)
- for num in nums 순환에 O(n) 발생
- hash_map 정렬에 O(m log m)으로 예측 되며 최대 m =< n 이므로 O(n log n) 발생

'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            if hash_map.get(num): 
                hash_map.update({num: hash_map[num]+1})
            else:
                hash_map.update({num: 1})

        # hash_map 정렬 
        sorted_hash_map = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        # 상위 k개 반환 
        return [x[0] for x in sorted_hash_map[:k]]
    

'''
[3차 시도 - Bucket Sort  활용]
Approach: Bucket Sort 방식을 활용할 수 있다는 것을 알게 됐습니다.
for loop와 조건문이 반복되기도 하지만, 배열의 크기에 맞춰 한번씩만 순회하기 때문에 
Time Complexity를 O(n)으로 개선할 수 있었습니다.

Time Complexity: O(n)
- for num in nums 순환하며 빈도수 카운팅: O(n)
- 빈도에 따라 숫자들을 버킷에 넣기: O(n)
- 버킷을 뒤에서부터 순회하며 상위 k개 숫자 채우기: O(n) 

Space Complexity: O(n)
- freq 딕셔너리와 bucket 리스트로 인해 O(n) 발생  
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        # 인덱스 = 등장 횟수, 값 = 그 횟수만큼 등장한 숫자 리스트
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, count in hash_map.items():
            bucket[count].append(num)

        result: List[int] = []
        # 가장 큰 빈도부터 내려오면서 숫자 수집 (for 루프 역순)
        for count in range(len(bucket) - 1, -1, -1):
            if not bucket[count]:
                continue

            for num in bucket[count]:
                result.append(num)
                if len(result) == k:
                    return result
    
        return result
