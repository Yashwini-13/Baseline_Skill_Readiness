##  Addition 
num1 = 4
num2 = 7
sum = num1+num2
print("Addition:",sum)

## Subtraction
num1 = 5
num2 = 3
diff = num1-num2
print("Subtraction:",diff)

## Multiplicaton
num1 = 6
num2 = 2
product = num1 * num2
print("Product:",product)

## Division
num1 = 10
num2 = 3
divide = num1/num2
print("Division:",divide)

## Floor division 
num1 = 10
num2 = 3
fdivision = num1//num2
print("Floor division:",fdivision)

## Modulus 
num1 = 10
num2 = 3
print("Modulus:",num1%num2)

## Exponentialtion
print("Exponentiation:",2**2)


#############################    BITWISE OPERATORS    #############################

## AND (&)
print("AND operator:",5&3)
# For and operator it always converts 5 to binary that is dividing by 2 and also 3 
# For 5 = 101 , 3 = 011
# If both are 1 o/p is 1 

## OR (|)
print("OR operator:",5|3)
# For OR operator it always converts 5 to binary that is dividing by 2 and also 3 
# For 5 = 101 , 3 = 011
# If one of i/p is 1 o/p is 1 

## NOT(~)
print("NOT operator:",~5)
# For OR operator it follows the rule 
## Rule: ~n = -(n+1)

## LEFT SHIFT (<<)
print("Left Shift:",5<<1)
# For left shift  operator it is just like adding zeros at the end in binary
# For 5 = 101 
# 5 << 1 → shift left by 1 bit:
# Rule: n << k = n × (2^k)

## RIGHT SHIFT (>>)
print("Right Shift:",20>>2)
# For right shift  operator it is just like chopping bits off the end
# For 20 = 10100 
# 20 >> 1 → shift right by 1 bit
# Rule: n >> k = n // (2^k) (integer division)

## XOR(^)
print("Xor operator:",5^3)
# For 5 = 101 , 3 = 011
# XOR rule → 1 if bits are different, 0 if same