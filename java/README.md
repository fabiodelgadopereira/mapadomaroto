# Java

Exemplo básico
```java
class Solution{
	public static void main(String args[] ) throws Exception {  
		System.out.println("teste");
	}
}
```
Funções lambda:
```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.IntStream;
import java.util.stream.Stream;

class Solution {
    public static void main(String args[]) throws Exception {

        List<Integer> numeros =  Arrays.asList(1, 2, 3, 5, 8, 13, 21, 34);                                       

        // soma 2 em um array de numeros e imprime
        numeros.stream().map(c ->  c+2).forEach(System.out::println);

        
        Stream<Person> pessoas = Stream.of(new Person("Paul", 24, 20000),
                                           new Person("Mark", 30, 30000),
                                           new Person("Will", 28, 28000),
                                           new Person("William", 28, 28000));

        // forEach                                   
        // imprimir todos os nomes da lista
        pessoas.forEach(p ->System.out.println(p.getName()));

        // filter
        // filtra apenas pessoas com idade maior que 28 anos
        pessoas.filter(p -> p.getAge()>28);
      
        // sorted
        //ordenar pelo atributo da classe
        pessoas.sorted(Comparator.comparing(Person::getAge));

        // allMatch
        //Retorna true se todos os elementos do fluxo correspondem ao predicado fornecido
        boolean adult =  pessoas.allMatch(p-> p.getAge()>18);
       
        // anyMatch
        // Retorna true se qualquer um dos elementos do fluxo corresponde ao predicado fornecido
        boolean underage =  pessoas.anyMatch(p-> p.getAge()>18);
      
        // noneMatch
        // Retorna true se nenhum dos elementos do fluxo corresponde ao predicado fornecido.
        boolean under =  pessoas.noneMatch(p-> p.getAge()>18);

        // mapToInt
        // Transformar idades em um stream de idades
        IntStream pontos  = pessoas.mapToInt(c -> c.getAge());
        
    }
 }
}
```

