/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    
    // 최악의 경우 3중 for문이므로 투포인터 기법을써서 최적화 해도 for문 하나는 필요함

    // 결과 배열
    const result = [];

    // 투포인터 기법 사용을 위한 정렬
    nums.sort((a,b)=>a-b);
    
    for(let i = 0; i < nums.length - 2; i++){
        // 첫 번째 요소의 중복 건너뛰기
        if(i > 0 && nums[i] === nums[i-1]) continue;
        
        let left = i + 1;
        let right = nums.length - 1;
        
        while(left < right){
            const sum = nums[i] + nums[left] + nums[right];
            
            if(sum < 0){
                left++;
            }
            else if (sum > 0){
                right--;
            }
            else{
                // 합이 0인 경우 결과에 추가
                result.push([nums[i], nums[left], nums[right]]);
                
                // 두 번째, 세 번째 요소의 중복 건너뛰기
                while(left < right && nums[left] === nums[left + 1]) left++;
                while(left < right && nums[right] === nums[right - 1]) right--;
                
                left++;
                right--;
            }
        }
    }
    
    return result;
};