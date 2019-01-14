x = int(input())
import random
y = random.randint(0, 100)
while True:
    if y > x:
        print ('koochikeh')
        x = int(input('ye adade bozorgtar vared kon! '))
    elif x > y:
        print ('bozorgeh')
        x = int(input('ye adade koochktar vared kon! '))
    else:
        print ('wwwooooowwww  dorosteh!!!!!!!!!!!!!!!!!!')
        break


