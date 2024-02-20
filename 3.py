def digital_root(n):
    strn=str(n)
    if len(strn)==1:
        return int(strn)
    else:
        s=[int(x) for x in strn]
        return digital_root(sum(s))

def __main__():
    print(digital_root(132189))
    print(digital_root(493193))

    
if __name__ == "__main__":
    __main__()