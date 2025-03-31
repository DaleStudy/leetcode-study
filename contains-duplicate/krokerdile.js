/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let dict = new Map();

    nums.forEach((num)=>{
        if(dict.has(num)){
            dict.set(num, dict.get(num)+1);
        }else{
            dict.set(num, 1);
        }
    })

    for (const num of nums) {
        if(dict.get(num) >= 2){
            return true;
        }
    }
    return false;
};
