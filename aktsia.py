#1
def max_income_for_one_operation(arr:list):
    max_diff = 0
    # # mini-optimisation
    # if index[max] > index[min]:
    #    return max-min
    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            max_diff = max(max_diff, arr[j]-arr[i])
    print(max_diff)

max_income_for_one_operation([1,2,2,0.5,1,0.5,2])

#1 v2
# failed(
def max_income_for_one_operation_v2(arr:list):
    max_diff = 0

    for i in range(len(arr)-1):
        for j in range(i, len(arr)):
            max_diff = max(max_diff, arr[j]-arr[i])
    print(max_diff)



#2
def max_income(arr:list):
    income = 0
    for i in range(len(arr)-1):
        if arr[i]<arr[i+1]:
            income+=arr[i+1]-arr[i]
    print(income)

max_income([1,2,2,0.5,1,0.5,2])



#3 можна робити з динамічним програмуванням (хз наскільки ефективно)

# array of intermediate values and just one operation

def max_income_for_two_operations(arr:list):
    intermediate_max_prices = [0 for i in arr]

    