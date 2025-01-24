/**
 * 시간 복잡도: s의 길이만큼 순회하므로, O(n)
 * 공간 복잡도: 스택은 최대 s의 길이만큼 문자를 저장하므로, O(n)
 */
/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
  const stack = [];
  const brackets = {
      '(': ')',
      '{': '}',
      '[': ']'
  }
  for(const b of s) {
      if(b in brackets) {
          stack.push(b);
      } else {
          const cur = stack.pop();
          if(brackets[cur] !== b) {
              return false;
          }
      }
  }
  return stack.length === 0;
};
