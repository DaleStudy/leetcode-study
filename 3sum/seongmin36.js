/**
중요한 것은 짝을 찾는 것이다.
즉, 정수가 0이 되는 '역원(inverse)'을 찾아야 한다.
역원을 담을 저장소가 필요한데,
찾아야할 역원은 여러개일 필요가 없기 때문에 주머니 역할로 Set 인스턴스를 사용한다.
중복 조건은 정렬된 배열에서 현재 인덱스보다 큰 원소 중에서 동일한 값을 제외한다.
 */
/**
 * @param {number[]} nums
 * @return {number[][]}
 */

function threeSum(nums) {
  let result = [];

  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) break;

    // 중복 제거 → i>0 이웃한 두 수가 일치하면 skip
    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let pocket = new Set();

    for (let g = i + 1; g < nums.length; g++) {
      let find_num = -(nums[i] + nums[g]);

      if (pocket.has(find_num)) {
        result.push([nums[i], find_num, nums[g]]);

        // 중복 제거 → 정렬된 상태에서 같은 수가 나오면 shift
        while (g + 1 < nums.length && nums[g] === nums[g + 1]) {
          g++;
        }
      }
      pocket.add(nums[g]);
    }
  }
  return result;
}
