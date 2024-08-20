import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    animals = animals.loc[animals['weight']>100]
    animals = animals.sort_values(by=['weight'], ascending=False)
    animals = animals[['name']]
    return animals