// Approach 2: HashMap (Using Map in TypeScript)
// ⏳ Time Complexity: O(n) ✅ (Efficient for large inputs)
// 💾 Space Complexity: O(n) ❌ (Extra memory used for Map)

function twoSum(nums: number[], target: number): number[] {

    const indices = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {

        const temp = target - nums[i];
        if (indices.has(temp)) {
            // Ensure correct order
            return [indices.get(temp)!, i];
            // The exclamation mark (!) in indices.get(temp)! is a non-null assertion operator in TypeScript.
        }
        // If you return [i, indices.get(temp)!], 
        // you would be returning the current index first, 
        // which is incorrect because the problem statement usually expects indices in the order they were found (earlier index first).

        indices.set(nums[i], i);
    }
    return [];
};


// Approach 1: Brute Force (O(n^2))
// ⏳ Time Complexity: O(n^2) ❌ (Inefficient for large inputs)
// 💾 Space Complexity: O(1) ✅ (Great, no extra memory used!)

// function twoSum(nums: number[], target: number): number[] {
//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] + nums[j] === target) {
//                 return [i, j]
//             }
//         }
//     }
//     return [];
// };


