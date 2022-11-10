import pandas as pd
import numpy as np
from palmerpenguins import load_penguins
penguins = load_penguins()
penguins = penguins.dropna()
bySex = penguins.groupby('sex')
pendes = bySex.describe()
penguins2 = penguins.assign(bill_area=penguins.bill_length_mm * penguins.bill_depth_mm)
byfem = penguins.loc[bySex.groups['female'].values]
bySpeciesf = byfem.groupby(['species']).aggregate({"bill_length_mm":np.mean})
penguinsfinal = penguins.assign(body_mass_kg=penguins.body_mass_g * 1000)
penguinsfinal_no_g = penguinsfinal.drop(columns=["body_mass_g"])
print(pendes)
print(penguins2)
print(byfem)
print(bySpeciesf)
print(penguinsfinal_no_g)