class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        주어진 숫자의 이진 표현에서, 1의 개수를 계산하는 함수
        예) 11 -> 1011 => 3

        방법:
        1. 숫자를 이진법으로 바꿔서 1을 찾아 계산하기
            - 이진법으로 바꾸는 과정에서 전체 순회를 하고, 1을 찾을때 또 순회해야햠.
            -> 한번에 해결할 수 없을까?
        2. 숫자를 직접 비트연산하며 계산하기
            - 숫자를 bitshift하면서 마지막 비트가 1인지 아닌지 찾기
            - 1이면 count + 1
            -> 시간 복잡도 O(k) (k는 비트길이), 공간복잡도 O(1)

        Args:
            n(int): 양수

        Returns:
            int: 이진 표현에서 1의 개수 
        """
        curr = n
        count = 0
        while curr > 0:
            if curr & 1 == 1:
                count += 1
            curr = curr >> 1
        return count
