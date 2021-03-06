"""
Copyright (C) 2019 Interactive Brokers LLC. All rights reserved. This code is subject to the terms
 and conditions of the IB API Non-Commercial License or the IB API Commercial License, as applicable.
"""

### Adapted from TWS API samples/Python/Testbed/OrderSamples.py

from ibapi.order import (OrderComboLeg, Order)


class Orders:

    """ <summary>
    #/ A Market order is an order to buy or sell at the market bid or offer price. A market order may increase the likelihood of a fill 
    #/ and the speed of execution, but unlike the Limit order a Market order provides no price protection and may fill at a price far 
    #/ lower/higher than the current displayed bid/ask.
    #/ Products: BOND, CFD, EFP, CASH, FUND, FUT, FOP, OPT, STK, WAR
    </summary>"""
    @staticmethod
    def MarketOrder(action:str, quantity:float):
    
        #! [market]
        order = Order()
        order.action = action
        order.orderType = "MKT"
        order.totalQuantity = quantity
        #! [market]
        return order

    """ <summary>
    #/ A Limit order is an order to buy or sell at a specified price or better. The Limit order ensures that if the order fills, 
    #/ it will not fill at a price less favorable than your limit price, but it does not guarantee a fill.
    #/ Products: BOND, CFD, CASH, FUT, FOP, OPT, STK, WAR
    </summary>"""
    @staticmethod
    def LimitOrder(action:str, quantity:float, limitPrice:float):
    
        # ! [limitorder]
        order = Order()
        order.action = action
        order.orderType = "LMT"
        order.totalQuantity = quantity
        order.lmtPrice = limitPrice
        # ! [limitorder]
        return order
