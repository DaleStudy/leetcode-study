var containsDuplicate = function(nums) {
    let set = new Set([nums[0]]);

    // check if the current value is in the set
    for(let i = 1; i < nums.length; i++){
        // if it's already in the set, return true
        if(set.has(nums[i])){
            return true;
        // if it's not in the set, add it to set and resume 
        } else {
            set.add(nums[i]);
        }
    }
    return false;
};
