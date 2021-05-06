def cuentapalabras(dirfichero, numlineas=1):

    f=open(dirfichero, "r")

    #inicializo
    numpalabras=0
    for i in range(numlineas):
        linea=f.readline()
        numpalabras+=len(str.split(linea))
    f.close()
    return numpalabras


print(cuentapalabras("/home/dsc/data/shell/Finn.txt",5))
