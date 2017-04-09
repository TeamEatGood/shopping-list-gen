from db import *
import math

def push_list(shopping_list, key, value):
    if key in shopping_list:
        shopping_list[key].append(value)
    else:
        shopping_list[key] = [value]

def shopping_list_for_household(household, day):
    working = {}
    for transaction in Household.get(Household.id==household).transactions.join(Product).order_by(Transaction.DAY):
        if transaction.PRODUCT.SUB_COMMODITY_DESC in working:
            state_for = working[transaction.PRODUCT.SUB_COMMODITY_DESC]
            period = transaction.DAY-state_for['last']
            state_for['average-period'] = (state_for['average-period']*state_for['samples']+period)/(state_for['samples']+1)
            state_for['samples'] += 1
            state_for['periods'].append(period)
        else:
            working[transaction.PRODUCT.SUB_COMMODITY_DESC] = {
                                                                "average-period": 0, 
                                                                "samples": 0, 
                                                                "last": transaction.DAY, 
                                                                "periods": [],
                                                                "COMMODITY_DESC": transaction.PRODUCT.COMMODITY_DESC,
                                                                "id": transaction.PRODUCT.id
                                                               }

    shopping_list = {}
    for SUB_COMMODITY_DESC, state in working.items():
        if state['samples'] == 0:
            continue
        error = 0 
        for period in state['periods']:
            error += (period - state['average-period'])*(period - state['average-period'])
        if error/len(state['periods']) < 10 and math.fabs(day-state['last'] - state['average-period']) < math.sqrt(error/len(state['periods'])):
            push_list(shopping_list, state["COMMODITY_DESC"], {
                                                                "id": state["id"],
                                                                "name": SUB_COMMODITY_DESC,
                                                                "last_purchased": state[last],
                                                                "norm_interval": state["average-period"],
                                                                "amount": 0
                                                                })
        

    return shopping_list