/**
 * @param {number[]} nums
 * @return {boolean}
 */
const canJump = function(nums) {
    // 마지막 인덱스에서 첫 인덱스로 거꾸로 돌면서
    // 필요한 점프 횟수를 변수에 저장
    // 만약 인덱스 i의 값이 필요한 점프 횟수를 충족한다면 초기화

    let need = 1;
    let answer = true;

    for (let i = nums.length - 2; i >= 0; i--) {
        if (nums[i] >= need) {
            need = 1;
            answer = true;
        } else {
            need += 1;
            answer = false;
        }
    }

    return answer;
};

// 시간복잡도: O(n)
// 공간복잡도: O(1)
