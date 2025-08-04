/**
 * 정수 숫자 배열과 정수 target
 * 숫자 합이 target과 같은 두 숫자의 index를 리턴.
 * 같은 요소 두번 X. 답은 항상 1개
 * 정렬필요 X
 */

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  //순회. target에서 nums[i]를 뺀 요소를 찾기.
  //2중포문. 시간복잡도 O(1)~O(N^2)
  for (let i = 0; i < nums.length; i++) {
    const subNum = target - nums[i]; // 공간 O(1)
    for (let j = i + 1; j < nums.length; j++) {
      if (nums[j] == subNum) {
        return [i, j];
      }
    }
  }
};

var twoSum2 = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    //시간복잡도 O(N)
    const subNum = target - nums[i]; // 공간 O(1)
    if (nums.includes(subNum) && nums.indexOf(subNum) !== i) {
      //시간복잡도 O(N). 2중포문과 같은 효과.
      return [i, nums.indexOf(subNum)];
    }
  }
};

//Better answer
var twoSum3 = function (nums, target) {
  // map으로 관리하여 indexing 최적화
  const numMap = new Map();
  for (let i = 0; i < nums.length; i++) {
    //시간복잡도 O(N)
    const subNum = target - nums[i];
    if (numMap.has(subNum)) {
      //시간복잡도 O(1)
      return [i, numMap.get(subNum)];
    }
    numMap.set(nums[i], i); // 공간 O(1)
  }
};


//25.7.24 
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    //우선 nums배열에서 target보다 큰것은 삭제한다. => 이것 또한 시간복잡도가 든다. 하지말자
    //1. 투포인터 방식으로 접근한다. 
    for(let i=0;i<nums.length-1;i++){
        let total = nums[i]
        for(let j=i+1;j<nums.length;j++){
            if(total+nums[j] == target){
                return [i,j]
            }
        }
    }    
};

/**
 * 시간복잡도: O(N^2)
 * 공간복잡도: O(1)
 */

/*
투포인터로 다시 풀었지만, 이 문제의 핵심은 map 메소드를 활용해서, 조회를 빠르게 하는것.. 
Map.get(key) : 	O(1) 평균	해시 테이블 기반이기 때문에, 키 조회가 상수 시간
Array.includes(value)	: O(n)	배열 처음부터 끝까지 순차 탐색 (최악의 경우 전체 탐색)
*/

var twoSum = function(nums, target) {
  //현재 nums에 대해서, subnums를 저장한다.
  const subNumsMap = new Map(); 
  for(let i = 0;i<nums.length;i++){
    const subNum = target - nums[i];
    if(subNumsMap.has(subNum)){
      return [subNumsMap.get(subNum),i]
    }
    subNumsMap.set(nums[i],i)
  }
};
//시간복잡도: O(n) , 공간복잡도 : O(n)

/*
Q. 여기서 의문. Map이좋냐 object가 좋냐?
알고리즘용 해시맵 대용이라면 대부분 Map 추천
Object는 JSON-like 데이터 보관용에 적합
 */
