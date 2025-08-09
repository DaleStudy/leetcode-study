function isPalindrome(s: string): boolean {
    // https://leetcode.com/problems/valid-palindrome/
    // Runtime: 6ms
    // Memory: 58.88MB
    const convertedString: string = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase()
    let lettersArray: string[]
    if(convertedString.length>0){
      lettersArray = convertedString.split("")
        for(let idx = 0; idx<(lettersArray.length/2); idx++){
            if(lettersArray[idx] !== lettersArray[lettersArray.length-idx-1]) return false
        }
    }
    return true

    // what I had done wrong at first: reducing the length of the array
    // simple solution: reverse and compare (return convertedString === convertedString.split("").reverse().join(""))
};
