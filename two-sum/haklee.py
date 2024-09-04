"""TC: O(n), SC: O(n)

아이디어: 
만약 nums에 있는 어떤 숫자 i에 대해 target - i도 nums 안에 있다면, 이 두 숫자의 인덱스를 리턴하면 된다.
그런데 이렇게 하면 다음과 같은 예외 상황이 발생할 수 있다.

case 1) nums = [3, 3], target = 6
- nums에 3이 두 번 나오면 i도 3이고 target - i도 3인데, 그럼 같은 숫자에 대해서 어떻게 서로 다른 인덱스를
  가져오는가?
case 2) nums = [2, 3, 4], target = 6
- nums에 3이 하나밖에 없는데, i = 3일때 i도 nums 안에 있고, target - i = 3이라 이 값도 nums 안에 있다.
  서로 다른 두 아이템을 더해서 6이 되어야 하므로 [1, 1]같은 답을 리턴하면 오답이다.

위의 문제를 해결하기 위해 다음과 같은 방법을 사용했다.
- nums에 있는 unique한 숫자에 대해 각 숫자의 마지막 인덱스를 dict로 저장한다.
- 만약 nums에 속하는 어떤 수 i에 대해 i와 target - i의 값이 같을 경우, nums 안에 있는 i 중에 제일 앞에 있는
  i의 인덱스를 찾아서 앞서 만든 dict에 있는 인덱스와 비교해서 다른지 확인한다.

Q) 그런데 만약 i, target - i 값이 서로 다를때 둘 중 하나라도 nums 안에 두 번 이상 등장하면 어떡하지...?
A) 그럴 일은 없다. 솔루션은 유일하기 때문에, i나 target - i가 두 번 이상 나오면 솔루션이 둘 이상이 됨.


SC:
- ind_dict를 만들 때랑 nums_set 만들때 각각 O(n).
- 즉, O(n)

TC:
- ind_dict를 만들때 O(n).
- nums_set에 있는 값의 개수만큼 순회, O(n)
    - 내부에서 일어나는 일은 O(1)
- 종합하면 O(n).
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 먼저 nums의 각 아이템마다 인덱스를 찾는다.
        # 여기서 주의할 것은, nums에 같은 숫자가 두 번 이상 나오면 마지막 아이템의 인덱스가 들어감.
        ind_dict = {k: i for i, k in enumerate(nums)}  # SC: O(n), TC: O(n)

        # nums에 있는 unique한 값 i마다,
        for i in (nums_set := set(nums)):  # SC: O(n), TC: O(n)
            # 만약 target - i도 nums 안에 있다면,
            if target - i in nums_set:
                # 그리고 i와 target - i가 서로 다른 숫자라면,
                if i != target - i:
                    # 쉬운 케이스. 그냥 두 숫자의 인덱스를 찾아서 결과로 리턴한다.
                    return [ind_dict[i], ind_dict[target - i]]

                # 여기에 도달했다면 i와 target - i값이 같음.
                if (x := nums.index(i)) != ind_dict[target - i]:
                    # 첫, 마지막 등장 인덱스가 다를 경우, 이 두 숫자를 리턴.
                    return [x, ind_dict[target - i]]
