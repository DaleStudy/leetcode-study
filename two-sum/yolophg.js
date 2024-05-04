var twoSum = function(nums, target) {
    const hash = new Map();
    
    for( let i = 0 ; i < nums.length; i++) {
        // find num to make a target
        const findTarget = target - nums[i];

        // if find num, return
        if(hash.get(findTarget) !== undefined)  return [hash.get(findTarget), i];
        
        // if couldn't find, set in the map
        hash.set(nums[i], i);
    }
    
    return [];
};