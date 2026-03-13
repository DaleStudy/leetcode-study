// ! 풀다가 막혀서 AI의 도움(힌트)을 받아 완성한 코드입니다..

// tc: o(n^2)
// sc: o(n)
const threeSum = function (nums) {
  const answer = [];

  // 먼저 오름차순 정렬하기
  const sortedArr = nums.sort((a, b) => a - b);

  for (let i = 0; i < sortedArr.length; i++) {
    if (i > 0 && sortedArr[i] === sortedArr[i - 1]) continue;

    let left = i + 1;
    let right = sortedArr.length - 1;

    while (left < right) {
      const sum = sortedArr[i] + sortedArr[left] + sortedArr[right];

      if (sum === 0) {
        answer.push([sortedArr[i], sortedArr[left], sortedArr[right]]);

        // 중복 처리
        // left가 가리키는 숫자가 이전 숫자와 똑같다면 계속 패스
        while (left < right && sortedArr[left] === sortedArr[left + 1]) {
          left++;
        }
        // right가 가리키는 숫자가 이전 숫자와 똑같다면 계속 패스
        while (left < right && sortedArr[right] === sortedArr[right - 1]) {
          right--;
        }
        // 똑같은 숫자들을 다 건너뛰었으니, 새로운 숫자로 넘어감
        left++;
        right--;
      } else if (sum < 0) {
        // 0보다 작으면 left를 키움 (오름차순 정렬이기 때문)
        left++;
      } else {
        right--;
      }
    }
  }

  return answer;
};
