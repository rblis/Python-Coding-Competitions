'''
Naive Hedging Algorithm
Programming challenge description:
Problem Statement

In order to properly offload risk, we need to implement a trading algorithm which places trades to offset the risk of incoming trades (this is called hedging). Each incoming trade has some risk associated with it, defined as quantity * riskPerUnit

    For example, if an incoming trade has bought 20 units of risk, we should sell 20 units of risk to offset it. If the incoming trade buys 20.9 units of risk, we should still sell 20 units of risk to offset it because we cannot buy fractions of a stock. However, we should remember that there is still 0.9 risk to be covered, and add it to the amount of risk for the next trade.

Given two incoming trades, each with 0.5 units of risk, we should not make any trades when we receive the first trade, and then sell 1 when we receive the second trade.

    For each incoming trade, you'll output the corresponding trade to offset the risk, and the average fill price.

We can define the average fill price of a trade as

AvgFillPrice = Sum(quantity_i * price_i) / Sum(quantity_i)

    When we make a trade, we trade against the given market data, affecting the state of the market for future trades. For example, if the best price/quantity in the market to buy was quantity 100 for price $1850, and we bought 75 for $1850, there would only be 25 remaining at that price level. If, for example, our next trade was for a quantity of 30, we would execute 25 at the remaining price level, and then the remaining 5 at the next-best price level.

Input:

    The first two lines of each test case will represent the market data. Each line of market data will always have exactly 3 quantities and exactly 3 prices. You can assume there is enough quantity to fully offset all the risk of all incoming trades.
    The first line will represent the "offers", or prices you can buy at. The second line will represent the "bids", or prices you can sell at. When trading with the market, we buy at the cheapest price available, and sell at the highest price available.

Market data will be formatted as follows

<quantity1> <price1> <quantity2> <price2> <quantity3> <price3>
100 1850.00 200 1850.25 300 1850.50
100 1849.75 200 1849.50 300 1849.25

This means that the first 100 purchased will be bought at a price of 1850.00, and the next 200 will be bought at a price of 1850.25. Similarily, the first 100 sold will be sold at 1849.75, and the next 200 will be sold at 1849.50

If we were to purchase 300, we would fill 100 at 1850.00, and 200 at 1850.25, for an average fill price of 1850.17 (rounded to two decimal places).

Incoming trades are formatted as follows:

<signed_quantity> <risk_per_unit>
+10 0.20
+15 -0.20
-40 0.50

This means we traded, in order

    Buy quantity 10, risk per unit of 0.20 (risk is +2)
    Buy quantity 15, risk per unit of -0.20 (risk is -3)
    Sell quantity 40, risk per unit of 0.50 (risk is -20)

NOTE: You have been given skeleton code to help parse this input. You may alter this code as you wish, including not using it at all.
Output:

    We should output the trades required to offset the risk, as well as the average fill price. Buying is represented as a positive quantity, and selling is represented as a negative quantity.
    The average fill price should output exactly two decimal places, rounded. For example, 1849.6666666 should be rounded to 1849.67.

For the above input, this is the correct output

<quantity bought/sold> <average fill price>
-2 1849.75
3 1850.00
20 1850.00

Test 1
Test Input
100 1850.00 200 1850.25 300 1850.50
100 1849.75 200 1849.50 300 1849.25
+10 0.20
+15 -0.20
-40 0.50
Expected Output
-2 1849.75
3 1850.00
20 1850.00
Test 2
Test Input
100 1850.00 200 1850.25 300 1850.50
100 1849.75 200 1849.50 300 1849.25
+15 0.25
+1 0.25
Expected Output
-3 1849.75
-1 1849.75
'''