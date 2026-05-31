/**
 * DP 문제라는 것을 알았지만 개념을 잘 몰라서 약간의 검색을 했습니다.
 * 하나의 문제를 여러 작은 문제들로 쪼갤 수 있고, 그 쪼갠 문제가 다시 해당 문제의 해답이 될 수 있으며, 중복된 값이 존재하는 조건에 맞기 떄문에 DP로 풀었습니다.
 * 처음에는 피보나치 형식으로 접근했다가 시간초과가 나버려서 bottom-up 방식으로 변경해서 적용했습니다
 */


/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    const answer = [1,2];
    
    for(let i = 2; i < n; i++){
        const value = answer[i-1] + answer[i-2];
        answer.push(value);
    }

    return answer[n-1];
};
