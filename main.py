from fastapi import FastAPI, HTTPException, Path
from uuid import uuid4
from typing import List, Dict

app = FastAPI(title= "Calculateur RPN")

piles = dict()

operateurs = {"+","-"
              "*","/"}

@app.get("/rpn/op", summary="Liste des opérateurs")
def lister_piles():
    return {"operateurs": list(operateurs)}

@app.post("/rpn/stack", summary="Créer une nouvelle pile")
def creer_pile():
    pile_id = str(uuid4())
    piles[pile_id] = []
    return {"pile_id": pile_id, "pile": piles[pile_id]}

@app.get("/rpn/stack", summary="Lister toutes les piles")
def recuperer_toutes_les_piles():
    return {"piles": list(piles.keys())}

@app.get("/rpn/stack/{pile_id}", summary="Voir une pile")
def recuperer_une_piles():
    pass

@app.delete("/rpn/stack/{pile_id}", summary="Vider une pile")
def nettoyer_une_pile():
    pass

@app.post("/rpn/stack/{pile_id}", summary="Ajouter une valeur à la pile")
def ajouter_element_dans_pile():
    pass


@app.post("/rpn/op/{operateur}/stack/{pile_id}", summary="Appliquer un opérateur")
def appliquer_operateur():
    pass














if __name__ == "__main__":
    pass