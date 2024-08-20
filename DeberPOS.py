carrito=[]
total=0.0

def mostrar_menu():
    print(" Bienvenido al POS")
    print("1. Agregar producto al carrito")
    print("2. Ver total del carrito")
    print("3. Pagar")
    print("4. Eliminar producto")
    print("5. Salir")
    
def agregar_producto():
    global total
    producto = input("Ingrese el nombre del producto: ")    
    precio = float(input("Ingrese el precio del producto: "))
    carrito.append({"producto": producto, "precio": precio})
    total +=precio
    print(f"Has agregado {producto} al carrito por {precio}.")
    
def ver_total():
    print("Productos en tu carrito:")
    for i, item in enumerate(carrito):
        print(f"{i + 1}. {item['producto']} - {item['precio']:.2f}")
    print(F"El total de tu carrito es: {total:.2f}")
    
def pagar():
    global total, carrito
    if total == 0:
        print("Tu carrito esta vacio, no hay nada que pagar.")
    else:
        print(f"El total a pagar es: {total:.2f}")
        pago = float(input("Ingrese la cantidad con la que vas a pagar:"))
        if pago >= total:
            cambio = pago - total
            print(f"Pago realizado con exito: Tu cambio es: {cambio:.2f}")
            carrito = []
            total=0.0
        else:
            print("No tienes suficiente dinero para pagar.")

def eliminar_producto():
    global total
    if carrito == []:
        print("El carrito está vacío, no hay nada que eliminar.")
        return
    
    print("Productos en tu carrito:")
    for i, item in enumerate(carrito):
        print(f"{i + 1}. {item['producto']} - {item['precio']:.2f}")
    
    opcion = int(input("Seleccione el número del producto que desea eliminar: "))
    
    if 1 <= opcion <= len(carrito):
        producto_eliminado = carrito.pop(opcion - 1)
        total -= producto_eliminado['precio']
        print(f"Has eliminado {producto_eliminado['producto']} del carrito.")
    else:
        print("Opción no válida, por favor vuelve a intentarlo.")
            
def ejecutar():
    while True:
        mostrar_menu()
        opcion = int(input("Seleccione una opcion: "))
    
        if opcion == 1:
            agregar_producto()
        elif opcion == 2:
            ver_total()
        elif opcion == 3:
            pagar()
        elif opcion == 4:
            eliminar_producto()
        elif opcion == 5:
            print("Gracias por usar el POS, ¡Hasta Luego!")
            break
        else: 
            print("Opcion no valida, por favor vuelve a intentarlo")
    
ejecutar()