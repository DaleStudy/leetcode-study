/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
    let result = [];
    
    function find_combination(index, target, current) {
        if (target === 0) {
            result.push([...current]);
            return;
        }
        
        for (let i = index; i < candidates.length; i++) {
            // Only proceed if current number doesn't exceed target
            if (candidates[i] <= target) {
                // Include current number in combination
                current.push(candidates[i]);
                
                // Recursive call with:
                // - same index i (allowing reuse of same number)
                // - reduced target by current number
                find_combination(i, target - candidates[i], current);
                
                // Backtrack: remove the last added number to try other combinations
                current.pop();
            }
        }
    }
    
    find_combination(0, target, []);
    return result;
};

/* 



*/

console.log(combinationSum([2,3,6,7], 7))


