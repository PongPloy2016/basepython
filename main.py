# Import ทัังหมดทุกฟังก์ชันใน Module
# import numbers

# Import มาบางฟังก์ชัน
# from numbers import factorial, fibonacci
# import ทุกฟังก์ชัน
# from numbers import *

# import และเปลี่ยนชื่อฟังก์ชัน (นามแฝง) alias
from numbers import factorial as fa, fibonacci as fi

# เรียกใช้งาน
# print(numbers.factorial(5))
# print(numbers.fibonacci(100))

print(fa(5))
print(fi(100))
