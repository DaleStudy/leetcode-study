'''
시간 복잡도
- format(n, 'b'): 정수를 이진 문자열로 변환하는 작업은 O(k)입니다.
- Counter(bits): 문자열을 순회하면서 각 문자의 빈도를 계산하며, 이 작업도 문자열 길이 k에 비례합니다.
- count['1']: 딕셔너리 조회는 상수 시간이므로 O(1)입니다.

총 시간 복잡도: O(k) + O(k) + O(1) = O(k)

공간 복잡도
- format(n, 'b'): 생성된 이진 문자열은 길이 k를 차지합니다.
- Counter(bits): 딕셔너리 형태로 각 문자의 빈도를 저장합니다. 최악의 경우, 두 가지 문자(‘0’과 ‘1’)만 있으므로 공간 복잡도는 O(2) = O(1)로 간주할 수 있습니다.

총 공간 복잡도: O(k)
'''

from collections import Counter

class Solution:
    def hammingWeight(self, n: int) -> int:
        bits = format(n, 'b')
        count = Counter(bits)

        return count['1']
