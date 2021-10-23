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
Exemplo de metodo
```kotlin
fun isValid (obj : Any?): Boolean {
    
    if (obj == null ) return false // valida se eh nullo
	if (obj !is String) return false // valida se eh String
	if (obj.equals("No")) return false // condicao de valor indesejado
    
    return true
}
```

## Operador de chamada segura: `?.`
O operador de chamada segura (sefe-call operator) ?., que permite combinar a verificação de null com uma chamada de método em uma única operação.

```kotlin
// Permitite verifica nulidade
fruta?.toUpperCase()

// Eh equivalente a:
if(fruta != null) fruta.toUpperCase() else null
```

## cast seguro para implementar equals
O operador de cast seguro tenta fazer cast de um valor para um dado tipo e devolve null se o tipo for diferente.
```kotlin
fun isNumber(entrada: Any?): Boolean { 
    val other = entrada as? Integer ?: return false 
    return true    
}
```

## Asserções de não null: `!!`
Ao usar uma asserção de não null, podemos lançar explicitamente uma exceção se o valor for null
```kotlin
fun ignoreNulls( value : String? ){
    val isNotNull: String = value!!
    print(isNotNull.length)
}
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
Kotlin permite passar lambda fora de parenteses as funções e referências um parâmetro único da lambda como `it`.
Podemos criar referências a métodos, construtores e propriedades  prefixando o nome da função com ` :: ` e passar essas referências a funções em vez de lambdas

```kotlin
internal object Solution {
    @Throws(Exception::class)
    @JvmStatic
    fun main(args: Array<String>) {

        val pessoas = listOf(Person("Paul", 24),
                Person("Mark", 30),
                Person("Will", 28),
                Person("William", 28))

        //Lista apenas com nomes de pessoas
        //Mais informações em métodos Eager e Lazy
        pessoas.map(Person::name)

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

        //startsWith
        //pesquisa nomes que comecam com a letra P
        println(pessoas.filter{it.name.startsWith("P")}.toList())

        //flatMap
        // Duas funcoes: transforma (ou mapeia) cada elemento para uma colecao de acordo com a funcao
        // dada como argumento e em seguida combina (serealiza) varias listas em uma so
        val livros = listOf(Livro("Piano Mecanico", listOf("Kurt Vonnegut")),
                       Livro("Va e venca", listOf("Paulo Storani")),
                       Livro("Darwin sem frescura", listOf("Pirula","Reinaldo Jose Lopes")))
    
       println(livros.flatMap{it.autores}.toSet())
       //resultado [Kurt Vonnegut, Paulo Storani, Pirula, Reinaldo Jose Lopes]

    }
}

data class Person(val name: String, val age: Int)
data class Livro(val titulo: String, val autores: List<String>)
```
## Operação lazy em coleções: sequencias
A avaliação eager executa cada operação em toda a coleção; a avaliação lazy processa os elementos um a um.

```kotlin
fun main() {
    
    val pessoas = listOf(Person("Paul", 24),
                Person("Mark", 30),
                Person("Will", 28),
                Person("William", 28))
    
    // Eager (ávido)
    pessoas.map(Person::name).filter{it.startsWith("P")}
    
    // Lazy (preguiçoso)
    pessoas.asSequence().map(Person::name).filter{it.startsWith("P")}.toList()
    
}
data class Person(val name: String, val age: Int)
```
## With
A função with converte seu primeiro argumento em um receptor da lambda passada como o segundo argumento. Podemos acessar esse receptor por meio de uma referencia this. Essa instrução pode ser usada para executar diversas operaçoes no mesmo objeto sem repetir seu nome
```kotlin
fun main() {

    // uso comum
    fun alphabet(): String {
        val result = StringBuilder()
        for (letter in 'A'..'Z'){
            result.append(letter)
        }
        return result.toString()
    }

    //uso com with para gerar o alfabeto
    fun alphabet2() : String {
        val stringBuilder = StringBuilder()
        return with(stringBuilder){
         for (letter in 'A'..'Z'){
                this.append(letter)
            }
         this.toString()
        }
    }

    //uso com with em um corpo de expressão para gerar o alfabeto
    fun alphabet3() = with(StringBuilder()){
         for (letter in 'A'..'Z'){
                append(letter)
        }
        toString()
    }
}
```
## Apply
A função apply fuciona quase do mesmo modo que with, a única diferença é que apply devolve o objeto passado para ele como argumento (em outras palavras, o objeto receptor)_
```kotlin
fun main() {

    //uso com apply
    fun alphabet() = StringBuilder().apply{
         for (letter in 'A'..'Z'){
                append(letter)
        }
    }.toString()
}
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
## Serialização de JSON
Solução leve que utiliza kotlin puro.
build.gradle.kts
```kotlin
plugins {
    `java-library`
}
repositories {
    mavenCentral()
    jcenter()
}
dependencies {
    // https://mvnrepository.com/artifact/com.beust/klaxon
    implementation("com.beust:klaxon:4.0.2")
}

```

```kotlin
package sample

import com.beust.klaxon.Klaxon

fun main() {

        val student = Klaxon()
            .parse < Person > (""" 
                {
                    "name": "John Smith",
                    "age": 23
                }
                """)

                print(student?.name)
            }
class Person(val name: String, val age: Int)
```
## JetBrains / Exposed & sqlserver

Exposed é uma biblioteca de código aberto (licença Apache) desenvolvida pela JetBrains, que fornece uma API Kotlin idiomática para algumas implementações de banco de dados relacional, ao mesmo tempo que elimina as diferenças entre os fornecedores de banco de dados.

pom.xml
```xml
        <dependency>
            <groupId>org.jetbrains.exposed</groupId>
            <artifactId>exposed-core</artifactId>
            <version>0.35.1</version>
        </dependency>
        <dependency>
            <groupId>org.jetbrains.exposed</groupId>
            <artifactId>exposed-jdbc</artifactId>
            <version>0.35.3</version>
            <scope>runtime</scope>
        </dependency>
        <dependency>
            <groupId>com.microsoft.sqlserver</groupId>
            <artifactId>mssql-jdbc</artifactId>
            <version>6.4.0.jre7</version>
        </dependency>
```
Exemplo de implementação
```kotlin
import org.jetbrains.exposed.sql.Database
import org.jetbrains.exposed.sql.transactions.TransactionManager
import org.jetbrains.exposed.sql.transactions.transaction

fun main() {
    Database.connect("jdbc:sqlserver://localhost:32768;databaseName=test", "com.microsoft.sqlserver.jdbc.SQLServerDriver", 
                 user = "root", password = "your_pwd") 

    transaction {
        TransactionManager.current().exec("select @@version") { it.next(); print(it.getString(1)) }
    }
}
```
