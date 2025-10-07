#Q3
is_run = True
arr = []
def show_seat():
    count=0
    for i in range(10):
        for j in range(4):
            j=0
            arr.append(j)
            count += 1
            print(f"{count}.  {j}", end=' ')
        print()
while(is_run):
    show_seat()
    print("\n1.Book a Seat\n2.Cancel a Seat\nShow seat status\n0.Exit")
    inp = int(input("Enter the value: "))

    if inp==1:
        seat_num = int(input("Enter seat number to book ticket: "))
        
        if seat_num==0:
            is_run=False
            break
        else:
            print(len(arr))
            if arr[seat_num-1] is not 0:

                arr[seat_num-1]=1
                show_seat

    elif inp==0:
        is_run==False
        break
print("you logged out!")
