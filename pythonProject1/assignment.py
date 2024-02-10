weight = int(input ( "weight: "))
metric = "l or L and k or K"
input( "(K)g or (L)bs: ")

if metric.upper() == "K" :
    converted= weight / 0.45
    print("weight in Lbs: " + str(converted))

else:
    converted = weight * 0.45
    print ( "weight in Kgs: " + str(converted) )