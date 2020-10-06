token = input().split(';')
trades = []*len(token)
keys = {}
# Use below function when printing solution
def printKeyAndWMA(key, weightedMovingAverage):
   print(str(key) + ": {:0.2f}".format(weightedMovingAverage))
class trd:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.quant = 0
        self.seq = 0

for index,line in enumerate(token):
    line = line.split(',')
    trade = trd()
    trade.key = line[0]
    trade.val = float(line[1])
    trade.quant = int(line[2])
    trade.seq = int(line[3])
    trades[index] = trade
    if trade.key not in keys:
        keys[trade.key] = []
    keys[trade.key].append(trade)

for t in trades:
    total = 0.0
    for items in keys[t.key]:
        if items.key:
            d
    

