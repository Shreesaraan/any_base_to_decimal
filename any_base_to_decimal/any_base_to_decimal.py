def any_base_to_decimal(number,base):
    decimal=0
    power=0
    while number>0:
        digit=number%10
        decimal+=digit*(base**power)
        number//=10
        power+=1
    return decimal


number=int(input("Enter the Number : "))
base=int(input("Enter the Base : "))
print(any_base_to_decimal(number,base))