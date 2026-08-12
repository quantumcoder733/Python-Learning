try:
    lines = ["Ali","John","Musadiq"]
    with open("students.txt","x") as f:
        f.writelines(lines)

    with open ("students.txt","r") as f:
        for line in f.readlines:
            print("Student : ",line)

except FileNotFoundError:
    print("File was Not Found")


