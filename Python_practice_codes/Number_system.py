# n=int(input("enter a number::"))

# print(bin(n))
# print(hex(n))
# print(oct(n))

def D_B(n):
	bin=''
	while n>0:
		bin= str(n%2)+bin
		n//=2
	return bin or 0
	
print("binary::",D_B(13))

def D_O(n):
	oct=''
	while n>0:
		oct=str(n%8)+oct
		n//=8
	return oct or 0
	
print("octal::",D_O(25))

def D_H(n):
	hex_char='0123456789ABCDEF'
	hex=''
	while n>0:
		hex= hex_char[n%16]+hex
		n//=16
	return hex or 0
	
print("hexadecimal",D_H(255))
 

