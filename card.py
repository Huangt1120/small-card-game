switch = 0
h1 = ['1', '2', '3', '4']
h2 = ['5', '6', '7', '8']
no = []
run = True
while run:
    if switch % 2 == 0:
        print(h1)
        in1 = input('p1, pick a card: ')
        while in1 not in h1:
            in1 = input('p1, pick a card: ')
        print('ok')
        h1.remove(in1)
        if h1 == no:
            run = False
        switch += 1
    else:
        print(h2)
        in2 = input('p2, pick a card: ')
        while in2 not in h2:
            in2 = input('p2, pick a card: ')
        print('ok')
        h2.remove(in2)
        if h2 == no:
            run = False
        switch += 1
