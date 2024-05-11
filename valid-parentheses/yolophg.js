var isValid = function(s) {
    let array = [];

    // loop and store elements in the char.
     for(let i = 0; i < s.length; i++) {
         let char = s[i];

        // if it's opening one, push a closing one in stack array.
         switch(char) {
             case "(": array.push(")");
             break;

             case "{": array.push("}");
             break;

             case "[": array.push("]");
             break;

             default: 
             // if it isn't opening one, pop last element and store it in the topElement.
             let topElement = array.pop();
             if(char !== topElement) {
                 return false;
             }
         }
     }
    // check the length of array is zero.
     return array.length === 0;
};

// Time complexity : O(n)
// Space complexity : O(n)
