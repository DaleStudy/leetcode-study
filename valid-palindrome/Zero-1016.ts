/**
 * 시간 복잡도 O(N)
 * 공간 복잡도 O(1)
 */
const isNotAlphanumeric = /[^a-zA-Z0-9]/;

function isPalindrome(s: string): boolean {
  let leftCursor = 0;
  let rightCursor = s.length - 1;

  while (leftCursor < rightCursor) {
    const currentLeftAlpha = s[leftCursor];
    const currentRightAlpha = s[rightCursor];

    if (isNotAlphanumeric.test(currentLeftAlpha)) {
      leftCursor++;
      continue;
    }

    if (isNotAlphanumeric.test(currentRightAlpha)) {
      rightCursor--;
      continue;
    }

    if (currentLeftAlpha.toLowerCase() === currentRightAlpha.toLowerCase()) {
      leftCursor++;
      rightCursor--;
    } else {
      return false;
    }
  }

  return true;
}
