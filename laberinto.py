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
