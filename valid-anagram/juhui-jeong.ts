// 시간 복잡도(Time Complexity): O(n)
// 공간 복잡도(Space Complexity): O(1)
function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false;

  const count = new Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    count[s.charCodeAt(i) - 97]++;
    count[t.charCodeAt(i) - 97]--;
  }

  return count.every((n) => n === 0);
}

/*
// 첫 번째 풀이
// 시간 복잡도(Time Complexity): O(n log n)
// 공간 복잡도(Space Complexity): O(n)

function isAnagram(s: string, t: string): boolean {
  let baseString = s.split('').sort().toString();
  let targetString = t.split('').sort().toString();

  return baseString === targetString ? true : false;
}
*/
