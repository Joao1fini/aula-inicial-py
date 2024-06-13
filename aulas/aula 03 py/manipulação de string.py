texto="curso de python"

print(texto[0]) #imprime a letra na posição 0
print(texto[0:15]) #imprime "de" e "até"
print(texto[0:15:2]) #impreme pulando o terceito numero digitado "2"
print(texto[:14]) #todos os anterios até o "14
print(texto[9:]) #todos os proximos do "9"

#informa a quatidade de caractereas no texto
tamanhodotxt = len(texto)
print (tamanhodotxt)

#conta quantas vezes uma letra/palavra aparece
print(f"quantidades de Letras O: {texto.count('o')}")

#imprime quando começa a palavra "python"
print(texto.find("python"))
print(texto.find("python ")) #-1 se nao encontrou

#indica se possui uma palavra em uma frase
print("python" in texto) # true ou False

#transformando string
trocatexto = texto.replace("python", "javascript")
print(f"temos {trocatexto} e {texto}")

textominusculos=texto.lower()
print(textominusculos)
textomaiusculo=texto.upper()
print(textomaiusculo)
textocap=texto.capitalize() #deixa a primeira letra em maiusculo
print(textocap)
textott=texto.title() #deixa toda letra inicial em maiusculos
print(textott)
snake=texto.strip()
print(snake)

#junta texto
junttx = "-".join(texto)
print(junttx)
#separa o texto
div=texto.split()
print(div)