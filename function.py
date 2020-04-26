# การสร้างฟังก์ชันแบบไม่มีการ return value
def hello(name):
    print(f"Hello {name}")


# สร้างฟังก์ชันแบบมีการ Return Value
def area(width, height):
    total = width * height
    return total


# เรียกใช้งานฟังก์ชัน hello()
hello("Samit")

# เรียกใช้งานฟังก์ชัน area()
print(area(5, 8))
print("พื้นที่ทั้งหมด", area(15, 7.5))
print()


# ฟังก์ชันแบบมีค่าเริ่มต้น
def show_info(name="", salary=0.00, lang="not define"):
    print(f"Name: {name}")
    print(f"Salary: {salary}")
    print(f"Language: {lang}")


# เรียกใช้งานฟังก์ชัน show_info()
show_info()
print()
show_info('Samit', 12000, 'PHP')
