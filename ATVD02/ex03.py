
def converter_temperatura(valor, de, para):
    match (de, para):
        case ('Celsius', 'Fahrenheit'):
            return (valor * 9/5) + 32
        case ('Celsius', 'Kelvin'):
            return valor + 273.15
        case ('Fahrenheit', 'Celsius'):
            return (valor - 32) * 5/9
        case ('Fahrenheit', 'Kelvin'):
            return (valor - 32) * 5/9 + 273.15
        case ('Kelvin', 'Celsius'):
            return valor - 273.15
        case ('Kelvin', 'Fahrenheit'):
            return (valor - 273.15) * 9/5 + 32
        case _:
            return None

def converter_distancia(valor, de, para):
    match (de, para):
        case ('metros', 'quilômetros'):
            return valor / 1000
        case ('quilômetros', 'metros'):
            return valor * 1000
        case ('milhas', 'quilômetros'):
            return valor * 1.60934
        case ('quilômetros', 'milhas'):
            return valor / 1.60934
        case _:
            return None

def converter_tempo(valor, de, para):
    match (de, para):
        case ('segundos', 'minutos'):
            return valor / 60
        case ('minutos', 'segundos'):
            return valor * 60
        case ('minutos', 'horas'):
            return valor / 60
        case ('horas', 'minutos'):
            return valor * 60
        case _:
            return None

def conversor(tipo, valor, de, para):
    match tipo:
        case 'temperatura':
            return converter_temperatura(valor, de, para)
        case 'distancia':
            return converter_distancia(valor, de, para)
        case 'tempo':
            return converter_tempo(valor, de, para)
        case _:
            return "Tipo de conversão inválido"

tipo = input("Digite o tipo de conversão (temperatura, distancia, tempo): ").lower()
valor = float(input("Digite o valor a ser convertido: "))
de = input("Digite a unidade de origem: ")
para = input("Digite a unidade de destino: ")

resultado = conversor(tipo, valor, de, para)
if resultado is not None:
    print(f"Resultado: {resultado} {para}")
else:
    print("Conversão inválida!")
