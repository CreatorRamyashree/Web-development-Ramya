print("Enter marks obtained in 4 subjects: ")
math = int(input("math: "))
english = int(input("english: "))
science = int(input("science: "))
literature = int(input("literature: "))

sum = math+english+science+literature
print("sum of math,english,science, and literature")

perc = (sum/400)*100

print(end= "Percentage Mark = ")
print(perc)