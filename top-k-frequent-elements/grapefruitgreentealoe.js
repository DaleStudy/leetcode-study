/**
 * 정수 array nums , 정수 k가 있을때, 가장 빈도가 높은 숫자 k개 리턴. 순서상관 X
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */

//nums에 대해서 각 요소에 대해 중복되는 횟수를 구한다. 그리고 내림차순으로 k개 리턴한다.

var topKFrequent = function (nums, k) {
  const numsFreqMap = new Map(); // O(1)

  // O(n) 시간 / O(n) 공간
  for (let num of nums) {
    numsFreqMap.set(num, (numsFreqMap.get(num) ?? 0) + 1);
  }

  const arrFromFreqMap = [...numsFreqMap]; // O(n) 시간 / O(n) 공간
  arrFromFreqMap.sort((a, b) => b[1] - a[1]); // O(n log n) 시간

  return arrFromFreqMap
    .map((x) => x[0]) // O(n) 시간 / O(n) 공간
    .slice(0, k); // O(k) 시간 / O(k) 공간
};

//O(n) + O(n log n) + O(n) + O(k) = O(n log n)


//7.22 소요시간 10분
/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    //우선은, Map으로 만들어서 숫자 각각에 대한 개수를 구한다. 
    const numsMap  = new Map();
    for(let num of nums){
        if(numsMap.has(num)){
            numsMap.set(num,numsMap.get(num)+1)
        }else{
            numsMap.set(num,1)
        }
    }
    //그런다음 Map에 대해서, 가장 큰 값을 가진 순으로 정렬을 한다. 
    const ret = [...numsMap].sort((a,b)=>b[1]-a[1]).slice(0,k).map(x=>x[0]);
    return ret
};

// 이전 답과 비슷하지만, for문 처리에 대해서, 조금 풀어서 작성을 하게 된거같다.
// 시간복잡도와 공간복잡도는 위의 코드와 같다. 

// 시간 복잡도 : for문 - O(n) , sort O(nlogn)
// 공간 복잡도 : O(n)
