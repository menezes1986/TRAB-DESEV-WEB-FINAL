import mysql.connector 

db_config = {
    'host':'monorail.proxy.rlwy.net',
    'port':'29478',
    'user':'root',
    'password':'cwOsMehfTlwcidAUisLOJJhPrjvIqeyn',
    'database':'railway',
}
try:
    Tr_Grupo19 = mysql.connector.connect(**db_config)
    print('Conexão com banco estabelecida')
    cnx = mysql.connector.connect(**db_config)
    cursor = cnx.cursor()

    # Definindo o comando SQL para criar a tabela
    alter_column_query = '''
    ALTER TABLE usuarios
    MODIFY COLUMN ID INT AUTO_INCREMENT NOT NULL
    '''

    # Executando o comando SQL
    cursor.execute(alter_column_query)
    print("Propriedades da coluna ID alteradas com sucesso.")
    

except mysql.connector.Error as err:
    print(f"erro ao conectar ao banco de dados:{err}")

