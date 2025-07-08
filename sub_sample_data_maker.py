from random import choice
from  csv import writer


# random data creation 
subject = [f"subject_{i+1}" for i in range(35)]
teacher = [f"t_{j+1}" for j in range(0)]
table = {
    # table[period_no] = { teacher: subject}
}

    # random table creation
for day in ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]:
    for period in [f"period_{i+1}" for i in range(8)]:
        temp = { # temp[teacher] = [subjects]
            teach : [] for teach in teacher
            }
        for sub in subject:
            teaching_teacher = choice(teacher)
            temp[teaching_teacher].append(sub)
        temp = { x : "|".join(y) for x,y in temp.items()}
        table[period] = temp
    with open(f"{day}.csv","w") as file:
         Csv_writer = writer(file,delimiter= ",")
         Csv_writer.writerow(["NAME"]+[f"period_{i+1}" for i in range(8)])
         for teach in teacher:
             temp = [teach] + [x for x in
                              [ table[f"period_{i+1}"][teach] for i in range(8)]]
             Csv_writer.writerow(temp)
