/*
 * Complete the vowelsAndConsonants function.
 * Print your output using 'console.log()'.
 */
function vowelsAndConsonants(s) {
    // print vowels
    var vowels = ['a', 'e', 'i', 'o', 'u'];
    for (let i in s){
        if(vowels.includes(s[i])){
            console.log(s[i]);
        } 
    }
    // print consonants
    for (let i in s){
        if(!vowels.includes(s[i])){
            console.log(s[i]);
        } 
    }
}