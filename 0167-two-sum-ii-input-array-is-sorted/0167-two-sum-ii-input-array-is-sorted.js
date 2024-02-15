/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    const result = [];
    let i = 0;
    let j=numbers.length-1;
    while(numbers[i] + numbers[j] !== target){

        if(numbers[i] + numbers[j] < target) i++;
        else j--
    }
    
    result.push(i+1);
    result.push(j+1);
    
    return result;
    
};