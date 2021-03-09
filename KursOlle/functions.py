import math

def area(r):
    """"Beräknar arean på cirkeln med r som radie som anges där nere"""
    c = r*r*math.pi 
    print(f"Arean är: {c}")

def omkrets():
    """"Beräknar omkretsen på cirkeln med r som radie som anges där nere"""
    global r
    c = r*2*math.pi
    print(f"Omkretsen är: {c}")


r = int(input("Välj din radie"))
print(f"Radien du valde: {r}")

area(r)
omkrets()