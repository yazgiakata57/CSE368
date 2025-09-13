# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 

"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop

#takes an order list and a list of fruitshops
#returns fruitshop where order costs the least
def shopSmart(orderList, fruitShops):
    """
        orderList: List of (fruit, numPound) tuples
        fruitShops: List of FruitShops
    """
    "*** YOUR CODE HERE ***"
    # shop to return
    ret_shop=fruitShops[0]
    #price at the shop
    ret_price=fruitShops[0].getPriceOfOrder(orderList)

    #iterate through all fruit shops
    for fruitShop in fruitShops:
        #estimate the total order cost
        total_cost= fruitShop.getPriceOfOrder(orderList)
        #am i returning this shop?
        if total_cost<ret_price:
            ret_price=total_cost
            ret_shop=fruitShop
    
    return ret_shop


# #estimate cost for all order
# def estimateCost(orderList, fruitShopDir):
#     #set up accumulator for totalcost
#     totalCost = 0.0

#     #want to iterate over our fruit list
#     for fruit, n in orderList:
#         #if we have the fruit in the prices
#         if fruit in fruitShopDir:
#             #calculate the total cost of the fruit price per fruit we have
#             totalCost += fruitShopDir[fruit]*n
#         else:
#             #otherwise the fruit is not in out list so tell user it is not here
#             print ('fruit not here!') 
#     return totalCost



if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    orders = [('apples', 1.0), ('oranges', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]
    print("For orders ", orders, ", the best shop is", shopSmart(orders, shops).getName())
    orders = [('apples', 3.0)]
    print("For orders: ", orders, ", the best shop is", shopSmart(orders, shops).getName())
