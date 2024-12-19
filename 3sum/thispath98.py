class Solution:
    def threeSumSet(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition:
            두 값을 더하고, 세트 안에 값에서 0을 만족시키는 값이 있을 경우
            정답에 추가한다.
            세트(해시)의 접근이 O(1) 임을 이용한다.

        Time Complexity:
            O(N^2):
                2중 for문이 있으므로, O(N^2)이다.
                for문 내부에 시간복잡도에 영향을 줄만한 코드는 없으며
                정렬은 O(3 log 3)이므로 무시 가능하다.

        Space Complexity:
            O(N):
                중복된 값이 없다면 seen 세트는 N - 1개의 값을 저장한다.

        Key takeaway:
            해시를 이용한 풀이는 잘 못풀어서 조금 더 연습해야겠다.
            또한, 리스트를 해시하기 위해 tuple로 변환하는 것에 대해서 처음 알았다.
        """
        answer = set()
        for i in range(len(nums) - 2):
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = -(nums[i] + nums[j])
                if complement in seen:
                    answer.add(tuple(sorted([nums[i], nums[j], complement])))
                seen.add(nums[j])

        return list(answer)


class Solution:
    def threeSumTwoPointer(self, nums: List[int]) -> List[List[int]]:
        """
        Intuition:
            i를 for문으로 증가시키면서, 매 iteration마다 two pointer를 사용한다.

        Time Complexity:
            O(N^2):
                2중 for문이 있으므로, O(N^2)이다.
                for문 내부에 시간복잡도에 영향을 줄만한 코드는 없으며
                정렬은 O(3 log 3)이므로 무시 가능하다.

        Space Complexity:
            O(1):
                포인터 3개만을 사용하므로, 공간 복잡도는 O(1)이다.

        Key takeaway:
            투포인터를 응용한 문제임을 떠올리긴 했으나,
            nested two pointer임을 인지하지 못했다.
            이러한 경우에도 더 고민을 해봐야겠다.
        """
        nums.sort()

        answer = set()
        for i in range(len(nums) - 2):
            # 만약 i가 이전의 값과 중복된 값이라면 이 작업은 필요 없다.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    answer.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    j += 1

        return list(answer)
