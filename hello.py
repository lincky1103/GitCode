# print ("Hello World!")
# a = -100
# if a >= 0:
#     print(a)
# else:
#     print(-a)
# =====================
# print ('''line1
# ...line2
# ...line3''')

# s3 =  r'''...Hello,
# ...Lisa!,
# ...NICE TO SEE YA!'''
# print(s3)
# =====================
# print('Hello,%s,%d' %('liao',3))
# ===============
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]

# print(L[2][2])
# ===================
# cars = 100
# space_in_a_car = 4.0
# drivers = 30
# passengers = 90
# cars_not_driven = cars - drivers
# cars_driven = drivers
# carpool_capacity = cars_driven*space_in_a_car
# average_passengers_per_car = passengers/cars_driven

# print(carpool_capacity) 

# =================================================
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# height = 1.75
# weight = 80.5
# BMI = weight/(height*height)
# if(BMI<18.5):
#     print('过轻')
# elif (18.5<=BMI<25):
#     print('正常')
# elif(25<=BMI<28):
#     print('过重😜')
# elif(28<=BMI<32):
#     print('肥胖')
# else:
#     print('严重肥胖')
# ==================================
# sum = 0
# for x in range(101):
#     sum = sum + x
# print(sum)

# =====================
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print(name)

# =====================
# i=0
# L = ['Bart', 'Lisa', 'Adam']
# while i<len(L):
#     print(L[i])
#     i=i+1
#     if i>1:
#         break

# =================
#计算平方根，有解无解尚需优化
#a不能等于0，delta大于等于0
# import math
# def quadratic(a,b,c):
#     delta = math.sqrt(b*b -4*a*c)
#     x1=(-b+delta)/(2*a)
#     x2=(-b-delta)/(2*a)
#     return x1,x2

# r = quadratic(1,2,1)
# print(r)

# ===========================
# 指数幂计算
# def power(x,n):
#     s=1
#     while n>0:
#         n = n-1
#         s = s*x
#     return s

# a = power(5,3)
# print(a)

# ==================
# 关键字参数
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name:', name, 'age:', age, 'other:', kw)

# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# ============================
# 命名关键字参数
def person(name, age, *, city='Beijing', job='Teacher'):
    print(name, age, city, job)

person('lincky',28)