from agregar import *
from borrar import *
from read import *
from estado import devolver

if __name__ == "__main__":
    
    # libros = {isaac:{id:1123123,
    #                  nombre:isaac,
    #                  libros= {libro:{no,bre:nmbre
    #                                 FECHA:
    #                                 estado:prestado}}}}
    libros = {  }
    while  True:
        
        print ("-"*50)
        print( )
        x = int(input( """Escoge lo que quieras que suceda:
                1.Prestar un libro
                2.Eliminar un usuario
                3.Leer la lista de libros prestados
                4.Devolver un libro
                5.No hacer nada
                (x): """))
        match x:
            case 1: 
                agregar(libros)
            case 2:
                borra(libros)
            case 3:
                leer_funcion(libros) 
            case 4:
                devolver(libros)
            case 5:
                print('\nYa finalizo el proceso, chauuu')
                break
                