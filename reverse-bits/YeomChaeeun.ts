/**
 * 정수를 비트로 변환후 뒤집어서 다시 정수로 반환
 * 알고리즘 복잡도
 * - 시간복잡도: O(1)
 * - 공간복잡도: O(1)
 * @param n
 */
function reverseBits(n: number): number {
    // 2진수 배열로 변환
    let arr = n.toString(2).split('')
    let len = arr.length
    // 32비트 정렬 - 부족한 앞쪽에 0으로 채움
    for (let i = 0; i < (32 - len); i++) {
        arr.unshift('0');
    }
    // 뒤집은 후 합침
    let result = arr.reverse().join('')
    // 2진수 정수로 변환하여 반환
    return parseInt(result,2)
}
