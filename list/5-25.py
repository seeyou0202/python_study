phone_list1=["010-2694-1608", "010-2639-8003", "010-3244-7648"]
print(phone_list1)
phone_list2=[]
for number in phone_list1:
    x=number.replace("-", "")
    phone_list2.append(x)
    print(phone_list2)
