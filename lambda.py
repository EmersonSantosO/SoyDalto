multi = lambda x, y: x * y

print(multi(100,200))


suma = lambda x, y: x + y

print(suma(300,400))


#Sumar dos listas

list1 = [1,2,3,4,5,6]
list2 = [1,2,3,4,5,6]

resultados = list(map(lambda x , y: x + y, list1, list2))

print(resultados)

#ver numeros mayores que...

list3 = [3,9,8,10,32,12,1]

mayor_que = list(filter(lambda x:x>10,list3))
print(mayor_que)


#ordenar numeros

list_num = [5,1,4,12,33,123]

ordenar = sorted(list_num,key=lambda x: x/500)

print(ordenar)