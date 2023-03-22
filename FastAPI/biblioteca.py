from fastapi import FastAPI
from clases_biblioteca import *

app = FastAPI(
    title='Biblioteca',
    version='0.4.1'
)

biblioteca ={ 1:{
        'nombre':'felipe',
        'edad':'23',
        'libros':{
            1:{'libro':'club 5 am',
            'fecha':'13/03/2023',
            'estado':'prestado'},
            
            2:{'libro':'apopeya',
                 'fecha':'13/03/2023',
                 'Estado':'prestado'}
        }
    }
}   


@app.get('/',tags=['Lectura de datos'])
def hello_wold_check():
    """Saber si el servidor esta funcionando.

    Returns:
        El titulo y version del servidor.
    """
    {
        'titulo':'Biblioteca',
        'version':'V.0.4.1'
    }
    return 'hello world'

    
@app.get('/personas/{id}',tags=['Lectura de datos'])
def id(id:int):
    """Le ingresamos la identificacion de una persona en especifico para que nos devuelva toda 
        la informacion de esta persona.

    Args:
        id (int): La identificacion de la persona.

    Returns:
        Los datos correspondientes a la identificacion de la persona.
    """
    return biblioteca[id]


@app.get('/personas',tags=['Lectura de datos'])
def all_people():
    """Lee todos los datos del diccionario "biblioteca".

    Returns:
        Todos los datos de este diccionario.
    """
    return biblioteca

    
@app.post('/personas',tags=['Agregar datos'])
def Personas_add(request:PersonaBiblioteca):
    """Funcion para agregar datos a nuestra central de datos.

    Args:
        request (PersonaBiblioteca): Un objeto que contiene el nombre, edad, clave,
        el nombre del libro que va a prestar y la fecha en la que estamos.

    Returns:
        Se agrega el usuario a la central de datos
    """
    x = {'nombre':request.nombre,
         'edad':request.edad,
         'libros':{
             request.clave:
                {  
                'libro':request.libro,
                'fecha':request.fecha,
                'estado':'prestado'
                }
            }
        }
    biblioteca[request.id] = x 
    return 'Ya se han agregado tus datos :D'
 
    
@app.put('/personas',tags=['Modificar datos'])
def personas_mod(request:PersonaBibliotecaSimple):
    """Funcion que modifica los datos de un usuario en especifico.

    Args:
        request (PersonaBibliotecaSimple): Es un objeto que contiene la id de la persona,
        su nombre y su edad.
    Returns:
        Modifica los datos que se necesitan.
    """
    if biblioteca[request.id]['nombre'] != request.nombre:
            biblioteca[request.id]['nombre'] = request.nombre
    elif biblioteca[request.id]['edad'] != request.edad:
            biblioteca[request.id]['edad'] = request.edad

   
@app.delete('/personas',tags=['Eliminar datos'])
def personas_del(request:PersonaBibliotecaBasica):
    """Se encarga de eliminar un usuario.

    Args:
        request (PersonaBibliotecaBasica): Un objeto que contiene la id de la persona.
    Returns: 
        Se elimina el usuario o persona correspondiente a la id que ingresamos.
    """
    biblioteca.pop(request.id)     
