e="true"
while(e=="true"):
    a = [x for x in input("input a string: ").split()]
    ans = ""
    for i in a:
        if 'a'<=i<='z' or 'A'<=i<="Z":
            if i == "and" or i == "or" or i == "of" or i == "to" or i == "in" or i=="is":
                continue
            else:
                c = (i[0]).upper()
                ans+=c
        else:
            print("Invalid input.")
    print(ans)
    print("Do you want to continue yes/no")
    c = input("yes or no: ")
    if c == "no":
        e="false"
    else:
        continue

