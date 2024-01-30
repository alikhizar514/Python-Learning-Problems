
students_tuple = ('Ali','Talha','Irtiqa','Husnain','Eman')

ict_grades= (50,95,92,75,90)
database_grades= (55,96,92,77,72)
datastructures_grades= (56,5,95,72,92)


average = 0 
highest = 0
lowest  = 0
for i in range(len(students_tuple)):
    count=0
    average = (ict_grades[i]+database_grades[i]+datastructures_grades[i])/3
    count=count+1
    print("\n\n",students_tuple[i]," ka data : ")
    print("Average Grade of ",students_tuple[i]," is ",average)   
    print("The highest Grade of ",students_tuple[i]," is ", max(ict_grades[i], database_grades[i], datastructures_grades[i]))
    print("The Lowest Grade of ",students_tuple[i]," is ", min(ict_grades[i], database_grades[i], datastructures_grades[i]))

    tuple_1=(average,max(ict_grades[i], database_grades[i], datastructures_grades[i]),min(ict_grades[i], database_grades[i], datastructures_grades[i]))
