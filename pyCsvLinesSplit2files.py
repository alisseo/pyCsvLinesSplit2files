def splitcsvline(file_in): #definisce il nome comando
        fin=open(file_in,"r",encoding="UTF-8") #assegna a fin il file aperto
        riga=fin.readline().strip().split(",") #legge riga e pulisce e divide su una lista

        while len(riga[0]) >0:
            files = open (riga[0],"w",encoding="UTF-8") #crea il file
            files.write (riga[1]) #scrive contenuto
            files.close
            riga=fin.readline().strip().split(",") #avanzamento riga successiva
        fin.close()
