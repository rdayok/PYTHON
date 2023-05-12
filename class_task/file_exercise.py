file = open("student_record.txt", mode='w')
file.write("001 mariam 75\n")
file.write("002 Segun 90\n")
file.write("003 Ebuka 80\n")
file.close()

# with open("records.txt", mode='w') as file:
#     file.write("001 mariam 75\n")
#     file.write("002 Segun 90\n")
#     file.write("003 Ebukizy 80\n")


with open("records.txt", mode='r') as records:
    for record in records:
        num, name, score = record.split()
        print(f"{num:<10} {name:<10} {score:<10}")
