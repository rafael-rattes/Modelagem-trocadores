def LMTD(T1, T2, t1, t2, flow = 'counter'):
    """
    Calcula a temperatura média logarítmica de um trocador de calor de casco e tubos.
    
    Parâmetros:
    T0: Temperatura de entrada do fluido quente [°C]
    T1: Temperatura de saída do fluido quente [°C]
    t0: Temperatura de entrada do fluido frio [°C]
    t1: Temperatura de saída do fluido frio [°C]
    flow: Tipo de fluxo de calor. Pode ser 'counter' (contracorrente) ou 'parallel' (co-corrente).
    
    Retorno:
    LMTD: Temperatura média logarítmica [°C]
    """
    
    from numpy import log
    
    if flow == 'counter':
        deltaT1 = T1 - t2
        deltaT2 = T2 - t1
    elif flow == 'parallel':
        deltaT1 = T1 - t1
        deltaT2 = T2 - t2
    else:
        raise ValueError("O parâmetro 'flow' deve ser 'counter' ou 'parallel'.")
    
    LMTD = (deltaT1 - deltaT2) / log(deltaT1 / deltaT2)
    
def nusselt(correlation, Re, Pr):
    """
    Calcula o número de Nusselt para um dado número de Reynolds e Prandtl.
    
    Parâmetros:
    correlation: Correlação para o cálculo do número de Nusselt. Pode ser 'Dittus-Boelter' ou 'Sieder-Tate'.
    Re: Número de Reynolds.
    Pr: Número de Prandtl.
    
    Retorno:
    Nu: Número de Nusselt.
    """
    
    if correlation == 'Dittus-Boelter':
        Nu = 0.023 * Re**0.8 * Pr**0.3
    elif correlation == 'Sieder-Tate':
        Nu = 0.027 * Re**0.8 * Pr**0.3
    else:
        raise ValueError("O parâmetro 'correlation' deve ser 'Dittus-Boelter' ou 'Sieder-Tate'.")
    
    return Nu

def fouling(U, Rf):
    """
    Calcula o coeficiente de transferência de calor corrigido para incrustações.
    
    Parâmetros:
    U: Coeficiente de transferência de calor sem incrustações [W/m²K].
    Rf: Resistência térmica de incrustações [m²K/W].
    
    Retorno:
    Uc: Coeficiente de transferência de calor corrigido [W/m²K].
    """
    
    Uc = 1 / (1 / U + Rf)
    
    return Uc