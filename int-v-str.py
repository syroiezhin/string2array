str = "0.123,4 56"

def search(str):
    result = []
    enumerator = 0
    while enumerator < len(str):
        overwriting = ''
        symbol = str[enumerator]
        
        while '0' <= symbol <= '9':
            overwriting += symbol
            enumerator += 1
            print("(",enumerator,"/",len(str),") :",symbol,"⮕ ",overwriting)
            
            if enumerator < len(str): symbol = str[enumerator]
            else: break
        
        enumerator += 1
        if overwriting != '': result.append(overwriting)
    return result

if __name__== '__main__':
    print( "\n", ', '.join(search(str)) )