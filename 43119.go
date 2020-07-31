package main

import (
    "fmt"
)

func pop(stack []int) (int, []int){
    lastIndex := len(stack) -1
    return stack[lastIndex], stack[:lastIndex]
}

func main(){
    var input string
    _, err := fmt.Scanln(&input);
    if err != nil {
        panic(err)
    }

    cSet := map[int32]int{
        '(': 0,
        '[': 1,
        '{': 2,
        ')': 3,
        ']': 4,
        '}': 5,
    }

    var order []int

    var this int
    for _, char := range input {
        if cSet[char] < 3{
            order = append(order, cSet[char])
        } else {
            if len(order) == 0{
                fmt.Printf("False")
                return
            }

            this, order = pop(order)

            if this != (cSet[char] - 3){
                fmt.Printf("False")
                return
            }
        }
    }

    if len(order) != 0{
        fmt.Printf("False")
        return
    }

    fmt.Printf("True")
}