n1,n2,n3,n4 = map(float, input().split())

media = ((n1*2)+(n2*3)+(n3*4)+(n4*1))/10
print('Media: %0.1f'%media)
if media >= 7.0:
    print('Aluno aprovado.')
if media < 5.0:
    print('Aluno reprovado.')
if media >= 5.0 and media < 7.0:
    print('Aluno em exame.')
    n_exame= float(input())
    print('Nota do exame: %0.1f'%n_exame)
    nfinal = (n_exame + media)/2
    if nfinal >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %0.1f'%nfinal)