// 풀이
// 1. 각 요소의 빈도를 계산하여 countObject 생성
// 2. countObject를 정렬하여 상위 k개의 요소 추출
// 3. 추출된 요소를 배열로 반환

// TC : O(NlogN)
// SC : O(N)

var topKFrequent = function(nums, k) {
  const countObject = {}
  nums.forEach((num) => {
      if(countObject[num]) {
          countObject[num] += 1
      }else {
          countObject[num] = 1
      }
  })

  const sortedObject = Object.entries(countObject)
      .sort((a,b) => b[1] - a[1]) 
      .slice(0, k)
      .map(item => Number(item[0]))
  
  return sortedObject
};

