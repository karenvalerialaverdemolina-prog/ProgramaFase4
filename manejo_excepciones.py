
# Creamos una clase llamada Calculadora.
class Calculadora:

    # Definimos un método para realizar una división.
    def dividir(self, numero1, numero2):

        # Verificamos que el segundo número no sea cero.
        if numero2 == 0:

            # Generamos una excepción si se intenta dividir entre cero.
            raise ZeroDivisionError("No se puede dividir entre cero.")

        # Si los datos son correctos, realizamos la división.
        return numero1 / numero2


# Creamos una función principal para ejecutar el programa.
def main():

    # Creamos un objeto de la clase Calculadora.
    calculadora = Calculadora()

    # Iniciamos el bloque que puede generar errores.
    try:

        # Solicitamos el primer número al usuario.
        numero1 = float(input("Ingrese el primer número: "))

        # Solicitamos el segundo número al usuario.
        numero2 = float(input("Ingrese el segundo número: "))

        # Llamamos al método dividir de la clase Calculadora.
        resultado = calculadora.dividir(numero1, numero2)

    # Capturamos los errores cuando se ingresan datos incorrectos.
    except ValueError:
        print("Error: debe ingresar solamente números.")

    # Capturamos el error cuando se intenta dividir entre cero.
    except ZeroDivisionError as error:
        print("Error:", error)

    # Este bloque se ejecuta cuando no ocurre ningún error.
    else:
        print("El resultado de la división es:", resultado)

    # Este bloque se ejecuta siempre, haya error o no.
    finally:
        print("Finalizó la ejecución del programa.")


# Comprobamos que el archivo se ejecute como programa principal.
if __name__ == "__main__":

    # Llamamos a la función principal.
    main()

