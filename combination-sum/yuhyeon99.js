/**
 * 각각 다른 정수 배열 candidates와, 목표 정수 target이 주어진다.
 * 반환하라, 타겟과 값이 같은 합을 보유한 고유한 조합을.
 * 조합은 어떤 순서(any order)로든 반환할 수 있습니다.
 * 같은 숫자를 여러 조합에 무제한(unlimited number of times) 쓸 수 있습니다.
 * 선택한 숫자 중 적어도 하나의 빈도가 다르다면 두 조합은 고유합니다.
 * target은 150보다 낮은 숫자입니다.
 * 
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    var result = []; 
    var nums = [];
    function dfs(start, total) {
        if (total > target) return;
        if (total === target) result.push(nums.slice());


        for (let i = start; i < candidates.length; i ++) {
            let num = candidates[i];
            nums.push(num);
            dfs(i, total + num);
            nums.pop();
        }

    }
    dfs(0, 0);

    return result;
};
