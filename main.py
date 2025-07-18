from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
from typing import List, Dict, Any
import webbrowser
import uvicorn

app = FastAPI(title= "Calculateur RPN")

piles: Dict[str, List[int]] = {}

operateurs: set[str] = {"+","-"
              "*","/"}

class Valeur(BaseModel):
    value: int

@app.get("/rpn/op", summary="Liste des opérateurs")
def lister_piles():
    return {"operateurs": list(operateurs)}

@app.post("/rpn/stack", summary="Créer une nouvelle pile")
def creer_pile() -> Dict[str, Any]:
    pile_id = str(uuid4())
    piles[pile_id] = []
    return {"pile_id": pile_id, "pile": piles[pile_id]}

@app.get("/rpn/stack", summary="Lister toutes les piles")
def recuperer_toutes_les_piles() -> Dict[str, List[str]]:
    return {"piles": list(piles.keys())}

@app.get("/rpn/stack/{pile_id}", summary="Voir une pile")
def recuperer_une_pile(pile_id: str ) -> Dict[str, List[int]]:
    if pile_id not in piles:
        raise HTTPException(status_code=404, detail="Pile introuvable")
    return {"pile": piles[pile_id]}

@app.delete("/rpn/stack/{pile_id}", summary="Vider une pile")
def nettoyer_une_pile(pile_id: str) -> Dict[str, str]:
    if pile_id not in piles:
        raise HTTPException(status_code=404, detail="Pile introuvable")
    del piles[pile_id]
    return {"message": "Pile supprimée"}

@app.post("/rpn/stack/{pile_id}", summary="Ajouter une valeur à la pile")
def ajouter_element_dans_pile(pile_id: str, val: Valeur) -> Dict[str, List[int]]:
            if pile_id not in piles:
                raise HTTPException(status_code=404, detail="Pile introuvable")
            piles[pile_id].append(val.value)
            return {"pile": piles[pile_id]}


@app.post("/rpn/op/{operateur}/stack/{pile_id}", summary="Appliquer un opérateur")
def appliquer_operateur(op: str, pile_id: str) -> Dict[str, List[Any]]:    
        if op not in operateurs:
            raise HTTPException(status_code=400, detail="Opérateur invalide")
        if pile_id not in piles:
            raise HTTPException(status_code=404, detail="Pile introuvable")
        pile = piles[pile_id]


        if len(pile) < 2:
            raise HTTPException(status_code=400, detail="Pas assez d'opérandes")
        
        b = pile.pop()
        a = pile.pop()

        try:
            match op:
                case "+":
                    res = a + b
                case "-":
                    res = a - b
                case "*":
                    res = a * b
                case "/":
                    res = a / b
                case _:
                    raise HTTPException(status_code=400, detail="Opérateur inconnu")

            pile.append(res)
            return {"pile": pile}
        except ZeroDivisionError:
            
            pile += [a, b]
            raise HTTPException(status_code=400, detail="Division par zéro")
        


def lancer_swagger():
    import threading
    threading.Timer(1.0, lambda: webbrowser.open("http://127.0.0.1:8000/docs")).start()



if __name__ == "__main__":
    lancer_swagger()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)