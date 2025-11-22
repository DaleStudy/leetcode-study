/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) { 
    //(n) = f(n - 1) + f(n - 2)
    let tempArray = [];
    
    for(let i = 0; i <= n; i++){
        if(i === 0 || i === 1){
            tempArray.push(1);
        }else{
            let tempSum = 0;
            tempSum = tempArray[i - 2] + tempArray[i - 1];
            tempArray.push(tempSum); 
        }
    }
    return tempArray[n];
};
