N = 0
e = 0
d = 0

def gcd(m,n):
	while (n != 0):
		t = m%n
		(m,n) = (n,t)
	return abs(m)

def makeKey(p,q):
	print("Calculating...")
	global e
	e = 2
	while True:							#공개키 생성
		if(gcd((p-1)*(q-1),e) == 1):
			break
		e = e+1
	print("[*] Public Key : "+str(p*q)+", "+str(e))

	global d
	d = 1
	while True:							#개인키 생성
		if((e*d) % ((p-1)*(q-1)) == 1):
			break
		d = d+1

	global N
	N = p*q 			#N 과 e는 공개 키, d는 개인키
	print("[*] Private Key : "+str(d))

def encrypt(RAWvalue):
	x = RAWvalue**e % N
	return x

def decrypt(x):
	a = x**d % N
	return a


print("-----------RSA Encryptor/Decryptor------------")
print("[*] input 2 prime number : ")
p = int(input())
q = int(input())

makeKey(p,q)

print("[*] encrypt 3 : "+str(encrypt(3)))
print("[*] decrypt 12 :"+str(decrypt(12)))