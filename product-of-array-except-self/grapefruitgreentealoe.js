var productExceptSelf = function(nums) {
    const n = nums.length;
    const left = new Array(n).fill(1);
    const right = new Array(n).fill(1);
    const answer = new Array(n).fill(1);

    // 오른쪽 누적곱
    for (let i = n - 2; i >= 0; i--) {
        right[i] = right[i + 1] * nums[i + 1];
    }

    // 왼쪽 누적곱
    for (let i = 1; i < n; i++) {
        left[i] = left[i - 1] * nums[i - 1];
    }

    // 최종 곱셈
    for (let i = 0; i < n; i++) {
        answer[i] = left[i] * right[i];
    }

    return answer;
};
};
//시간복잡도 O(n)
//공간복잡도 O(n)
// 어려웠던 점: 한번 풀었던 문제지만, 인덱스 범위를 설정하는 점에서 어려움을 겪엇다. 


//여기서 공간복잡도를 O(1)로 최적화 할 수 있다. ( 리턴 배열 제외)
/**
 * 문제 내에서  Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
 */
var productExceptSelf = function(nums) {
    const n = nums.length;
    const answer = new Array(n).fill(1);

    // 왼쪽 곱
    for (let i = 1; i < n; i++) {
        answer[i] = answer[i - 1] * nums[i - 1];
    }

    // 오른쪽 곱 누적하면서 answer에 곱해줌
    let right = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= right;
        right *= nums[i];
    }

    return answer;
};
