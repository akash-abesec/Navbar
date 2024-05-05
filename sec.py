def find_palindromes(input, j, k):
  palindromes = []
  while j >= 0 and k < len(input) and input[j] == input[k]:
    palindromes.append(input[j: k + 1])
    j -= 1
    k += 1
  return palindromes


def find_palindromes_expand_from_center(input_string):
  palindromes = []
  for i in range(len(input_string)):
    palindromes += find_palindromes(input_string, i - 1, i + 1)
    palindromes += find_palindromes(input_string, i, i + 1)
  if len(palindromes)==0:
    return False
  return True


def find_winner(names, N):
    GFlag=True
    while len(names) != 1 and GFlag==True:
        substring = ""
        GFlag=False
        for name in names:
            substring += name[0]
            if find_palindromes_expand_from_center(substring.lower()):
                GFlag=True
                names.remove(name)
                break
    i = 0
    while len(names) > 1:
        i = (i + N - 1) % len(names)
        names.pop(i)

    return names[0]
names =input().split()
N = int(input())

winner = find_winner(names, N)
print(winner)



# def find_palindromes(input, j, k):
#   palindromes = []
#   while j >= 0 and k < len(input) and input[j] == input[k]:
#     palindromes.append(input[j: k + 1])
#     j -= 1
#     k += 1
#   return palindromes
# def find_palindromes_expand_from_center(input_string):
#   palindromes = []
#   for i in range(len(input_string)):
#     palindromes += find_palindromes(input_string, i - 1, i + 1)
#     palindromes += find_palindromes(input_string, i, i + 1)
#   if len(palindromes)==0:
#     return False
#   return True
# def find_winner(names, N):
#   GFlag=True
#   while len(names) != 1 and GFlag==True:
#     substring = ""
#     GFlag=False
#     for name in names:
#       substring += name[0]
#       if find_palindromes_expand_from_center(substring.lower()):
#         GFlag=True
#         names.remove(name)
#         break
#     i = 0
#     while len(names) > 1:
#       i = (i + N - 1) % len(names)
#       names.pop(i)
#     return names[0]
# names = input().split()
# N = int(input())
# winner = find_winner(names, N)
# print(winner)

# def find_pd(input,j,k):
#   pal=[]
#   while j>=0 and k<len(input) and input[j]==input[k]:
#     pal.append(input[j:k+1])
#     j-=1
#     k+=1
#   return pal
# def find_pc(input_string):
#   pal=[]
#   for i in range(len(input_string)):
#     pal+=find_pd(input_string,i-1,i+1)
#     pal+=find_pd(input_string,i,i+1)
#   if len(pal)==0:
#     return False
#   return True

# def find_w(names,N):
#   Gflag=True
#   while len(names)!=1 and Gflag==True:
#     substring=""
#     Gflag=False
#     for name in names:
#       substring +=name[0]
#       if find_pc(substring.lower()):
#         Gflag=True
#         names.remove(name)
#         break
#   i=0
#   while len(names)>1:
#     i=(i+N-1)%len(names)
#     names.pop(i)
#   return names[0]
# names=input().split()
# N=int(input())
# winner=find_w(names,N)
# print(winner)


