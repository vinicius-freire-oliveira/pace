def calcular_pace(distancia_km, tempo_horas, tempo_minutos, tempo_segundos):
    # Calcula o tempo total em minutos
    tempo_total_minutos = tempo_horas * 60 + tempo_minutos + tempo_segundos / 60
    
    # Calcula o pace em minutos por quilômetro
    pace_min_por_km = tempo_total_minutos / distancia_km
    
    # Calcula os minutos inteiros do pace
    minutos_pace = int(pace_min_por_km)
    
    # Calcula os segundos do pace
    segundos_pace = int((pace_min_por_km - minutos_pace) * 60)
    
    return minutos_pace, segundos_pace

# Exemplo de uso
distancia_km = 45  # Distância total da corrida em quilômetros
tempo_horas = 4     # Tempo total da corrida em horas
tempo_minutos = 45  # Tempo total da corrida em minutos
tempo_segundos = 30 # Tempo total da corrida em segundos

# Chama a função para calcular o pace
minutos_pace, segundos_pace = calcular_pace(distancia_km, tempo_horas, tempo_minutos, tempo_segundos)

# Exibir apresentação
print("\n ###### Cálculo Pace (tempo/distância) #####")
# Imprime o resultado
print(f'O pace é {minutos_pace}:{segundos_pace} min/km')
