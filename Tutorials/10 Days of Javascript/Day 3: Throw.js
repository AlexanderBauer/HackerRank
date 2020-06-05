/*
 * Complete the isPositive function.
 * If 'a' is positive, return "YES".
 * If 'a' is 0, throw an Error with the message "Zero Error"
 * If 'a' is negative, throw an Error with the message "Negative Error"
 */
function isPositive(a) {
    try {
        if(a == 0) throw "Zero Error";
        if(a < 0) throw "Negative Error";
        return 'YES';
    }
    catch(err) {
        return err;
    }
}