/**
 * @param {number[]} nums
 * @return {boolean}
 */

/**
 * 문제설명: 2개 이상 반복되는 값이 있으면 true, 모두 반복되지 않으면 false.

제한사항
 1 <= nums.length <= 10^5
-109 <= nums[i] <= 109
 */

var containsDuplicate = function (nums) {
  const numberSet = new Set();
  //시간 복잡도 O(n)
  for (let i of nums) {
    if (!numberSet.has(i)) {
      //공간복잡도 O(n)
      numberSet.add(i);
    } else {
      return true;
    }
  }
  return false;
};

//25.7.23 풀이시간 10분
/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    //두번 이상 나타나는게 있으면 바로 리턴하시오. 
    //이중 순회하게 되면 시간 초과할 예정.
    //시간복잡도 중요. 
    //1. 저장하는 배열을 만들고, 그 배열에 값이 있으면 리턴 false. 
    //2.배열보다 Set을 사용한,삽입 및 조회 속도 최적화 활용하기. 
    const container = new Set();
    for(let i =0; i<nums.length;i++){
        if(container.has(nums[i])) return true;
        else container.add(nums[i])
    }
    return false
};
//위의 코드보다, 리턴을 더 빨리한다는 이점이 있다.