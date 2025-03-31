/**
 * @param {number[]} nums
 * @return {boolean}
 */

/**
 * 1차 풀이
 * - Map을 사용하여 각 숫자의 개수를 세는 방법
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

/**
 * 2차풀이
 * - Map을 사용하여 각 숫자의 개수를 세는 방법
 * - forEach를 사용하지 않고 for of문을 사용하여 반복문을 돌리는 방법 
 */
var containsDuplicate = function(nums) {
    let dict = new Map();

    for (const num of nums) {
         if(dict.has(num)){
            dict.set(num, dict.get(num)+1);
        }else{
            dict.set(num, 1);
        }
        if(dict.get(num) >= 2){
            return true;
        }
    }
    return false;
};
