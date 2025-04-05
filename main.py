rounds = [
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': True},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': False},
'Viper': {'kills': 1, 'assists': 2, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 0, 'assists': 2, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 0, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': False},
'Frost': {'kills': 2, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 0, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 0, 'deaths': False},
'Blaze': {'kills': 2, 'assists': 2, 'deaths': True},
'Viper': {'kills': 1, 'assists': 1, 'deaths': True},
'Frost': {'kills': 0, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 2, 'assists': 1, 'deaths': False},
'Blaze': {'kills': 1, 'assists': 0, 'deaths': True},
'Viper': {'kills': 0, 'assists': 2, 'deaths': False},
'Frost': {'kills': 1, 'assists': 1, 'deaths': True},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': False}
},
{
'Shadow': {'kills': 1, 'assists': 2, 'deaths': True},
'Blaze': {'kills': 0, 'assists': 1, 'deaths': False},
'Viper': {'kills': 2, 'assists': 0, 'deaths': True},
'Frost': {'kills': 1, 'assists': 1, 'deaths': False},
'Reaper': {'kills': 1, 'assists': 1, 'deaths': True}
}
]


#dic para llevar estadisticas
stats = {}

#pongo en 0 la stat de cada jugador (uso las claves de rounds para sacar los nombbres)
for player in rounds[0].keys():
    stats[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'score': 0}

def calcular_puntos(k, a, d):
    return k * 3 + a * 1 - d  # tendria que evitar el puntaje negativo? (uso de max)


for i, ronda in enumerate(rounds):     # enumerate me devuelve indice y valor
    print(f'Ranking de ronda numero {i+1} :')

    #actualizo datos de ronda
    round_points = {}     # dicc para clave nombre y valor puntaje
    for player, data in ronda.items():     # items me devuelve clave y valor, parecido a items en listas
        kills = data['kills']
        assists = data['assists']
        deaths = 1 if data['deaths'] else 0
        points = calcular_puntos(kills, assists, deaths)

        stats[player]['kills'] += kills
        stats[player]['assists'] += assists
        stats[player]['deaths'] += deaths
        stats[player]['score'] += points

        round_points[player] = points

    #determinar mvp de cada ronda
    mvp = max(round_points, key=round_points.get)   #no termine de entender pero se usa get en vez de get()
    stats[mvp]['mvp'] += 1

    # ordeno de forma descendente por puntajes e imprimo
    scores = sorted(stats.items(), key=lambda x: x[1]['score'], reverse=True)
    for player, data in scores:
        print(f"{player}: {data['score']} puntos")
    
    print("-" * 35)

# Ranking final
print("\n")
print("Ranking final:\n")
print("Jugador  Kills  Asistencias  Muertes  MVPs  Puntos")
print("-" * 52)
for player, data in scores:
    print(f"{player:6} {data['kills']:5} {data['assists']:9} {data['deaths']:10} {data['mvp']:6} {data['score']:7}")
print("-" * 52)

