def plus_grand_nombre ( a : float, b : float) -> int :
    """"
    :param a: nombre de choisit
    :param b: nombre de choisit
    :return: le plus grand nombre
    """
    if a > b:
        return a
    else:
        return b

print(plus_grand_nombre(5,4))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def seuil (a:int, b=10) -> int:
    """"
    :param a: nombre de choisit
    :param b: seuil choisit
    :return: inférieur ou supérieur au seuil choisit
    """
    if a > b:
        return (f"{a} est supérieur au seuil")
    else:
        return (f"{a} est inférieur au seuil")

print(seuil(3, 4)) #changement de parametres avec B
print(seuil(13))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def liste (a:list) -> int:
    """
    :param a: liste
    :return: plus grand nombre de la liste

    """

    sup = a[0]
    for i in range(len(a)):
        if a [i] > sup:
            sup = a[i]
    return sup

print(liste([5,6,3,7]))
print(liste([5,9,2,-7]))
print(liste([4,9,8,-7]))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

