

# def getBondPrice_Z(face, couponRate, times, yc):
#     return(1996533)

def getBondPrice_Z(face, couponRate, times, yc):
    # for t, y in zip(times, yc):
    pv = [(1 + y) ** -t for t, y in zip(times, yc)] 
    bondPrice = (sum(pv) * couponRate + pv[-1]) * face
    return(int(round(bondPrice, 0)))
    


# Test values
yc = [.010,.015,.020,.025,.030]
times=[1,1.5,3,4,7]
face = 2000000
couponRate = .04

result = getBondPrice_Z(face, couponRate, times, yc)
print(result)