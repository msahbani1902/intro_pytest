import numpy as np

def inverse(chaine):
    if isinstance(chaine,int):
        raise ValueError("Vous devez passer une chaine de caracteres")
    
    if len(chaine)==4 and isinstance(chaine,list):
        chaine.pop()
    assert np.all([ isinstance(e,str) for e in chaine]), "les elements doivent etre des caracteres"
    print(np.all([ isinstance(e,str) for e in chaine]))
    return "".join(chaine[::-1])

if __name__ == "__main__":
    print(inverse(["a","b","c","d"]))
    print(isinstance("abcd",list))