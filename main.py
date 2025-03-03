from module_funcs import *

def inicio():
    print('\n' + '='*50)
    print('🛍️  Bienvenido a PyShop - Tu Tienda Online 🛍️')
    print('='*50)
    while True:
        print('\n📝 Inicie Sesión o Regístrese')
        print('╔══════════════════════╗')
        print('║ 1. Iniciar Sesión    ║')
        print('║ 2. Registrarse       ║')
        print('║ 3. Salir             ║')
        print('╚══════════════════════╝')
        option = input('➤ Opción: ')
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
            print('\n👋 Gracias por visitarnos. ¡Vuelva pronto! 💫')
            break
        else:
            print('❌ Opción no válida. Intente nuevamente.')
            inicio()

def menu(id):
    while True:
        data_user = get_user_data(id)
        print('\n' + '='*50)
        print(f'👤 Bienvenido {data_user["usuario"].values[0]}!')
        print('='*50)
        print('\n📱 Menú Principal')
        print('╔═════════════════════════╗')
        print('║ 1. Ver Productos        ║')
        print('║ 2. Historial Compras    ║')
        print('║ 3. Cerrar Sesión        ║')
        print('╚═════════════════════════╝')
        option = input('➤ Opción: ')
        if option == '1':
            menu_products(id)
        elif option == '2':
            purchases_historial(id)
        elif option == '3':
            print('\n🔄 Cerrando sesión...')
            break
        else:
            print('❌ Opción no válida. Intente nuevamente.')
            menu(id)

def menu_products(user_id):
    while True:
        print('\n' + '='*50)
        print('🛒 Catálogo de Productos')
        print('='*50)
        print('\n🎯 Recomendaciones Personalizadas Para ti:')
        print('-'*50)

        recommendations = final_recommend(user_id)
        if not recommendations:
            print('No hay productos recomendados para ti. 😢')
            return
        
        for idx, product in enumerate(recommendations, 1):
            print(f"📦 {idx}. {product['nombre']}")
            print(f"   └─ {product['categoria']} | ${product['precio']:.2f}")

        print('\n📋 Categorías Disponibles')
        print('╔═════════════════════════╗')
        print('║ 1. Tecnología           ║')
        print('║ 2. Periféricos          ║')
        print('║ 3. Electrodomésticos    ║')
        print('║ 4. Deportes             ║')
        print('║ 5. Hogar                ║')
        print('║ 6. Libros               ║')
        print('║ 7. Salud                ║')
        print('║ 8. Moda                 ║')
        print('║ 9. Volver               ║')
        print('╚═════════════════════════╝')
        option = input('➤ Seleccione una categoría: ')
        categories = {
            '1': 'Tecnología',
            '2': 'Periféricos',
            '3': 'Electrodomésticos',
            '4': 'Deportes',
            '5': 'Hogar',
            '6': 'Libros',
            '7': 'Salud',
            '8': 'Moda'
        }

        if option in categories:
            result = list_products_by_category(categories[option], user_id)
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