import numpy as np

# temp = {'harden':13, 'curry':30, 'james':23, 'paul':3}
# a = sorted(temp.items(), key = lambda item:item[1], reverse = True)
# print(a)
# b = []
# for i in a:
#     b.append(i[0])
# print(b)
# b = b[0:3]
# print(b)

# a = 0
# x = []
# y = {'a':[]}
# for i in range(4):
#     a += 1
#     x.append(a)
# print(x)
# y['a'] = x
# print(y)


# temp = ['harden', 'curry', 'james', 'paul']
# temp1 = ['harden\n', 'curry\n', 'james\n', 'paul\n']
# x = 0
# for i in temp:
#     temp[x] = i + '\n'
#     x += 1
#
#
# print(temp)
# print(temp1)


# a = np.array([[1,2,3],[4,5,6]])
# b = np.transpose(a)
# print(type(a))
# print(a.shape)
# print(b)


# a = []
# for i in range(5):
#     a.append(0.123234)
# print(a)

# t = np.zeros((2,3))
# print(t)

# c = 1
# t = np.array([[1,2,3],[4,5,6]]).astype(float)
# for i in range(len(t)):
#     t[i, :] = t[i, :] / c
#     c += 1
#
# print(t)


# t1 = np.array([[1,2],[3,4]])
# t2 = np.ones((2,3))
# t3 = np.ones((3,2)) * 2
# t4 = np.ones((3,3)) * 3
# print(t1)
# print(t2)
# print(t3)
# print(t4)
# t5 = np.concatenate((t1, t2), axis = 1)
# t6 = np.concatenate((t3, t4), axis = 1)
# t7 = np.concatenate((t5, t6), axis = 0)
# print(t7)



# t = []
# t.append('harden')
# print(t)
# t.append('harden')
# print(t)
# print('harden' in t)
# c = 0
# t =[1, 1, 3]
# for i in t:
#     for j in t:
#         if i != j:
#             c += 1
# print(c)



# a = ['curry']
# b = ['harden']
# c = ['james']
#
# d = a + b + c
# print(d)




mz = np.loadtxt('dataset/sym_prio.txt')
print(mz.shape)

dxy = np.loadtxt('dataset_dxy/sym_prio_dxy.txt')
print(dxy.shape)