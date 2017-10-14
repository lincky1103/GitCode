def silly():
    res = []
    done = False
    while not done:
        elem = input('Enter elements, return when done：')
        if elem == '':
            done = True
        else:
            res.append(elem)
    tmp = res
    
    #print(res)
    tmp.reverse()
    print(tmp)
    isPal = (res == tmp)
    if isPal:
        print('isPal')
    else:
        print('notPal')
