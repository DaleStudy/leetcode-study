/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
var reverseBits = function (n) {
  // 문자열로 변환
  let nString = n.toString(2).padStart(32, "0");
  //console.log(nString);

  // 스택 생성 (스택은 나중에 들어온게 먼저 나가므로)
  let stack = [];

  // nString 스택에 넣기
  for (let i = 0; i < nString.length; i++) {
    stack.push(nString[i]);
  }

  // pop하여 뒤집힌 문자열 만들기
  let reverseNString = "";
  for (let i = 0; i < nString.length; i++) {
    reverseNString += stack.pop();
  }

  // 뒤집힌 문자열을 정수로 변환
  return parseInt(reverseNString, 2);
};

// 시간 복잡도: O(1)
// 공간 복잡도: O(1)
