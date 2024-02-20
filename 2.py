def first_non_repeating_letter(str):
    for i in range(len(str)):
        if str.lower().count(str.lower()[i])==1:
            return str[i]
        
def __main__():
    print(first_non_repeating_letter('Hello'))
    print(first_non_repeating_letter('Anaconda'))

if __name__ == "__main__":
    __main__()