function isPalindrome(s: string): boolean {
    
    let formatedInput = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    
    return formatedInput.split('').reverse().join('') === formatedInput;
    
// if array use this kind of two pointers
    
// let i = 0;
// let j = s.length - 1;
    
//     while (i < j) {
//         if(arr[i] !== arr[j]){
//             return false;
//         } else {
//             i++;
//             j--;
            
//         };
//     };
//     return true;
    
    
};