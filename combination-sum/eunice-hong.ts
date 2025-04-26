/**
 * Finds all unique combinations of numbers from the candidates array that sum up to the target.
 * 
 * @param candidates - An array of numbers.
 * @param target - The target sum.
 * @returns An array of arrays, each containing a unique combination of numbers that sum up to the target.
 * 
 * Time Complexity: O(n^2)
 * Space Complexity: O(n)
 */
function combinationSum(candidates: number[], target: number): number[][] {
    // 1. Initialize result array
    let combinations: number[][] = [];
    let candidate: number[] = [];

    // 2. Define recursive function
    function combination(start: number, total: number) {
        console.log(`start:${start}, total:${total}`)
        if (target < total) {
          // 3. If total is greater than target, return
            return;
        } else if (target === total) {
            // 4. If total is equal to target, push candidate to result
            combinations.push([...candidate])
            return;
        } else {
          // 5. If total is less than target, iterate through candidates
            for (let i = start; i < candidates.length; i++) {
                // 6. Push candidate to result
                candidate.push(candidates[i])
                // 7. Recursively call combination function
                combination(i, total + candidates[i])
                // 8. Pop candidate from result
                candidate.pop();
            }
        }
    }
    combination(0, 0);

    return combinations;
};
