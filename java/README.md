# Java

Exemplo básico
```java
class Solution{
	public static void main(String args[] ) throws Exception {  
		System.out.println("teste");
	}
}
```
Stream:
```java
import java.util.stream.Stream;

class Solution {
    public static void main(String args[] ) throws Exception {
		new Solution().getValues()
			.map(p-> p.getAge()) 
			.filter(p -> p>10) 
			.forEach(System.out::println);
	}

    private Stream<Person> getValues() {
        return Stream.of(new Person("Paul", 24, 20000), 
                         new Person("Mark", 30, 30000), 
                         new Person("Will", 28, 28000),
                         new Person("William", 28, 28000));
    }

    class Person {

        private String name;
        private int age;
        private long salary;

        public int getAge() {
            return age;
        }

        Person(String name, int age, long salary) {

            this.name = name;
            this.age = age;
            this.salary = salary;
        }
    }
}
```
Data Classes: purpose is to hold data
'equals()'/ 'hashCode()' pair

'toString()' of the form "User(name=John, age=42)"

'componentN()' functions corresponding to the properties in their order of declaration.

'copy()' function (see below).
```kotlin
data class User(val name: String, val age: Int)
```


