class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        가장 길게 연속된 숫자들의 길이를 반환하는 함수
        ** 조건: O(n) 시간복잡도로 풀이해야 한다.
        
        방법
        0. set 자료구조를 사용해 중복 제거
        1. 정렬한 후 순회하면 연속된 숫자가 끊기는 지점을 찾아 max 길이를 업데이트 하는 방법.
            => O(nlogn) => 시간복잡도 조건을 만족하지 못한다.
        2. DP 방식으로 max(list) 만큼 리스트를 만들어, 각 숫자가 존재하는지 체크하면서 연속된 숫자들의 길이를 업데이트 하는 방법.
            => 음수 숫자가 존재할 수 있어, 해당 방법은 사용할 수 없다.
        3. 목록을 순회하면서, 각 숫자가 연속된 숫자의 시작점인지 확인한 후, 연속된 숫자들의 길이를 파악해, max 길이를 업데이트 하는 방법.
            => O(n)
        4. union-find 자료구조를 사용해, 각 숫자들을 연결한 후, 가장 긴 연결된 숫자들의 길이를 반환하는 방법.
            => O(n), 구현 x
    
        Args:
            nums (list[int]): 정렬되지 않은 중복 포함 정수 배열

        Returns:
            int: 가장 길게 연속된 숫자들의 길이
        """
        u_nums = set(nums)
        longest = 0
        for u_num in u_nums:
            if u_num - 1 not in u_nums:
                local = 1
                while u_num + local in u_nums:
                    local += 1
                longest = max(local, longest)
        return longest
