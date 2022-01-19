# Python

## Venv
```shell
virtualenv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Exemplo básico
```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

## Input via teclado de vetor (quantidade de elementos e vetor)
```python
print ("Digite a quantidade de elementos no vetor:")
a = int(input())
print ("Digite o vetor separado por espaço:")
N = list(map(int, input().split()))
print (N)
```

## Diferentes formas de print:
```python
print("Hello World!", end = '')
print('\n')

print(*a) 
// 1 2 3 4 5

print(*a, sep = ", ") 
 // 1, 2, 3, 4, 5
```

## Dictionary
```python
#
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
#
entrada = int(input())
dict1={}

for indice in range (entrada):
    n, m = [str(x) for x in input().strip().split()]
    dict1[n]=m

for indice in range (entrada):
    try:
        pesquisa =  input()
    except:
        break
    if(pesquisa in dict1):
        print (pesquisa+"="+dict1[pesquisa])
    else:
        print ("Not found")
```
## Bash
```python
python -c ' import math;   print(math.sqrt(0)) '
```