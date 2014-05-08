import sys
import time
import pylab as dibujo
def calcular_pi(n):
  pi35 = 3.1415926535897931159979634685441852
  sumatorio = 0.0
  ini = 0
  intervalos = 1.0/float(n)
  for i in range(n):
    x_i = ((i+1)-1.0/2.0)/n
    fx_i = 4.0/(1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio/n
  return (valor_pi)
#Programa principal.

if(__name__== "__main__"):
  argumentos = sys.argv[1:]
  if (len(argumentos) == 2):
    n = int (argumentos[0])
    aproximaciones = int(argumentos(1))
  else:
    print "Introduzca el numero de intervalos (n > 0):"
    n = int(raw_input())
    print "Introduzca el numero de aproximaciones:"
    aproximaciones = int(raw_input())
  inicio = time.time()
  inicio2 = time.clock()
  lista = []
  if (n>0):
    intervalo = n
    for i in range(aproximaciones):
      inicio = time.time()
      valor = calcular_pi (intervalo)
      final = time.time() - inicio
      lista.append (final)
      intervalo += n
  else:
    print "El valor de los intervalos debe ser mayor que 0"
  
  print range(aproximaciones)
  print lista 
  dibujo.title ("Calculo del numero pi")
  dibujo.plot (range(aproximaciones), lista, marker = "o", color ="r", label= "Linea 1")
  dibujo.legend()
  dibujo.show()
