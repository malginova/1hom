def ip(n):
    octet1 = (n >> 24) & 255
    octet2 = (n >> 16) & 255
    octet3 = (n >> 8) & 255
    octet4 = n & 255
    address = f"{octet1}.{octet2}.{octet3}.{octet4}"
    
    return address

def __main__():
    print(ip(2149583361)) 
    print(ip(32))          
    print(ip(1))
    
if __name__ == "__main__":
    __main__()