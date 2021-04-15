from thrift.protocol.TBinaryProtocol import TBinaryProtocol
from thrift.transport.TSocket import TSocket
from thrift.transport.TTransport import TBufferedTransport

from service.calculadora.calculadora import Client
from service.calculadora.ttypes import CalculadoraException

if __name__ == "__main__":
    host = "localhost"
    port = 50000
    transporte = TBufferedTransport(TSocket(host, port))
    protocol = TBinaryProtocol(transporte)
    conexion = Client(protocol)
    continuarMenu = True
    while continuarMenu:
        resultado = 0

        try:
            print("Digite el primer numero\n")
            numero1 = int(input())
            print("Digite el segundo numero\n")
            numero2 = int(input())

            print("Que operacion desea realizar?\n"
                  "[+, -, *, /]")
            operador = str(input())

            if operador == "+":
                transporte.open()
                resultado = conexion.adicion(numero1, numero2)
                transporte.close()
            elif operador == "-":
                transporte.open()
                resultado = conexion.substraccion(numero1, numero2)
                transporte.close()
            elif operador == "*":
                transporte.open()
                resultado = conexion.multiplicacion(numero1, numero2)
                transporte.close()
            elif operador == "/":
                transporte.open()
                resultado = conexion.division(numero1, numero2)
                transporte.close()
            else:
                print("No es un operador valido")
        except CalculadoraException:
            print("Numero invalido")
        except ValueError:
            print("Numero de entrada invalido")
        finally:
            transporte.close()

        print("El resultado es: " + str(resultado))

        print("Si desea continuar, presione la tecla << Y >>")
        respuesta = str(input())

        if respuesta == "Y" or respuesta == "y":
            continuarMenu = True
        else:
            continuarMenu = False
            print("Saliendo...")
