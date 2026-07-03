/**
풀이
해시맵에 각 숫자들의 개수를 저장하고, 총 개수와 해시맵의 키 개수를 비교하여 중복 여부를 판단한다.
 */
var containsDuplicate = function (nums) {
  let map = {};
  for (const n of nums) {
    map[n] = map[n] ? map[n] + 1 : 1;
  }
  let count = 0;
  for (const key of Object.keys(map)) {
    count += map[key];
  }
  if (count === Object.keys(map).length) {
    return false;
  } else return true;
};
