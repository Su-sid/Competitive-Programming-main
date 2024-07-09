damage_capability= list(map(int, input ().split()))
no_of_soldiers= list(map(int, input ().split()))
package_soldiers= list (zip(damage_capability,no_of_soldiers))

for i, value in enumerate(package_soldiers):
    package_soldiers[i]= value[0]*value[1]

bilbo_side, enemies= package_soldiers[:3], package_soldiers[-2:]

if sum(bilbo_side)== sum(enemies):
    print( 'DRAW')
elif sum (bilbo_side)< sum(enemies):
    print('LOSE')
else:
    print('WIN')