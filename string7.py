t = input()
l = int(len(t))
if len(t) %2 == 0:
        print(t[0], t[-1])
else:
        sr = l // 2
        print(t[0], t[sr], t[-1])