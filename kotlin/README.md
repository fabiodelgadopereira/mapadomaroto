# Kotlin

Exemplo básico
```kotlin
fun main(){ 
  println("Coding is fun!")
}
```
Variaveis:
```kotlin
var x = 1 //general variable, assigned multiple times.
val y = 2 //immutable , is same as the final modifier in java
```
Function":
```kotlin
fun sayHello (greeting:String, ItemToGreet:String) = println ("Hello $itemToGreet")
```
Data Classes: purpose is to hold data
`equals()`/ `hashCode()` pair

`toString()` of the form "User(name=John, age=42)"

`componentN()` functions corresponding to the properties in their order of declaration.

`copy()` function (see below).
```kotlin
data class User(val name: String, val age: Int)
```


