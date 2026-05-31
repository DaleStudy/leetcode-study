/**
 * @param {number[]} nums
 * @return {number}
 */
/*
    문제명: Missing Number (LeetCode 268)

    문제 설명:
    길이가 n인 배열 nums가 주어진다.
    이 배열에는 0부터 n까지의 숫자 중에서
    정확히 하나를 제외한 n개의 숫자가 들어 있다.
    (즉, 원래는 n+1개의 숫자가 있어야 함)

    목표:
    0부터 n까지의 범위 안에서
    배열 nums에 존재하지 않는 "단 하나의 숫자"를 찾아 반환한다.

    입력 조건:
      - nums.length == n
      - 1 <= n <= 10^4
      - nums[i]는 0 이상 n 이하의 정수
      - nums 안의 모든 값은 서로 다르다 (중복 없음)

    출력:
      - nums 배열에 없는 숫자 1개를 반환

    핵심 포인트:
      - 정상 상태라면 숫자 범위는 [0, n] (총 n+1개)
      - 실제 배열에는 n개만 존재 → 반드시 하나는 빠져 있음
      - 배열은 정렬되어 있지 않음

    예시 1:
      입력: nums = [3, 0, 1]
      해석:
        n = 3
        정상 범위: [0, 1, 2, 3]
        빠진 숫자: 2
      출력: 2

    예시 2:
      입력: nums = [0, 1]
      해석:
        n = 2
        정상 범위: [0, 1, 2]
        빠진 숫자: 2
      출력: 2

    예시 3:
      입력: nums = [9,6,4,2,3,5,7,0,1]
      해석:
        n = 9
        정상 범위: [0, 1, 2, ..., 9]
        빠진 숫자: 8
      출력: 8

    추가 요구사항 (Follow up):
      - 시간 복잡도: O(n)
        → 배열을 한 번만 순회해야 함
      - 공간 복잡도: O(1)
        → 추가 배열, 해시맵 등 사용 불가

    문제 의도:
      - 단순 탐색이 아니라
        "전체 범위의 성질"을 이용해
        빠진 숫자를 찾아낼 수 있는지 확인
      - 수학적 사고 또는 비트 연산적 사고를 요구하는 문제
*/
var missingNumber = function(nums) {
    const n = nums.length;

    const expectedSum = (n * (n + 1)) / 2;

    let actualSum = 0;
    for (let i = 0; i < n; i++) {
        actualSum += nums[i];
    }

    return expectedSum - actualSum;
};

console.log(missingNumber([3, 0, 1]))
console.log(missingNumber([0, 1]))
console.log(missingNumber([9,6,4,2,3,5,7,0,1]))

