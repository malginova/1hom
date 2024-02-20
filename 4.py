def count_target(nlist,n):
    k=0
    for i in range(len(nlist)-1):
        if nlist[i]+nlist[i+1]==n:
            k+=1
    return k

def __main__():
    input_list = [1, 3, 6, 2, 2, 0, 4, 5]
    print(count_target(input_list,5))
    print(count_target(input_list,9))

if __name__ == "__main__":
    __main__()