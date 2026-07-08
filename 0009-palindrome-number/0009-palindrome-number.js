/**
 * @param {number} x = [1,2,1]
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let array = Array.from(String(x), Number);

    if(x<0) return false;

    let i = 0
    let j = array.length - 1 // x = 10, x.length = 2, 2 - 1 = 1

    while (i<j) {
        if(array[i] !== array[j]) { // 1 !== 0
            return false;
        } 
        i++; // i = 1
        j--; // j = 0
    }

    return true;

};