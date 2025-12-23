# unit=(int(input("Enter units consumed:")))
# total=0
# if unit>0 and unit<=100:
#     total+=unit*10
# elif unit >= 101 and unit <= 200:
#     total+=(100*10)+((unit-100)*15)
# else:
#     total += (100 * 10)+(100*15)
#     unit-=200
#     total+=unit*20
# print("Total bill=",total)
#
#
#
# age=int(input("Enter age:"))
# income=int(input("Enter income:"))
# if age<=60:
#   if income<=500000:
#     tax=(income*5)/100
#   elif income>=500001 and income<=1000000:
#     tax=(income*10)/100
#   else:
#     tax=(income*15)/100
# else:
#   tax=(income*5)/100
# print("Income Tax:",tax)
#
# distance=(int(input("Enter distance in km:")))
# age=int(input("Enter age:"))
# dis=distance*10
# fare=0
# if age<12:
#   fare=dis-((dis*50)/100)
# if age>=60:
#   fare=dis-((dis*25)/100)
# print("Ticket Fare:",fare)
#
#
# l=[]
# for i in range(0,5):
#   marks=int(input("Enter marks:"))
#   l.append(marks)
# def average(l):
#   s=0
#   for i in l:
#     s+=i
#   print("Average:",s/len(l))
# average(l)
#
# def highest_marks(l):
#   print("Highest score:",max(l))
# highest_marks(l)
#
# def grades(l):
#   grade=["A" if i>=90 else "B"if i>=75
#          else "C" if i>=60 else "F" for i in l]
#   return grade
# print(grades(l))


whole=[]
for k in range(0,3):
 id=int(input("Enter id:"))
 list1=[]
 print("Enter attendence for 5 days P for present \n A for absent")
 for i in range(0,5):
  list1.append(input())
 whole.append((id,list1),)
 print(whole)

def  attendance_percentage(whole):
      allper=[]
      for k in whole:
       c=sum(1  for j in k[1] if j.lower()=="p")
       allper.append((c*100)/5)
      return allper
print("Attendance per:",attendance_percentage(whole))

def low_attendance_students(whole, threshold):
   low=[]
   for index,i in enumerate(attendance_percentage(whole)):
     if i<threshold:
        low.append(whole[index][0])
   return low
print(low_attendance_students(whole, 75))

def absentCheck(whole):
    count=[sum(1 for i in whole if i[1][t].lower()=="a")for t in range(0,5)]
    for ind,i in enumerate(count):
      print("Day",ind+1,"Absent:" ,i)
absentCheck(whole)








l=[]
n=int(input("Enter number of items:"))
for i in range(1,n+1):
    item=int(input("Enter price of item:"))
    l.append(item)
def total(l):
    return (sum(i for i in l))
print("Total before discount:",total(l))
p=total(l)
a=(p-((p*5)/100) if n>=5 and n<=10 else  p-((p*10)/100) if n>=11 and n<=20 else p-((p*15)/100) if n>20 else p  )
print("Total after discount:",a)


inventory=[("Apple", 50, 30), ("Banana", 10, 20), ("Orange", 15, 10)]
def items_to_reorder(inventory):
    item=[i[0]  for i in inventory if i[1]<i[2]]
    return item


price_list=[100,200,400]
def total_stock_value(inventory, price_list):
    return sum(i[1]*price_list[ind] for ind ,i in enumerate(inventory) )

def overstock(inventory):
    item=[i[0] for i in inventory if i[1]>2*i[2]]
    return item

print("Total Stock value:",total_stock_value(inventory,price_list))
print("OverStock value:",overstock(inventory))
print("UnderStock value:",items_to_reorder(inventory))









# (p input
# (Start)
# -->
# (write"Enter unit consumed:")
# (read<unit>)
# (insert'ConditionCheck <unit>)
# (remove 1)))
#
#
# (p check
# (ConditionCheck <unit>>=0)
# (ConditionCheck <unit><=100)
# -->
# (insert'Print (unit*10))
# (remove 1)))
#
#
#
# (p check
# (ConditionCheck <unit>>100)
# (ConditionCheck <unit><=200)
# -->
# (insert'Print (100*10+((unit-100)*15)))
# (remove 1)))
#
#
#
# (p check
# (ConditionCheck <unit>>200)
# -->
# (insert'Print ((100*10)+((100*15)+((unit-200)*20))
# (remove 1)))
#
#
#
# (p print
# (Print <total>)
# -->
# (write "Total bill:"<total>)
# (remove1)
# )
#
#
# # Question2
#
# (p input
# (Start)
# -->
# (write"Enter age:")
# (read<age>)
# (write "Enter income:")
# (read<income>)
# (insert  'Process <income><age>)
# (remove 1)))
#
#
# (p process
# (Process <income><age><=60)
# (Process <income><age>  income<=500000)
# -->
# (insert  'Print ((income*5)/100))
# (remove 1)))
#
# (p process
# (Process <income><age><=60)
# (Process <income><age>  income>500000)
# (Process <income><age>  income<=1000000)
# -->
# (insert  'Print ((income*10)/100))
# (remove 1)))
#
# (p process
# (Process <income><age><=60)
# (Process <income><age>  income> 1,000,000)
# -->
# (insert  'Print ((income*15)/100))
# (remove 1)))
#
# (p process
# (Process <income><age>>60)
# -->
# (insert  'Print ((income*5)/100))
# (remove 1)))
#
#
# (p Print
# (Print <total>)
#  -->
# (write "Income Tax:"<total>)
# (remove 1))
#
# # Question3
# (p input
# (Start)
# -->
# (write"Enter distance(km):")
# (read<d>)
# (write"Enter age:")
# (read<age>)
# (insert ('Process <age> <d>*10))
# (remove1)
# )
#
# (p process
# (Process <age><d> age<12)
# -->
# (insert 'Print (<d>-((<d>*50)/100) )
# (remove 1))
#
#
# (p process
# (Process <age><d> age>=60)
# -->
# (insert `Print (<d>-((<d>*25)/100) )
# (remove 1))
#
# (P print
# (Print <total>)
# -->
# (write"Fare:"total)
# (remove1)
# )


