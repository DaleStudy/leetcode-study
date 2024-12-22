/**
 *
 * 접근 방법 : dp 사용
 *  - 배열 길이가 1개 일때는 첫 번쨰 값 리턴하고, 2개면 더 큰 수를 리턴한다.
 *  - 3개 부터는 바로 옆집 값에 현재집 값을 더한 값과 옆옆집의 값을 비교해서 큰 값을 계산한다.
 *  - 다음 집 값에 현재까지의 값 활용하기 위해서, 바로 옆집, 옆옆집 값을 업데이트해준다.
 *  - 현재 값이 저장된 옆집값을 리턴한다.
 *
 * 시간복잡도 :
 *  - 주어진 숫자 배열 길이만큼 1회 순회하니까 O(n)
 *
 * 공간복잡도 :
 *  - 옆집과 옆옆집 값을 2개의 변수에 저장해야하니까 O(1)
 *
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function (nums) {
  if (nums.length === 1) return nums[0];
  if (nums.length === 2) return Math.max(nums[0], nums[1]);

  let prevPrevHouse = nums[0];
  let prevHouse = Math.max(nums[0], nums[1]);

  for (let i = 2; i < nums.length; i++) {
    const current = Math.max(prevHouse, prevPrevHouse + nums[i]);
    prevPrevHouse = prevHouse;
    prevHouse = current;
  }

  return prevHouse;
};
