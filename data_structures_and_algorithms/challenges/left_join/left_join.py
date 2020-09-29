def left_join(d1,d2):
    arr=[]
    for elem in d1.keys():
        if elem in d2.keys():
            arr.append([elem,d1[elem],d2[elem]])
        else:
            arr.append([elem,d1[elem],None])

    return arr


if __name__ == "__main__":
    pass
    dict_one = {'fond':'enamored','wrath':'anger','diligent':'employed','outfit':'garb','guide':'usher'}
    dict_two = {'fond':'averse','wrath':'delight','diligent':'idle','guide':'follow','flow':'jam'}
    print(left_join(dict_one,dict_two))


