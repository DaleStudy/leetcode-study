/**
s의 문자 빈도를 기록하는 charMap을 만들고, t를 순회하면서 charMap의 빈도를 1씩 줄여 가며 같은지 비교한다.

시간복잡도: O(N) (s의 length N)

 */

function isAnagram(s: string, t: string): boolean {
  if (s.length !== t.length) return false
  const charMap = new Map()

  for (let char of s) {
    charMap.set(char, (charMap.get(char) || 0) + 1)
  }

  for (let char of t) {
    if (!charMap.has(char) || charMap.get(char) === 0) {
      return false
    }
    charMap.set(char, charMap.get(char) - 1)
  }

  return true
}
