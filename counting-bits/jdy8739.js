/**
 * @param {number} n
 * @return {number[]}
 */
var countBits = function (n) {
    const arr = [0];

    for (let i = 1; i <= n; i++) {
        const num = binary(i);
        arr.push(num);
    }

    return arr;
};

/** 성능이 느리지만 간결한 함수 */
function binary(n) {
    return n.toString(2).split('').filter((el) => el === '1').length;
}

// 시간복잡도 O(n2) -> n을 이진수문자열로 변환하고 이를 벼열화하여 1인 원소만 필터링하고 그 결과의 길이를 구한다.
// 여기서 filter를 사용하여 배열을 한 번 순회하기 때문에 for문과 중첩되어 2중 루프의 시간복잡도를 가짐

/** 성능이 빠르지만 복잡한 함수 */
function binary(n) {
    let num = 1;
    let count = 0;

    while (num * 2 <= n) {
        num = num * 2;
    }

    while (0 <= n) {
        if (num <= n) {
            n = n - num;
            count++;
        }

        if (num === 1) {
            break;
        }

        num = num / 2;
    }

    return count;
}

// 시간복잡도 O(n2) -> for문 안에 while문이 돌면서 i가 이진수로 변환될 경우 1이 몇개인지 반환하기 때문에 2중 루프의 시간복잡도를 가짐
// 공간복잡도 O(n) -> for문을 돌면서 arr에 i가 이진수로 변환될 경우 1이 몇 개인지 원소로 추가함
