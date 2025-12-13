var encode = function (strs) {
    // strs: string[]
    // return: string
    // write your code here

    let encode_result = "";

    for (const encode_strs of strs)
    {
        const encode_strs_length = encode_strs.length;

        if(encode_result != undefined)
        {
            encode_result = encode_result + encode_strs_length + "|" + encode_strs; 
        }
          
    }

    return encode_result;
};

var decode = function (str) {
    // str: string
    // return: string[]
    // write your code here

    let results = [];

    while (str.length > 0) {
        let i = 0;
        while (str[i] >= '0' && str[i] <= '9') {
            i++;
        }

        let decode_str_length = str.substring(0, i);
        let len = parseInt(decode_str_length, 10);

        let newStr = str.substring(i + 1);
        let result = newStr.substr(0,decode_str_length)

        str = newStr.substring(len);
        
        results.push(result);
    } 

    return results;
};

console.log(decode(encode(["lint","code","love","you"])));
console.log(decode(encode(["we","say",":","yes"])));

