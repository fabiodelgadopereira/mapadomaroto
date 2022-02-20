import requests
import csv
import sys
old_stdout = sys.stdout

def request_get(cep):
    r = requests.get('https://viacep.com.br/ws/'+cep+'/json/')
    ## output em format csv
    print(cep+", "+r.json().get('logradouro'))

def read_file():
    ficheiro = open('input.csv')
    ## lê o CSV e pega o primeiro elemento
    reader = csv.reader(ficheiro, delimiter=':', quoting=csv.QUOTE_NONE)
    for linha in reader:
        request_get(linha[0])
    ficheiro.close()

def main():  
    ## envia todo o log para o output.log
    log_file = open("output.log","w")
    sys.stdout = log_file 
    read_file()
    sys.stdout = old_stdout
    log_file.close()

if __name__ == "__main__":
    main()