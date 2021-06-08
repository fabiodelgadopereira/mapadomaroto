# Kotlin

Kotlin online: https://play.kotlinlang.org 

## Compilação:
```bash
kotlinc <arquivo-fonte-ou-diretorio> -include-runtime -d <nome-do-jar>
java -jar <nome-do-jar>
}
```
## Exemplo básico
```kotlin
fun main(){ 
  println("Coding is fun!")
}
```
Uma Amostra inicial de Kotlin
![amostra de classe](/kotlin/assets/classe.PNG)
## Variaveis:
Em Java, iniciamos uma declaração de variável com um tipo. Isso não funcionaria em Kotlin porque você pode omitir os tipos de muitas declarações de veriaveis. Portanto, em Kotlin, devemos começar com uma palavra reservada, e voce pode (ou não) colocar o tipo depois do nome da variável.
```kotlin
var x = 1 //general variable, assigned multiple times.
val y = 2 //(final) immutable , is same as the final modifier in java
val s: String = null //pode ser null
val s2: String = "" // Não pode ser null
```
## Funções:
Toda variável e toda expressão tem um tipo, e toda função tem um tipo de retorno. Porém, para funções com corpo de expressão, o compilador é capaz de analisar a expressão usada como corpo da função e utilizar seu tipo como o tipo de retorno da função, mesmo quando ele não for digitado explicitamente. Esse tipo de análise geralmente é chamado de inferência de tipo (type inference)

![amostra de classe](/kotlin/assets/funcoes.PNG)

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