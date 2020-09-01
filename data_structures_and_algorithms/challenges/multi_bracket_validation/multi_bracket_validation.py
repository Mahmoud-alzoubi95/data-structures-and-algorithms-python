from collections import Counter

def multi_bracket_validation(input):
    # a=Counter(input)
    # # a=a.keys()

    # print(list(a))
    # print(a)
    curly_I =input.count('{')
    curly_II=input.count('}')
    parantheses_I =input.count('(')
    parantheses_II=input.count(')')
    bracket_I =input.count('[')
    bracket_II=input.count(']')
    openning=[curly_I,parantheses_I,bracket_I]
    closing=[curly_II,parantheses_II,bracket_II]

    
    if curly_I==curly_II and parantheses_I==parantheses_II and bracket_I==bracket_II:
        print("Equal")
        
        return True
    
    else:
        index=0
        for i,j in zip(openning,closing):
            if index ==0:
                if i>j:
                    return "error unmatched opening { remaining."
                if i<j:
                    return "error closing } arrived without corresponding opening."
            elif index ==1:
                if i>j:
                    return "error unmatched opening ( remaining."
                if i<j:
                    return "error closing ) arrived without corresponding opening."
            elif index ==2:
                if i>j:
                    return "error unmatched opening [ remaining."
                if i<j:
                    return "error closing ] arrived without corresponding opening."
            index+=1
                    
    
    
    

if __name__=='__main__':

    a=multi_bracket_validation("[]")
    print(a)