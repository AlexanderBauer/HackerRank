/*
 * Implement a Polygon class with the following properties:
 * 1. A constructor that takes an array of integer side lengths.
 * 2. A 'perimeter' method that returns the sum of the Polygon's side lengths.
 */

class Polygon {
    constructor(side_length) {
        this.side_length = side_length;
    }

    perimeter(){
        let s = 0
        for (let i in this.side_length) {
            s = s + this.side_length[i]
        }
        return s
    }
}