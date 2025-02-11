#----- start of file -----
# ------------ imports ------------
from map import Direction

# ------------ functions ------------
def ana(phrase: str) -> str:
    ana = 'a'
    vowels: list[str]= ['a', 'e', 'i', 'o', 'u']
    if phrase[0].lower() in vowels:
        ana ='an'

    return ana

#----- end of file -----
