/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) { 

    // ways(n) = ways(n-1) + ways(n-2)

    const waysArray = new Array(n);

    waysArray[0] = 1; //실제 1번째 계단까지 오르는 경우의 수
    waysArray[1] = 2; //실제 2번째 계단까지 오르는 경우의 수

    for(let i = 2; i < n; i++){
        waysArray[i] = waysArray[i-1] + waysArray[i-2]; 
    }

    return waysArray[n-1];

};

//------------1회차 풀이-----------------
// /**
//  * @param {number} n
//  * @return {number}
//  */
// var climbStairs = function(n) { 
//     //(n) = f(n - 1) + f(n - 2)
//     let tempArray = [];
    
//     for(let i = 0; i <= n; i++){
//         if(i === 0 || i === 1){
//             tempArray.push(1);
//         }else{
//             let tempSum = 0;
//             tempSum = tempArray[i - 2] + tempArray[i - 1];
//             tempArray.push(tempSum); 
//         }
//     }
//     return tempArray[n];
// };

