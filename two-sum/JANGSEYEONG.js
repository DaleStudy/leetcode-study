/*
  시간복잡도:  O(n²)
  - nums.indexOf()는 배열 전체를 순회하는 O(n) 작업
  - 이 작업이 for 루프(O(n)) 내부에서 실행되므로 전체 시간복잡도는 O(n) * O(n) = O(n²)

  var twoSum = function (nums, target) {
    for (let i = 0; i < nums.length; i++) {
      let x = nums.indexOf(target - nums[i]);
      if (x > -1 && x !== i) {
        return [i, x];
      }
    }
    return [];
  };

*/

/* 
  시간복잡도: O(n) - 전체 배열을 한 번만 순회 O(n) + 키-값 쌍 저장에 O(1)
  - Map 대신 객체(Object)를 사용해도 될듯 함
  - 일반 객체는 {}, 접근은 obj[key]로 가능, has() 대신 (key in obj) 또는 obj[key] !== undefined 또는 key in obj 사용 가능 */
/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let minus = new Map();
  for (let i = 0; i < nums.length; i++) {
    let current = nums[i];

    // 현재 숫자가 이전에 저장된 보수(complement)와 일치하는지 확인 - Map 객체의 has는 O(1) 연산
    if (minus.has(current)) {
      return [minus.get(current), i];
    }

    // 현재 숫자의 보수(target-current)와 인덱스를 맵에 저장 - Map 객체의 set은 O(1) 연산
    minus.set(target - current, i);
  }

  return [];
};
