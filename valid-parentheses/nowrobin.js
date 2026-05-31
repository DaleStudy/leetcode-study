/**
 * @param {string} s
 * @return {boolean}
 */
var isValid = function(s) {
    const a = [...s]
    const stack  =[] 
    const mapping = {} 
    mapping[')'] = '('
    mapping[']'] = '['
    mapping['}'] = '{'

    for(let i of a){
        if(Object.values(mapping).includes(i)){
            stack.push(i)
        }else if (mapping.hasOwnProperty(i)){
            if(!stack.length || mapping[i] !== stack.pop()){
                return false 
            }
        }
    }
        return stack.length === 0
};  
