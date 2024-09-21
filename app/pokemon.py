import requests
import json
import psycopg2

def pokedata(info):
    url = f"https://pokeapi.co/api/v2/pokemon/{info}"
    request = requests.get(url)
    dadosjson = json.loads(request.content)
    pokemoninfo = {
        "name":dadosjson["name"],
        "weight":dadosjson["weight"],
        "type":dadosjson["types"][0]["type"]["name"]
    }
    return (pokemoninfo)

def main():

    connection = psycopg2.connect(
        host="db",
        port="5432",
        database="database",
        user="user",
        password="password"
    )

    cur = connection.cursor()

    insert_query = """
    INSERT INTO pokemons (name, weight, type) VALUES (%(name)s, %(weight)s, %(type)s)
    """

    for n in range(1, 152):
        try:
            values = pokedata(n)
            cur.execute(insert_query, values)
            connection.commit()
            print(f"Pokemon {values['name']} inserido com sucesso")
        except Exception as e:
            print(f"Erro: {e}")
    cur.close()
    connection.close()

main()
