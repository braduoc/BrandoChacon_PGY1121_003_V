inv = []
asi = []
gan = []
total = 0
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
x
while True:
  print ("""1.compra entradas
  2.mostrar ubicaciones disponibles
  3.ver listado de asistente
  4.mostrar ganacias totales
  5.salir""")
  op = int(input("ingrese el numero de la opcion que desea realizar:  "))
  if op == 1:
    while True:  
      print(x)
      print("""     Platinum, $120.000. (Asientos del 1 al 20).
      Gold, $80.000. (Asientos del 21 al 50).
      Silver, $50.000. (Asientos del 51 al 100.).""")
      com = int(input("ingrese el numero de asiento que desea comprar:  "))
      rut = int(input("ingrese su rut para registrar el asiento a su rut: "))
      if com > 0 and com < 21:
        total = total + 120000
      if com > 20 and com < 51:
        total = total + 80000
      if com > 50 and com < 101:
        total = total + 50000
      x.remove(com)
      inv.append(rut)
      asi.append(com)
      gan.append(total)
      print(x)
      print("su reserva se a realizado con exito")
      otracom = int(input("desea comprar otro asiento?  1 = si / 2 = no:  "))
      if otracom == 1:
        True
      if otracom == 2:
        break
  print(f" el total de la compra es: {total}")
  if op == 2:
    print(f"los asientes disponibles son {x}")
  if op == 3:
    print(f"invitados:  {inv}")
    print(f" asientos:  {asi}")
  if op == 4:
    print("detalle de venta:  ")
    print(f"ventas:   {gan}")
    print(f"asiento:  {asi}")
    print(f"cliente:  {inv}")
    import numpy as np
    gan = np.array(gan)
    print("la ganancia total es: ", gan.sum())
  if op == 5:
    print("gracias hasta luego")
  otraop = int(input("desea hacer otra operacion?  1 = si / 2 = no:  "))
  if otraop == 1:
    True
  if otraop == 2:
    break