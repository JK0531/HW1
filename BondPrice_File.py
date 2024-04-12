

# def getBondPrice(y, face, couponRate, m, ppy=1):
#     if ppy == 1:
#         x = 2170604
#     if ppy == 2:
#         x = 2171686
#     return(x)


def getBondPrice(y, face, couponRate, m, ppy = 1):
    if ppy == 1:
        pv = [(1 + y) ** -x for x in range(1, m + 1)]
    if ppy == 2:
        pv = [(1 + y / 2) ** -x for x in range(1, m * 2 + 1)]
    bondPrice = (sum(pv) * couponRate / ppy + pv[-1]) * face
    return(int(round(bondPrice, 0)))

# Test values
y = 0.03
face = 2000000
coupon_rate = 0.04
m = 10
ppy = 1
result1 = getBondPrice(y, face, coupon_rate, m, ppy)
print(result1)

ppy = 2
result2 = getBondPrice(y, face, coupon_rate, m, ppy)
print(result2)
