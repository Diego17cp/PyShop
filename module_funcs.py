# Import libraries
import pandas as pd
import datetime as dt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split
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

def list_products_by_category(category, user_id):
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
        buy_product(user_id, product)
    elif option == '2':
        return 'back'
    elif option == '3':
        return 'main_menu'
    else:
        print('❌ Opción no válida. Intente nuevamente.')
        list_products_by_category(category)

def buy_product(user_id, product):
    global df_orders, df_products

    if product.isdigit():
        product_id = int(product)
        product_match = df_products[df_products['producto_id'] == product_id]
    else:
        product_match = df_products[df_products['nombre'] == product]
        
    quantity = int(input('Ingrese la cantidad de productos a comprar: '))
    if quantity <= 0:
        print('❌ La cantidad debe ser mayor a 0.')
        
    product_id = product_match['producto_id'].values[0]
    precio = product_match['precio'].values[0]
    total = precio * quantity
    new_id = df_orders['compra_id'].max() + 1 if not df_orders.empty else 1
    date = dt.datetime.now().strftime('%Y-%m-%d')

    new_order = {
        'compra_id': new_id,
        'usuario_id': user_id,
        'producto_id': product_id,
        'cantidad': quantity,
        'precio_unitario': precio,
        'total': total,
        'fecha': date
    }
    df_new_order = pd.DataFrame([new_order])
    df_orders = pd.concat([df_orders, df_new_order], ignore_index=True)
    df_orders.to_csv('data/orders.csv', index=False)
    print('✅ Producto comprado con éxito.')

def purchases_historial(user_id):
    global df_orders, df_products
    user_orders = df_orders[df_orders['usuario_id'] == user_id]
    if user_orders.empty:
        print('No tienes compras aún.')
    else:
        print('\nHistorial de compras')
        for order in user_orders.iterrows():
            product = df_products[df_products['producto_id'] == order[1]['producto_id']]
            print(f"🔹 ID: {order[1]['compra_id']}: {product['nombre'].values[0]} - ${order[1]['total']}")

def recommend_by_similarity(product_name, top_n=3):
    global df_products

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df_products['categoria'])

    simimilarity = cosine_similarity(tfidf_matrix)

    idx = df_products[df_products['nombre'] == product_name].index[0]

    scores = list(enumerate(simimilarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)[1:top_n+1]

    recommended_products = df_products.iloc[[i[0] for i in scores]][['nombre', 'categoria', 'precio']]
    return recommended_products.to_dict(orient='records')

def recommend_by_colab(user_id, top_n=3):
    global df_orders, df_products

    reader = Reader(rating_scale=(1, 5))
    data = Dataset.load_from_df(df_orders[['usuario_id', 'producto_id', 'total']], reader)

    trainset, testset = train_test_split(data, test_size=.2)
    model = SVD()
    model.fit(trainset)

    available_products = df_products['producto_id'].unique()
    predicts = [
        (p_id, model.predict(user_id, p_id).est)
        for p_id in available_products
    ]
    predicts = sorted(predicts, key=lambda x: x[1], reverse=True)[:top_n]

    return df_products[df_products['producto_id'].isin([p[0] for p in predicts])][['nombre', 'categoria', 'precio']].to_dict(orient='records')

def final_recommend(user_id, top_n=5):
    global df_orders, df_products

    user_orders = df_orders[df_orders['usuario_id'] == user_id]['producto_id'].tolist()

    recommends = []

    for product_id in user_orders:
        product_name = df_products[df_products['producto_id'] == product_id]['nombre'].values[0]
        similar = recommend_by_similarity(product_name, top_n)
        recommends.extend(similar)

    colab = recommend_by_colab(user_id, top_n)

    final_recommend = {
        p['nombre']: p
        for p in (recommends + colab)
    }.values()

    return list(final_recommend)[:top_n]