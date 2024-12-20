/**
 * @param {number[]} nums
 * @return {number[][]}
 * 
 * 문제: 세 수를 더해서 0을 만들어야함.
 * 
 * 주의사항: 인덱스 상관없어 세 수의 조합이 같으면 안됨.
 * 핵심: 배열을 오름차순으로 정렬해서 
 * 양 끝에 각 인덱스넣고 사이에 있는인덱스로 계속 더하면서 
 * 좌우 인덱스를 0에 가깝게 +- 하면된다~
 * 
 */
var threeSum = function (nums) {
  // 결과를 저장할 배열
  let result = [];
  // 주어진 수를 오름차순으로 정렬
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length; i++) {
    // nums[i] > 0보다 크다면? 반복 끝
    if (nums[i] > 0) {
      break;
    }

    let j = i + 1;            // 중간에서 바뀔 인덱스
    let k = nums.length - 1;  // 맨 마지막에서 부터 움직일 인덱스

    while (j < k) {
      let sum = nums[i] + nums[j] + nums[k];

      // 총합이 양수라면 k인덱스 한칸뒤로 ㄱ
      if (sum > 0) {
        k--;
      }
      // 음수라면 j진행 ㄱ
      else if (sum < 0) {
        j++;
      }
      // 0이면 result배열에 추가, j진행
      else {
        result.push([nums[i], nums[j], nums[k]]);
        j++;

        // j가 이전값과 같다면 무시하고 진행하기
        while (nums[j] === nums[j - 1] && j < k) {
          j++;
        }
      }
    }
  }

  return result;

};
