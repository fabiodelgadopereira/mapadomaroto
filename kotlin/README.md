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
Data Classes: Não é necessario implementar metodos get() e set()
```kotlin
data class User(val name: String, val age: Int)
```
Funções lambda:
```kotlin
import java.util.*
import java.util.stream.Stream

internal object Solution {
    @Throws(Exception::class)
    @JvmStatic
    fun main(args: Array<String>) {

        val numeros = Arrays.asList(1, 2, 3, 5, 8, 13, 21, 34)

        // soma 2 em um array de numeros e imprime
        numeros.stream().map { c: Int -> c + 2 }.forEach { x: Int? ->
            println(
                x
            )
        }
        val pessoas = Stream.of(
            Person("Paul", 24, 20000),
            Person("Mark", 30, 30000),
            Person("Will", 28, 28000),
            Person("William", 28, 28000)
        )

        // imprimir todos os nomes da lista
        pessoas.forEach { p: Person -> println(p.name) }

        // filtra apenas pessoas com idade maior que 28 anos
        pessoas.filter { p: Person -> p.age > 28 }

        // Transformar idades em um stream de idades
        val pontos = pessoas.mapToInt { c: Person -> c.age }
    }
}

internal class Person(val name: String, val age: Int, private val salary: Long)
```