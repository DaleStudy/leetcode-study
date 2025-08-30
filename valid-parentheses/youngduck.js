/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function (s) {
  // stack문제. open,close에 따라 스택처리
  // 최종 stack 비워져있는지 마지막 확인까지.
  const stack = [];
  // open,close Bracket index 위치로 짝궁 판단할예정
  const openBracket = ['(', '[', '{'];
  const closeBracket = [')', ']', '}'];
  // 반환할 결과값 flag
  let result = true;

  [...s].map((item) => {
    // indexOf자체는 선형검색이라 O(n)이지만 데이터 양이 3으로 고정되어있으므로 O(1)로 볼 수 있음
    const itemIndexAtOpenBracket = openBracket.indexOf(item);
    const itemIndexAtCloseBracket = closeBracket.indexOf(item);
    // openBracket 타입
    if (itemIndexAtOpenBracket > -1) {
      // push,pop 모두 O(1) 시간복잡도를 가짐. 끝에 요소 추가제거이므로
      stack.push(item);
    }
    // clseBracket 타입
    else if (itemIndexAtCloseBracket > -1) {
      const target = stack.pop();
      if (target !== openBracket[itemIndexAtCloseBracket]) {
        result = false;
      }
    }
  });

  if (stack.length !== 0) {
    result = false;
  }

  return result;
};

// 시간복잡도 : O(n)
// 공간복잡도 : O(n)
