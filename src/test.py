from db import * 
from predict import shopping_list_for_household

shopping_list_for_household(1, 55)

print(len(Household.select()))

for household in Household.select():
    print(household.id)
    break
    print('============================================================')