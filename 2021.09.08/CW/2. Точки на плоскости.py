quarter1 = quarter2 = quarter3 = quarter4 = 0
asi = []

for i in range(int(input())):
    x, y = [int(number) for number in input().strip().split()]
    if x == 0 or y == 0:
        asi.append((x, y))
    elif x > 0 and y > 0:
        quarter1 += 1
    elif y > 0 and x < 0:
        quarter2 += 1
    elif y < 0 and x < 0:
        quarter3 += 1
    else:
        quarter4 += 1

# for elem in asi:
#     print(elem)
if asi:
    print(*asi, sep='\n')
print(f'I: {quarter1}, II: {quarter2}, III: {quarter3}, IV: {quarter4}.')
