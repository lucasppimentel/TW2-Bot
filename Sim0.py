from Memory import *

# Objetivos
M = 391040
A = 433590
F = 351490

wood = 850
clay = 860
iron = 870

NvBosque = 1
NvMina = 1
NvPoco = 1
t = 0

# Simulação upar os recursos para nivel 10, com ordem fixa
for i in range(0, 10):
    if wood >= MBosque[NvBosque] and clay >= ABosque[NvBosque] and iron >= FBosque[NvBosque]:
        wood = wood - MBosque[NvBosque] + TRec[NvBosque] * PBosque[NvBosque]
        clay = clay - ABosque[NvBosque] + TRec[NvBosque] * PPoco[NvPoco]
        iron = iron - FBosque[NvBosque] + TRec[NvBosque] * PMina[NvMina]
        t = t + TRec[NvBosque]
        NvBosque = NvBosque + 1
    else:
        difs = [MBosque[NvBosque] - wood, ABosque[NvBosque] - clay, FBosque[NvBosque] - iron]
        if difs[0] > difs[1] > difs[2]:
            t = t + difs[0] / PBosque[NvBosque]
            wood = wood + difs[0] - MBosque[NvBosque] + TRec[NvBosque] * PBosque[NvBosque]
            clay = clay + (difs[0] / PBosque[NvBosque]) * PPoco[NvPoco] - ABosque[NvBosque] + TRec[NvBosque] * PPoco[
                NvPoco]
            iron = iron + (difs[0] / PBosque[NvBosque]) * PMina[NvMina] - FBosque[NvBosque] + TRec[NvBosque] * PMina[
                NvMina]
            t = t + TRec[NvBosque]
            NvBosque = NvBosque + 1
        elif difs[0] > difs[1] < difs[2]:
            t = t + difs[2] / PMina[NvMina]
            wood = wood + (difs[2] / PMina[NvMina]) * PBosque[NvBosque] - MBosque[NvBosque] + TRec[NvBosque] * PBosque[
                NvBosque]
            clay = clay + (difs[2] / PMina[NvMina]) * PPoco[NvPoco] - ABosque[NvBosque] + TRec[NvBosque] * PPoco[NvPoco]
            iron = iron + difs[2] - FMina[NvMina] + TRec[NvBosque] * PBosque[NvBosque]
            t = t + TRec[NvMina]
            NvBosque = NvBosque + 1
        else:
            t = t + difs[1] / PPoco[NvPoco]
            wood = wood + (difs[1] / PPoco[NvPoco]) * PBosque[NvBosque] - MBosque[NvBosque] + TRec[NvBosque] * PBosque[
                NvBosque]
            clay = clay + difs[1] - APoco[NvPoco] + TRec[NvBosque] * PBosque[NvBosque]
            iron = iron + (difs[1] / PPoco[NvPoco]) * PMina[NvMina] - FBosque[NvBosque] + TRec[NvBosque] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvBosque = NvBosque + 1

    if wood >= MMina[NvMina] and clay >= AMina[NvMina] and iron >= FMina[NvMina]:
        wood = wood - MMina[NvMina] + TRec[NvMina] * PBosque[NvBosque]
        clay = clay - AMina[NvMina] + TRec[NvMina] * PPoco[NvPoco]
        iron = iron - FMina[NvMina] + TRec[NvMina] * PMina[NvMina]
        t = t + TRec[NvMina]
        NvMina = NvMina + 1
    else:
        difs = [MMina[NvMina] - wood, AMina[NvMina] - clay, FMina[NvMina] - iron]
        if difs[0] > difs[1] > difs[2]:
            t = t + difs[0] / PBosque[NvBosque]
            wood = wood + difs[0] - MMina[NvMina] + TRec[NvMina] * PBosque[NvBosque]
            clay = clay + (difs[0] / PBosque[NvBosque]) * PPoco[NvPoco] - AMina[NvMina] + TRec[NvMina] * PPoco[NvPoco]
            iron = iron + (difs[0] / PBosque[NvBosque]) * PMina[NvMina] - FMina[NvMina] + TRec[NvMina] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvMina = NvMina + 1
        elif difs[0] > difs[1] < difs[2]:
            t = t + difs[2] / PMina[NvMina]
            wood = wood + (difs[2] / PMina[NvMina]) * PBosque[NvBosque] - MMina[NvMina] + TRec[NvMina] * PBosque[
                NvBosque]
            clay = clay + (difs[2] / PMina[NvMina]) * PPoco[NvPoco] - AMina[NvMina] + TRec[NvMina] * PPoco[NvPoco]
            iron = iron + difs[2] - FMina[NvMina] + TRec[NvMina] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvMina = NvMina + 1
        else:
            t = t + difs[1] / PPoco[NvPoco]
            wood = wood + (difs[1] / PPoco[NvPoco]) * PBosque[NvBosque] - MMina[NvMina] + TRec[NvPoco] * PBosque[
                NvBosque]
            clay = clay + difs[1] - AMina[NvMina] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + (difs[1] / PPoco[NvPoco]) * PMina[NvMina] - FMina[NvMina] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvMina = NvMina + 1

    if wood >= MPoco[NvPoco] and clay >= APoco[NvPoco] and iron >= FPoco[NvPoco]:
        wood = wood - MPoco[NvPoco] + TRec[NvPoco] * PBosque[NvBosque]
        clay = clay - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
        iron = iron - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
        t = t + TRec[NvPoco]
        NvPoco = NvPoco + 1
    else:
        difs = [MPoco[NvPoco] - wood, APoco[NvPoco] - clay, FPoco[NvPoco] - iron]
        if difs[0] > difs[1] > difs[2]:
            t = t + difs[0] / PBosque[NvBosque]
            wood = wood + difs[0] - MPoco[NvPoco] + TRec[NvPoco] * PBosque[NvBosque]
            clay = clay + (difs[0] / PBosque[NvBosque]) * PPoco[NvPoco] - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + (difs[0] / PBosque[NvBosque]) * PMina[NvMina] - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvPoco]
            NvPoco = NvPoco + 1
        elif difs[0] > difs[1] < difs[2]:
            t = t + difs[2] / PMina[NvMina]
            wood = wood + (difs[2] / PMina[NvMina]) * PBosque[NvBosque] - MPoco[NvPoco] + TRec[NvPoco] * PBosque[
                NvBosque]
            clay = clay + (difs[2] / PMina[NvMina]) * PPoco[NvPoco] - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + difs[2] - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvPoco]
            NvPoco = NvPoco + 1
        else:
            t = t + difs[1] / PPoco[NvPoco]
            wood = wood + (difs[1] / PPoco[NvPoco]) * PBosque[NvBosque] - MPoco[NvPoco] + TRec[NvPoco] * PBosque[
                NvBosque]
            clay = clay + difs[1] - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + (difs[1] / PPoco[NvPoco]) * PMina[NvMina] - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvPoco]
            NvPoco = NvPoco + 1
print('pt1 t={}, bosque={} poço={} mina={}'.format(t, NvBosque, NvPoco, NvMina))
print('{} madeira, {} argila e {} ferro'.format(wood, clay, iron))
print('-' * 30)


# Simulação combinações
def upbosque():
    global wood
    global clay
    global iron
    global NvPoco
    global NvBosque
    global NvMina
    global t

    if wood >= MBosque[NvBosque] and clay >= ABosque[NvBosque] and iron >= FBosque[NvBosque]:
        wood = wood - MBosque[NvBosque] + TRec[NvBosque] * PBosque[NvBosque]
        clay = clay - ABosque[NvBosque] + TRec[NvBosque] * PPoco[NvPoco]
        iron = iron - FBosque[NvBosque] + TRec[NvBosque] * PMina[NvMina]
        t = t + TRec[NvBosque]
        NvBosque = NvBosque + 1
    else:
        dif = [MBosque[NvBosque] - wood, ABosque[NvBosque] - clay, FBosque[NvBosque] - iron]
        if dif[0] > dif[1] > dif[2]:
            t = t + dif[0] / PBosque[NvBosque]
            wood = wood + dif[0] - MBosque[NvBosque] + TRec[NvBosque] * PBosque[NvBosque]
            clay = clay + (dif[0] / PBosque[NvBosque]) * PPoco[NvPoco] - ABosque[NvBosque] + TRec[NvBosque] * PPoco[
                NvPoco]
            iron = iron + (dif[0] / PBosque[NvBosque]) * PMina[NvMina] - FBosque[NvBosque] + TRec[NvBosque] * PMina[
                NvMina]
            t = t + TRec[NvBosque]
            NvBosque = NvBosque + 1
        elif dif[0] > dif[1] < dif[2]:
            t = t + dif[2] / PMina[NvMina]
            wood = wood + (dif[2] / PMina[NvMina]) * PBosque[NvBosque] - MBosque[NvBosque] + TRec[NvBosque] * PBosque[
                NvBosque]
            clay = clay + (dif[2] / PMina[NvMina]) * PPoco[NvPoco] - ABosque[NvBosque] + TRec[NvBosque] * PPoco[NvPoco]
            iron = iron + dif[2] - FMina[NvMina] + TRec[NvBosque] * PBosque[NvBosque]
            t = t + TRec[NvMina]
            NvBosque = NvBosque + 1
        else:
            t = t + dif[1] / PPoco[NvPoco]
            wood = wood + (dif[1] / PPoco[NvPoco]) * PBosque[NvBosque] - MBosque[NvBosque] + TRec[NvBosque] * PBosque[
                NvBosque]
            clay = clay + dif[1] - APoco[NvPoco] + TRec[NvBosque] * PBosque[NvBosque]
            iron = iron + (dif[1] / PPoco[NvPoco]) * PMina[NvMina] - FBosque[NvBosque] + TRec[NvBosque] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvBosque = NvBosque + 1


def upmina():
    global wood
    global clay
    global iron
    global NvPoco
    global NvBosque
    global NvMina
    global t

    if wood >= MMina[NvMina] and clay >= AMina[NvMina] and iron >= FMina[NvMina]:
        wood = wood - MMina[NvMina] + TRec[NvMina] * PBosque[NvBosque]
        clay = clay - AMina[NvMina] + TRec[NvMina] * PPoco[NvPoco]
        iron = iron - FMina[NvMina] + TRec[NvMina] * PMina[NvMina]
        t = t + TRec[NvMina]
        NvMina = NvMina + 1
    else:
        dif = [MMina[NvMina] - wood, AMina[NvMina] - clay, FMina[NvMina] - iron]
        if dif[0] > dif[1] > dif[2]:
            t = t + dif[0] / PBosque[NvBosque]
            wood = wood + dif[0] - MMina[NvMina] + TRec[NvMina] * PBosque[NvBosque]
            clay = clay + (dif[0] / PBosque[NvBosque]) * PPoco[NvPoco] - AMina[NvMina] + TRec[NvMina] * PPoco[NvPoco]
            iron = iron + (dif[0] / PBosque[NvBosque]) * PMina[NvMina] - FMina[NvMina] + TRec[NvMina] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvMina = NvMina + 1
        elif dif[0] > dif[1] < dif[2]:
            t = t + dif[2] / PMina[NvMina]
            wood = wood + (dif[2] / PMina[NvMina]) * PBosque[NvBosque] - MMina[NvMina] + TRec[NvMina] * PBosque[
                NvBosque]
            clay = clay + (dif[2] / PMina[NvMina]) * PPoco[NvPoco] - AMina[NvMina] + TRec[NvMina] * PPoco[NvPoco]
            iron = iron + dif[2] - FMina[NvMina] + TRec[NvMina] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvMina = NvMina + 1
        else:
            t = t + dif[1] / PPoco[NvPoco]
            wood = wood + (dif[1] / PPoco[NvPoco]) * PBosque[NvBosque] - MMina[NvMina] + TRec[NvPoco] * PBosque[
                NvBosque]
            clay = clay + dif[1] - AMina[NvMina] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + (dif[1] / PPoco[NvPoco]) * PMina[NvMina] - FMina[NvMina] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvMina]
            NvMina = NvMina + 1


def uppoco():
    global wood
    global clay
    global iron
    global NvPoco
    global NvBosque
    global NvMina
    global t

    if wood >= MPoco[NvPoco] and clay >= APoco[NvPoco] and iron >= FPoco[NvPoco]:
        wood = wood - MPoco[NvPoco] + TRec[NvPoco] * PBosque[NvBosque]
        clay = clay - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
        iron = iron - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
        t = t + TRec[NvPoco]
        NvPoco = NvPoco + 1
    else:
        dif = [MPoco[NvPoco] - wood, APoco[NvPoco] - clay, FPoco[NvPoco] - iron]
        if dif[0] > dif[1] > dif[2]:
            t = t + dif[0] / PBosque[NvBosque]
            wood = wood + dif[0] - MPoco[NvPoco] + TRec[NvPoco] * PBosque[NvBosque]
            clay = clay + (dif[0] / PBosque[NvBosque]) * PPoco[NvPoco] - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + (dif[0] / PBosque[NvBosque]) * PMina[NvMina] - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvPoco]
            NvPoco = NvPoco + 1
        elif dif[0] > dif[1] < dif[2]:
            t = t + dif[2] / PMina[NvMina]
            wood = wood + (dif[2] / PMina[NvMina]) * PBosque[NvBosque] - MPoco[NvPoco] + TRec[NvPoco] * PBosque[
                NvBosque]
            clay = clay + (dif[2] / PMina[NvMina]) * PPoco[NvPoco] - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + dif[2] - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvPoco]
            NvPoco = NvPoco + 1
        else:
            t = t + dif[1] / PPoco[NvPoco]
            wood = wood + (dif[1] / PPoco[NvPoco]) * PBosque[NvBosque] - MPoco[NvPoco] + TRec[NvPoco] * PBosque[
                NvBosque]
            clay = clay + dif[1] - APoco[NvPoco] + TRec[NvPoco] * PPoco[NvPoco]
            iron = iron + (dif[1] / PPoco[NvPoco]) * PMina[NvMina] - FPoco[NvPoco] + TRec[NvPoco] * PMina[NvMina]
            t = t + TRec[NvPoco]
            NvPoco = NvPoco + 1


tb = t
MemoriaMina = NvMina
MemoriaPoco = NvPoco
MemoriaWood = wood
MemoriaClay = clay
MemoriaIron = iron
valores = {}

# Entre os níveis de 14 até 20, testar todos os valores entre 14 a 20 dos outros recursos
for a in range(0, 18):
    NvMina = MemoriaMina
    t = tb
    wood = MemoriaWood
    clay = MemoriaClay
    iron = MemoriaIron

    upbosque()

    MemoriaWood = wood
    MemoriaClay = clay
    MemoriaIron = iron
    MemoriaMina = NvMina
    tb = t
    tm = t
    MMWood = wood
    MMClay = clay
    MMIron = iron

    for b in range(0, 18):
        NvPoco = MemoriaPoco
        t = tm
        wood = MMWood
        Iron = MMIron
        clay = MMClay

        upmina()

        MMWood = wood
        MMClay = clay
        MMIron = iron
        MemoriaPoco = NvPoco
        tm = t
        tp = t
        MPWood = wood
        MPClay = clay
        MPIron = iron

        for c in range(0, 18):
            wood = MPWood
            clay = MPClay
            iron = MPIron
            t = tp

            uppoco()

            MPWood = wood
            MPClay = clay
            MPIron = iron
            tp = t
            lista = [(M - wood) / PBosque[NvBosque], (A - clay) / PPoco[NvPoco], (F - iron) / PMina[NvMina]]
            if lista[0] > lista[1] > lista[2]:
                t = t + lista[0]
                g = 'madeira'
            elif lista[0] > lista[1] < lista[2]:
                t = t + lista[2]
                g = 'mina'
            else:
                t = t + lista[1]
                g = 'argila'
            print('para bosque nivel {}, mina nivel {} e poço nivel {}, t = {}. Gargalo = {}'.format(NvBosque, NvMina,
                                                                                                     NvPoco, t, g))
            valores['Bosque = {}, Poço = {}, Mina = {}'.format(NvBosque, NvPoco, NvMina)] = float(t)

minimo = min(valores.values())
fras = [key for key in valores if valores[key] == minimo]
print('-'*80)
print('Tempo ótimo = {}, sendo {}'.format(minimo, fras))
print('-'*80)
