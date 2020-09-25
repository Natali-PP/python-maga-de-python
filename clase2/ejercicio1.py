#print('Ejercicio1 Hello world');
#mensaje = 'Hola mundo';
#print('Ejercicio2 ' + mensaje);

#print('Ejercicio3');
#nombre = input('Pasa el nombre: ');
#edad = input('Tu edad: ');
#
#print(nombre);
#print(edad);

#print('Ejercicio4');
#nombre = input('Pasa el nombre: ');
#cantidad = input('Numero entero: ');
#for i in range(int(cantidad)):
#    print(nombre);
# Ejercicio 5
#nombre = input('Pasa el nombre: ');
# cantidadLetras = len(nombre)
#print(f" {nombre} tiene {cantidadLetras})
#
# Ejercico 6
#print( ((3+2)/(2*5))**2 );

#Ejercicio 7
#numero1 = int(input('Primer numero: '))
#numero2 = int(input('Segundo numero: '))
#division = numero1 / numero2;
#modulo = numero1 % numero2;
#print(f" La division entre {numero1} y {numero2} es {division} y el resto es {modulo}")


#Ejercicio 8
#cantidad = int(input('Capital inicial: '))
#interesAnual = int(input('Interes anual: ')) / 100
#tiempo = int(input('tiempo (años): '))
#interes = cantidad * interesAnual * tiempo;
#capitalFinal = cantidad + interes
#print(str(capitalFinal))

#Ejercicio 9
#cantPayasos = int(input('Cantidad de payasos: '));
#cantMunecas = int(input('CAnt de muñecas: '));
#pesoPayasos = cantPayasos * 112;
#pesoMunecas = cantMunecas * 75;
#pesoTotal = pesoPayasos + pesoMunecas;
#print(f"El peso total será de {pesoTotal} gramos.")


#Ejercicio 10
#edad = int(input('Ingresa tu edad: '));
#if edad < 18:
#    print('Sos menor de edad')
#else:
#    print('Sos mayor de edad')


#Ejercicio 11
#contraseña = 'contraseña';
#password = input('Pasa la password pa lo pi: ')
#if password == contraseña :
#    print('Coinciden!');
#else:
#    print('No coincidden!');


#Ejercicio 12
#numero1 = int(input('Primer numero: '))
#numero2 = int(input('Segundo numero: '))
#if numero2 == 0:
#    print('Division por cero nooooooooooo')
#else:
#    print(f"{numero1 / numero2}")

#Ejercicio 13
#numero = int(input('Pasa el numero: '));
#if numero % 2 == 0:
#    print('Es par');
#else:
#    print('Es impar');

#Ejercicio 14
#rendimiento = float(input('Entre el rendimiento del laburante: '))
#
#if rendimiento == 0:
#    print(f'Inaceptable, el beneficio es {rendimiento* 100000}')
#elif rendimiento == 0.4:
#    print(f'Aceptable, el beneficio es {rendimiento* 100000}')
#else:
#    print(f'Metitorio, el beneficio es {rendimiento* 100000}')

#Ejercicio 15
#edad = int(input('Edad: '))
#if edad < 4:
#    print('Gratis')
#elif edad >=4 and edad < 18:
#    print('El costo de la entrada es 500')
#else:
#    print('El costo de la entrada es 1000')

#Ejercicio 16
#edad = int(input('Edad: '))
#count = 1
#for i in range(1,edad):
#    print(f'{i}')

#Ejercicio 17
#for i in range(11):
#    print(f'1 x {i} = {1*i}')

#Ejercicio 18
#palabra = input('Pasa la palabra: ')
#reversedPalabra = palabra[::-1]
#for i in range(len(reversedPalabra)):
#    print(reversedPalabra[i])

#Ejercicio 19

#frase = input('Ingrese la frase: ')
#letraABuscar = input('Ingrese la letra: ')
#count = 0
#for letra in frase:
#    if letra == letraABuscar:
#        count+=1
#
#print(f'En " {frase} ", la letra {letraABuscar} aparece {count} vez/veces')

#Ejercicio 21
#materias = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
#for materia in materias:
#    print(f'Yo estudio {materia}')

#Ejercicio 22
#vector1 = [1,2,3]
#vector2 = [-1,0,2]
#productoEscalar = 0
#for i in range(3):
#    productoEscalar += vector1[i]*vector2[i]
#
#print(f'{productoEscalar}')

#Ejercicio 23
#precios = {
#    'banana': 80,
#    'manzana': 100,
#    'pera': 50,
#    'naranja': 70
#}
#
#frutaConsulta = input('fruta: ')
#kilos = int(input('kilos: '))
#
#precioDeConsulta = 0
#
#for fruta, precio in precios.items():
#    if fruta == frutaConsulta:
#        precioDeConsulta+= precio * kilos
#
#if precioDeConsulta == 0:
#    print('No encuentro esa fruta')
#else:
#    print(f'{precioDeConsulta}')

#Ejercicio 24
asignaturas = {
    'Matemáticas': 6,
    'Física': 4,
    'Química': 5
}
