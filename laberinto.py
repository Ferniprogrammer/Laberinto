laberinto = [
    ["X", "X","X", "X", "X", "X", "X"],
    ["X",'E', 'X', 'X', 'X', 'X', "X"], 
    ["X",' ', 'X', ' ', ' ', ' ', "X"],
    ["X",' ', 'X', ' ', 'X', ' ', "X"], 
    ["X",' ', ' ', ' ', 'X', ' ', "X"], 
    ["X",'X', 'X', 'X', 'X', 'S', "X"]
    ]
muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))
print("\n")

def imprimir_laberinto(laberinto):
    for fila in laberinto:
        for celda in fila:
            print(celda, end=' ')
        print()
        
imprimir_laberinto(laberinto)
print("Intenta resolver el laberinto, empiezas en la posición (2, 2) y debes llegar a la posición (6,6)")
print("Par moverte escribe: abajo, arriba, derecha, izquierda")
print("primer movimiento, estas en la posición (2, 2)")
if input() == "abajo":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit
     
imprimir_laberinto(laberinto)
print("segundo movimiento, estas en la posición (2, 3)")
if input() == "abajo":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("tercer movimiento, estas en la posición (2, 4)")
if input() == "abajo":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("cuarto movimiento, estas en la posición (2, 5)")
if input() == "derecha":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("quinto movimiento, estas en la posición (3, 5)")
if input() == "derecha":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("sexto movimiento, estas en la posición (4, 5)")
if input() == "arriba":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("séptimo movimiento, estas en la posición (4, 4)")
if input() == "arriba":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("octavo movimiento, estas en la posición (4, 3)")
if input() == "derecha":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("noveno movimiento, estas en la posición (5, 3)")
if input() == "derecha":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("décimo movimiento, estas en la posición (6, 3)")
if input() == "abajo":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("penúltimo movimiento, estas en la posición (6, 4)")
if input() == "abajo":
     print("movimiento correcto, sigue así")
else:
     print("movimiento no válido, empieza de nuevo")
     quit

imprimir_laberinto(laberinto)
print("último movimiento, estas en la posición (6, 5)")
if input() == "abajo":
    print("Lo lograstes, llegastes al final")
else:
    print("Movimiento no válido, empieza de nuevo")
    quit
