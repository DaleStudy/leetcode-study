"""TC: O(n), SC: O(1)

n은 주어진 리스트의 길이.

아이디어:
- Rotated Sorted Array는 특성상 `값이 증가하다가 -> 갑자기 값이 한 번 감소 -> 이후 다시 쭉 증가`한다.
- 위의 관찰에 따르면 값이 감소하는 `절점`은 최대 한 군데 있을 수 있다.
    - rotate 시행을 0번 한 경우 절점이 없음. 그 외에는 절점이 한 번 생김.
- 즉, 리스트에서 두 구간을 겹치지 않게 잡으면 이 두 구간 중 적어도 한 구간은 ascending order가 보장된다.
- ascending하는 구간에 찾고자 하는 값이 있는지 판별하는 방식으로 binary search와 비슷한 방식으로 search 가능.
- 자세한 내용은 코드를 참조하면 된다.

SC:
- binary search와 비슷하게, 탐색 구간의 시작, 끝, 중간 인덱스를 관리. O(1).

TC:
- binary search와 비슷하게 구간이 계속 절반 크기로 줄어든다. O(log(n)).
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s, e = 0, len(nums) - 1
        while s < e:
            m = (s + e) // 2

            # 절점은 하나다. [s, m]과 [m+1, e]구간 중 한 곳에 절점존재.
            # 절점이 없는 구간은 ascending order가 보장되므로,
            # 이 구간에 target이 있는지 여부로 둘 중 한 구간을 탐색 구간에서 제외한다.
            if nums[s] < nums[m]:
                # [s, m] 구간이 ascending order.
                if (nums[s] > target and nums[m] > target) or (
                    nums[s] < target and nums[m] < target
                ):
                    # nums[s]와 nums[m]이 target보다 둘 다 크거나 둘 다 작으면
                    # [m + 1, e] 구간에서 탐색을 이어간다.
                    s = m + 1
                else:
                    # 아니면 [s, m] 구간에서 탐색을 이어간다.
                    e = m
            else:
                # [m + 1, e] 구간이 ascending order.
                if (nums[m + 1] > target and nums[e] > target) or (
                    nums[m + 1] < target and nums[e] < target
                ):
                    # nums[m + 1]과 nums[e]가 target보다 둘 다 크거나 둘 다 작으면
                    # [s, m] 구간에서 탐색을 이어간다.
                    e = m
                else:
                    # 아니면 [m + 1, e] 구간에서 탐색을 이어간다.
                    s = m + 1

        return s if nums[s] == target else -1
