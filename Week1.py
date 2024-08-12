import math
import random
#1
def calculate_cube_volume(s):
    # s là cạnh
    return s**3
def calculate_rectangular_volume(l,w,h):
    # l là chiều dài, w là chiều rộng, h: là chiều cao
    return l*w*h
def calculate_round_cylinder_volume(r,h):
    # r là bán kính đáy, h là chiều cao
    return math.pi*(r**2)*h
def calculate_shpere_volume(r):
    # r là bán kính hình cầu
    return 4/3*(math.pi*(r**3))

print(calculate_cube_volume(3))
print(calculate_rectangular_volume(1,2,3))
print(calculate_round_cylinder_volume(1.2,4))
print(calculate_shpere_volume(1.3))
#2
def calculate_f1_score(tp,fp,fn):
    if not isinstance(tp,int):
        print("tp must be int")
        return -1
    if not isinstance(fp,int):
        print("fp must be int")
        return -1
    if not isinstance(fn,int):
        print("fn must be int")
        return -1
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must be greater than zero")
        return -1
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1_score = 2*((precision*recall)/(precision+recall))
    print("precision is ",precision)
    print("recall is ",recall)
    print("f1 - score is ",f1_score)

calculate_f1_score(2,3,4)
#3
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True
def activation_function(x):
    if is_number(x):
        type = input("Choose activation function you want ( binary | sigmoid | elu ): ")
        if type =="binary":
            return x if x<0 else 1
        elif type =="sigmoid":
            return 1/(1+math.e**(-x))
        elif type =="elu":
            alpha = int(input("alpha: "))
            if x<0:
                return x if x>= 0 else alpha*(e**x-1)
        else:
            print(f"{type} is not supported")
    else:
        print("x must be a number")

print(activation_function(4))
#4
def regression_loss_function(num_samples):
    if isinstance(num_samples,int):
        loss_name = input("Choose loss function you want ( MAE | MSE | RMSE ): ")
        loss = 0
        if loss_name == "MAE":
            for sample in range(num_samples):
                pred = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss += math.fabs(pred-target)
                print(f"loss name: {loss_name}, sample: {sample}, pred: {pred}, target: {target}, loss: {loss}")
            loss = (1/num_samples)*loss
            print(f"final {loss_name}: {loss}")
        elif loss_name == "MSE":
            for sample in range(num_samples):
                pred = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss += (pred-target)**2
                print(f"loss name: {loss_name}, sample: {sample}, pred: {pred}, target: {target}, loss: {loss}")
            loss = (1/num_samples)*loss
            print(f"final {loss_name}: {loss}")
        elif loss_name == "RMSE":
            for sample in range(num_samples):
                pred = random.uniform(0, 10)
                target = random.uniform(0, 10)
                loss += (pred-target)**2
                print(f"loss name: {loss_name}, sample: {sample}, pred: {pred}, target: {target}, loss: {loss}")
            loss = math.sqrt((1/num_samples)*loss)
            print(f"final {loss_name}: {loss}")
        else:
            print(f"{loss_name} is not supported")

    else:
        print("number of samples must be an integer number")

regression_loss_function(5)
#5
def pascal_triangle(level):
    if level < 1:
        return
    queue = [1]
    print(queue)
    for i in range(1, level):
        new_row = [1]
        for j in range(1, len(queue)):
            new_row.append(queue[j - 1] + queue[j])
        new_row.append(1)
        print(new_row)
        queue = new_row
pascal_triangle(10)

def fibonacci_sequence(length):
    if length == 1:
        return 0
    elif length == 2:
        return 1
    return fibonacci_sequence(length-1)+fibonacci_sequence(length-2)

print(fibonacci_sequence(1))

def giaithua(n):
    results = 1
    for i in range(1,n+1):
        results *=i
    return results
#6
def approx_sin(radian,n):
    results = 0
    for i in range(n):
        term = ((-1) ** i) * (radian ** (2 * i + 1)) /(giaithua(2*i+1))
        results += term
    return results
def approx_cos(radian,n):
    result = 1
    for i in range(1,n+1):
        term = ((-1)**i)*(radian**(i*2))/(giaithua(i*2))
        result+=term
    return result
def approx_sinh(radian,n):
    results = 0
    for i in range(n):
        term = (radian ** (2 * i + 1)) /(giaithua(2*i+1))
        results += term
    return results
def approx_cosh(radian,n):
    result = 1
    for i in range(1,n+1):
        term = (radian**(i*2))/(giaithua(i*2))
        result+=term
    return result
print(approx_sin(3.14,10))
print(approx_cos(3.14 ,10))
print(approx_sinh(3.14 ,10))
print(approx_cosh(3.14 ,10))

#7
def count_number(n):
    cnt = 1
    while n>=10:
        cnt +=1
        n//=10
    return cnt
def inverse_number(n):
    new = 0
    num_digits = count_number(n)
    for i in range(num_digits):
        digit = n % 10
        new += digit * 10 ** (num_digits - i - 1)
        n //= 10
    return new
print(inverse_number(123456789))
