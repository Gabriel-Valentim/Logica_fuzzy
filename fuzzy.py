import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# Definindo as variáveis do universo
Volume_Trafego = ctrl.Antecedent(np.arange(0, 11, 1), 'Volume_Trafego')
Condicao_Estrada = ctrl.Antecedent(np.arange(0, 11, 1), 'Condicao_Estrada')
Hora_Dia = ctrl.Antecedent(np.arange(0, 24, 1), 'Hora_Dia')
Dia_Semana = ctrl.Antecedent(np.arange(0, 7, 1), 'Dia_Semana')
Duracao_Semaforo = ctrl.Consequent(np.arange(0, 101, 1), 'Duracao_Semaforo')

# Definindo as funções de pertinência
Volume_Trafego['baixo'] = fuzz.trimf(Volume_Trafego.universe, [0, 0, 5])
Volume_Trafego['medio'] = fuzz.trimf(Volume_Trafego.universe, [0, 5, 10])
Volume_Trafego['alto'] = fuzz.trimf(Volume_Trafego.universe, [5, 10, 10])

Condicao_Estrada['boa'] = fuzz.trimf(Condicao_Estrada.universe, [0, 0, 5])
Condicao_Estrada['media'] = fuzz.trimf(Condicao_Estrada.universe, [0, 5, 10])
Condicao_Estrada['ruim'] = fuzz.trimf(Condicao_Estrada.universe, [5, 10, 10])

Hora_Dia['madrugada'] = fuzz.trimf(Hora_Dia.universe, [0, 0, 6])
Hora_Dia['manha'] = fuzz.trimf(Hora_Dia.universe, [6, 12, 12])
Hora_Dia['tarde'] = fuzz.trimf(Hora_Dia.universe, [12, 18, 18])
Hora_Dia['noite'] = fuzz.trimf(Hora_Dia.universe, [18, 24, 24])

Dia_Semana['semana'] = fuzz.trimf(Dia_Semana.universe, [0, 3, 4])
Dia_Semana['fim_semana'] = fuzz.trimf(Dia_Semana.universe, [4, 6, 6])

Duracao_Semaforo['curta'] = fuzz.trimf(Duracao_Semaforo.universe, [0, 0, 50])
Duracao_Semaforo['media'] = fuzz.trimf(Duracao_Semaforo.universe, [0, 50, 100])
Duracao_Semaforo['longa'] = fuzz.trimf(Duracao_Semaforo.universe, [50, 100, 100])