from module_funcs import *

def inicio():
    print('Bienvenido a PyShop - Tienda Online 🛒')
    while True:
        print('\nInicie Sesión o Regístrese')
        print('1. Iniciar Sesión')
        print('2. Registrarse')
        print('3. Salir')
        option = input('Opción: ')
        if option == '1':
            login_result = login_user()
            if login_result['response']:
                user_id = login_result['user_id']
                menu(user_id)
            else:
                continue
        elif option == '2':
            add_user()
        elif option == '3':
            print('Gracias por visitarnos. Vuelva pronto.')
            break
        else:
            print('❌ Opción no válida. Intente nuevamente.')
            inicio()

def menu(id):
    while True:
        data_user = get_user_data(id)
        print(f'\n👤 Bienvenido {data_user["usuario"].values[0]}')
        print('\nMenú Principal')
        print('1. Ver Productos')
        print('2. Ver Historial de Compras')
        print('3. Cerrar Sesión')
        option = input('Opción: ')
        if option == '1':
            menu_products()
        elif option == '2':
            pass
        elif option == '3':
            print('Cerrando sesión...')
            break
        else:
            print('❌ Opción no válida. Intente nuevamente.')
            menu(id)

def menu_products():
    print('\nProductos')
    print('Algunas recomendaciones para ti:')
    # Recomendaciones de productos
    print('Selecciona una de las categorías para ver más productos:')
    print('1. Tecnología')
    print('2. Periféricos')
    print('3. Electrodomésticos')
    print('4. Deportes')
    print('5. Hogar')
    print('6. Libros')
    print('7. Salud')
    print('8. Moda')
    print('9. Volver')
    option = input('Opción: ')
    if option == '1':
        list_products_by_category('Tecnología')
    elif option == '2':
        list_products_by_category('Periféricos')
    elif option == '3':
        list_products_by_category('Electrodomésticos')
    elif option == '4':
        list_products_by_category('Deportes')
    elif option == '5':
        list_products_by_category('Hogar')
    elif option == '6':
        list_products_by_category('Libros')
    elif option == '7':
        list_products_by_category('Salud')
    elif option == '8':
        list_products_by_category('Moda')
    elif option == '9':
        menu(id)
    else:
        print('❌ Opción no válida. Intente nuevamente.')
        menu_products()

if __name__ == '__main__':
    inicio()