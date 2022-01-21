def IL(x,y,z):
    print(x,y,z)
    if len(z)==0:
        return True
    if (len(x)>0) and (len(y)>0) and (z[-1]==x[-1]) and (z[-1]==y[-1]):
        return IL(x[:-1],y,z[:-1]) or IL(x,y[:-1],z[:-1])
    elif (len(x)>0) and (z[-1]==x[-1]):
        return IL(x[:-1],y,z[:-1])
    elif (len(y)>0) and (z[-1]==y[-1]):
        return IL(x,y[:-1],z[:-1])
    else:
        return False
qwe = IL('dynamic','programming','dypnroagrmammiicng')
print(qwe)
qwe = IL('abc','qde','qabwce')
print(qwe)        