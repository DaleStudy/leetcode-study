/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    const result = []
    function backtrack(start, curr, sum) {
        // 현재 합계가 타겟과 같으면 결과에 추가
        if(sum === target) {
            result.push([...curr])
        }

        // 합계가 타겟을 초과하면 더 이상 진행하지 않음
        if(sum > target) {
            return
        }
        
        // 현재 인덱스부터 시작하여 모든 후보를 시도
        for(let i = start; i < candidates.length; i++) {
            curr.push(candidates[i])
            // 같은 숫자를 여러 번 사용할 수 있으므로 i부터 다시 시작
            backtrack(i, curr, sum + candidates[i])
            curr.pop()
        }
    }
    backtrack(0, [], 0)
    return result
};
