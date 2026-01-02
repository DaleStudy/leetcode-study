'''
Approach:
    주어진 배열에서 중복된 요소가 존재하는지 확인하는 문제입니다.
    해시 테이블 자료구조인 set을 이용해 nums의 모든 요소를 순회하며 중복을 제거한 객체를 생성했습니다.
    이후 set의 길이와 원본 배열의 길이를 비교하여, 길이가 다르다면 중복된 요소가 존재함을 의미합니다.

Time Complexity:
    O(n) 
    - set(nums)를 생성할 때 nums의 모든 원소를 한 번씩 순회하며 해시 테이블에 삽입하기 때문입니다.

Space Complexity:
    O(n)
    - 중복을 제거한 원소들이 새로운 집합(set)에 저장되므로, 
      최대 nums의 크기만큼 추가 공간이 필요합니다.
'''
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
