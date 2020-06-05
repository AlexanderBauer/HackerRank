/*
 * Complete the Rectangle function
 */
function Rectangle(a, b) {
    var obj         =   {length: 0,width: 0,perimeter: 0,area: 0}
    obj.length      =   a
    obj.width       =   b
    obj.perimeter   =   2 * (a + b)
    obj.area        =   a * b
    return obj;
}