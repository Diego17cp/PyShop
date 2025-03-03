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
            menu_products(id)
        elif option == '2':
            purchases_historial(id)
        elif option == '3':
            print('Cerrando sesión...')
            break
        else:
            print('❌ Opción no válida. Intente nuevamente.')
            menu(id)

def menu_products(user_id):
    while True:
        print('\nProductos')
        print('\n🎯 Recomendaciones Personalizadas')
        recommendations = final_recommend(user_id)

        if not recommendations:
            print('No hay productos recomendados para ti. 😢')
            return
        
        for idx, product in enumerate(recommendations, 1):
            print(f"🔹 {idx}. {product['nombre']} - {product['categoria']} - ${product['precio']}")

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
            result = list_products_by_category('Tecnología', user_id)
        elif option == '2':
            result = list_products_by_category('Periféricos', user_id)
        elif option == '3':
            result = list_products_by_category('Electrodomésticos', user_id)
        elif option == '4':
            result = list_products_by_category('Deportes', user_id)
        elif option == '5':
            result = list_products_by_category('Hogar', user_id)
        elif option == '6':
            result = list_products_by_category('Libros', user_id)
        elif option == '7':
            result = list_products_by_category('Salud', user_id)
        elif option == '8':
            result = list_products_by_category('Moda', user_id)
        elif option == '9':
            break
        else:
            print('❌ Opción no válida. Intente nuevamente.')
            continue
        if result == 'main_menu':
            break
        elif result == 'back':
            continue

if __name__ == '__main__':
    inicio()