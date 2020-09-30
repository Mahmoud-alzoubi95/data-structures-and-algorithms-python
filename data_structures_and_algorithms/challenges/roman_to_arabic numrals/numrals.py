dict={"i":1, "v":5, "x":10, "l":50, "c": 100, "d":500, "m":1000}

# a=input("enter roman number : ").lower()
def splitLetters(roman):
        return [letter  for letter in roman]

def to_roman(rString):
    roman=rString.lower()

    

    a=splitLetters(roman)
    # for i in a:
    #     []
    output=0
    b=[dict[i] for i in a]
    for x,i in enumerate(b):
        if x ==len(b)-1:
            output+=i
            # print(output)
            break
        validate = b[x+1]<=i*10 and b[x+1]>i 
        if validate:
            b[x]=-i
        output+=b[x]
        # print(output)
    return output

a="XXX"
b="XLIX"
c="CXC"

print(to_roman(a))
print(to_roman(b))
print(to_roman("XCIX"))

# print(a,b)