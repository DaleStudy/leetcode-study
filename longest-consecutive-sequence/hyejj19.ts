// nums 에서 순서에 상관없이 가장 길게 이을 수 있는 연속된 숫자의 카운트
// Constraints : Time complexity O(n)

// 1번째 시도
/*
1. O(n)이 되도록 정렬한다. 
-> 어차피 전체 시간복잡도가 O(n)이 될거기 때문에, 정렬 알고리즘은 그보다 빨라도 된다.
-> 근데 다시보니 nums 와 nums[i]의 길이가 -10^9 ~ 10^9 가 될 수 있기 때문에 정렬로 푸는게 맞지 않을 수도 있다.
2. 정렬된 배열을 순차적으로 돌면서 이어질 때 카운트를 한다.
3. 숫자가 달라질 때 카운트를 다시 초기화하고, 이전 값보다 높아질 때마다 max 를 갱신
4. 최종 max 값을 반환한다.
 */

// 2번째 시도
/*
 1. nums 배열을 set으로 만든다.
 2. set에서 값을 하나씩 순회한다. 
 3. 여기서 어떻게 해야하지..? (막혀서 ai 에게 도움을 요청함.)
 */

function longestConsecutive(nums: number[]): number {
  const numSet = new Set(nums);
  let max = 0;
  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let curNum = num;
      let curLen = 1;

      while (numSet.has(curNum + 1)) {
        curNum++;
        curLen++;
      }

      max = Math.max(max, curLen);
    }
  }

  return max;
}
