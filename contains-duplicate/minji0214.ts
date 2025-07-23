function containsDuplicate(nums: number[]): boolean {
    let answer = false
  for(let i = 0; i< nums.length; i ++ ){
    if(nums.findIndex((value)=> value === nums[i]) !== i){
        answer = true
        break;
     }
    }  
    return answer
};
//-> time lit 초과 오류 발생