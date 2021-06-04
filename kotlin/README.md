# Kotlin

Kotlin online: https://play.kotlinlang.org 


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
Function:
```kotlin
fun sayHello (greeting:String, ItemToGreet:String) = println ("Hello $itemToGreet")
```
Data Classes: Não é necessario implementar metodos get() e set()
```kotlin
data class User(val name: String, val age: Int)
```
Tipo nullable (Int?); o valor default para o argumento:
```kotlin
val age: Int? = null
```
O operador Elvis (?:) devolve zero se age for null.:
```kotlin
pessoas.map { it.age ?: 0 + 2}
```
Colletions:
```kotlin
internal object Solution {
    @Throws(Exception::class)
    @JvmStatic
    fun main(args: Array<String>) {

        val pessoas = listOf(Person("Paul", 24),
                Person("Mark", 30),
                Person("Will", 28),
                Person("William", 28))

        // forEach
        // imprimir todos os nomes da lista
        pessoas.forEach { p: Person -> println(p.name) }

        // map
        // soma 2 em um array de numeros e imprime
        println( pessoas.map { it.age + 2} )

        // filter
        // filtra apenas pessoas com idade maior que 25 anos
        println(pessoas.filter { p: Person -> p.age > 25 })

        // operações que percorrem o array completo
        var sum = 0
        pessoas.map {
            sum += it.age
        }
        println(sum)

        // sorted
        //ordenar pelo atributo da classe
        println(pessoas.sortedBy { it.age })

        // Group by
        // agregar uma única propriedade dos elementos ou apenas contar o número de elementos por grupo
        println(pessoas.groupBy { it.age })

        // minByOrNull
        // retorna o menor valor do vetor
        println(pessoas.minByOrNull { it.age })

        // minByOrNull
        // retorna o menor valor do vetor
        println(pessoas.maxByOrNull { it.age })

        // all (allMatch)
        //Retorna true se todos os elementos do fluxo correspondem ao predicado fornecido
        println(pessoas.all { p: Person -> p.age > 20 })

        // any (anyMatch)
        // Retorna true se qualquer um dos elementos do fluxo corresponde ao predicado fornecido
        println(pessoas.any { p: Person -> p.age > 20 })

        // none (noneMatch)
        // Retorna true se nenhum dos elementos do fluxo corresponde ao predicado fornecido.
        println(pessoas.none { p: Person -> p.age > 20 })

       // println(pessoas.max())

    }
}

data class Person(val name: String, val age: Int)
```
Exemplo livro:
```kotlin
data class Person(val name: String, val age: Int?=null)

fun main (args: Array<String>){
    
    val persons = listOf(Person("Alice"),
                        Person("Bob",age = 29))
    
    val oldest = persons.maxByOrNull({ it.age ?: 0 }) 
    
    println("The oldest is $oldest")
}
```