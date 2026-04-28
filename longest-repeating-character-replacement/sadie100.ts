/*
start, end 투 포인터 변수를 생성하고 end를 하나씩 늘려 가며 s를 탐색
글자별 개수를 저장하는 map, 최빈 등장수 maxCount를 통해 가장 많이 나온 캐릭터의 카운트를 저장하고
만약 end-start+1-maxCount가 k를 넘어가면 start를 +1한다
매번 end-start+1와 현 result를 비교하여 큰 값을 result로 갱신한다

시간복잡도 : O(N)
*/

function characterReplacement(s: string, k: number): number {
  let start = 0
  let end = 0
  let result = 0
  let maxCount = 0
  const charMap = new Map()

  while (end < s.length) {
    const thisChar = s[end]
    const updatedCount = (charMap.get(thisChar) || 0) + 1
    charMap.set(thisChar, updatedCount)
    maxCount = Math.max(maxCount, updatedCount)

    if (end - start + 1 - maxCount > k) {
      const startChar = s[start]
      charMap.set(startChar, charMap.get(startChar) - 1)
      start += 1
    }

    result = Math.max(result, end - start + 1)
    end += 1
  }

  return result
}
