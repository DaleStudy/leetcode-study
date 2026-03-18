/**
 * 문제: https://leetcode.com/problems/product-of-array-except-self/description/
 *
 * 요구사항:
 * nums: number[]가 주어질 때 자기자신을 제외한 값들의 곱을 O(n)으로 나눗셈 없이 number[]로 리턴
 *
 * * */

const productOfArrayExceptSelf = (nums) => {
    let answer = new Array(nums.length);
    // 가장 왼쪽에는 아무것도 없으니 1로 시작
    answer[0] = 1;

    // 왼쪽에서 오른쪽으로 가면서 누적 곱
    for(let i = 1; i < nums.length; i++) {
        answer[i] = answer[i - 1] * nums[i - 1];
    }

    // 가장 오른쪽 끝이 없으니 1로 시작
    let right = 1;

    // 역순회
    for(let i = nums.length -1; i >=0; i--) {
        answer[i] = answer[i] * right;

        right = right * nums[i];
    }

    return answer;
}
