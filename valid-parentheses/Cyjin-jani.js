// tc: O(n)
// sc: O(n)
const isValid = function (s) {
  const bracketMap = {
    '(': ')',
    '{': '}',
    '[': ']',
  };

  if (s.length % 2 !== 0 || isCloseBracket(s[0])) return false;

  const stack = [];

  for (let i = 0; i < s.length; i++) {
    if (stack.length === 0) {
      stack.push(s[i]);
      continue;
    }

    let topBracket = stack.pop();
    if (bracketMap[topBracket] !== s[i]) {
      stack.push(topBracket);
      stack.push(s[i]);
    }
  }

  return stack.length === 0;
};

function isCloseBracket(char) {
  const closeBrackets = [')', '}', ']'];

  return closeBrackets.includes(char);
}
