# Python

Venv
```shell
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```
Exemplo básico
```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```
Input via teclado de vetor (quantidade de elementos e vetor)
```python
print ("Digite a quantidade de elementos no vetor:")
a = int(input())
print ("Digite o vetor separado por espaço:")
N = list(map(int, input().split()))
print (N)
```
Diferentes formas de print:
```python
print("Hello World!", end = '')
print('\n')

print(*a) 
// 1 2 3 4 5

print(*a, sep = ", ") 
 // 1, 2, 3, 4, 5
```
