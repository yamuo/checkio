from typing import List

def checkio(game_result: List[str]) -> str:
    result = []
    ret = "D" 
    for i in game_result:
        result.append(list(i))

    for i in range(3):
        if result[0][i] == result[1][i] == result[2][i] == "O":
            ret = "O"
        if result[i][0] == result[i][1] == result[i][2] == "O":
            ret = "O"
        if result[0][i] == result[1][i] == result[2][i] == "X":
            ret = "X"
        if result[i][0] == result[i][1] == result[i][2] == "X":
            ret = "X"

    if result[0][0] == result[1][1] == result[2][2] == "O":
            ret = "O"
    if result[0][2] == result[1][1] == result[2][0] == "O":
            ret = "O"
    if result[0][0] == result[1][1] == result[2][2] == "X":
            ret = "X"
    if result[0][2] == result[1][1] == result[2][0] == "X":
            ret = "X"
            
    return ret

print(checkio([
        "X.O",
        "XX.",
        "XOO"]))
