// nums 에서 가장 자주 나타나는 요소 k개 추출하여 배열로 반환
// 1번째 시도
function topKFrequent(nums: number[], k: number): number[] {
  const answer = [];

  // 1. 각 요소의 등장 횟수를 카운트하여 맵으로 만든다.
  const countMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    const cur = nums[i];
    countMap.set(cur, (countMap.get(cur) || 0) + 1);
  }

  // 2. 카운트를 오름차순으로 정렬한다.
  const sorted = [...countMap].sort((a, b) => b[1] - a[1]);

  // 3. 정렬된 데이터에서 answer 의 길이가 k가 될 때까지 Map 을 순회하여 추출한다.
  for (const [val] of sorted) {
    if (answer.length < k) answer.push(val);
  }

  return answer;
}

/* 개선점?
 * Map 과 sort 이외의 방식이 없을까?
 * Map 의 장점은 get 할 때 O(1) 인건데, sort 를 하면서 시간복잡도가 증가함.
 */

// 2번째 시도
function topKFrequent(nums: number[], k: number): number[] {
  const answer = [];

  // 1. 카운트를 인덱스로 하는 기준 배열 생성
  const bucket = Array.from({length: nums.length + 1}, () => []);

  // 2. 각 요소의 등장 횟수를 카운트하여 맵으로 만든다.
  const countMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    const cur = nums[i];
    countMap.set(cur, (countMap.get(cur) || 0) + 1);
  }

  // 3. 등장 횟수를 기준 배열로 옮긴다
  for (const [num, count] of countMap) {
    bucket[count].push(num);
  }

  // 4. 버킷을 뒤에서 순회하면서 answer 배열에 push
  for (let i = bucket.length - 1; i >= 0; i--) {
    // 값이 비어있지 않다면, 해당 인덱스 순서만큼 카운팅된 숫자 밸류를 의미
    if (bucket[i].length > 0) {
      answer.push(...bucket[i]);

      if (answer.length === k) {
        return answer;
      }
    }
  }

  return answer;
}
