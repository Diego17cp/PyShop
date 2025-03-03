# Import libraries
import pandas as pd
import datetime as dt
# Define DataFrames with the csv's data
df_products = pd.read_csv('data/products.csv')
df_users = pd.read_csv('data/users.csv', dtype={'contraseña': str})
df_orders = pd.read_csv('data/orders.csv')

# Func add user
def add_user():
    global df_users
    new_id = df_users['usuario_id'].max() + 1 if not df_users.empty else 1
    name = input('Ingrese su nombre: ')
    user = input('Ingrese su usuario: ')
    password = input('Cree una contraseña: ')
    email = input('Ingrese su email: ')
    register_date = dt.datetime.now().strftime('%Y-%m-%d')

    new_user = {
        'usuario_id': new_id,
        'nombre': name,
        'usuario': user,
        'contraseña': password,
        'email': email,
        'fecha_registro': register_date
    }

    df_new_user = pd.DataFrame([new_user])

    df_users = pd.concat([df_users, df_new_user], ignore_index=True)
    df_users.to_csv('data/users.csv', index=False)
    print(f"✅ Usuario '{user}' agregado con éxito.")

# Func login user
def login_user():
    global df_users
    att = 3
    user = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')
    user_data = df_users[(df_users['usuario'] == user) & (df_users['contraseña'] == password)]

    while att > 0:
        user_data = df_users[(df_users['usuario'] == user) & (df_users['contraseña'] == password)]
        if not user_data.empty:
            print(f"✅ Iniciando sesión como '{user}'...")
            return {
                'response': True,
                'user_id': user_data['usuario_id'].values[0],
            }
        else:
            att -= 1
            if att > 0:
                print('❌ Usuario o contraseña incorrectos.')
                print(f'Intentos restantes: {att}')
                user = input('Ingrese su usuario: ')
                password = input('Ingrese su contraseña: ')
            else:
                print('❌ Ha superado el número de intentos permitidos. Intente más tarde.')
                return {
                    'response': False,
                }

# Func get data from user by id
def get_user_data(user_id):
    global df_users
    user_data = df_users[df_users['usuario_id'] == user_id]
    return user_data

def list_products_by_category(category):
    global df_products
    products = df_products[df_products['categoria'] == category]
    print(f'\nProductos de la categoría {category}')
    for product in products.iterrows():
        print(f"🔹 ID: {product[1]['producto_id']}: {product[1]['nombre']} - ${product[1]['precio']}")
    print('\n1. Comprar producto')
    print('2. Volver')
    print('3. Ir al menú principal')
    option = input('Opción: ')
    if option == '1':
        print('Ingrese el nombre o el ID del producto que desea comprar:')
        product = input('Producto: ')
    elif option == '2':
        pass
    elif option == '3':
        pass
    else:
        print('❌ Opción no válida. Intente nuevamente.')
        list_products_by_category(category)