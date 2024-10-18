"""TC: O(n), SC: O(1)

n은 주어진 리스트의 길이

아이디어:
- 끝에 있는 아이템부터 시작해서 '최소 어디까지는 도달해야 끝 칸까지 점프 가능한지'를 업데이트 한다.
- example들로 이해해보자. index는 0부터 시작.
    - example 1: [2,3,1,1,4]
        - 4번째 칸에 도달할 수 있으면 성공이다. reach_at_least 값을 4로 초기화 한다.
        - 3번째 칸에서는 최대 4번째 칸까지 갈 수 있다. 즉, 적어도 3번 칸까지 가면 성공이므로
        reach_at_least를 3으로 업데이트 한다.
        - 2번째 칸에서는 최대 3번째 칸까지 갈 수 있다. reach_at_least를 2로 업데이트 한다.
        - 1번째 칸에서는 최대 1+3=4번째 칸까지 갈 수 있다. 이 칸에서 현 reach_at_least 값인 2번째 칸까지
        충분히 갈 수 있으므로 reach_at_least 값을 1로 업데이트 한다.
        - 0번째 칸에서는 최대 0+2=2번째 칸까지 갈 수 있다. 현 reach_at_least 값인 1번째 칸까지 충분히
        갈 수 있으므로 reach_at_least 값을 0으로 업데이트 한다.
        - 0번째 칸에서 끝 칸까지 갈 수 있다.
    - example 2: [3,2,1,0,4]
        - 4번째 칸에 도달할 수 있으면 성공이다. reach_at_least 값을 4로 초기화 한다.
        - 3번째 칸에서는 최대 3번째 칸까지 갈 수 있다. 여기서는 현 reach_at_least 값인 4까지 갈 수 없으니
          아무 일도 일어나지 않는다.
        - 2번째 칸에서는 최대 2+1=3번째 칸까지 갈 수 있다. 여기서도 현 reach_at_least 값인 4까지 갈 수 없고,
          아무 일도 일어나지 않는다.
        - 1번째 칸에서는 최대 1+2=3번째 칸까지 갈 수 있다. 비슷하게 아무 일도 일어나지 않는다.
        - 0번째 칸에서는 최대 0+3=3번째 칸까지 갈 수 있다. 비슷하게 아무 일도 일어나지 않는다.
        - reach_at_least 값이 0이 아니다. 즉, 0번째 칸에서는 끝 칸까지 갈 수 없다.

SC:
- reach_at_least 값에 인덱스 하나만 관리한다. 즉, O(1).

TC:
- nums의 끝에서 두 번째 아이템부터 첫 번째 아이템까지 순차적으로 접근하면서 reach_at_least값을 업데이트 한다. O(n).
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach_at_least = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= reach_at_least:
                reach_at_least = i

        return reach_at_least == 0
