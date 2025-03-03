from module_funcs import *

def inicio():
    print('Bienvenido a PyShop - Tienda Online 🛒')
    print('Inicie Sesión o Regístrese')
    print('1. Iniciar Sesión')
    print('2. Registrarse')
    print('3. Salir')
    option = input('Opción: ')
    if option == '1':
        login_user()
    elif option == '2':
        add_user()
    elif option == '3':
        print('Gracias por visitarnos. Vuelva pronto.')
    else:
        print('Opción no válida. Intente nuevamente.')
        inicio()

if __name__ == '__main__':
    inicio()