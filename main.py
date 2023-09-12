from enum import Enum
import keyboard

# Creamos un enum para asignar los 4 movimientos
class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4

def tetris():

    screen = [  
                ['🔳', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔳', '🔳', '🔳', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲'],
                ['🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲', '🔲']]

    # Imprimimos pantalla inicio
    print_screen(screen)

     @ Inicializamos la rotación a 0 como inicial
    rotation = 0
    
# While para correr el programa añadiendo con la biblioteca de keyboard los movimientos que se pueden hacer
    while(True):
        event = keyboard.read_event()
        if event.name=="esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            if event.name == 'down':
                (screen, rotation) = move_piece(screen, Movement.DOWN, rotation)
            elif event.name == 'right':
                (screen, rotation) = move_piece(screen, Movement.RIGHT, rotation)
            elif event.name == 'left':
                (screen, rotation) = move_piece(screen, Movement.LEFT, rotation)
            elif event.name == 'space':
                (screen, rotation) = move_piece(screen, Movement.ROTATE, rotation)


 
# definimos la función y asignamos la pantalla como lista, el movimiento como la clase movement asignada en el enum, y la rotación como un entero y
    que de como return lista y entero que será la pantalla modificada y la rotación en la que se encuentra.
def move_piece(screen: list, movement: Movement, rotation: int) -> (list, int):
    
# Creamos pantalla en blanco como el tablero de arriba pero en  una línea
    new_screen = [['🔲'] * 10 for _ in range(10)]

    # Creamos las rotaciones que tiene que dar la ficha, sumando en cada eje de coordenadas lo correspondiente a su siguiente movimiento y teniendo en cuenta donde se encuentra en ese momento.
    rotation_item = 0
    rotations = [[(1,1), (0,0), (-2,0), (-1,-1)],
                 [(0,1), (-1,0), (0,-1), (1,-2)],
                 [(0,2), (1,1), (-1,1), (-2,0)],
                 [(0,1), (1,0), (2,-1), (1,-2)]]

    # Le decimos a la nueva rotación que es igual que la rotación en la que se encuentra
    new_rotation = rotation

    # Creamos una condición comprimida para asignar a la nueva rotación siempre que sea menor que 4, + 1 o que empiece de 0
    if movement is Movement.ROTATE:
        new_rotation = 0 if rotation == 3 else rotation + 1

    # recorremos cada casilla del tablero para ver si tiene una pieza negra, cuando demos con ella a esa coordenada le asignamos 0,0 y poder trabajar sobre ella
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == '🔳':
                new_row_index = 0
                new_column_index = 0

    # Creamos un case para hacer los movimientos según el enum que hagamos
                match movement:
                    case Movement.DOWN:
            # Sólo sumamos en la fila puesto que para los lados no vamos a movernos
                        new_row_index = row_index + 1
                        new_column_index = column_index
                        
                    case Movement.RIGHT:
                        new_row_index = row_index
                        new_column_index = column_index + 1
                        
                    case Movement.LEFT:
                        new_row_index = row_index
                        new_column_index = column_index - 1

                # La más compleja, repasar bien para ver lo que hacemos con ello
                    case Movement.ROTATE:
                        new_row_index = row_index + rotations[new_rotation][rotation_item][0]
                        new_column_index = column_index + rotations[new_rotation][rotation_item][1]
                        rotation_item +=1

                # Creamos esta condición para trabajar las colisiones con las paredes, si colisiona no se puede realizar el movimiento
                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print('No se puede realizar el movimiento')
                    return (screen, rotation)
                else:
                    new_screen[new_row_index][new_column_index] = "🔳"

    print_screen(new_screen)

    # Retornamos los dos valores que necesitamos, la pantalla con la ficha movida y la rotación con su incrementación o puesta a 0
    return (new_screen, new_rotation)

def print_screen(screen: list):
    print('\nPantalla Tetris:\n')
    for row in screen:
        print(''.join(map(str, row)))

tetris()
