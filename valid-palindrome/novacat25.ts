/*
시간 복잡도: O(n)
공간 복잡도: replace()와 toLowerCase() 연산이 포함되어 O(n)
풀이: 
(1) Regex를 이용하여 NonAlphanumeric 문자를 일괄 제거한다.
(2) toLowerCase()를 이용하여 대문자를 전부 소문자로 치환한다.
(3) Two Pointer 기법을 이용하여 index의 시작/끝을 동시에 탐색한다. 일치하지 않는 문자가 걸리면 false를 반환한다.
(4) 공백 문자열의 경우에는 따로 체크하지 않고 바로 true를 반환한다.
풀이 이력
1트: 투 포인터 기법을 일부 사용했으나, 그 과정에서 불필요하게 배열을 나누었으며 처리 로직이 꼬여 답이 틀렸음.
2트: 아래와 같이 수정하여 정답 획득.
3트: 문자열을 따로 수정하지 않고 투 포인터 기법을 적용. 다만, toLowerCase()로 비교 가능한 상황이므로 두 문자열 비교 메소드는 배제하기로 함.
4트: j < k 방어 로직을 달지 않아 무한 루프가 터짐.
5트: 방어 로직을 달아 해결 완료.
*/
const isAlphanumeric = (str: string) => /^[a-zA-Z0-9]$/.test(str)

const isPalindrome = (s: string): boolean => {
  if (!s) return true

  const n = s.length

  let j = 0
  let k = n - 1

  while (j < k) {
    while (j < k && !isAlphanumeric(s[j])) j++
    while (j < k && !isAlphanumeric(s[k])) k--

    if (s[j].toLowerCase() !== s[k].toLowerCase()) return false

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

/* 2트 풀이: 원리는 맞췄으나, 공간 복잡도 개선이 필요했음. */
/*

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
*/

/* 3트 풀이: 공간 복잡도 개선 완료. 다만, Regex 코드를 조금 더 최적화할 수 있어서 기각. */
/*
const isAlphanumeric = (str: string) => new RegExp(/^[a-zA-Z0-9]+$/).test(str)

// 4트에서 터진 ".," 반례는 엉뚱하게도 comStr(undefined, undefined)가 true를 반환하는 바람에 생뚱맞게 통과했다...
const comStr = (s1: string, s2: string) => new RegExp(`^${s1}$`, "i").test(s2)

const isPalindrome = (s: string): boolean => {
  if (!s) return true

  const n = s.length

  let j = 0
  let k = n - 1

  while (j < k) {
    while(!isAlphanumeric(s[j])) j++
    while(!isAlphanumeric(s[k])) k--

    if (!comStr(s[j],s[k]))
      return false

    j++
    k--
  }

  return true
}
*/

/* 4트 풀이: 원리는 맞췄으나, while 문의 방어 조건을 고려하지 않아 TLE가 발생. 개선 도중 아깝게 실패함. */
/*
const isAlphanumeric = (str: string) =>  /^[a-zA-Z0-9]$/.test(str)

const isPalindrome = (s: string): boolean => {
  if (!s) return true

  const n = s.length

  let j = 0
  let k = n - 1

  // ".," 코드에서 반례가 터졌다! 방어 로직 필수.
  while (j < k) {
    while(!isAlphanumeric(s[j])) j++
    while(!isAlphanumeric(s[k])) k--

    if (s[j].toLowerCase() !== s[k].toLowerCase())
      return false

    j++
    k--
  }

  return true
}
*/
