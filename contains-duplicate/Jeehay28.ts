// Approach 3: HashSet (Using TypeScript Set)
// ⏳ Time Complexity: O(n)
// 💾 Space Complexity: O(n)

function containsDuplicate(nums: number[]): boolean {

    const seen = new Set<number>();

    for (const num of nums) {
        if (seen.has(num)) {
            return true;
        }
        seen.add(num);
    }

    return false;

};


// Approach 2: Sorting + Scan
// ⏳ Time Complexity: O(n * log(n)) ❌ (Faster than O(n^2), but still not optimal)
// 💾 Space Complexity: O(1)

// function containsDuplicate(nums: number[]): boolean {

//     nums.sort();

//     for (let i = 0; i < nums.length - 1; i++) {
//         if (nums[i] === nums[i + 1]) {
//             return true;
//         }
//     }

//     return false;

// };


// Approach 1: Brute Force (O(n^2))
// 🚨⏳ TLE (Time Limit Exceeded)!
// ⏳ Time Complexity: O(n^2) ❌ (Inefficient for large inputs)
// 💾 Space Complexity: O(1) ✅ (Great, no extra memory used!)

// function containsDuplicate(nums: number[]): boolean {

//     for (let i = 0; i < nums.length; i++) {
//         for (let j = i + 1; j < nums.length; j++) {
//             if (nums[i] === nums[j]) {
//                 return true;
//             }
//         }
//     }

//     return false;

// };



