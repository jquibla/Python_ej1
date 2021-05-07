def encuentrafichmasgrande(directorio):

    import os
    import datetime

    listaficheros=list()
    for root, dirs, files in os.walk(directorio):
        for name in files:
          listaficheros.append([os.path.join(root, name), os.path.getsize(os.path.join(root, name))])

    listaficheros = sorted(listaficheros, key=lambda tup: tup[1], reverse=True)
    ficheromasgrande=listaficheros[0][0]
    return ficheromasgrande + "\nPermisos: " + str(oct(os.stat(ficheromasgrande).st_mode)[-3:]) \
         + "\nTamaño: " + str(os.path.getsize(ficheromasgrande)) \
         + "\nModificado: " + str(datetime.datetime.fromtimestamp(os.stat(ficheromasgrande).st_mtime))


print(encuentrafichmasgrande("/home/dsc/data/opentraveldata"))
