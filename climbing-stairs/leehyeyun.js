/**
 * @param {number} n
 * @return {number}
 */
/*
    계단을 올라가고 있을 때,
    꼭대기에 도달하려면 총 n 계단을 올라가야 한다.

    한 번에 오를 수 있는 계단 수는
    - 1계단
    - 2계단
    두 가지뿐이다.

    이때, 정확히 n번째 계단(꼭대기)에 도달하는
    서로 다른 방법의 수를 반환하는 함수.

    요청형식 : climbStairs(n)

    입력형식 :
      - n은 정수
      - 1 <= n <= 45

    출력형식 :
      - n번째 계단에 도달할 수 있는 서로 다른 방법의 수 (정수)

    예시 :

      Example 1
      입력 :
        n = 2
      출력 :
        2
      설명 :
        1) 1계단 + 1계단
        2) 2계단

      Example 2
      입력 :
        n = 3
      출력 :
        3
      설명 :
        1) 1계단 + 1계단 + 1계단
        2) 1계단 + 2계단
        3) 2계단 + 1계단

    제약사항 :
      - 1 <= n <= 45

    참고 :
      - 각 계단에 도달하는 "방법의 수"를 잘 관찰하면
        일정한 규칙(수열)이 나타난다.
*/
var climbStairs = function(n) {
    
    const map = new Map();

    map.set(1,1);
    map.set(2,2)

    for (var stairs = 3; stairs <= n; stairs ++)
    {
        var stairs_hap = map.get(stairs-1) + map.get(stairs-2)
        map.set(stairs,stairs_hap)
    }

    var result = map.get(n);

    return result; 
};

console.log(climbStairs(2)); //2
console.log(climbStairs(3)); //3

