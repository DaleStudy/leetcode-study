function productExceptSelf(nums: number[]): number[] {
    // 시간 복잡도: O(n), 공간 복잡도: O(1)
    const n = nums.length;
    const answer = new Array(n).fill(1);

    // answer[i]에 left 곱 저장
    for (let i = 1; i < n; i++) {
        answer[i] = answer[i - 1] * nums[i - 1];
    }

    // right 곱을 한 변수에 저장하면서 answer에 곱하기
    let rightProduct = 1;
    for (let i = n - 1; i >= 0; i--) {
        answer[i] *= rightProduct;
        rightProduct *= nums[i];
    }

    return answer;
}
