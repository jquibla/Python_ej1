ef imprimelineas(dirfichero, numlineas=1):

    f=open(dirfichero, "r")

    for i in range(numlineas):
        linea=f.readline()
        print(str(i+1) + " " + linea, end='')
    f.close()
    
imprimelineas("/home/dsc/data/shell/Text_example.txt",3)
