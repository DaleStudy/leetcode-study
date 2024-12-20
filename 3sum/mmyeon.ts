/**
 *
 * 접근 방법 :
 *  - 3개의 숫자를 더한 값이 0이 되는 숫자의 조합 찾는 문제
 *  - for문과 투 포인터 사용해서 숫자 조합 찾도록 접근
 *  - 투 포인터 이동 조건을 정하기 위해서 배열 오름차순으로 정렬
 *  - 합이 0보다 크면 오른쪽 포인터 1 감소하고, 0보다 작으면 왼쪽 포인터 1 증가
 *  - 합이 0인 경우에는, 결과값에 조합 저장하고, 포인터 2개 모두 이동시키기
 *  - 조합 중복 제거하기 위해서, 첫 번째 숫자와 두 세 번째 숫자 지정할 때 값 같은지 체크해서 같으면 다음 숫자로 넘어가도록 처리
 *
 * 시간복잡도 : O(n^2)
 *  - 배열 정렬 O(nlogn)
 *  - for문 순회하고 내부에서 while문으로 요소 모두 순회하니까 O(n^2)
 *
 * 공간복잡도 :
 *  - 포인터 변수, sum 변수만 사용해서 O(1)
 *
 * 배운 점 :
 * - Set을 활용해서 마지막에 중복 제거하려고 했는데 참조값이라서 원하는대로 동작 안했다. 결과값에 추가하고 중복 제거하는 것보다 추가하기 이전에 중복 제거하는 방식 고려해보기.
 */

function threeSum(nums: number[]): number[][] {
  const result: number[][] = [];
  // 투 포인터 사용하기 위해서 배열 정렬
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    // 중복 조합 제거하기 위해서 같은 값인 경우 넘어가도록 처리
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let leftPointer = i + 1,
      rightPointer = nums.length - 1;

    while (leftPointer < rightPointer) {
      const sum = nums[i] + nums[leftPointer] + nums[rightPointer];

      if (sum < 0) leftPointer++;
      else if (sum > 0) rightPointer--;
      else {
        result.push([nums[i], nums[leftPointer], nums[rightPointer]]);

        // 중복 조합 제거하기 위해서 같은 값인 경우 넘어가도록 처리
        while (
          leftPointer < rightPointer &&
          nums[leftPointer] === nums[leftPointer + 1]
        )
          leftPointer++;
        while (
          leftPointer < rightPointer &&
          nums[rightPointer] === nums[rightPointer - 1]
        )
          rightPointer--;
        leftPointer++;
        rightPointer--;
      }
    }
  }

  return result;
}
