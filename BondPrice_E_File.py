
# def getBondPrice_E(face, couponRate, m, yc):
#     return(2098949)

def getBondPrice_E(face, couponRate, m, yc):
    # pv = for index, item in enumerate(yc):
        # pv = (1+item)**-(index+1)
    pv = [(1 + item) ** -(index + 1) for index, item in enumerate(yc)]
    bondPrice = (sum(pv) * couponRate + pv[-1]) * face
    return(int(round(bondPrice, 0)))


# Test values

yc = [.010,.015,.020,.025,.030]
face = 2000000
couponRate = .04
m = 5

result = getBondPrice_E(face, couponRate, m, yc)
print(result)