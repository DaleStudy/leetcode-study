/*
시간 복잡도: O(n)
공간 복잡도: replace()와 toLowerCase() 연산이 포함되어 O(n)
풀이: 
(1) Regex를 이용하여 NonAlphanumeric 문자를 일괄 제거한다.
(2) toLowerCase()를 이용하여 대문자를 전부 소문자로 치환한다.
(3) Two Pointer 기법을 이용하여 index의 시작/끝을 동시에 탐색한다. 일치하지 않는 문자가 걸리면 false를 반환한다.
(4) 공백 문자열의 경우에는 따로 체크하지 않고 바로 true를 반환한다.
풀이 이력
1트:
2트: 아래와 같이 수정하여 정답 획득.
개선점: 있음(replace(), toLowerCase()를 사용하지 않고 공간 복잡도 최적화가 가능하다고 함)
*/
const removeNonAlphanumeric = (str: string) =>
  str.replace(/[^A-Za-z0-9]/g, "").toLowerCase()

const isPalindrome = (s: string): boolean => {
  const removedNonAlphanumericString = removeNonAlphanumeric(s)

  if (!removedNonAlphanumericString) return true

  const n = removedNonAlphanumericString.length

  let j = 0
  let k = n - 1

  while (j < k) {
    if (removedNonAlphanumericString[j] !== removedNonAlphanumericString[k])
      return false

    j++
    k--
  }

  return true
}

/* 1트 풀이: 불필요한 배열 조작으로 계산 로직 자체가 실패함. */
/*
const removeNonAlphabetic = (str: string) => str.replace(/[^A-Za-z]/g, '').toLowerCase()

function failedIsPalindrome(s: string): boolean {
    const removedNonAlphabeticString = removeNonAlphabetic(s)
    
    if(!removedNonAlphabeticString) return true

    const n = removedNonAlphabeticString.length
    const centerIdx = Math.floor(n / 2)

    const leftTxtArr = removedNonAlphabeticString.slice(0,centerIdx).split("")
    const rightTxtArr = removedNonAlphabeticString.slice(centerIdx + 1,n).split("")

    if(leftTxtArr.length !== rightTxtArr.length) return false
    let rightIdx = rightTxtArr.length - 1

    for(let i = 0; i <= rightIdx; i++){
        const leftWord = leftTxtArr[i]
        const rightWord = rightTxtArr[rightIdx]

        if(leftWord !== rightWord) return false

        rightIdx--
    }

    return true
}
*/
