"""TC: O(n), SC: O(1)

아이디어: 
다음의 세 상황 중 하나가 될 것이다.
- 0이 둘 이상 포함. 모든 결과값이 0이 된다.
- 0이 하나 포함.
    - 0에 해당하는 인덱스에는 nums에 있는 숫자들 중 0 말고 나머지 숫자들을 전부 곱한 값.
    - 그 외 모두 0.
- 0이 하나도 없다.
    - nums에 있는 모든 숫자들을 곱한 값을 p라고 할때, 각 인덱스 i마다 p를 nums[i]로 나눈 값.

그러므로, 먼저 nums에 있는 숫자들을 돌면서
- 0이 아닌 숫자를 전부 곱한 값 p를 만든다.
- 0이 들어있는 인덱스를 찾는다.
- 0이 들어있는 인덱스가 둘 이상인지 체크한다.

그 다음
- 0이 들어있는 인덱스가 둘 이상인지, 0이 들어있는 인덱스가 있는지 보고 상황에 맞게 결과값을 리턴.

SC:
- 0이 아닌 숫자들을 곱한 값 p를 관리할때 O(1)
- 0이 등장하는 인덱스 zero_ind와 둘 이상 있는지 여부 all_zero 플래그를 관리할때 O(1).
- 결과로 리턴할 값 O(n) <- 이건 공간 복잡도 분석에서 제외한다.
- 종합하면 O(1).

TC:
- nums값을 한 번 순회하면서 p, zero_ind, all_zero값을 업데이트 할때 O(n)
- 결과로 리턴할 값 만들때 O(n)
- 종합하면 O(n).
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_zero = True
        zero_ind = None
        p = 1
        for i, e in enumerate(nums):
            if e == 0:
                if zero_ind is not None:
                    break
                zero_ind = i
            else:
                p *= e
        else:
            all_zero = False
        sol = [0] * len(nums)
        if all_zero:
            return sol
        elif zero_ind is not None:
            sol[zero_ind] = p
            return sol
        else:
            return [p // i for i in nums]


""" TC: O(n), SC: O(1)
하지만 윗 솔루션은 문제에서 사용하지 말라고 한 `/`(정확히는 `//`)를 썼다는 문제가 있다.
나누기를 하지 말라고 했으니 이를 어떻게 잘 우회해보자.

※ 주의: 정밀한 계산에 취약한 접근 방법이므로 구현한 것이 잘 작동할 것이라는 사실에
        정말 자신 있는 경우가 아니면 이렇게 구현하면 안된다.

아이디어:
다음의 등식을 보자.

x / y = 2^(log2(x)) / 2^(log2(y)) = 2^(log2(x)-log2(y))

즉, 우리는 나누기 연산을 power, log, - 연산으로 우회 가능하다.

위의 우회 방법을 활용하기 위해 기존의 접근 방식을 다음과 같이 수정한다.
- 원래는 p를 1로 초기화한 다음 nums에 있는 값들 중 0이 아닌 것들을 전부 곱해줬다.
- 이제 p에는 2^p을 계산했을때 곱셈의 결과값이 나오는 값을 저장할 것이다. 그러므로,
  p를 0으로 초기화하고 p에는 nums에 있는 값들 중 0이 아닌 값에 log를 취한 값을 더해준다.

하지만 0이하의 실수 x에 대해서는 log(x)가 정의되지 않는 문제가 있다.
그러므로 다음과 같은 조치를 취해야 한다.
- nums에 있는 값 x가 0이면 그냥 넘어간다. 이는 기존의 접근 방법과 동일하다.
- nums에 있는 값 x가 0보다 작으면 절대값을 취하고 로그를 씌운다.
  즉, log(|x|)를 계산한다.
- 이 경우 결과에도 -1도 곱해줘야 한다는 사실을 알아야 하므로 이 정보를
  `is_neg`라는 변수로 관리하자.

주의점:
설명에 등장하는 기호와 아래의 코드에 등장하는 기호를 헷갈리면 안된다.
- 위에서는 power를 `^`기호로 썼지만 python에서는 `**`기호를 쓴다.
- 그리고 python에서 `^`기호는 xor을 의미한다.

문제점:
- 위의 접근 방법은 이론적으로는 문제될 것이 없지만 안타깝게도 컴퓨터를 통한 연산에서는
  log를 계산한 값의 소수점 뒷 자리수들이 잘려나간다.
- 이로 인해 2^p를 계산한 결과값이 깔끔한 정수가 아니라 더러운 소수가 나온다. 그래서 
  이 숫자가 정답에 근접한 값일 것이라고 굳게 믿고 여기에 `round` 함수를 써서 반올림을
  해야 원하는 답이 나온다.
- 그런데 생각해보면 nums에 들어있는 값들에 로그를 취하고 더하는 과정에서 이 잘린 소수점
  값들이 점점 누적되면서 오차가 점점 커질 것이다. 오차가 충분히 커지면 2^p를 계산한 값을
  반올림 하더라도 우리가 원하는 정확한 답이 나오지 않게 될 것이다.
	- e.g.) nums = range(2, 18) 일때
		- expected answer: [177843714048000, 118562476032000, 88921857024000, 71137485619200, ...]
		- result: [177843714047999, 118562476031999, 88921857023999, 71137485619200, ...]
		- diff: [-1, -1, -1, 0, ...]
- 곱하는 수에 큰 수가 섞여도 문제가 쉽게 발생한다.
	- e.g.) nums = [2, 10, 44444444444444] 일때
		- expected answer: [444444444444440, 88888888888888, 20]
		- result: [444444444444441, 88888888888888, 20]
		- diff: [1, 0, 0]
- 그렇다면 얼마나 많은 숫자를 곱하거나 큰 숫자를 곱하는 상황에서 문제가 발생하는가?
  문제에 주어진 조건 범위 내에서 위의 방법이 잘 작동할 것이라는 사실이 보장되는가?
  이에 대해 생각하는 것은 매우 귀찮은 일이다...

그런데
- 대충 관찰을 해보니 숫자들의 곱이 문제에서 주어진 조건인 `The product ... fit in a 32-bit integer.`
  보다 훨씬 큰 경우에만 위의 오차가 치명적인 영향을 준다.
- 그래서 일단 리트코드에 풀이를 던져보았더니 accept 되었다. 나는 leetcode피셜 잘 풀었다고
  볼 수 있는 것이다.
- 만약 이 풀이가 잘못되었다고 말하고 싶다면 나 말고 문제 조건을 설계한 사람과 테케를 만든
  사람들에게 돌을 던져라 ¯\_(ツ)_/¯
"""

import math


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        all_zero = True
        zero_ind = None
        p, is_neg = 0, False
        for i, e in enumerate(nums):
            if e == 0:
                if zero_ind is not None:
                    break
                zero_ind = i
            else:
                is_neg ^= e < 0
                p += math.log2(abs(e))
        else:
            all_zero = False

        sol = [0] * len(nums)
        if all_zero:
            return sol
        elif zero_ind is not None:
            sol[zero_ind] = round(2**p * (-1) ** (is_neg))
            return sol
        else:
            return [
                round(2 ** (p - math.log2(abs(i))) * (-1) ** (is_neg ^ (i < 0)))
                for i in nums
            ]
