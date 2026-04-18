/*
strs의 문자열들을 등장빈도를 바탕으로 계산한 특수 문자열로 전환하고 같은 것끼리 묶는다.

시간복잡도 : O(N * K) - N은 strs의 개수, K는 strs의 길이. N 순회 안에 K 순회
*/

function groupAnagrams(strs: string[]): string[][] {
  const anagramMap = {}
  const result = strs.reduce((acc, cur) => {
    const charArray = new Array(26).fill(0)

    for (let char of cur) {
      const charIdx = char.charCodeAt(0) - 'a'.charCodeAt(0)
      charArray[charIdx] += 1
    }

    const sortedValue = charArray.join('#')

    const targetIdx = anagramMap[sortedValue]
    if (targetIdx !== undefined) {
      acc[targetIdx].push(cur)
    } else {
      anagramMap[sortedValue] = acc.length
      acc.push([cur])
    }
    return acc
  }, [])

  return result
}
