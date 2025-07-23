/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
  //HashMap 선언
  const counter = new Map()

  //HashMap에 빈도를 value로 저장
  for(const num of nums){
    counter.set(num,(counter.get(num)|| 0) +1);
  }

  //keys를 가져와 정렬 후, k만큼 -slice 리턴
  return [...counter.keys()]
    .sort((a,b) => counter.get(a) - counter.get(b))
    .slice(-k)
};
