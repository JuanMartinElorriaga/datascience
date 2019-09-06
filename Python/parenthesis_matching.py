# PARENTHESIS MATCHING

expresiones_abertura = [
	"[", 
	"(",
	"{"
] #Signos de apertura

expresiones_cierre = [
	"]",
	")",
	"}"
] #Signos de cierre

input_usuario = str(input("Colocar cadena a ser verificada: "))

def balance_de_expresiones(input_usuario): #funcion basada en pila
	pila = []
	for i in entrada:
		if i in expresiones_abertura:
			pila.append(i)
		elif i in expresiones_cierre:
			position = expresiones_cierre.index(i) #busca elemento en closing expresiones_cierre y devuelve el index
			if ((len(pila) > 0) and 
				(expresiones_abertura[position] == pila[len(pila)-1])):
				pila.pop()
			else:
				print("NO BALANCEADO")
		if len(pila) == 0:
				print("BALANCEADO")


balance_de_expresiones(input_usuario)

