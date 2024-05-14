// My cheat sheets of go
/*
Basic types
Go's basic types are
bool
string
int  int8  int16  int32  int64
uint uint8 uint16 uint32 uint64 uintptr
byte // alias for uint8
rune // alias for int32
     // represents a Unicode code point

float32 float64
complex64 complex128
The example shows variables of several types, and also that variable declarations may be "factored" into blocks, as with import statements.
The int, uint, and uintptr types are usually 32 bits wide on 32-bit systems and 64 bits wide on 64-bit systems. When you need an integer value you should use int unless you have a specific reason to use a sized or unsigned integer type.
*/

// package main

// import (
// 	"fmt"
// 	"math/cmplx"
// )

// var (
// 	ToBe   bool       = false
// 	MaxInt uint64     = 1<<64 - 1
// 	z      complex128 = cmplx.Sqrt(-5 + 12i)
// )

// func main() {
// 	fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
// 	fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
// 	fmt.Printf("Type: %T Value: %v\n", z, z)
// }

/*
Zero values
Variables declared without an explicit initial value are given their zero value.
The zero value is:
    0 for numeric types,
    false for the boolean type, and
    "" (the empty string) for strings.
*/

package main

import "fmt"

func main() {
	var i int
	var f float64
	var b bool
	var s string
	fmt.Printf("%v %v %v %q\n", i, f, b, s)
}

/*
Type conversions
The expression T(v) converts the value v to the type T.
Some numeric conversions:
var i int = 42
var f float64 = float64(i)
var u uint = uint(f)
Or, put more simply:
i := 42
f := float64(i)
u := uint(f)
Unlike in C, in Go assignment between items of different type requires an explicit conversion. Try removing the float64 or uint conversions in the example and see what happens.
*/

// package main
// import (
// 	"fmt"
// 	"math"
// )
// func main() {
// 	var x, y int = 3, 4
// 	var f float64 = math.Sqrt(float64(x*x + y*y))
// 	var z uint = uint(f)
// 	fmt.Printf("%T %T %T",x, y,z)
// }

/*
Type inference
When declaring a variable without specifying an explicit type (either by using the := syntax or var = expression syntax), the variable's type is inferred from the value on the right hand side.
When the right hand side of the declaration is typed, the new variable is of that same type:
var i int
j := i // j is an int
But when the right hand side contains an untyped numeric constant, the new variable may be an int, float64, or complex128 depending on the precision of the constant:
i := 42           // int
f := 3.142        // float64
g := 0.867 + 0.5i // complex128
Try changing the initial value of v in the example code and observe how its type is affected.
*/

// package main

// import "fmt"

// func main() {
// 	v := "halo" // change me!
// 	fmt.Printf("v is of type %T\n", v)
// }

/*
Constants
Constants are declared like variables, but with the const keyword.
Constants can be character, string, boolean, or numeric values.
Constants cannot be declared using the := syntax.
*/

// package main

// import "fmt"

// const Pi = 3.14

// func main() {
// 	const World = "世界"
// 	fmt.Println("Hello", World)
// 	fmt.Println("Happy", Pi, "Day")

// 	const Truth = true
// 	fmt.Println("Go rules?", Truth)
// }

/*

Numeric Constants

Numeric constants are high-precision values.

An untyped constant takes the type needed by its context.

Try printing needInt(Big) too.

(An int can store at maximum a 64-bit integer, and sometimes less.)
when i cheking it was 62 bit
*/
