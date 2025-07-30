function containsDuplicate(nums: number[]): boolean {
    let tmp: number[] = nums.toSorted()
    for(let i = 0 ; i < nums.length - 1 ; i++){
        if(tmp[i]===tmp[i+1]) return true
    }
   return false 
};
