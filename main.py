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
            pass
        elif option == '2':
            pass
        elif option == '3':
            print('Cerrando sesión...')
            break
        else:
            print('❌ Opción no válida. Intente nuevamente.')
            menu(id)

if __name__ == '__main__':
    inicio()