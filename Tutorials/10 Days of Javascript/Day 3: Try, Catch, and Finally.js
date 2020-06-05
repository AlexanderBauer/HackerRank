function reverseString(s) {
    try{
        s = s.split("").reverse().join("")
    }
    catch(err){
        console.log(err.message)
    }
    console.log(s)
}