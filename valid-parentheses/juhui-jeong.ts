/*
시간복잡도: O(n)
공간복잡도: O(n)
*/
function isValid(s: string): boolean {
  if (s.length % 2 !== 0) {
    return false;
  }

  const stack: string[] = [];
  const pair: Map<string, string> = new Map<string, string>([
    [')', '('],
    ['}', '{'],
    [']', '['],
  ]);

  for (const char of s) {
    // close brackts인지 확인
    if (pair.has(char)) {
      let topItem = stack.pop();
      // pair 확인
      if (topItem !== pair.get(char)) {
        return false;
      }
    } else {
      stack.push(char);
    }
  }

  if (stack.length === 0) {
    return true;
  } else {
    return false;
  }
}
