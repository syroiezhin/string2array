str = ".00,0500.0...0.600 .... .08000,,,"

def search(str):
    result = []
    enumerator = 0
    while enumerator < len(str):
        overwriting = ''
        symbol = str[enumerator]
        while '0' <= symbol <= '9' or symbol == '.':
            overwriting += symbol
            enumerator += 1
            if enumerator < len(str): symbol = str[enumerator]
        enumerator += 1
        if overwriting != '': 
            print("(",enumerator,"/",len(str),") :", overwriting, end=" ")
            # remove all surplus dots  after  the comma
            if ( n:=overwriting.count('.') ) > 1: 
                overwriting = (''.join(overwriting[::-1].split(".", n-1)))[::-1]
            # Pay attention, the sequence is important, you need to make sure that we are not dealing with a point, otherwise we will not be able to process the point in a float.
            if overwriting == '.' or float(overwriting) == 0: overwriting = '0' 
            else:                 
                # remove all surplus zeros before the decimal point
                while overwriting[0] == '0': overwriting = overwriting[1:]
                # set the missing zero before the decimal point
                while overwriting[0] == '.': overwriting = (overwriting[::-1] + "0")[::-1]
                # remove all surplus zeros after  the decimal point
                while overwriting[-1] == '0': overwriting = overwriting[:-1]
                
            result.append(overwriting)
            print("⮕ ",overwriting)
    return result

if __name__== '__main__':
    print( "\nThat's what was: ", str, "\n" )
    print( "\nThat's what now:", ', '.join(search(str)), "\n" )