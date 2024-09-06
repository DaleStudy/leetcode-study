/*
* 조건
* 연속된 수가 가장 긴 경우, 몇 번인지 구하기. 같은 값은 이어서 연결할 수 있음.
* 시간복잡도는 O(n)이어야함 = nums 배열을 한번만 돌아서 구할 것, 정렬 메소드는 쓸 수 없음(O(nlogn))
*
* 아이디어
* 시작지점과 끝나는 지점, 그 길이가 가장 긴 것을 구해야함
* 배열 값들을 한번만 체크할 수 있도록 배열을 돌면서 값을 set 자료구조에 저장해둔다
* 이때 set 사용하는 이유는, 
* 특정 값이 중복인 경우를 고려할 필요가 없기 때문
* 
* 다시 nums 배열을 돌면서 현재 값 직전값이나 이후값이 있는지, 앞뒤로 연속되는 수가 몇개가 있는지 체크한다
* 앞뒤로 연속되는 숫자의 개수로 새로운 배열을 만든다
* 새로 만들어진 배열 중 가장 큰 값을 리턴한다

* 이렇게 했을때 leetcode 시간초과가 뜬다.
* 중복계산 하는 부분을 줄여보자.
* 왼쪽에 있는 값은 왼쪽값에서 체크를 할거라 미리 계산해줄 필요가 없다, 현재 값부터 오른쪽 값만 계산한다.
* nums 배열을 돌면서 왼쪽값이 없는 경우만 오른쪽 값에 대해 길이를 계산한다
* 값에 대한 오른쪽 길이를 이미 계산한 적 있는 경우, memo된 값을 사용한다
* 
*/
function longestConsecutive(nums: number[]): number {
  // TC: O(n)
  // SC: O(n)
  const numSet: Set<number> = new Set(nums);

  // SC: O(n)
  const numLengthMemo: Map<number, number> = new Map();
  let maxLength = 0;

  // TC: O(n)
  for (let n of nums) {
    if (!numSet.has(n - 1)) {
      let length = 1;

      if (numLengthMemo.has(n)) {
        length = numLengthMemo.get(n);
        maxLength = Math.max(maxLength, length);
        continue;
      }

      // TC: O(n)
      while (numSet.has(n + length)) {
        length++;
      }

      numLengthMemo.set(n, length);
      maxLength = Math.max(maxLength, length);
    }
  }

  return maxLength;
}

function getNumCount(current: number, dict: Map<number, number>) {
  return dict.get(current) ?? 0;
}

// TC: O(n)
// SC: O(n)
