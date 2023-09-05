# Función para procesar una línea del archivo de entrada y escribir en el archivo de salida
#Procesa cada linea, en una li
def procesar_linea(linea):
    elementos = linea.strip().split(',')
    Hex = elementos[0].split('/')[0]  #elimina la linea '/#' siendo # cualquier numero
    ip = elementos[-1]  # -1 accede al ultimo elemento de una lista
    segunda_cadena = elementos[2] #accede al segunda cadena de texto pero 3er elemento de la lista

    numeros_hex = Hex.split(':') #Separa los elementos en varios cuando encuentra el caracter ":"
    numeros_decimal = [] #arreglo para guardar los hexadecimales que seran guardados como decimales
    numeros_ip_a_hex = [] #guardando la ip que será convertida a hexadecimal

    #ciclo para transformar cada elemento de la lista de hexadecimal a decimal
    for num_hex in numeros_hex:
        num_decimal = int(num_hex, 16)
        numeros_decimal.append(str(num_decimal))

    #obtenemos las partes de la Ip, separando cada vez que se encuentre con un "."
    partes_ipv4 = ip.split('.')
    #Se transforman los string a int, y posteriormente se les da el formato hexadecimal, añadiendo un "0" en caso de ser necesario, poseriormente con join se unen las partes de la lista con un "."
    ultimos_numeros_hex = '.'.join(format(int(part, 10), '02X') for part in partes_ipv4)
    numeros_ip_a_hex.append(ultimos_numeros_hex)

    resultado = f"{segunda_cadena} : {' : '.join(numeros_decimal)} : {'.'.join(numeros_ip_a_hex)}\n"
    return resultado

# Abre el archivo de entrada y salida
with open('prueba2.txt', 'r') as archivo_entrada, open('salida.txt', 'w') as archivo_salida:
    for linea in archivo_entrada:
        resultado = procesar_linea(linea)
        archivo_salida.write(resultado)

print("Proceso completado. Los resultados se han guardado en 'salida.txt'.")
