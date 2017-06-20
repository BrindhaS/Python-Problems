def substrings(string):
   length = len(string)+1
   return [string[x:y] for x in range(length) for y in range(length) if string[x:y]]

   x=int(input('Enter test cases'))
   y=int(input('Enter length'))
   while(x>0):
    s = input('Enter string')
    lst = substrings(s)
    new_list = list(filter(lambda w:w[0]==w[len(w)-1], lst))
    print(len(new_list))
    x=x-1
