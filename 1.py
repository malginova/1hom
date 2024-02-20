def filter_list(pos_list):
    return [x for x in pos_list if isinstance(x, int) and x >= 0]

def __main__():
    input_list = [1, "apple", 2, "banana", 3, "cherry", 4]
    print(filter_list(input_list))
    
if __name__ == "__main__":
    __main__