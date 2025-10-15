"""
Hari ke 5 python
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""
a = 7
y = 5
lebar = 30
hasil = 10
print(f"Jumlah {a} ditambah {y}".ljust(lebar)," = ", f"{(a + y):,.2f}".rjust(hasil))
print(f"Jumlah {a} dikurang {y}".ljust(lebar)," = ", f"{(a - y):,.2f}".rjust(hasil))
print(f"Jumlah {a} dikali {y}".ljust(lebar), " = ", f"{(a * y):,.2f}".rjust(hasil))
print(f"Jumlah {a} dibagi {y}".ljust(lebar), " = ", f"{(a / y):,.2f}".rjust(hasil))
print(f"Sisa {a} dibagi {y}".ljust(lebar), " = ", f"{(a + y):,.2f}".rjust(hasil))
print(f"{a} pangkat {y}".ljust(lebar), " = ", f"{(a ** y):,.2f}".rjust(hasil))
print(f"Integer {a} pembagian integer {y}".ljust(lebar), " = ", f"{(a // y):,.2f}".rjust(hasil))

x = 5
x += 3
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3
# x &= 3
# x |= 3
# x ^= 3
# x >>= 3
# x <<= 3
print (x)

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
