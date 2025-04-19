// https://leetcode.com/problems/number-of-1-bits/

// TC: O(logN) - n을 2로 나누며 1을 셈 
// SC: O(1) - 배열을 사용하지 않고, 변수만 사용하여 추가 메모리 x

function hammingWeight(n: number): number {
    let answer = 0

    while (n > 0) {
        answer += n % 2
        n = Math.floor(n / 2)
    }

    return answer
}
