/**
 *
 * @param n
 *
 * 풀이 1
 *
 * function hammingWeight(n: number): number {
 *     let parse = (n).toString(2);
 *     let count = 0;
 *     for (const item of parse){
 *         if(+item ===1) count ++
 *     }
 *     return count
 * };
 *
 * 숫자를 문자열로 변환할때 오버헤드 발생
 * 비트 연산을 사용해야할듯!
 *
 * 검색해보니 Brian Kernighan 알고리즘을 사용하면 더 효율적이라고 한다
 */

function hammingWeight(n: number): number {
    let count = 0;

    while (n !== 0) {
        n &= (n - 1);
        count++;
    }

    return count;
}
