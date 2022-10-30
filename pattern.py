# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     print('\n')

# for i in range (6):
#     for j in range(6-i):
#         print(" ",end=' ')
#     for k in range(i+1):
#         print("*",end=" ")
#     print('\n')

# for i in range(5):
#     for j in range(i):
#         print("*",end=" ")
#     print('\n')
# for i in range (5):
#     for j in range(5-i):
#         print("*",end=" ")
#     print('\n')

# for i in range(6):
#     for j in range(6-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print('\n')
# for i in range(6):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(6-i):
#         print("*", end=" ")
#     print('\n')

# g=1
# for i in range(6):
#     for j in range(i):
#         print(g,end=" ")
#         g+=1
#     print('\n')

# for i in range(6):
#     for j in range(i):
#         print("*",end=" ")
#     for k in range(6-1-i):
#         print(" ", end=" ")
#     for o in range(6-1-i):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print('\n')

for i in range(6):
    for j in range(i):
        print("*",end=" ")
    for k in range(6-1-i):
        print(" ", end=" ")
    for o in range(6-1-i):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print('\n')
for i in range(6):
    for j in range(5-i-1):
        print("*",end=" ")
    for k in range(i+1):
        print(" ", end=" ")
    for o in range(i+1):
        print(" ",end=" ")
    for j in range(5-i-1):
        print("*",end=" ")
    print('\n')

print("yash jain pattern programs")