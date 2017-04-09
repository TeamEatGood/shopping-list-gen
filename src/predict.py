

def shopping_list_for_household(household):
    working = {}
    for transaction in Household.get(household.id==household).transactions.join(Product).order_by(Transaction.day):
        if transaction.PRODUCT.SUB_COMMODITY_DESC in working:
            state_for = working[transaction.PRODUCT.SUB_COMMODITY_DESC]
            state_for['average-period'] = (state_for['average-period']*state_for['samples']+transaction.day-state_for['last'])/(state_for['samples']+1)
            state_for['samples'] += 1
        else:
            working[transaction.PRODUCT.SUB_COMMODITY_DESC] = {"average-period": 0, "samples": 0, "last": transaction.day}
    return working