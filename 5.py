def party(names):
    l=names.upper().split(';')
    l.sort(key=lambda x: (x.split(':')[1], x.split(':')[0]))
    res=''
    for i in l:
        first, last = i.split(':')
        res+=f'({last}, {first}) '
    return res

def __main__():
    input_list ="Fired:Corwill;Wilfred:Corwill;Barney:TornBull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"
    print(party(input_list))

if __name__ == "__main__":
    __main__()