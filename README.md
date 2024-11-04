# Prewritten Content
This is the prewritten content in the markdown file.

# Collected main.go Files Content

<details close>
<summary><h2 style="display: inline;"> 0. hello-in-golang <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("Hello world :)")
	fmt.Println("Hellooooo Earthians!!")
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 1. variables <br> </h2></summary>

```go
package main

// https://astaxie.gitbooks.io/build-web-application-with-golang/content/en/02.2.html

import (
	"fmt"
	"reflect"
)

// iota is a special variable which get increment in group
const (
	WHITE  = iota // 0
	BLACK         // 1
	BLUE          // 2
	RED           // 3
	YELLOW        // 4
)

const (
	Reset = iota // 0 (new const block)
	Fifth        // 1
)

// will work outside main() function
// var name_1 = "My Name outside"
var name_1 string = "My Name outside"

//will not work outs0ide main() function
// name_1 := "My Name"

func main() {
	fmt.Println("Variables in Golang")
	fmt.Println()

	// Decalaring variables
	var num1 int32 = 230023
	fmt.Println(num1)

	var num2 = 89
	fmt.Println(num2)

	num3 := 56
	fmt.Println(num3)

	//will work in main() function
	name := "My Name inside"
	fmt.Println(name)
	fmt.Println(name_1)

	//multiple variable declaration
	// var integer1, integer2, integer3 int32 = 1, 2, 3
	// var integer1, integer2, integer3 = 1, 2, 3
	integer1, integer2, integer3 := 1, 2, 3
	fmt.Println(integer1, integer2, integer3)

	// SPECIAL VARIABLES
	_, a := 100, 99

	// error, Any value that is given to "_" will be ignored
	// fmt.Println(_)
	fmt.Println(a)

	// constants
	// it can be of any type
	const pi = 3.1415926535
	fmt.Println(pi)

	// reassigning to const
	// error
	// pi = 3.45

	// Grouping similar variables
	var (
		z int     = 78
		y float32 = 78.90
		x string  = "I am X"
	)

	fmt.Println(z, y, x)

	fmt.Println()
	fmt.Println("Golang iota <special-var>")

	Strings := []string{"WHITE", "BLACK", "BLUE", "RED", "YELLOW"}

	fmt.Println("Value at[YELLOW]: ", Strings[YELLOW])
	fmt.Println("Type: ", reflect.TypeOf(Strings[YELLOW]))
	fmt.Println()
	fmt.Println("Value of YELLOW: ", YELLOW)
	fmt.Println("Type: ", reflect.TypeOf(YELLOW))
	fmt.Println()
	fmt.Println("Value of Reset: ", Reset)
	fmt.Println("Type: ", reflect.TypeOf(Reset))
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 2. string <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("String in Golang")

	var name string = "Your Name"
	fmt.Println(name)

	// string are mutable
	name = "My Name"
	fmt.Println(name)

	// but we cannot modify string char like C
	// name[0] = 'Z'

	// cannot change name but can get value
	// fmt.Println(name[0]) // give ASCII value
	fmt.Println(string(name[0]))
	fmt.Printf("%s\n", name[0:1]) // from 0 to < 1

	// golang way to do that
	// converting string --> byte
	b := []byte(name)

	// now we can do that :)
	b[0] = 'W'
	fmt.Println(b)

	// converting back to string from byte
	fmt.Println(string(b))

	// adding to string using +
	name1 := "This is Jhon"
	name2 := "This is Marcus"
	name3 := name1 + ", " + name2
	fmt.Println(name3)

	// multiline string
	long_name := `Hello My name is 
	long lol :)`
	fmt.Println(long_name)

}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 3. array <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("Array in Golang")

	// array declaration
	arr1 := [5]int{1, 2, 3, 4, 5}
	var arr2 = [5]int{1, 2, 3, 4, 5}
	var arr3 [5]int = [5]int{1, 2, 3, 4, 5}
	// use `…` to replace the length parameter
	arr4 := [...]int{5, 4, 3, 2, 1}

	fmt.Println(arr1)
	fmt.Println(arr2)
	fmt.Println(arr3)
	fmt.Println(arr4)

	//default value of array is 0
	var arr [10]int
	arr[0] = 90
	arr[9] = 99
	for i := 0; i < 10; i++ {
		fmt.Print(arr[i], ",")
	}
	fmt.Println()

	// multidimensional Array
	// method 1
	// mat := [2][3]int{[3]int{2, 2, 2}, [3]int{3, 3, 3}}
	// method 2
	mat := [2][3]int{{2, 2, 2}, {3, 3, 3}}
	fmt.Println(mat)
	for i := 0; i < 2; i++ {
		for j := 0; j < 3; j++ {
			fmt.Print(mat[i][j], " ")
		}
		fmt.Println()
	}
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 4. slice <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("Slice in Golang")

	// NOTE:
	// slice is a reference type
	// defined same as array but without size limitation
	// there is something related to size in slice will deal with that later

	var my_slice []byte = []byte{'a', 'b', 'c', 'd'}
	fmt.Println(my_slice)
	fmt.Println(string(my_slice))

	// array
	var arr = [10]byte{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
	var a, b []byte
	a = arr[2:5]
	b = arr[3:5]
	fmt.Println(string(a))
	fmt.Println(string(b))

	// length --> start index to last index of that slice [2 to 5]
	// The length of slice
	fmt.Println("Length [a]: ", len(a))

	// capacity --> start index to end of array [2 to 10]
	fmt.Println("Capacity [a]: ", cap(a))
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 5. refernce-data-slice-array <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("Understanding reference data type in Golang")

	var mySlice = []int{1, 2, 3, 4, 5}
	fmt.Println("My Slice: ", mySlice)

	// creating slice from array
	var mySlice1 = mySlice[:]

	// here I am changing 5th elem of mySlice
	// but value in mySlice1 changed
	// means mySlice1 is just pointing in mySlice
	mySlice[4] = 99
	fmt.Println()
	fmt.Println("--- After changing mySlice { mySlice[4] = 99 }---")

	// expectation - [1 2 3 4 5]
	// reality - [1 2 3 4 99]
	fmt.Println("My Slice: ", mySlice)
	fmt.Println("My Slice 1: ", mySlice1)

	// Now appending elem more than capacity of mySlice
	// current size of mySlice is 5
	fmt.Println()
	fmt.Println("Capacity of mySlice: ", cap(mySlice))
	fmt.Println("--- After Appending element in mySlice [exceeding capacity] ---")
	mySlice = append(mySlice, 6)
	fmt.Println("My Slice: ", mySlice)

	// now mySlice1 is not pointing toward mySlice new Value
	// it is now poiting toward old value of mySlice so new value are not shown
	// by mySlice
	fmt.Println("My Slice 1: ", mySlice1)
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 6. map <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("Map in Golang")
	// map is also refernce data type

	// similar to dictionary in python
	// SYNTAX
	// map[keyType]valueType

	// METHOD 1
	// var myMap map[int]string     //create a nil map
	// myMap = make(map[int]string) //initialize it via make
	// after that we can add entries

	// METHOD 2
	// shorthand for above create and initialize code
	myMap := make(map[int]string)

	myMap[1] = "value 1"
	myMap[2] = "value 2"
	myMap[3] = "I am value 3"
	fmt.Println("myMap1: ", myMap[1])
	fmt.Println("myMap1: ", myMap[2])
	fmt.Println("myMap1: ", myMap[3]) //nil

	//initialize with default value
	myMap2 := map[int]string{1: "I am value 1 from map 2"}
	fmt.Println("myMap2: ", myMap2[1])

	//checing if key exist
	fmt.Println()
	students := map[int]string{1: "Mohit", 2: "Utkarsh", 3: "Mark", 4: "Manson"}
	fmt.Println(students)

	//checking if key
	// DNE --> Do Not Exists
	// name, is_exists := students[5] //DNE
	name, is_exists := students[1] //E
	// students[1] return 2 value
	// first --> value or nil if DNE
	// second --> bool if E or DNE
	fmt.Println("Does student exists: ", is_exists)
	fmt.Println("Name: ", name)

	//better example would be
	fmt.Println()
	fmt.Println("-- better example --")
	name, is_exists = students[5]
	if is_exists {
		fmt.Println("name: ", name)
	} else {
		fmt.Println("student DNE")
	}

	//deleting value in map
	fmt.Println()
	fmt.Println("-- deletion in map --")
	delete(students, 1)
	fmt.Println(students)

	//map are refernce data
	fmt.Println()
	fmt.Println("-- showcasing map is reference data type --")
	//if we change one it will affect another
	students_2 := students
	//only deleting value in students
	//but it will affect students_2
	delete(students, 3)
	fmt.Println("students: ", students)
	fmt.Println("students_2: ", students_2)
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 7. control-statement-1 <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("Control Statement in Golang [Part 1]")

	//if-else
	fmt.Println()
	fmt.Println(" -- if-else -- ")
	// var flag1 int = 1
	var flag1 int = 2
	if flag1 == 1 {
		fmt.Println("value of flag1 is 1")
	} else {
		fmt.Println("value of flag1 is not 1")

	}

	// chained if-else
	fmt.Println()
	fmt.Println(" -- chained if-else -- ")
	flag2 := 3
	if flag2 == 0 {
		fmt.Println("flag2 : 0")
	} else if flag2 == 1 {
		fmt.Println("flag2 : 1")
	} else if flag2 == 2 {
		fmt.Println("flag2 : 2")
	} else {
		fmt.Println("flag2 : value is something we cannot guess :)")

	}

	// goto
	// It is same as in C language
	// work something like for loop
	// RECOMENDEDATION : DO NOT USE

	// for-loop
	fmt.Println()
	fmt.Println(" -- for-loop -- ")
	for i := 0; i < 10; i++ {
		fmt.Print(i, ", ")
	}
	fmt.Println()

	// while-loop
	fmt.Println()
	fmt.Println(" -- while-loop -- ")
	counter := 0
	for counter < 10 {
		fmt.Print(counter, ", ")
		counter++
	}
	fmt.Println()

	// infinite loop
	// fmt.Println()
	// fmt.Println(" -- infinite loop -- ")
	// press ctrl+c or ctrl+z to stop
	// for {
	// 	fmt.Println("I will run forever, util you kill me !!")
	// }

	fmt.Println()
	fmt.Println(" -- break & continue -- ")
	//printing from 1 to 10 except 7
	fmt.Println(" -- using continue -- ")
	for i := 1; i <= 10; i++ {
		if i == 7 {
			continue
		}
		fmt.Print(i, ", ")
	}
	fmt.Println()

	fmt.Println(" -- using break -- ")
	for i := 1; i <= 10; i++ {
		if i == 7 {
			break
		}
		fmt.Print(i, ", ")
	}
	fmt.Println()

	// for with range [slice]
	// defining slice
	fmt.Println()
	fmt.Println(" -- for with range [slice] -- ")
	mySlice := []int{1, 2, 3, 4, 5}
	for index, value := range mySlice {
		fmt.Println("index: ", index, "value: ", value)
	}

	// for with range [slice]
	// defining slice
	fmt.Println()
	fmt.Println(" -- for with range [map] -- ")
	myMap := map[int]string{
		1: "Ram",
		2: "Shyam",
		3: "Mark",
		4: "Manson",
	}

	for key, value := range myMap {
		fmt.Println("Key: ", key, "Value: ", value)
	}
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 8. control-statement-2 <br> </h2></summary>

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Control Statement in Golang [Part 2]")

	//switch
	fmt.Println()
	fmt.Println("-- switch [type 1] --")
	day := 2
	switch day {
	case 1:
		fmt.Println("Monday")
	case 2:
		fmt.Println("Tuesday")
	case 3:
		fmt.Println("Wednesday")
	case 4:
		fmt.Println("Thursday")
	case 5:
		fmt.Println("Friday")
	case 6:
		fmt.Println("Saturday")
	case 7:
		fmt.Println("Sunday")
	default:
		fmt.Println("Invalid day number")
	}

	// in go by default there is break after each case
	// if you explicitly want to continue then
	// use fallthrough
	fmt.Println()
	fmt.Println("-- switch [type 2] --")
	category := 2
	switch category {
	case 1:
		fmt.Println("<=1")
	case 2:
		fmt.Println("<=2")
		fallthrough
	case 3:
		fmt.Println("<=3")
		fallthrough
	case 4:
		fmt.Println("<=4")
		fallthrough
	case 5:
		fmt.Println("<=5")
		// fallthrough //otherwise default will run
	default:
		fmt.Println("Invalid !!")
	}

	fmt.Println()
	fmt.Println("-- switch [type 3] --")
	number := 7
	switch {
	case number == 0 || number == 1:
		fmt.Println("number is 0 or 1")
	case number%2 == 0:
		fmt.Println("number is even")
	case number%2 != 0:
		fmt.Println("number is odd")
	default:
		fmt.Println("This is W number")
	}

	// multiple expression in single case
	fmt.Println()
	fmt.Println("-- switch [type 4] --")
	cgpa := 10
	switch cgpa {
	case 0, 1, 2, 3, 4:
		fmt.Println("Sorry!!, FAILED")
	case 5, 6, 7, 8:
		fmt.Println("Congrats!!, PASSED")
	case 9:
		fmt.Println("Well Done!!, PASSED:)")
	case 10:
		fmt.Println("Outstanding!!, PASSED:) ^_^")
	default:
		fmt.Println("Invalid CGPA Value")
	}
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 9. functions-1 <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("functions in golang [part: 1]")

	//function calling single value return
	fmt.Println("Max: {3, 4}", max(3, 4))
	x := 3
	y := 4
	z := 5
	max_xy := max(x, y)
	max_xyz := max(max(x, y), z)
	fmt.Println("MAX xy: ", max_xy)
	fmt.Println("MAX xyz: ", max_xyz)

	//function calling multiple value return
	// Method 1
	x_plus_y, x_multiply_y := SumAndMultiply1(x, y)
	fmt.Println("x+y: ", x_plus_y)
	fmt.Println("x*y: ", x_multiply_y)

	// Method 2
	x_plus_y, x_multiply_y = SumAndMultiply2(x, y)
	fmt.Println("x+y: ", x_plus_y)
	fmt.Println("x*y: ", x_multiply_y)

	// calling variadic function
	square(3, 4, 5, 6)

}

// function declarartion single value return
func max(a, b int) int {
	if a > b {
		return a
	} else {
		return b
	}
}

// Method 1
// function declarartion multiple value return
func SumAndMultiply1(a, b int) (int, int) {
	return a + b, a * b
}

// Method 2
// function declarartion multiple value return
func SumAndMultiply2(a, b int) (sum int, product int) {
	sum = a + b
	product = a * b
	return
}

// Variadic function
// variable no of args
func square(arg ...int) {
	// NOTE:
	// <arg> becomes a slice of int

	// for _, n := range arg {
	// fmt.Printf("And the number is: %d\n", n)
	for i, n := range arg {
		fmt.Printf("index: %d, number: %d\n", i, n)
	}
	fmt.Println()
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 10. functions-2 <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("functions in golang [part: 2]")

	// pass by value
	fmt.Println()
	fmt.Println("-- PASS BY VALUE --")
	x := 3
	fmt.Println("x = ", x)
	x1 := add_value_1(x)
	fmt.Println("x1 = ", x1)
	fmt.Println("x = ", x)

	// pass by reference
	fmt.Println()
	fmt.Println("-- PASS BY REFERENCE [part-1] --")
	y := 3
	fmt.Println("y = ", y)
	y1 := add_by_reference_1(&y)
	fmt.Println("y1 = ", y1)
	fmt.Println("y = ", y)

	// pass by reference
	fmt.Println()
	fmt.Println("-- PASS BY REFERENCE [part-2] --")
	z := 3
	fmt.Println("z = ", z)
	// add_by_reference_2 return pointer

	// here we are passing the address of z
	z1 := add_by_reference_2(&z)
	fmt.Println("z1 [address]= ", z1)
	fmt.Println("z1 [value]= ", *z1)
	fmt.Println("z = ", z)
}

func add_value_1(a int) int {
	a = a + 1
	return a
}

func add_by_reference_1(a *int) int {
	*a = *a + 1
	return *a
}

func add_by_reference_2(a *int) *int {
	*a = *a + 1
	return a
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 11. functions-3 <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("functions in golang [part: 3]")

	// defer in Golang
	// works like STACK [LIFO Rule]
	// defer fmt.Println()
	// for i := 0; i < 5; i++ {
	// 	defer fmt.Printf("%d ", i)
	// }

	// Just run to get to know how this work
	defer func_1()
	defer func_2()
	defer func_3()

	// OUTPUT
	// I am from function 3
	// I am from function 2
	// I am from function 1

}

func func_1() {
	fmt.Println("I am from function 1")
}
func func_2() {
	fmt.Println("I am from function 2")
}
func func_3() {
	fmt.Println("I am from function 3")
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 12. functions-4 <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("functions in golang [part: 4]")

	var natural_number = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
	odd := filter(natural_number, isOdd)
	even := filter(natural_number, isEven)

	fmt.Println("natural no: ", natural_number)
	fmt.Println("Odd: ", odd)
	fmt.Println("Even: ", even)
}

// Definign type of function, so that we can use this type
// while pass function as parameter in other function
type boolFunc func(int) bool

func isEven(integer int) bool {
	return integer%2 == 0
}

func isOdd(integer int) bool {
	return integer%2 != 0
}

// function with parameter as function <func_pass>
func filter(mySlice []int, func_pass boolFunc) []int {
	var result []int
	for _, value := range mySlice {
		if func_pass(value) {
			result = append(result, value)
		}
	}

	return result
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 13. functions-5 <br> </h2></summary>

```go
package main

import "fmt"

func main() {
	fmt.Println("functions in golang [part: 5]")

	a := 10
	b := 0
	safeDivide(a, b)
	fmt.Println("I am after the divide")

}

func safeDivide(a, b int) {
	// using defer as it will run at last
	defer func() {
		r := recover()
		if r != nil {
			fmt.Println(r)
			fmt.Println("Recovered from panic !!")
		}
	}()

	// in case of 0/x will cause PANIC
	fmt.Println(a / b)
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 14. main-init-func <br> </h2></summary>

```go
package main

import "fmt"

// there can be multiple init function
// and it will be executed before main

// usually used in pkg to initialize the variables

func init() {
	fmt.Println("I am the init function, so I will first")
}

func main() {
	fmt.Println()
	fmt.Println("main function and init function")
	fmt.Println("I am the main function")

}
func init() {
	fmt.Println("I am the init function, so I will another first")
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 15. import-in-go <br> </h2></summary>

```go
package main

import (
	"fmt"
	. "fmt"
	f "fmt"

	_ "database/sql"
	// The _ operator actually means we just want to import that package
	// and execute its init function
	// we do not wish to use its other function
)

func main() {
	fmt.Println("Import in Golang")

	// using alias for fmt
	f.Println("I am using f alias for fmt")

	// when using dot (.) notation we can directly call the func
	Println("I am directly using Println without fmt")

}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 16. struct-1 <br> </h2></summary>

```go
package main

import (
	"fmt"
)

// defining the person struct
type person struct {
	name string
	age  int
}

func main() {
	fmt.Println("Struct in Golang [part: 1]")

	// METHOD 1
	// initializing the person struct
	var marcus person

	//setting value to it
	marcus.name = "Marcus"
	marcus.age = 34

	// METHOD 2
	// initializing and setting variable at same time
	vishal := person{
		name: "Vishal",
		age:  22,
	}
	// METHOD 3
	// initializing and setting variable at same time
	ram := person{
		"Ram",
		23,
	}

	fmt.Println(marcus.name, marcus.age)
	fmt.Println(vishal.name, vishal.age)
	fmt.Println(ram.name, ram.age)

	//NOTE
	//defining the anonymous struct and initializing and setting value
	var Person1 = struct {
		firstName string
		lastName  string
	}{firstName: "Munshi", lastName: "Premchand"}

	fmt.Println(Person1.firstName, Person1.lastName)

	// struct as funct param
	p1 := person{"banda1", 23}
	p2 := person{"banda1", 25}

	fmt.Println(Older(p2, p1))
	fmt.Println(Older(p2, p1).name, Older(p2, p1).age)

}

// struct as funct param
func Older(p1, p2 person) person {
	if p1.age > p2.age {
		return p1
	}

	return p2
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 17. struct-2 <br> </h2></summary>

```go
package main

import (
	"fmt"
)

// embedded fields in struct
type Human struct {
	name   string
	age    int
	weight int
}

// all types can be embedded fields
// other struct, string, int, slice
type Student struct {
	// embedded fields in struct
	Human
	speciality string
}

func main() {
	fmt.Println("Struct in Golang [part: 2]")

	// instantiate and initialize a student
	premchand := Student{Human{name: "Munshi Premchand", age: 45, weight: 70}, "writer"}
	// fmt.Println(premchand)
	fmt.Println("Name: ", premchand.name)
	fmt.Println("Age: ", premchand.age)
	fmt.Println("Weight: ", premchand.weight)
	fmt.Println("Speciality: ", premchand.speciality)

	//modifying the data
	fmt.Println()
	fmt.Println("-- After DATA Modification --")
	fmt.Println()
	premchand.speciality = "Novel Writer"
	premchand.weight -= 5
	fmt.Println("Weight: ", premchand.weight)
	fmt.Println("Speciality: ", premchand.speciality)

	//other way to acess embedded data
	fmt.Println()
	fmt.Println("-- Other way to acess embedded data --")
	fmt.Println()
	fmt.Println(premchand.Human.name)
	fmt.Println(premchand.Human.age)
	fmt.Println(premchand.Human.weight)
	fmt.Println(premchand.speciality)
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 18. struct-3 <br> </h2></summary>

```go
package main

import (
	"fmt"
)

type Skills []string

type speciality string

// embedded fields in struct
type Human struct {
	name   string
	age    int
	weight int
}

// all types can be embedded fields
// other struct, string, int, slice
type Student struct {
	// embedded fields in struct
	Human
	Skills
	int
	speciality

	// I have already defined speciality as type
	// so no need to write its <type> explicitly
	// speciality string
}

type Player struct {
	ID string
	Human
	name string
}

func main() {
	fmt.Println("Struct in Golang [part: 3]")

	//Initiate and Initialize the Student named Satya
	satya := Student{Human: Human{name: "Satya Vyas", age: 32, weight: 68}, speciality: "Novel Writer"}
	fmt.Println("Name: ", satya.name)
	// other method to get data
	// fmt.Println("Speciality: ", satya.Human.name)
	fmt.Println("Age: ", satya.age)
	fmt.Println("Weight: ", satya.weight)
	fmt.Println("Speciality: ", satya.speciality)

	//here we have not set int yet, so it default value = 0
	fmt.Println("Int: ", satya.int)

	satya.Skills = []string{"novel", "poem"}
	//appending in the Skills <slice> data-type
	satya.Skills = append(satya.Skills, "stories", "short-stories")
	fmt.Println("Skils: ")
	for _, skill := range satya.Skills {
		fmt.Println("  ", skill)
	}

	satya.int = 1001
	fmt.Println("Int: ", satya.int)

	fmt.Println()
	fmt.Println("-- Priority in Struct --")
	fmt.Println()
	player_1 := Player{ID: "1018", Human: Human{name: "Virat Kohli", age: 35, weight: 68}, name: "Rohit Sharma"}

	fmt.Println("ID: ", player_1.ID)

	//this will get latest value
	//similar to method overloading in OOPS
	fmt.Println("Name: ", player_1.name) //Rohit Sharma
	//this will get exact defined value
	fmt.Println("Name: ", player_1.Human.name) //Virat Kohli
	fmt.Println("Age: ", player_1.age)
	fmt.Println("Weight: ", player_1.weight)
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 19. object-oriented-1 <br> </h2></summary>

```go
package main

import (
	"fmt"
	"math"
)

type Circle struct {
	radius float64
}

type Rectangle struct {
	length float64
	width  float64
}

func main() {
	fmt.Println("Object-oriented in Golang [part: 1]")
	// c1 := Circle{radius: 7}
	c1 := Circle{7}
	// r1 := Rectangle{length: 5, width: 7}
	r1 := Rectangle{5, 7}

	// using normal function
	fmt.Println("Area of circle [normal func]: ", area(c1))
	// using method
	fmt.Println("Area of circle [method]: ", c1.Area())

	fmt.Println("Area of rectangle [method]: ", r1.Area())

}

// normal func with struct as param
func area(c Circle) float64 {
	return c.radius * c.radius * math.Pi
}

//now its time for method
//my dear method, welcome hai apka

// SYNTAX
// func (r recieveType) funcName(param) returnType
func (c Circle) Area() float64 {
	return c.radius * c.radius * math.Pi
}

func (r Rectangle) Area() float64 {
	return r.length * r.width
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 20. object-oriented-2 <br> </h2></summary>

```go
package main

import (
	"fmt"
	"reflect"
)

const (
	WHITE  = iota // index --> 0
	BLACK         // 1
	BLUE          // 2
	RED           // 3
	YELLOW        // 4
)

type Color byte

type Box struct {
	width, height, depth float64

	// color variable of type Color, which is type of <byte>
	color Color
}

// slice of type Box
type BoxList []Box

// method to calc valume
func (b Box) Volume() float64 {
	return b.width * b.height * b.depth
}

// method with pointer receiver
// by default it passes by value
// so a copy of Box will pass, but to change color of Box, we need
// pointer pointing to Box itself not to copy of Box
func (b *Box) setColor(c Color) {
	b.color = c
}

// method
// to get Biggest Box by Volume
func (bl BoxList) BiggestsColor() Color {
	v := 0.00
	var k Color
	for _, box := range bl {
		if box.Volume() > v {
			v = box.Volume()
			k = box.color
		}
	}

	return k
}

// method
// to color all black
func (bl BoxList) paintItBlack() {
	for i, value := range bl {
		fmt.Println("set color: ", value)
		bl[i].setColor(BLACK)
	}

	// NOTE:
	// this will not work as box is just copy passed via BoxList
	// so it is actually changing color of that copy
	// we have to use <bl[index].setColor>

	// for _, box := range bl {
	// 	fmt.Println("set color: ", box)
	// 	box.setColor(BLACK)
	// }
}

// method
// even I don't understand whats going on
// trying to figure out :)
// I figured it out by playing with similar code
// check 1. variables [for more detail info]
func (c Color) String() string {
	StringSlice := []string{"WHITE", "BLACK", "BLUE", "RED", "YELLOW"}
	// just for quick, it <c> is acting as index
	return StringSlice[c]
}

func main() {
	fmt.Println("Object-oriented in Golang [part: 2]")

	boxes := BoxList{
		Box{4, 4, 4, RED},
		Box{10, 10, 10, YELLOW},
		Box{1, 1, 20, BLACK},
		Box{10, 10, 1, BLUE},
		Box{10, 30, 1, WHITE},
	}

	fmt.Println("Total boxes: ", len(boxes))
	fmt.Println("Volume[0]: ", boxes[0].Volume())
	fmt.Println("Volume[last]: ", boxes[len(boxes)-1].Volume())

	fmt.Println("Biggest [type]: ", reflect.TypeOf(boxes.BiggestsColor().String()))
	fmt.Println("Biggest [value]: ", boxes.BiggestsColor().String())
	fmt.Println()
	fmt.Println("Bigges [type]: ", reflect.TypeOf(boxes.BiggestsColor()))
	fmt.Println("Biggest [value]: ", boxes.BiggestsColor())

	// lets point it all black
	boxes.paintItBlack()
	fmt.Println()
	fmt.Println("After painting it black")
	fmt.Println("Boxes[0] [value]: ", boxes[0].color.String())
	fmt.Println("Biggest [value]: ", boxes.BiggestsColor().String())

	// fmt.Println(boxes.BiggestsColor().String())
	// fmt.Println(boxes[0].color.String())

}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 21. object-oriented-3 <br> </h2></summary>

```go
package main

import (
	"fmt"
)

type Human struct {
	name  string
	age   int
	phone string
}

type Student struct {
	Human
	school string
}

type Employee struct {
	Human
	company string
}

func main() {
	fmt.Println("Object-oriented in Golang [part: 3]")

	// Inheritance of method
	// method inheritance is similar to inheritance of fields of struct
	// here sayHi() is method belog to Human
	// so it is acessible by both Student & Employee
	sam := Employee{Human: Human{"Sam", 34, "6235475253"}, company: "TCS Ninja"}
	premchand := Student{Human: Human{"Munshi Premchand", 65, "53532646328"}, school: "ABC  school"}

	sam.sayHi()
	premchand.sayHi()
	fmt.Println(sam.company)
	fmt.Println(premchand.school)
}

// method in Human
// we are using pointer as it does not make copy
// which is good for memory :)
func (h *Human) sayHi() {
	// func (h Human) sayHi() {
	fmt.Printf("Hi, I am %s\n", h.name)
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 22. object-oriented-4 <br> </h2></summary>

```go
package main

import (
	"fmt"
)

type Human struct {
	name  string
	age   int
	phone string
}

type Student struct {
	Human
	school string
}

type Employee struct {
	Human
	company string
}

func main() {
	fmt.Println("Object-oriented in Golang [part: 3]")

	// Method Overriding
	macson := Human{name: "Mark Manson", age: 35, phone: "8746853468"}
	sam := Employee{Human: Human{"Sam", 34, "6235475253"}, company: "TCS Ninja"}
	premchand := Student{Human: Human{"Munshi Premchand", 65, "53532646328"}, school: "XYZ Vidyalaya"}

	// sayHi() of Human
	macson.sayHi()
	// sayHi() of Employee
	sam.sayHi()
	// sayHi() of Student
	premchand.sayHi()
}

// method in Human
// we are using pointer as it does not make copy
// which is good for memory :)
func (h *Human) sayHi() {
	// func (h Human) sayHi() {
	fmt.Printf("Hi, I am %s\n", h.name)
}

// Overriding sayHi() func for Employee
func (e *Employee) sayHi() {
	fmt.Printf("Hi, I am %s, I work at %s\n", e.name, e.company)
}

// Overriding sayHi() func for Student
func (s *Student) sayHi() {
	fmt.Printf("Hi, I am %s, I study at %s\n", s.name, s.school)
}

// LOL I completed this section <object-oriented> in Golang 👍
```
</details>


<details close>
<summary><h2 style="display: inline;"> 23. interface-1 <br> </h2></summary>

```go
package main

// https://youtu.be/SX1gT5A9H-U?si=-spXnjKKcIjS5qYI

import (
	"fmt"
	"math"
)

// a method is essentially a function associated with an object (or struct, in some languages),
// and it implicitly takes the instance of that object (known as the receiver) as its first parameter.

// In Go, an interface is a type that specifies a set of method signatures, without implementing them.
// Any type that implements all methods in an interface's method set is considered to satisfy that interface.
// Interfaces allow Go to achieve polymorphism

// NOTE:
// In Go, a type automatically satisfies an interface if it has all the methods in the interface.
// There’s no need to explicitly declare that a type implements an interface.
type Shape interface {
	// only func definition
	// without implementation
	// basically function prototyping just like C
	Area() float64
}

type Rectange struct {
	width, height float64
}

type Circle struct {
	radius float64
}

// For Rectangle to satisfy the Shape interface, it needs to implement the methods Area()
// with the same signatures as in the interface.
func (r Rectange) Area() float64 {
	return r.width * r.height
}

// For Circle to satisfy the Shape interface, it needs to implement the methods Area()
// with the same signatures as in the interface.
func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

// This allows the function to handle any type that implements Shape without knowing the specifics of Rectangle or Circle
func calculateArea(s Shape) float64 {
	return s.Area()
}
func main() {
	fmt.Println("Interface in Golang [part: 1]")

	rect1 := Rectange{5, 4}
	cir1 := Circle{2}

	//normal method calling
	fmt.Println("Area of Rectangle: ", rect1.Area())
	fmt.Println("Area of Circle: ", cir1.Area())

	// using interface
	fmt.Println("Area of Rectangle: ", calculateArea(rect1))
	fmt.Println("Area of Circle: ", calculateArea(cir1))
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 24. interface-2 <br> </h2></summary>

```go
package main

import (
	"fmt"
	"math"
)

// NOTE:
// In Go, a type automatically satisfies an interface if it has all the methods in the interface.
// There’s no need to explicitly declare that a type implements an interface.
type Shape interface {
	//declaring method for interface

	// now any func with same signature i.e Area or Perimeter will be linked with Shape Interface automatically
	Area() float64
	Perimeter() float64
}

type Rectange struct {
	width, height float64
}

type Circle struct {
	radius float64
}

func (r Rectange) Area() float64 {
	return r.width * r.height
}

func (c Circle) Area() float64 {
	return math.Pi * c.radius * c.radius
}

func (r Rectange) Perimeter() float64 {
	return 2 * (r.height + r.width)
}

// If I delete this Perimeter method for circle, then it will not implement the Shape interface
// In order to implement shape interface correctly, one have to defined all method declared in interface as method of that type
// Here type is <struct> :)

func (c Circle) Perimeter() float64 {
	return 2 * math.Pi * c.radius
}

func calculateArea(s Shape) float64 {
	return s.Area()
}

func calculatePerimeter(s Shape) float64 {
	return s.Perimeter()
}
func main() {
	fmt.Println("Interface in Golang [part: 2] [implementing and twiking]")

	rect1 := Rectange{5, 4}
	cir1 := Circle{2}

	fmt.Println("Reactangle: ")
	fmt.Printf("Area: %v, Perimeter: %v\n", calculateArea(rect1), calculatePerimeter(rect1))
	fmt.Println("Circle: ")
	fmt.Printf("Area: %v, Perimeter: %v\n", calculateArea(cir1), calculatePerimeter(cir1))

}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 25. interface-3 <br> </h2></summary>

```go
package main

import (
	"fmt"
)

// NOTE:
// In Go, a type automatically satisfies an interface if it has all the methods in the interface.
// There’s no need to explicitly declare that a type implements an interface.

type Human struct {
	name  string
	age   int
	phone string
}

type Student struct {
	Human
	school string
	loan   float64
}

type Employee struct {
	Human
	company string
	money   float64
}

// defining interface
type Men interface {
	sayHi()
	singSong(lyrics string)
	Guzzle(beerGlass string)
}

type YoungChap interface {
	sayHi()
	singSong(lyrics string)
	borrowMoney(amount float64)
}

type ElderlyGent interface {
	sayHi()
	singSong(lyrics string)
	spendMoney(amount float64)
}

// NOTE: To satisfy an interface, a type must implement all methods required by the interface.

// implementihg Men interface's method sayHi()
func (h *Human) sayHi() {
	fmt.Printf("Hi, I am %s, my contact: %s\n", h.name, h.phone)
}

// implementihg Men interface's method singSong()
func (h *Human) singSong(lyrics string) {
	fmt.Println("singing.., ", lyrics)
}

// implementihg Men interface's method Guzzle()
func (h *Human) Guzzle(beerGlass string) {
	fmt.Println("Guzzle......", beerGlass)
}

// overriding the sayHi() for employee
func (e *Employee) sayHi() {
	fmt.Printf("Hi, I am %s, my contact: %s, I work at: %s\n", e.name, e.phone, e.company)
}

// implementihg YoungChap interface's method spendMoney()
func (s *Student) borrowMoney(amount float64) {
	s.loan += amount
}

// implementihg ElderlyGent interface's method borrowMoney()
func (e *Employee) spendMoney(amount float64) {
	e.money += amount
}

func main() {
	fmt.Println("Interface in Golang [part: 3] [some more exploration]")

	mike := Student{Human{"Mike", 25, "222-222-XXX"}, "MIT", 0.00}
	sam := Employee{Human{"Sam", 36, "444-222-XXX"}, "Golang Inc.", 1000}

	// a can store Student

	// a := mike
	// b := sam
	// a := &mike
	// a.sayHi()

	fmt.Println(mike.loan)
	StudentsMethodCall(&mike)
	fmt.Println(mike.loan)

	fmt.Println(sam.money)
	EmployeeMethodCall(&sam)
	fmt.Println(sam.money)

	// slice of Men
	// Human type implement all method of <Men> interface
	// so Human <type> can all interface property
	mark := Human{name: "Mark Manson", age: 34, phone: "23458923"}

	// Student type implement all method of <Men> interface
	// i.e. sayHi() & singSong()
	// also implement other method i.e. borrowMoney(), but for Men interface, first 2 method are enough to satisfy
	premchand := Student{Human: Human{name: "Munshi Premchand", age: 34, phone: "56348990"}, school: "Prathmik vidyalaya", loan: 67.8008}

	menList := make([]Men, 2)
	menList[0] = &mark
	menList[0] = &premchand
	// menList[1] = &mark
	// menList[1] = &premchand
	// menList[1] = &premchand

	for _, value := range menList {
		value.sayHi()
	}

	// ALTERNATE METHOD
	// for i := range menList {
	// 	menList[i].sayHi()
	// }
}

// here we are calling all method of YoungChap
// which is link to Student type
// as Student satisfies all the method of YoungChap interface
func StudentsMethodCall(y YoungChap) {
	y.sayHi()
	y.borrowMoney(100)
}

func EmployeeMethodCall(e ElderlyGent) {
	e.sayHi()
	e.spendMoney(1000)
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> 26. interface-4 <br> </h2></summary>

```go
package main

import "fmt"

// empty interface --> which can store any data type
type Element interface{}

func main() {
	fmt.Println("Interface in Golang [part: 4] [Homogeneous type Slice]")

	// here we are going to implement slice of any data type using <empty> interface
	// declaring slice of initial length 4
	myHomogeneouSlice := make([]Element, 4)
	myHomogeneouSlice[0] = 23 //int
	myHomogeneouSlice[1] = "This is String"
	myHomogeneouSlice[2] = 2234.45 //float
	myHomogeneouSlice[3] = []int{45, 67, 78}

	// cannot use mymyHomogeneouSlice[4] --> out of bound error
	myHomogeneouSlice = append(myHomogeneouSlice, 100)
	myHomogeneouSlice = append(myHomogeneouSlice, "Oh Yeah, I am string too")

	fmt.Println()
	fmt.Println(myHomogeneouSlice)
	fmt.Println()
	for _, value := range myHomogeneouSlice {
		fmt.Println(value)
	}
}
```
</details>


<details close>
<summary><h2 style="display: inline;"> __playground <br> </h2></summary>

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Golang Playground")
}
```
</details>

