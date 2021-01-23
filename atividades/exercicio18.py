import math
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cose = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O ângulo de {} tem o SENO: {:.2f}'.format(angulo,seno))
print('O ângulo de {} tem o COSSENO: {:.2f}'.format(angulo,cose))
print('O ângulo de {} tem a TANGENTE: {:.2f}'.format(angulo,tang))