/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    let ch = {};
    ch[')'] = '(';
    ch['}'] = '{';
    ch[']'] = '[';

    let list = s.split('');
    let stack = [];

    list.forEach((ele)=>{
        if(stack.length == 0){
            stack.push(ele);
        }else{
            let len = stack.length;
            if(stack[len-1] == ch[ele]){
                stack.pop();
            }else{
                stack.push(ele);
            }
        }
    })
    if(stack.length == 0){
        return true;
    }else{
        return false;
    }
};
