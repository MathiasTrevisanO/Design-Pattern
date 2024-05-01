import sqlite3

def _executar(query):
    db_path = './geek.university'
    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    result = None
    
    try:
        cursor.execute(query)
        result = cursor.fetchall() # lista de tuplas
        connection.commit()
    except Exception as err:
        print(f'Erro na execução da query: {err}')
    connection.close()
    
    return result


    """
    resultado = [(1, "Playstation 5", 1234, 1), (2, "Playstation 5", 1566, 0)]
    """