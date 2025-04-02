/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    let dict = new Map();
    let temp = Array.from(new Set([...nums]));
    for(const num of nums){
        if(dict.has(num)){
            dict.set(num, dict.get(num)+1);
        }else{
            dict.set(num,1);
        }
    }

    temp = temp.sort((a,b)=>{
        let aCount = dict.get(a);
        let bCount = dict.get(b);

        return bCount - aCount;
    })

    let slice = temp.slice(0,k);
    return slice;
};
