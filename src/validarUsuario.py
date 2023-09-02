# Mauricio Quiñones
usuario1 = {'edad': 25, 'tipo_documento': 'ce', 'nombre': 'Juan'}
usuario2 = {'edad': 16 , 'tipo_documento': 'ti', 'nombre': 'Pedro'}
usuario3 = {'edad': 60 , 'tipo_documento': 'cc', 'nombre': 'Jhon'}

def validarUsuario(usuario):
    if usuario['edad'] > 18 and usuario['tipo_documento'] == 'cc' :
        print(f'Bienvenido {usuario["nombre"]}')
    else :
        print(f'Acceso denegado')

validarUsuario(usuario1)
validarUsuario(usuario2)
validarUsuario(usuario3)