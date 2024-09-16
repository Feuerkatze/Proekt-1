immutable_var = (1,2,3, "Привет", False, [3,2,1]) # 1 задание
print(immutable_var)
immutable_var = 1,2,3, "Привет", False
print(immutable_var)
#immutable_var[1]=3  - не изменяется элемент в составе картежа
#print(immutable_var)
mutable_list = [1,2,3, "Привет","2ka",False]
print(mutable_list)
mutable_list[4] = 'mir' # в составе списка с [] скобками элементы могут быть изменены
print(mutable_list)
