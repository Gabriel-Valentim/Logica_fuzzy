import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis do universo

# Gênero do filme anterior 
Genero_Filme_Anterior = ctrl.Antecedent(np.arange(0, 11, 1), 'Genero_Filme_Anterior')

# Avaliações anteriores de filmes 
Avaliacoes_Anteriores = ctrl.Antecedent(np.arange(0, 11, 1), 'Avaliacoes_Anteriores')

# Gênero preferido 
Genero_Preferido = ctrl.Antecedent(np.arange(0, 11, 1), 'Genero_Preferido')

# Tempo de visualização 
Tempo_Visualizacao = ctrl.Antecedent(np.arange(0, 11, 1), 'Tempo_Visualizacao')

# Idade do usuário 
Idade_Usuario = ctrl.Antecedent(np.arange(0, 101, 1), 'Idade_Usuario')

# Recomendação de filme 
Recomendacao = ctrl.Consequent(np.arange(0, 11, 1), 'Recomendacao')

# Definindo as funções de pertinência para cada variável
# Avaliações anteriores de filmes
Avaliacoes_Anteriores['baixa'] = fuzz.trimf(Avaliacoes_Anteriores.universe, [0, 0, 5])
Avaliacoes_Anteriores['media'] = fuzz.trimf(Avaliacoes_Anteriores.universe, [0, 5, 10])
Avaliacoes_Anteriores['alta']  = fuzz.trimf(Avaliacoes_Anteriores.universe, [5, 10, 10])

# Definindo a função de pertinência para Genero_Filme_Anterior
Genero_Filme_Anterior['acao']    = fuzz.trimf(Genero_Filme_Anterior.universe, [0, 0, 5])
Genero_Filme_Anterior['comedia'] = fuzz.trimf(Genero_Filme_Anterior.universe, [0, 5, 10])
Genero_Filme_Anterior['romance'] = fuzz.trimf(Genero_Filme_Anterior.universe, [5, 10, 10])


# Gênero preferido 
Genero_Preferido['acao']    = fuzz.trimf(Genero_Preferido.universe, [0, 0, 5])
Genero_Preferido['comedia'] = fuzz.trimf(Genero_Preferido.universe, [0, 5, 10])
Genero_Preferido['romance'] = fuzz.trimf(Genero_Preferido.universe, [5, 10, 10])

# Tempo de visualização
Tempo_Visualizacao['curto'] = fuzz.trimf(Tempo_Visualizacao.universe, [0, 0, 5])
Tempo_Visualizacao['medio'] = fuzz.trimf(Tempo_Visualizacao.universe, [0, 5, 10])
Tempo_Visualizacao['longo'] = fuzz.trimf(Tempo_Visualizacao.universe, [5, 10, 10])

# Idade do usuário
Idade_Usuario['jovem']  = fuzz.trimf(Idade_Usuario.universe, [0, 0, 40])
Idade_Usuario['adulto'] = fuzz.trimf(Idade_Usuario.universe, [20, 50, 80])
Idade_Usuario['idoso']  = fuzz.trimf(Idade_Usuario.universe, [60, 100, 100])

# Recomendação
Recomendacao['baixa'] = fuzz.trimf(Recomendacao.universe, [0, 0, 5])
Recomendacao['media'] = fuzz.trimf(Recomendacao.universe, [0, 5, 10])
Recomendacao['alta']  = fuzz.trimf(Recomendacao.universe, [5, 10, 10])


# Definindo as regras de produção
rules = []
for av in ['baixa', 'media', 'alta']:
    for gf in ['acao', 'comedia', 'romance']:
        for gp in ['acao', 'comedia', 'romance']:
            for tv in ['curto', 'medio', 'longo']:
                for iu in ['jovem', 'adulto', 'idoso']:
                    if av == 'alta' and gf == gp:
                        rules.append(ctrl.Rule(Avaliacoes_Anteriores[av] & Genero_Filme_Anterior[gf] & Genero_Preferido[gp] & Tempo_Visualizacao[tv] & Idade_Usuario[iu], Recomendacao['alta']))
                    elif av == 'media' and gf == gp:
                        rules.append(ctrl.Rule(Avaliacoes_Anteriores[av] & Genero_Filme_Anterior[gf] & Genero_Preferido[gp] & Tempo_Visualizacao[tv] & Idade_Usuario[iu], Recomendacao['media']))
                    else:
                        rules.append(ctrl.Rule(Avaliacoes_Anteriores[av] & Genero_Filme_Anterior[gf] & Genero_Preferido[gp] & Tempo_Visualizacao[tv] & Idade_Usuario[iu], Recomendacao['baixa']))

