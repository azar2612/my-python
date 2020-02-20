Num = int(input("Please Enter any Number: "))
 
Result = 0
def Result_Int(Num):
    global Result
    if(Num > 0):
        Reminder = Num %10
        Result = (Result *10) + Reminder
        Result_Int(Num //10)
    return Result
 
Result = Result_Int(Num)
print("n Reverse of entered number is = %d" %Result)