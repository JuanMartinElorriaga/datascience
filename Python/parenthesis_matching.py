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

def balance_de_expresiones(entrada): #funcion basada en pila
	pila = []
	for i in entrada:
		if i in expresiones_abertura:
			pila.append(i)
		elif i in expresiones_cierre:
			position = expresiones_cierre.index(i) #busca elemento en closing expressions y devuelve el index
			if ((len(pila) > 0) and 
				(expresiones_abertura[position] == pila[len(pila)-1])):
				pila.pop()
			else:
				print("NO BALANCEADO")
		if len(pila) == 0:
				print("BALANCEADO")


balance_de_expresiones("][][][]))")

