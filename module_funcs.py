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

    df_users = pd.concat([df_users, new_user], ignore_index=True)
    df_users.to_csv('data/users.csv', index=False)
    print(f"✅ Usuario '{user}' agregado con éxito.")

def login_user():
    global df_users
    att = 3
    user = input('Ingrese su usuario: ')
    password = input('Ingrese su contraseña: ')
    user_data = df_users[(df_users['usuario'] == user) & (df_users['contraseña'] == password)]

    while att > 0:
        user_data = df_users[(df_users['usuario'] == user) & (df_users['contraseña'] == password)]
        if not user_data.empty:
            print(f"✅ Bienvenido {user_data['nombre'].values[0]}")
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