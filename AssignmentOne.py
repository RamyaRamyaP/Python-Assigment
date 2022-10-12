import collections
Number_of_inputs = int(input())
mydict = collections.OrderedDict()

for i in range(Number_of_inputs):
    myword = input()
    if myword in mydict:
        mydict[myword] += 1
    else:
        mydict[myword] = 1

print(len(mydict));

for k, v in mydict.items():
    print(v, end=" ");
