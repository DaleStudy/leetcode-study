var isPalindrome = function(s) {
    let regex = /[!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"" ]/g;
    let convertToLowerCase = s.replace(regex, '').toLowerCase();
    let middleOftheString = parseInt(convertToLowerCase.length / 2);
    let result;

    // iterate over each value of string till to reache the middle of the string
    for (let i = 0; i <= middleOftheString; i++) {
        // check if values match
        if (convertToLowerCase[i] === convertToLowerCase[convertToLowerCase.length - 1 - i]) {
            result = true;
        // if there's nothing else to check for, return false and break the loop
        } else {
            result = false;
            break;
        }
    }
    return result;    
};
