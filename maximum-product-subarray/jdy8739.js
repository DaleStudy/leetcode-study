/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function (nums) {
    let answer = nums[0];
    let max = 1;
    let min = 1;

    for (let i = 0; i < nums.length; i++) {
        const current = nums[i];

        const candidates = [max * current, min * current, current];

        max = Math.max(...candidates);
        min = Math.min(...candidates);
        answer = Math.max(answer, max);
    }

    return answer;
};

// 시간복잡도 O(n) * O(8) -> nums의 길이 만큼을 for 문으로 순환하면서 Math클래스의 max, min메소드를 호출(인자가 3개, 3개, 2개 이므로 총 8회 순회)
// 공간복잡도 O(1) -> 파라미터 nums에 대해 의미있는 공간복잡도를 가지는 변수할당이 없음
