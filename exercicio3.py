#Inicialização das Variáveis
tot_hab = 5
conta_emp = 0
conta_desemp = 0

# Entrada de Dados com tratamento de erro + Processamento de Ddados
for hab in range(tot_hab):
    while True:
        resp = int ( input(f"\n\tHabitante {hab+1} digite [1] para empregado ou [0] para Desempregado: "))
        if ( resp < 0) or ( resp > 1 ):
            print("\n\tOpção Inválida!\n")
        else:
            break
    if ( resp == 1):
        print(f"\n\tO habitante {hab+1} afirmou estar empregado!")
        conta_emp += 1
    else:
        print(f"\n\tO habitante {hab+1} afirmou estar desempregado!")
        conta_desemp += 1
    
# Saída de Dados
print(f"\n\tPorcentagem Final: Empregados={conta_emp/tot_hab * 100}%     Desempregados={conta_desemp/tot_hab * 100}%")