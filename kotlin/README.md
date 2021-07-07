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
## Uma Amostra inicial de Kotlin:
<img src="/kotlin/assets/classe.PNG" alt="drawing" width="440"/>

## Variaveis:
Em Java, iniciamos uma declaração de variável com um tipo. Isso não funcionaria em Kotlin porque você pode omitir os tipos de muitas declarações de veriaveis. Portanto, em Kotlin, devemos começar com uma palavra reservada, e voce pode (ou não) colocar o tipo depois do nome da variável.
```kotlin
var x = 1 //general variable, assigned multiple times.
val y = 2 //(final) immutable , is same as the final modifier in java
val s: String = null //pode ser null
val s2: String = "" // Não pode ser null
val multLine = """|  /
		  | /
                  |/ \ """
```
## Funções:
Toda variável e toda expressão tem um tipo, e toda função tem um tipo de retorno. Porém, para funções com corpo de expressão, o compilador é capaz de analisar a expressão usada como corpo da função e utilizar seu tipo como o tipo de retorno da função, mesmo quando ele não for digitado explicitamente. Esse tipo de análise geralmente é chamado de inferência de tipo (type inference)

<p align="center">
  <img src="/kotlin/assets/funcoes.PNG" alt="drawing" width="400"/>
</p>

```kotlin
fun sayHello (greeting:String, ItemToGreet:String) = println ("Hello $itemToGreet")
```

Quando chamamos uma função para criar uma lista, podemos passar qualquer quantidade de argumentos nela:
```kotlin
val list = listOf(2, 4, 6, 8)

fun listOf<T>(vararg values: T) List<T> {....}
```

*Funções Locais*: são utilizadas para diminuir repetição de código e deixar mais  limpo a contrução
```kotlin
fun savePerson(person: Person ) {
    // funcao dentro de funcao
    fun validate (person: Person ,
                 value: String,
                 fieldName: String){
        		if (value.isEmpty()){
                    throw IllegalArgumentException("Nao pode salver ${person.id}: empty $fieldName")
                	}
    }
}
```

## Classes

### Classes de dados:
Classe de repositório de dados, com implementação dos metodos: toString, equals e hashCode. 
```kotlin
data class User(val name: String, val age: Int)
```

### Classes abertas com metodos abertos:
```kotlin
// Classe aberta, outra clases podem herdar dela
open class Button : Clickable {
    fun disable() {
        // função é final, não é possivel sobrescrevê-la em uma subclasse.
    }
    open fun animate() {
        // função é aberta, pode ser sobrescrita
    }
    override fun click(){
        // essa função sobrescreve uma função aberta
    }
}
```

### Classes aninhadas
Uma classe aninhada em Kotlin sem modificadores explicitos é iugual auma classe aninhada static em Java. Utilize o modificador inner para transformar uma classe em interna de modo a ela contenha uma referência a uma classe externa.
```kotlin
class Outer {
    private val bar: Int = 1
    inner class Inner {
        fun foo() = bar
    }
}

val demo = Outer().Inner().foo() // == 1
```

### Declaração de objeto (Singleton)

É comum em designe de sistemas orientados a objetos uma classe para a qual precisamos somente uma instância. Em Java, geralmente ela é implmentada como o padrão Singleton (private com campo estático para armazenar apenas uma instância)
Em Kotlin, a declaração objeto prove uma implementação para uma única instância de classe.
```kotlin
object DataProviderManager {
    fun registerDataProvider(provider: DataProvider) {
        // ...
    }

    val allDataProviders: Collection<DataProvider>
        get() = // ...
}
```

### Modificadores de classes:
| Modificador | Membro correspondente                                     | Descrição                                                                                      |
|-------------|-----------------------------------------------------------|------------------------------------------------------------------------------------------------|
| final       | Não pode ser sobrescrito                                  | Default para membros da classe                                                                 |
| open        | Pode ser sobrescrito                                      | Deve ser especificado explicitamente                                                           |
| abstract    | Deve ser sobrescriito                                     | Pode ser usado apenas em classes abstratas; membros abastratos não podem ter uma implementação |
| override    | Sobreve um membro de uma superclasse ou de uma interface  | O membro sobrescrito é aberto por padrão caso não esteja marcado com final                     |

### Modoficador de visibilidade em Kotlin
| Modificador       | Membro da classe (Visível)  | Declaração de nível superior (Visível) |
|-------------------|-----------------------------|----------------------------------------|
| public (default)  | todos os lugares            | todos os lugares                       |
| internal          | módulo                      | módulo                                 |
| protected         | subclasses                  | ---                                    |
| private           | uma classe                  | um arquivo                             |

## Tipo nullable
Tipo nullable (Int?); o valor default para o argumento:
```kotlin
val age: Int? = null
```

## Operador Elvis
O operador Elvis (?:) devolve zero se age for null.:
```kotlin
pessoas.map { it.age ?: 0 + 2}
```

## @JvmName
Para mudar o nome da classe gerada contendo as funções de nível superior de kotlin, adione a anaotação @JvmName ao arquivo.
```kotlin
@file:JvmName("MotorCalculo")
package motor
fun calcular(...): String {...}

```
## enum 
• Esse é um caso raro onde uma declaração em Kotlin usa mais palavras chave do que o correspondente em Java: *enum class* vs somente *enum* <br>
• Em Kotlin, *enum* é chamado de soft-keyword <br>
• Significado especial quando ela vem antes de *class*, mas podemos usá-la como um nome regular em outros lugares (*val* enum = "abc") <br>
• Assim como em Java, enums não são lista de valores: podemos declarar propriedades e métodos em classes Enum 
```kotlin
enum class Color(
	val r: Int, val g: Int, val b:Int
){
    RED(255, 0, 0), ORANGE(255, 165, 0),
    YELLOW(255, 255, 0), GREEN(0, 255, 0), BLUE(0, 0, 255),
    INDIGO(75, 0, 130), VIOLET(238, 130, 238);
    
    fun rgb() = (r * 256 + g) * 256 + b
}
```
## when
• *when* é um substituto do switch do Java <br>
• Porém mais poderoso e é usado mais frequentemente <br>
• *when* é uma expressão que retorna um valor (corpo de expressão), assim como o *if*. <br>
• Não precisamos escrever afirmações *break* em cada branch, como em Java <br>
• Podemos também combinar múltiplos valores no mesmo branch separando por vírgulas
```kotlin
fun obterTemperatura(cor: Color): String {
    return when(cor){
        Color.RED, Color.ORANGE, Color.YELLOW -> "Quente"
        Color.GREEN -> "Neutro"
        Color.BLUE -> "Frio"
    }
}
```
A biblioteca padrão de Kotlin contém uma função *setOf* que cria um *Set* contendo os objetos especificados como seus argumentos. Um conjunto (set) é uma coleção na qual a ordem dos itens não importa; dois conjuntos são iguais se contivertem os mesmo itens. Assim, se os conjuntos *setOf(c1, c2)* e *setOf(RED, YELLOW)* forem iguais, é sinal de que c1 é RED e c2 é YELLOW ou vice-versa.
```kotlin
fun mix (c1: Color, c2: Color) = 
    when (setOf(c1, c2)) {
        setOf(Color.RED, Color.YELLOW) -> Color.ORANGE
        setOf(Color.YELLOW, Color.BLUE) -> Color.GREEN
        else -> throw Exception("Dirty color")
        
    }
```
Para testes do *enum* e *when*
```kotlin
fun main() {
var temp  = obterTemperatura(Color.RED)
println(temp)
var mistura  = mix(Color.RED, Color.YELLOW)
println(mistura)
}
```
## For
Podemos usar a mesma sintaxe de desempacotamento para iterar por uma coleção, ao mesmo tempo que controlamos o índice do item atual. Não é necessario criar uma variável apartada.
```kotlin
fun main()  {
val list = arrayListOf("10", "11", "1001")

for (element in list){
    println("$element")
}

for ((index, element) in list.withIndex()){
    println("$index: $element")
}
  /* 10
   * 11
   * 1001
   * 0: 10
   * 1: 11
   * 2: 1001
   */
}
```
## Interfases
Interfaces contém definições de métodos abstratos e implementações de métodos não abstratos, mas não podem conter estados. Usamos a declaração abaixo para exemplificar a utilização de uma interfase em Kotlin. Usamos o modificador override para sobrescrever um método, de forma semelhante em JAVA.

```kotlin
interface Clickble {
    fun click()
}

class Button : Clickble{
    override fun click() = println("I was clicked")
}

fun main (){
    val b= Button()
    b.click()
}
```

## Programação com lambdas:

Expressões lambda são pequenos trechos de código que podem ser passadas para outras funções. Tem como obejtivo facilitar a estrutura de código comum em funções de bibliotecas, diminuindo a complexidade de leitura e reuso de código.

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
## Data Structure:
<p align="center">
  <img src="/kotlin/assets/data-structure.png" alt="drawing" width="600"/>
</p>

```kotlin
fun main()  {
    
// Array List
// dimensionado dinamicamente, com elementos sejam acessados diretamente.
// Quando um elemento é adicionado, ele é colocado na matriz. Se o array não
//  for grande o suficiente, um novo array maior é criado para substituir o
//  antigo e o antigo é removido.
val list = arrayListOf(1,1,2,3,5,8)

// Linked List
// A lista possui um link para o primeiro container e cada container possui 
// um link para o próximo container na lista. 
val list = ListOf(1,1,2,3,5,8)

//Hash Set
// é uma coleção de itens onde cada item é único
val hash = hashSetOf(3,4,5)

// Hash Map
// armazene itens em pares "chave / valor", e você pode acessá-los por um índice de outro tipo
val map = hashMapOf(1 to "um", 2 to "dois", 3 to "tres")

}
```