list=[6, 0, 0, 0, 0]

def Score(Liste):
    liste_Werte=[]
    for list in Liste:
        if list<7 and list >1:
            wert=list-1
        elif list==7 or list==1 or list==0:
            wert=0
        else:
            wert=13-list
        liste_Werte.append(wert)
    Summe=sum(liste_Werte)
    return Summe

