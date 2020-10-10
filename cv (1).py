fb=open("products.txt","r")
lines=fb.read().split("\n")
while True:
    match=[]
    request=raw_input("Enter a term to search:")
    if request=="exit":
        break
    else:
        lower=request.lower()
        for i in lines:
            linelower=i.lower()
            if lower in linelower:
                match.append(i)
        if len(match)==0:
            print"No Products found for",request
        else:
            print "Product Matching",request
            for k in match:
                print"\t",k
