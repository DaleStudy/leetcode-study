/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function (s, t) {
    //1. s와 t를 Array로 만든다.
    const sArray = s.split("");
    const tArray = t.split("");

    //2. sArray와 tArray의 sort를 같게 만든다.
    const sortedSArray = sArray.sort();
    const sortedTArray = tArray.sort();

    //3. sArray와 tArray가 같은지 판별한다.
    const result = JSON.stringify(sortedSArray) === JSON.stringify(sortedTArray);

    //4. 같으면 true를, 다르면 false를 반환한다.
    return result;

};
