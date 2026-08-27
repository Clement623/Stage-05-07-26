# Argumentation Framework Solver (CBR-based)

[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/dependency-networkx-orange.svg)](https://networkx.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#-licence)

Solveur avancé pour les **cadres d'argumentation abstraite** (*Abstract Argumentation Frameworks*). Il permet de calculer et d'évaluer des extensions sémantiques (Préférée, Fondée, Stable, etc.) en optimisant la résolution via des stratégies de **Raisonnement à Partir de Cas (CBR — Case-Based Reasoning)** et la décomposition en **Composantes Faiblement Connexes (WCC)**.

##  Sommaire

- [Prérequis et installation](#-prérequis-et-installation)
- [Formats de fichiers supportés](#-formats-de-fichiers-supportés-entrée)
- [Utilisation](#-utilisation)
- [Architecture du code](#-architecture-du-code)
- [Licence](#-licence)

## Prérequis et Installation

Le projet est développé en **Python 3** et nécessite la bibliothèque [`networkx`](https://networkx.org/) pour la manipulation des graphes et le calcul d'isomorphisme (utilisé dans les stratégies de résolution).

1. Cloner ou extraire le projet
   ```bash
   git clone <url-du-repo>
   cd <nom-du-projet>
   ```
2. Installer la dépendance requise :
   ```bash
   pip install networkx
   ```

##  Formats de Fichiers Supportés (Entrée)

Le module `Src/Parse/Parser.py` est capable de lire deux formats standards pour représenter les graphes d'argumentation.

### 1. Format `.af` (texte simple)

Ce format définit le nombre d'arguments sur la première ligne, puis liste les attaques.

- **Ligne 1 :** `p af <nombre_arguments>` (le parser extrait le chiffre)
- **Lignes suivantes :** `source cible` (représente une attaque de l'argument source vers la cible)

```text
p af 3
1 2
2 1
2 3
```

### 2. Format `.apx` (format logique)


- **Arguments :** `arg(aX).` (où `X` est l'identifiant numérique)
- **Attaques :** `att(aX, aY).` (où l'argument `X` attaque l'argument `Y`)

```text
arg(a1).
arg(a2).
arg(a3).
att(a1,a2).
att(a2,a1).
att(a2,a3).
```

##  Utilisation

> **Note :** actuellement, le fichier `main.py` lance uniquement une fonction `test1()` codée en dur.

### Exemple d'exécution actuelle

```bash
python main.py
```

Cela lance la suite de tests démontrant la décomposition WCC et l'application des stratégies d'isomorphisme linéaire et fondé.

### 💡 Option CLI recommandée

Pour permettre de tester n'importe quel fichier en argument, ajoutez ceci dans `main.py` :

```python
import argparse
from Src.Parse.Parser import Parser

def main():
    parser = argparse.ArgumentParser(description="Solveur de Cadres d'Argumentation")
    parser.add_argument("file", help="Chemin vers le fichier d'entrée (.af ou .apx)")
    # Ajoute d'autres arguments pour choisir la sémantique si nécessaire

    args = parser.parse_args()

    # Lecture du fichier
    my_parser = Parser(args.file)
    af = my_parser.parse()
    print(f"Graphe chargé : {af}")
    # Suite de ta logique de résolution ici...

if __name__ == "__main__":
    main()
```

**Commande résultante :**
```bash
python main.py graphe.apx
```

## Architecture du Code

L'architecture est modulaire et orientée objet, séparée en plusieurs dossiers stratégiques :

| Dossier | Rôle |
|---|---|
| `Src/Core/` | Les fondations du système (classes `Argument`, `Attack`, `ArgFramework`) |
| `Src/Parse/` | Lecture et conversion des fichiers texte en objets manipulables (`Parser.py`) |
| `Src/ExtFile/` | Sémantiques d'acceptabilité (Grounded, Preferred, Stable, Complete, Admissible) et structures d'Extensions |
| `Src/CaseFile/` | Implémentation du Case-Based Reasoning (base de cas, problèmes, questions, solutions) et convertisseurs vers NetworkX (`GraphConverter.py`) |
| `Src/Solver/` | Le cœur logique du programme |
| `Src/Solver/Orchestrator.py` | Gère le flux d'exécution |
| `Src/Solver/Strategy/` | Approches de résolution (`GroundedIsomorphismStrategy`, `LinearPatternIsomorphismStrategy`, `DirectResolutionStrategy`) |
| `Src/Solver/Specialist/` | Tâches spécialisées : décomposition WCC/SCC, calcul de bijection, réduction du graphe fondé |

Les design patterns **Strategy** et **Specialist** structurent proprement la logique de résolution du solveur.

