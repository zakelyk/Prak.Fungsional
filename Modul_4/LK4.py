import math

x = 3
y = 5
p = x,y
trans = 2,-1
dilat = 2,-1
rotate = 30

def translasi(p):
    global trans
    def transform(trans):
        tx,ty=trans
        x,y = p
        return x+tx, y+ty
    return transform

def dilatasi(p):
    global dilat
    def transform(dilat):
        sx,sy=dilat
        x,y=p
        return x*sx,y*sy
    return transform
    
def rotation(p):
    global rotate
    def transform(rotate):
        x,y=p
        radian = math.radians(rotate)
        return x*math.cos(radian) - y*math.sin(radian), y*math.sin(radian) + x*math.cos(radian)
    return transform

print("Koordinat setelah translasi: "+str(translasi(p)(trans)))
print("Koordinat setelah dilatasi: "+str(dilatasi(p)(dilat)))
print("Koordinat setelah rotasi: "+str(rotation(p)(rotate)))