

def inicializar_stats(rounds):
    """Crea un diccionario con las estadisticas completas de cada jugador iniciadas en 0"""
    stats = {}
    for player in rounds[0].keys():
        stats[player] = {'kills': 0, 'assists': 0, 'deaths': 0, 'mvp': 0, 'score': 0}
    return stats



def calcular_puntos(k, a, d):
    return k * 3 + a * 1 - d  # tendria que evitar el puntaje negativo? (uso de max)


def ordenar_puntaje_descendente(stats, scores):
            scores = sorted(stats.items(), key=lambda x: x[1]['score'], reverse=True)
            for player, data in scores:
                print(f"{player}: {data['score']} puntos")
        
            print("-" * 35)
            return scores


def determinar_mvp(stats, round_points):
            mvp = max(round_points, key=round_points.get)   #no termine de entender pero se usa get en vez de get()
            stats[mvp]['mvp'] += 1


def procesar_rondas(stats, rounds):
    """Funcion que procesa cada ronda imprimiendo su puntaje y determinando el mvp. La ultima ronda será el punatje final"""
    for i, ronda in enumerate(rounds):     # enumerate me devuelve indice y valor
        print(f'Ranking de ronda numero {i+1} :')
        round_points = {}   #creo dictt para ir llevando nombre y puntaje por ronda
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
   
        determinar_mvp(stats, round_points)
        last_score = ordenar_puntaje_descendente(stats, list(stats))
    return last_score



def imprimir_rank_final(scores):
    """Esta funcion recibe las stats de la ronda final y presenta el ranking con estadisticas completas"""
    print("\n")
    print("Ranking final:\n")
    print("Jugador  Kills  Asistencias  Muertes  MVPs  Puntos")
    print("-" * 52)
    for player, data in scores:
        print(f"{player:6} {data['kills']:5} {data['assists']:9} {data['deaths']:10} {data['mvp']:6} {data['score']:7}")
    print("-" * 52)