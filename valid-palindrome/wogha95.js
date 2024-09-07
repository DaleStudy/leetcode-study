// 3차
// TC: O(N)
// SC: O(1)
// N: s.length

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // 1. 투포인터를 양끝에서 시작합니다.
  let left = 0;
  let right = s.length - 1;

  while (left < right) {
    // 2. 현재 가리키는 문자가 영대소문자, 숫자가 아니면 건너뜁니다.
    while (left < right && !isValid(s[left])) {
      left += 1;
    }
    while (left < right && !isValid(s[right])) {
      right -= 1;
    }

    // 3. 문자의 갯수가 홀수인 경우 투 포인터가 모두 가운데를 가리키는 경우 순회를 끝났다고 생각합니다.
    if (left === right) {
      break;
    }

    // 4. 투 포인터가 가리키는 문자가 다른 경우 정답(false)를 반환합니다.
    if (!isSame(s[left], s[right])) {
      return false;
    }

    // 5. 다음 문자로 넘어갑니다.
    left += 1;
    right -= 1;
  }

  // 6. 모든 순회가 끝냈다면 palindrome이라고 판단합니다.
  return true;

  function isValid(spell) {
    if ("0" <= spell && spell <= "9") {
      return true;
    }
    if ("a" <= spell && spell <= "z") {
      return true;
    }
    if ("A" <= spell && spell <= "Z") {
      return true;
    }

    return false;
  }

  function isSame(spellA, spellB) {
    if (spellA === spellB) {
      return true;
    }
    if (Math.abs(s[left].charCodeAt() - s[right].charCodeAt()) === 32) {
      return true;
    }

    return false;
  }
};

// 2차
// TC: O(N)
// SC: O(N)
// N: s.length

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  const phrase = s.toLowerCase();
  // 1. 투포인터를 양끝에서 시작합니다.
  let left = 0;
  let right = phrase.length - 1;

  while (left < right) {
    // 2. 현재 가리키는 문자가 영소문자, 숫자가 아니면 건너뜁니다.
    while (left < right && !isValid(phrase[left])) {
      left += 1;
    }
    while (left < right && !isValid(phrase[right])) {
      right -= 1;
    }

    // 3. 문자의 갯수가 홀수인 경우 투 포인터가 모두 가운데를 가리키는 경우 순회를 끝났다고 생각합니다.
    if (left === right) {
      break;
    }

    // 4. 투 포인터가 가리키는 문자가 다른 경우 정답(false)를 반환합니다.
    if (phrase[left] !== phrase[right]) {
      return false;
    }

    // 5. 다음 문자로 넘어갑니다.
    left += 1;
    right -= 1;
  }

  // 6. 모든 순회가 끝냈다면 palindrome이라고 판단합니다.
  return true;

  function isValid(spell) {
    if ("0" <= spell && spell <= "9") {
      return true;
    }
    if ("a" <= spell && spell <= "z") {
      return true;
    }

    return false;
  }
};

// 1차
// TC: O(N)
// SC: O(N)
// N: s.length

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function (s) {
  // 1. 문자열을 모두 소문자로 바꾸고 영소문자, 숫자만 남기고 모두 제거합니다.
  const phrase = s
    .toLowerCase()
    .split("")
    .filter(
      (spell) =>
        ("0" <= spell && spell <= "9") || ("a" <= spell && spell <= "z")
    );

  // 2. 양끝의 문자를 확인해서 palindrome인지 판별합니다.
  for (let index = 0; index < Math.floor(phrase.length / 2); index++) {
    if (phrase[index] !== phrase[phrase.length - index - 1]) {
      return false;
    }
  }

  return true;
};
