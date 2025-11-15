/*


// Create a empty hash table(seen) and store numbers as a key and their indices as a value
// Iterate through the given array(nums) 
// For each numbers in given array, calculate complement (target - num)
// If complement is in hash table(seen), return array of index of the currnet number and index of complement in hash table(seen)
// If complement is not in has table(seen), store the current number in hash table(seen) and continue checking the numbers
// The algorithm uses a single loop that goes through each element in nums exactly one time.
// If the array contains n elements, the loop runs n times → O(n).
   We use a hash table (seen) to store numbers we've already visited.
  seen could contain up to n − 1 entries, so its size grows linearly with input size → O(n).


*/

function twoSum2(nums: number[], target: number): number[] {
    const seen:{[key:number] : number} = {};
    for (let i = 0; i<nums.length; i++){
      let complement = target - nums[i]
      if (complement in seen) {
        return [seen[complement],i]
      }
      seen[nums[i]] = i
    }
    return []
};
