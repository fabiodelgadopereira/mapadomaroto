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

        // reduce                                   
        // Combinar elementos, no caso abaxio é uma soma.
        int result = numeros.stream().reduce(0, (subtotal, element) -> subtotal + element);
        


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

        // max
        // Encontra o maior de uma lista
        Person older =  pessoas.max(Comparator.comparing(Person::getAge)).get();

        //min
        // Encontra o menor de uma lista
        Person younger =  pessoas.min(Comparator.comparing(Person::getAge)).get();

        // allMatch
        //Retorna true se todos os elementos do fluxo correspondem ao predicado fornecido
        boolean adult =  pessoas.allMatch(p-> p.getAge()>18);
       
        // anyMatch
        // Retorna true se qualquer um dos elementos do fluxo corresponde ao predicado fornecido
        boolean underage =  pessoas.anyMatch(p-> p.getAge()>18);
      
        // noneMatch
        // Retorna true se nenhum dos elementos do fluxo corresponde ao predicado fornecido.
        boolean under =  pessoas.noneMatch(p-> p.getAge()>18);

        // Group by 
        // agregar uma única propriedade dos elementos ou apenas contar o número de elementos por grupo
        pessoas.collect(Collectors.groupingBy(foo -> foo.getAge(), Collectors.counting()))
               .forEach((id,count)->System.out.println(id+"\t"+count));
        
        // mapToInt
        // Transformar idades em um stream de idades
        IntStream pontos  = pessoas.mapToInt(c -> c.getAge());
        
    }
 }
}
```
Complete the palindromeIndex function below
```java
static int palindromeIndex(String line) {                  
            char [] chars = line.toCharArray();
    int ret = -1;

    for( int i = 0,j = line.length() - 1; j >= i; i++, j--)
    {
            if ( chars[i] != chars[j] )
            {                   
                String before = line.substring(0, i);
                String after = line.substring(i + 1, line.length());
                if ( checkPalindrome(before + after) )
                {
                    return i;
                }
                else
                {
                    return j;
                }
            }
    }
    return ret;
}
public static boolean checkPalindrome(String str)
{
    for( int i = 0, j = str.length() - 1; j >= i; i++,j-- )
    {
        if ( str.charAt(i) != str.charAt(j) )
        {
            return false;
        }
    }
    return true;
    ///return IntStream.range(0, s.length() / 2)
    .noneMatch(i -> s.charAt(i) != s.charAt(s.length() - i - 1));
}
```

