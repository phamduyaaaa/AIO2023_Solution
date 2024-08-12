#1
k = 3
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
sliding_window = []
for i in range(len(num_list)):
    sliding_window.append(num_list[i])
    if len(sliding_window)==k:
        print(max(sliding_window))
        sliding_window.pop(0)
#2
nums1 = list(input("list 1: "))
nums2 = list(input("list 2: "))
list_check =[]
for i in nums1:
    if i in nums2:
        list_check.append(i)
print(list_check)
#3
def count_chars(string:str):
    list_cnt = []
    list_chars = list(string)
    list_check = list(set(string))
    for i in list_check:
        cnt = 0
        for j in list_chars:
            if j == i:
                cnt +=1
        list_cnt.append(cnt)
    dict = {list_check[i]:list_cnt[i] for i in range(len(list_check))}
    return dict
print(count_chars("smiles"))
#4
def count_chars_txt(path: str) -> dict:
    list_cnt = {}
    with open(path,'r') as file:
        for line in file:
            chars = line.split()
            for char in chars:
                char = char.lower()
                if char in list_cnt:
                    list_cnt[char] +=1
                else:
                    list_cnt[char] = 1
    return list_cnt
path = 'data.txt'
print(count_chars_txt(path))
