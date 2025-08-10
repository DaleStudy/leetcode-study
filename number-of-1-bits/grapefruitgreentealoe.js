


//풀이1. 나머지와 몫을 이용한 개수 구하기

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    let remain = n;
    let count = 0;
    while(remain){
       if(remain == 2 || remain ==1 ){
            count +=1;
            break;
       }
        if(remain %2 == 1){
            count +=1
        }
        remain = Math.floor(remain /2)
    }
    return count;
};
/*2진법을 구할때, 나머지가 1일때마다 count++ 해주고,
마지막에 2나 1이 남으면 count ++ 하고 break 해주면 된다.

입력 값을 반으로 나누기 때문에 시간 복잡도는 O(log n)
공간복잡도 O(1)
*/

//풀이 2. n의 이진수에서 가장 오른쪽 1비트를 하나씩 제거하여 1의 개수를 세는 방법

/**
 * @param {number} n
 * @return {number}
 */
var hammingWeight = function(n) {
    //정수 n이 주어졌을때, 1의 개수?
    let count = 0;
    while (n !== 0) {
        n = n & (n - 1);
        count++;
    }
    return count
};

/*
시간복잡도: O(k) : 여기서 k는 n에 포함된 1의 개수
공간복잡도: O(1)
*/

//이 외에도 비트연산자, 비트마스킹 방법으로 시간복잡도를 O(1), O(logn)으로 풀수있다.
