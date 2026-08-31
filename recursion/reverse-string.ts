/**
 Do not return anything, modify s in-place instead.
 */
function reverseString(s: string[]): void {
   helper(0, s.length - 1, s)  
};

function helper(l: number, r: number, s: string[]): void {
    
    if(l >= r){
        return 
    }
    
    let temp = s[l]
    s[l] = s[r]
    s[r] = temp
    
     helper(l + 1, r - 1, s)
    
}


const arr = ["h", "e", "l", "l", "o"]
reverseString(arr)
console.log(arr)