
# def getBondDuration(y, face, couponRate, m, ppy = 1):
#     return(8.51)

def getBondDuration(y, face, couponRate, m, ppy = 1):
    pv = [(1 + y) ** -x for x in range(1, m + 1)]
    cf = [face * couponRate if x != m else face + face * couponRate for x in range(1, m + 1)]
    pvcf = [pv[i] * cf[i] for i in range(m)]
    pvcft = sum([(i + 1) * pvcf[i] for i in range(m)])
    pvcfs = sum(pvcf)
    bondDuration = pvcft / pvcfs
    return(round(bondDuration, 2))

# Test values

y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1

result = getBondDuration(y, face, couponRate, m, ppy)
print(result)