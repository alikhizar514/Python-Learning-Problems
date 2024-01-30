
print("Ali is here")
number = input("Write a positive number:")
length = len(number)
number = int(number)
number1 = number
list_val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
list_numerals = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}

while(number<0):
    number = input("Write a positive number:")
    number = int(number)
else:
    n=0
    answer = ' '
    while(number>0):
        for i in range(len(list_val)):
            nm=number/list_val[i]
            if(nm>0):
                count = number/list_val[i]
                if(number/list_val[i]>0):
                    number =  number%list_val[i]
                    while(count>1):
                        count=count-1
                        answer += list_numerals[list_val[i]]
                    if(count==1):
                        answer += list_numerals[list_val[i]]

print("Number = ",number1, "Roman Numeral = ",answer)



