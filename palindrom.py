def str_palindrom(my_palindrom):
    my_list = []
    new_list = []
    for i in my_palindrom:
        my_list.append(i)
    for y in my_list:
        new_list.append(y)
    if my_list == new_list[::-1]:
        print(True)
    else:
        print(False)


str_palindrom('лепсспел')
#str_palindrom('helloworld')



