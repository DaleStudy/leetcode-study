/**
 * 정수 배열 nums
 * 가장 많이 연속되는 요소의 길이 리턴.
 * O(n) 시간안에 돌아가는 알고리즘 사용할것.
 */
/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function (nums) {
  const numSet = new Set(nums);
  let maxCount = 0;
  for (let i of numSet) { //n 번 순회
    // ++ 이전에 연속체크가 되었을 수 있으므로, 이전 숫자가 존재한다면 pass
    if (numSet.has(i - 1)) continue; //이미 진행 된 연속체크의 경우 하지 않는다.
    //연속이 되는지 확인해서 있으면 1추가.
    let length = 0;
    while (numSet.has(i + length)) {
      //연속이 끊기는 순간 멈추는 반복문. 즉 for문 전체 통틀어 최대 n번 실행.
      length++;
    }
    maxCount = Math.max(length, maxCount);
  }
  return maxCount;
};

//시간복잡도 O(n) + O(n) = O(n) /공간복잡도 O(n)