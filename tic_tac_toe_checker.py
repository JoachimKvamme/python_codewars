# Denne funksjonen tar 2d-array som tilsvarer en bondesjakkstilling.
# Funksjonen skal sjekke hvem som vant, eventuelt om det endte i uavgjort (kaller man det remis i bondesjakk),
# eller om spillet fremdeles er i gang.

def is_solved(tic_tac):
    OneDGame = []

    for i in tic_tac:
        for x in i:
            OneDGame.append(x)

    if OneDGame[0] == 1 and OneDGame[1] == 1 and OneDGame[2] == 1:
        return 1
    if OneDGame[3] == 1 and OneDGame[4] == 1 and OneDGame[5] == 1:
        return 1
    if OneDGame[6] == 1 and OneDGame[7] == 1 and OneDGame[8] == 1:
        return 1
    if OneDGame[0] == 1 and OneDGame[3] == 1 and OneDGame[6] == 1:
        return 1
    if OneDGame[1] == 1 and OneDGame[4] == 1 and OneDGame[7] == 1:
        return 1
    if OneDGame[2] == 1 and OneDGame[5] == 1 and OneDGame[8] == 1:
        return 1
    if OneDGame[2] == 1 and OneDGame[4] == 1 and OneDGame[6] == 1:
        return 1
    if OneDGame[0] == 1 and OneDGame[4] == 1 and OneDGame[8] == 1:
        return 1
    
    if OneDGame[0] == 2 and OneDGame[1] == 2 and OneDGame[2] == 2:
        return 2
    if OneDGame[3] == 2 and OneDGame[4] == 2 and OneDGame[5] == 2:
        return 2
    if OneDGame[6] == 2 and OneDGame[7] == 2 and OneDGame[8] == 2:
        return 2
    if OneDGame[0] == 2 and OneDGame[3] == 2 and OneDGame[6] == 2:
        return 2
    if OneDGame[1] == 2 and OneDGame[4] == 2 and OneDGame[7] == 2:
        return 2
    if OneDGame[2] == 2 and OneDGame[5] == 2 and OneDGame[8] == 2:
        return 2
    if OneDGame[2] == 2 and OneDGame[4] == 2 and OneDGame[6] == 2:
        return 2
    if OneDGame[0] == 2 and OneDGame[4] == 2 and OneDGame[8] == 2:
        return 2
    
    if OneDGame.count(0) > 0:
        return 0
    return -1
