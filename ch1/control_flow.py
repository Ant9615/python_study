#if-else 
x=5 
if x>=5 or x!=9:
    print("#1: {}".format(x))
else: 
    print("#1: 조건문에 안맞음") 

#elif 
if x>7: 
    print("#2: x는 7보다 큼")
elif x>1 and x<=3:
    print("#2: x는 1보다 크고 3보다 작음")
else: 
    print("#2: 사실 X는 5임")

#for 
y=['heart shaker', 'likey', 'signal','knock knock','tt','cheer up']
z=['병장','상병','일병','이병','훈련병']

for twice in y:
    print("#3: {!s}".format(twice))

#{0!s}을 선언하여 z의 요소 수만큼, {1!s}를 선언하여 요소를 순서대로 출력
for rank in range(len(z)):
    print("#3.{0!s}: {1!s}".format(rank, z[rank]))

for q in range(len(y)):
    if y[q].startswith('Q'):
        print("#3.5: {!s}".format(y[q])) 