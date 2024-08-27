var combinationSum = function (candidates, target) {
    let results = [];

    function helper(idx, curr, total) {
        // base case - when total = target push into results
        if (total === target) {
            results.push([...curr]);
            return;
        }
        // base exit case - when the index is greater or equal to candidates or the total is greater than target, exit
        if (idx >= candidates.length || total > target) {
            return;
        }

        // recursive case
        // case where we include the current value without advancing the index
        curr.push(candidates[idx]);
        helper(idx, curr, total + candidates[idx]);
        curr.pop()
        // case where we advance the index 
        helper(idx + 1, curr, total);
    }
    helper(0, [], 0);
    
    return results;
};

// time - O(2^n) backtracking
// space - O(1)
