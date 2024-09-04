var twoSum = function (nums, target) {
    let map = new Map(); // create a map to store the number and index of each element
    for(let i = 0; i < nums.length; i++) {
        let diff = target - nums[i];
        if(map.has(diff)) { // once the differnece is found, return both index
            return [i, map.get(diff)];
        } else { // otherwise add to map
            map.set(nums[i], i)
        }
    }
};

// time - O(n) at worst, iterate through the entire nums array 
// space - O(n) at worst, map the entire nums array
