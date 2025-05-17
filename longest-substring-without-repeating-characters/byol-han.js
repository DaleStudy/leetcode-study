/**
 * https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function (s) {
  let longestS = [];
  let result = 0;
  for (let char of s) {
    if (!longestS.includes(char)) {
      longestS.push(char);
    } else {
      result = Math.max(result, longestS.length);
      longestS = longestS.slice(longestS.indexOf(char) + 1);
      longestS.push(char);
    }
  }
  return Math.max(result, longestS.length);
};

/*
Sliding Window
Sliding Window는 문자열이나 배열에서 연속된 부분(subarray/substring)을 다룰 때 아주 유용한 알고리즘 기법
고정되거나 유동적인 “창(window)”을 좌우로 움직이며 문제를 해결하는 방식

슬라이딩 윈도우 핵심 아이디어
1. 두 포인터 사용: left, right
2. 조건을 만족하는 윈도우 유지
3. 조건이 깨지면 left를 이동
4. 조건을 만족하면 결과 업데이트
*/
var lengthOfLongestSubstring = function (s) {
  let set = new Set();
  let left = 0;
  let maxLen = 0;

  for (let right = 0; right < s.length; right++) {
    while (set.has(s[right])) {
      set.delete(s[left]); // 중복 문자 제거
      left++; // 왼쪽 포인터 이동
    }
    set.add(s[right]); // 현재 문자 추가
    maxLen = Math.max(maxLen, right - left + 1); // 최대 길이 업데이트
  }

  return maxLen;
};
