def reverse(s):
    words=s.split(" ")
    k=[i[::-1] for i in words]
    new=" ".join(k)
    print(new)
s=input()
reverse(s)