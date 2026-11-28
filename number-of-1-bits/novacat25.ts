/*
시간 복잡도: O(k) (정수 k에 비례)
공간 복잡도: O(1)
풀이 기법: Brian Kernighan's Algorithm를 응용, Bitwise AND(&)를 이용해 n & n-1를 수행, 가장 오른쪽의 1을 지우면서 count를 도출한다.
풀이 이력
1트: mod 연산을 이용한 풀이로 정답은 맞았으며, 시간 복잡도 역시 O(k)를 유지했으나 공간 복잡도가 O(k)를 차지하고 있었고 조금 더 효율적인 알고리즘을 지향하고 싶었음.
2트: Brian Kernighan's Algorithm를 이용하여 공간 복잡도를 O(1)로 단축 완료
*/
const hammingWeight = (n: number): number => {
  let currentVal = n
  let count = 0
  while (currentVal != 0) {
    currentVal = currentVal & (currentVal - 1)
    count++
  }

  return count
}

/* 1트 풀이: 정답은 맞았으나, 조금 더 효율적인 코드를 찾기 위해 기각함. */
/*
const modSelf = (num: number) => {
    let currentNum = num
    const numArr = []

    while (Math.floor(currentNum / 2) > 0) {
        const quotient = Math.floor(currentNum / 2)
        const mod = currentNum % 2
        numArr.push(mod)
        currentNum = quotient
    }

    numArr.push(1)

    return numArr
}
function hammingWeight(n: number): number {
    const reversedByteArr = modSelf(n)
    let count = 0

    for(const byteItem of reversedByteArr) {
        if(byteItem) count++
    }

    return count
}
*/
