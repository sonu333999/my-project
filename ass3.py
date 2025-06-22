p=float(input("enter marks:"))
chm=float(input("enter marks:"))
bio=float(input("enter marks:"))
com=float(input("enter marks:"))
maths=float(input("enter marks:"))
total_marks=(p+chm+bio+com+maths)
Percentage=(total_marks/500)*100
if Percentage >= 90% :
grade ="A"
elif Percentage >= 80% :
grade ="B"
elif Percentage >= 70% :
grade ="C"
elif Percentage >= 60% : 
grade ="D"
elif Percentage >= 40% : 
grade ="E"
elif Percentage < 40% : 
grade ="F"
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")