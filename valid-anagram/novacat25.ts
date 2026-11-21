/* 
시간 복잡도(TC): O(n)
공간 복잡도(SC): O(1) (개선 완료)
풀이: 0-25 lowercase alphabet을 담은 고정 배열을 선언하여 count 값을 계산함.

풀이 이력
1트: 배열 쪼개기 + 정렬(Merge Sort) + 순차 비교. 답 자체는 맞췄으나 로직이 다소 비효율적이었고, 빈도 수를 파악하는 데 알맞은 방법이 아니라고 판단하여 기각.
2트: Map을 이용해 정렬 연산을 제거하고 탐색 연산 역시 줄이는 데 성공함. 공간 복잡도의 경우 O(k)(문자 종류가 늘어날수록 저장 공간도 증가)
3트: 배열을 이용할 경우 공간 복잡도를 O(k)에서 O(1)로 더욱 줄일 수 있으므로, 알파벳 수를 26개로 고정하여 문제 해결. 
*/
const BASE_CHAR_CODE = "a".charCodeAt(0)

const getCodeIndex = (code: number) => code - BASE_CHAR_CODE

const isAnagram = (s: string, t: string): boolean => {
  if (s.length !== t.length) return false

  const countArr = new Array<number>(26).fill(0)

  for (const sWord of s) {
    const code = sWord.charCodeAt(0)
    countArr[getCodeIndex(code)]++
  }

  for (const tWord of t) {
    const code = tWord.charCodeAt(0)
    const accessedValue = countArr[getCodeIndex(code)]

    if (accessedValue <= 0) {
      return false
    }

    countArr[getCodeIndex(code)]--
  }

  return true
}

// 기존 풀이/제출 내역.
/*
[1트] 배열 쪼개기 + 정렬(Merge Sort) + 순차 비교. 로직이 다소 비효율적이었음.

// Function to merge two sorted parts of array
const merge = (arr: number[], left: number, middle: number, right: number) => {
    // Length of both sorted aub arrays
    const l1 = middle - left + 1
    const l2 = right - middle
    // Create new subarrays
    const arr1 = new Array(l1)
    const arr2 = new Array(l2)
    
    // Assign values in subarrays
    for (let i = 0; i < l1; ++i) {
        arr1[i] = arr[left + i]
    }
    for (let i = 0; i < l2; ++i) {
        arr2[i] = arr[middle + 1 + i]
    }

    // To travesrse and modify main array
    let i = 0,
        j = 0,
        k = left
        
    // Assign the smaller value for sorted output
    while (i < l1 && j < l2) {
        if (arr1[i] < arr2[j]) {
            arr[k] = arr1[i]
            ++i
        } else {
            arr[k] = arr2[j]
            j++
        }
        k++
    }
    // Update the remaining elements
    while (i < l1) {
        arr[k] = arr1[i]
        i++
        k++
    }
    while (j < l2) {
        arr[k] = arr2[j]
        j++
        k++
    }
}

// Function to implement merger sort in javaScript
const mergeSort = (arr: number[], left: number, right: number) => {
    if (left >= right) {
        return
    }
    
    // Middle index to create subarray halves
    const middle = left + Math.floor((right - left) / 2)
    
    // Apply mergeSort to both the halves
    mergeSort(arr, left, middle)
    mergeSort(arr, middle + 1, right)
    
    // Merge both sorted parts
    merge(arr, left, middle, right)
}

const isAnagram = (s: string, t: string): boolean => {
    if(s.length !== t.length) return false
    
    const splitedSArr = s.split("")
    const splitedTArr = t.split("")

    const sCodeArr = splitedSArr.map((item) => item.charCodeAt(0))
    const tCodeArr = splitedTArr.map((item) => item.charCodeAt(0))
    
    const n = sCodeArr.length

    mergeSort(sCodeArr, 0, n - 1)
    mergeSort(tCodeArr, 0, n - 1)

    for(let i = 0; i < n; i++) {
        if (sCodeArr[i] !== tCodeArr[i]) {
            return false
        }
    }

    return true
}

[2트] [빈도수] Map을 이용해 풀이함. 공간 복잡도의 경우 O(k).
const isAnagram = (s: string, t: string): boolean => {
    if(s.length !== t.length) return false

    const anagramMap = new Map<string, number>()
    const sArr = Array.from(s)
    const tArr = Array.from(t)

    for(const sWord of sArr) {
        const count = (anagramMap.get(sWord) || 0) + 1
        anagramMap.set(sWord, count)
    }

    for(const tWord of tArr) {
        const count = anagramMap.get(tWord)
        if(!count || count <= 0) {
            return false
        }

        anagramMap.set(tWord, count - 1)
    }

    return true
}
*/
