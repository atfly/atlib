
#!/usr/bin/python3

days = 365

numPeople = 1

prob = 0

#有两个人的生日相同的概率大于50%时，停止循环。

while prob < 0.5:
    numPeople += 1
    prob = 1 - ((1-prob) * (days-(numPeople-1)) / days)
    print("Number of people:",numPeople)
    print("Prob. of same birthday:",prob)