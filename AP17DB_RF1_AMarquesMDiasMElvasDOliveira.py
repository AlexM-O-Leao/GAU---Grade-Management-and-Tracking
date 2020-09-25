'''
Projeto AP
'''
#Listas Locais
elementos_AP=['Teste Teórico 1', 'Teste Teórico 2', 'Trabalho', 'Presenças']
elementos_EDC=['Teste Teórico 1', 'Teste Teórico 2', 'Trabalho', 'Presenças']
elementos_MBD=['Teste Teórico 1', 'Teste Teórico 2', 'Teste Prático', 'Projeto']
elementos_SD=['Teste Teórico 1', 'Teste Teórico 2', 'Laboratório 0', 'Laboratório 1', 'Laboratório 2', 'Laboratório 3', 'Laboratório 4']
elementos_MAT=['Teste Teórico 1', 'Teste Teórico 2','Mini-Teste 1', 'Mini-Teste 2', 'Presenças']
nomes=['AP', 'EDC', 'MBD', 'SD', 'MAT']
docente_AP='Paulo Enes da Silva'
docente_EDC='Rui Neves'
docente_MBD='Valéria Pequeno'
docente_SD='João Guerreiro, Daniel Silvestre'
docente_MAT='Patricia Ramos, Rui Neves'
datas_AP=[]
datas_EDC=[]
datas_MBD=[]
datas_SD=[]
datas_MAT=[]
nf_AP=[]
nf_EDC=[]
nf_MBD=[]
nf_SD=[]
nf_MAT=[]
notas_AP=[]
notas_EDC=[]
notas_MBD=[]
notas_SD=[]
notas_MAT=[]
#Funções
def introducao():
    global nome_uti
    a=input('Antes de prosseguir confirme que o seu curso é Engenharia Informática.\n'
                  'S/N\n')
    if a == 'N' or a == 'n':
        import sys
        sys.exit()
        print('\n')
    print('Bem vindo ao GAU - Gestão da Avaliação na Universidade.\n')
    nome_uti=input('Indique o seu nome:\n')
    print('\n')
    print('Seja bem vindo {}! '.format(nome_uti))
    print('\n')#Separação por parágrafo
    print('Como o seu curso é E.I., verificamos que tem {} disciplinas. Essas são:\n'.format(len(nomes)))
    for i in range (0,len(nomes)):
        print('-', nomes[i])
    print('\n')
def menu():
    print('\n')
    opmenu=input('Escolha a sua opção:\n'
          '1) Editar Notas das Disciplinas\n'
          '2) Verificar Notas e Gráficos Das Disciplinas\n'
          '3) Observar Avaliação Final das Disciplinas\n'
          '4) Verificar Datas dos Elementos de Avaliação\n'
          '5) Verificar dados guardados em ficheiro\n'
          '6) Sair do Programa\n')
    print('\n')
    if opmenu == '1':
        print('\n')#Parágrafo
        menu_calc()
    else:
        if opmenu == '2':
            print('\n')#Parágrafo
            menu_check()
        else:
            if opmenu == '3':
                print('\n')#Parágrafo
                menu_fin()
            else:
                if opmenu == '4':
                    print('\n')#Parágrafo
                    menu_datas()
                else:
                    if opmenu == '5':
                        ver_fich()
                    else:
                        if opmenu== '6':
                            import sys
                            sys.exit
                        else:
                            if opmenu != '1' and opmenu != '2' and opmenu != '3' and opmenu != '4' and opmenu!= '5' and opmenu!= '6':
                                print('Opção Inválida!\n')
                                menu()

def menu_datas():
    if not datas_AP or not datas_EDC or not datas_MBD or not datas_SD or not datas_MAT:
        print('Como não foram encontradas datas na nossa base de dados, queira por favor voltar a introduzi-las.\n')
        menu()
    opc=input('Escolha qual a disciplina que pretende visualizar:\n'
              '1)AP\n'
              '2)EDC\n'
              '3)MBD\n'
              '4)SD\n'
              '5)MAT\n')
    print('\n')#Parágrafo
    if opc == '1':#Visualizar Datas de AP
        datas_a=[elementos_AP, datas_AP]
        tabela(datas_a)
        cont_c()
    else:
        if opc == '2':
            datas_a=[elementos_EDC, datas_EDC]
            tabela(datas_a)
            cont_c()
        else:
            if opc == '3':
                datas_a=[elementos_MBD, datas_MBD]
                tabela(datas_a)
                cont_c()
            else:
                if opc == '4':
                    datas_a=[elementos_SD, datas_SD]
                    tabela(datas_a)
                    cont_c()
                else:
                    if opc == '5':
                        datas_a=[elementos_MAT, datas_MAT]
                        tabela(datas_a)
                        cont_c()
                    else:
                        if opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5':
                            print('Opção Inválida!\n')
                            menu()#Voltar ao inicio
def menu_fin():
    if not nf_AP or not nf_EDC or not nf_MBD or not nf_SD or not nf_MAT:
        print('Como não foram encontradas notas na nossa base de dados, queira por favor voltar a introduzi-las.\n')
        menu()
    print('Iremos apresentar a tabela com as suas notas finais.\n')
    nf_curso=[nf_AP, nf_EDC, nf_MBD, nf_SD, nf_MAT]
    tabela_int_f=[nomes, nf_curso]
    tabela(tabela_int_f)
    graph_y(nf_curso, nomes)
    print("\n")
    cont_b()

def menu_check():
    if not notas_AP or not notas_EDC or not notas_MBD or not notas_SD or not notas_MAT:
        print('Como não foram encontradas notas na nossa base de dados, queira por favor voltar a introduzi-las.\n')
        menu()
    opc=input('Escolha qual a disciplina que pretende visualizar:\n'
              '1)AP\n'
              '2)EDC\n'
              '3)MBD\n'
              '4)SD\n'
              '5)MAT\n'
              '6)Fechar Programa\n')
    print('\n')
    if opc == '1':#Visualizar Notas de AP
        menu_check_a(notas_AP, nf_AP)#Função print
        graph_x(notas_AP, elementos_AP)
        cont_a()
    else:
        if opc == '2':
            menu_check_a(notas_EDC, nf_EDC)#Função Print
            graph_x(notas_EDC, elementos_EDC)
            cont_a()
        else:
            if opc == '3':
                menu_check_a(notas_MBD, nf_MBD)#Função Print
                graph_x(notas_MBD, elementos_MBD)
                cont_a()
            else:
                if opc == '4':
                    menu_check_a(notas_SD, nf_SD)#Função Print
                    graph_x(notas_SD, elementos_SD)
                    cont_a()
                else:
                    if opc == '5':
                        menu_check_a(notas_MAT, nf_MAT)#Função Print
                        graph_x(notas_MAT, elementos_MAT)
                        cont_a()
                    else:
                        if opc == '6':
                            import sys
                            sys.exit
                        else:
                            if opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5' and opc != '6':
                                print('Opção Inválida!\n')
                                menu_check()

def menu_check_a(notas_inter, nota_final):
    print('As suas notas nos diversos elementos de avaliação foram: {}\n'.format(notas_inter))
    print('A sua nota final nesta disciplina foi: {}\n'.format(nota_final))
    
def cont():
    #Continuação
    cont=input('Deseja continuar a introduzir dados nas disciplinas?\n')
    if cont == 's':
        menu_calc()
    else:
        if cont == 'n':
            menu()
def cont_a():
    #Continuação
    cont=input('Deseja continuar?\n')
    if cont == 's':
        menu_check()
    else:
        if cont == 'n':
            menu()

def cont_b():
    #Continuação
    cont=input('Deseja continuar?\n')
    if cont == 's':
        menu_fin()
    else:
        if cont == 'n':
            menu()
            
def cont_c():
    #Continuação
    cont=input('Deseja continuar?\n')
    if cont == 's':
        menu_datas()
    else:
        if cont == 'n':
            menu()
            
def menu_calc():
    opc=input('Escolha qual a disciplina que pretende editar:\n'
              '1)AP\n'
              '2)EDC\n'
              '3)MBD\n'
              '4)SD\n'
              '5)MAT\n')
    print('\n')
    import pickle
    if opc == '1':#Calcular Notas de AP
        print('\n')#Parágrafo
        global notas_AP, nf_AP, datas_AP#Para serem utilizadas fora da função
        intro(nomes[0], docente_AP,elementos_AP)
        a=int(input('Quantos elementos de avaliação deseja inserir?\n'))
        print('\n')#Parágrafo
        cot_AP=[]
        notas_AP=[]
        datas_AP=[]
        nf_AP=0
        i=0
        while i < a:
            print('Data do Elemento a Introduzir:\n')
            import datetime
            ano = int(input('Introduza o ano:\n'))
            mês = int(input('Introduza o mês:\n'))
            dia = int(input('Introduza o dia:\n'))
            date1 = datetime.date(ano, mês, dia)
            datas_AP.append(date1.__str__())
            cot_AP.append(float(input('Introduza a percentagem relativa a esse elemento (sem %):\n')))
            print('\n')#Parágrafo
            print('Próximo elemento\n')
            i=i+1
        i=0
        for i in range(len(cot_AP)):
            notas_AP.append(float(input('Introduza a nota:\n')))
            b=float((cot_AP[i]/100)*notas_AP[i])
            nf_AP=nf_AP+b
            i=i+1
            if i == (a-1) and nf_AP < 9.5:
                min=(10-nf_AP)/(cot_AP[-1]/100)
                if min >20:
                    print('Reprovado à disciplina.')
                    break
                else:
                    print('ATENÇÃO! - Para ter aprovação da disciplina com 10 valores precisa de ter no minimo {} valores no próximo item de avaliação\n'.format(min))
            if i == (a-1) and nf_AP > 9.5:
                opc_nota=int(input('Indique o que pretende que seja a sua nota final para ser calculada a nota minima (0 a 20):\n'))
                opc_nota_calc=(opc_nota - nf_AP)/(cot_AP[-1]/100)
                if opc_nota_calc <20 and opc_nota_calc >0:
                    print('Para ter aprovação da disciplina com {} valores precisa de ter no minimo {} valores no próximo item de avaliação:\n'.format(opc_nota, opc_nota_calc))
                else:
                    print('Não conseguirá atingir essa nota pretendida.')
        print('A sua nota final é:\n')
        print(int(nf_AP))
        #Gráfico
        graph_x(notas_AP, elementos_AP)
        #Tabela
        dados_AP=[elementos_AP, cot_AP, datas_AP,notas_AP]
        tabela(dados_AP)
        #Adição dos dados a um ficheiro
        adc_fich(dados_AP, nomes[0], docente_AP)
        #Pickle
        #Data
        with open('datas_AP.pkl','wb') as f: 
            pickle.dump(datas_AP,f)
        f.close()
        #Nota Final
        with open('nota_final_AP.pkl','wb') as f: 
            pickle.dump(nf_AP,f)
        f.close()
        #Notas
        with open('notas_AP.pkl','wb') as f: 
            pickle.dump(notas_AP,f)
        f.close()
        #Cotação
        with open('cot_AP.pkl','wb') as f: 
            pickle.dump(cot_AP,f)
        f.close()
        #Continuação do Programa
        cont()
    else:
        if opc== '2':#Calcular Notas de EDC
            print('\n')#Parágrafo
            global notas_EDC, nf_EDC, datas_EDC
            intro(nomes[1], docente_EDC, elementos_EDC)
            a=int(input('Quantos elementos de avaliação deseja inserir?\n'))
            print('\n')#Parágrafo
            cot_EDC=[]
            notas_EDC=[]  
            datas_EDC=[]
            nf_EDC=0
            i=0
            while i < a:
                print('Data do Elemento a Introduzir:\n')
                import datetime
                ano = int(input('Introduza o ano:\n'))
                mês = int(input('Introduza o mês:\n'))
                dia = int(input('Introduza o dia:\n'))
                date1 = datetime.date(ano, mês, dia)
                datas_EDC.append(date1.__str__())
                
                cot_EDC.append(float(input('Introduza a percentagem relativa a esse elemento (sem %):\n')))
                print('\n')#Parágrafo
                print('Próximo elemento\n')
                i=i+1
            i=0
            for i in range(len(cot_EDC)):
                notas_EDC.append(float(input('Introduza a nota:\n')))
                b=float((cot_EDC[i]/100)*notas_EDC[i])
                nf_EDC=nf_EDC+b
                i=i+1
                if i == (a-1) and nf_EDC < 10:
                    min=(10-nf_EDC)/(cot_EDC[-1]/100)
                    if min >20:
                        print('Reprovado à disciplina.')
                        break
                    else:
                        print('ATENÇÃO! - Para ter aprovação da disciplina com 10 valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(min))
            
                if i == (a-1) and nf_EDC > 9.5:
                    opc_nota=int(input('Indique o que pretende que seja a sua nota final para ser calculada a nota minima (0 a 20):\n'))
                    opc_nota_calc=(opc_nota - nf_EDC)/(cot_EDC[-1]/100)
                    if opc_nota_calc <20 and opc_nota_calc >0:
                        print('Para ter aprovação da disciplina com {} valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(opc_nota, opc_nota_calc))
                    else:
                        print('Não conseguirá atingir essa nota pretendida.')
                     
            print('A sua nota final é:\n')
            print(int(nf_EDC))
            #Gráfico
            graph_x(notas_EDC, elementos_EDC)
            #Tabela
            dados_EDC=[elementos_EDC, cot_EDC, datas_EDC, notas_EDC]
            tabela(dados_EDC)
            #Adição dos dados a um ficheiro
            adc_fich(dados_EDC, nomes[1], docente_EDC)
            #Pickle
            #Datas
            with open('datas_EDC.pkl','wb') as f: 
                pickle.dump(datas_EDC,f)
            f.close()
            #Nota Final
            with open('nota_final_EDC.pkl','wb') as f: 
                pickle.dump(nf_EDC,f)
            f.close()
            #Notas
            with open('notas_EDC.pkl','wb') as f: 
                pickle.dump(notas_EDC,f)
            f.close()
            #Cotação
            with open('cot_EDC.pkl','wb') as f: 
                pickle.dump(cot_EDC,f)
            f.close()
            #Continuação do Programa
            cont()
        else:
            if opc == '3':#Calcular Notas de MBD
                print('\n')
                global notas_MBD, nf_MBD, datas_MBD
                intro(nomes[2], docente_MBD,elementos_MBD)
                a=int(input('Quantos elementos de avaliação deseja inserir?\n'))
                print('\n')#Parágrafo
                cot_MBD=[]
                notas_MBD=[]   
                datas_MBD=[]
                nf_MBD=0
                i=0
                while i < a:
                    print('Data do Elemento a Introduzir:\n')
                    import datetime
                    ano = int(input('Introduza o ano:\n'))
                    mês = int(input('Introduza o mês:\n'))
                    dia = int(input('Introduza o dia:\n'))
                    date1 = datetime.date(ano, mês, dia)
                    datas_MBD.append(date1.__str__())
                    
                    cot_MBD.append(float(input('Introduza a percentagem relativa a esse elemento (sem %):\n')))
                    print('\n')#Parágrafo
                    print('Próximo elemento\n')
                    i=i+1
                i=0
                for i in range(len(cot_MBD)):
                    notas_MBD.append(float(input('Introduza a nota:\n')))
                    b=float((cot_MBD[i]/100)*notas_MBD[i])
                    nf_MBD=nf_MBD+b
                    i=i+1
                    if i == (a-1) and nf_MBD < 10:
                        min=(10-nf_MBD)/(cot_MBD[-1]/100)
                        if min >20:
                            print('Reprovado à disciplina:')
                            break
                        else:
                            print('ATENÇÃO! - Para ter aprovação da disciplina com 10 valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(min))
                
                    if i == (a-1) and nf_MBD > 9.5:
                        opc_nota=int(input('Indique o que pretende que seja a sua nota final para ser calculada a nota minima (0 a 20):\n'))
                        opc_nota_calc=(opc_nota - nf_MBD)/(cot_MBD[-1]/100)
                        if opc_nota_calc <20 and opc_nota_calc >0:
                            print('Para ter aprovação da disciplina com {} valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(opc_nota, opc_nota_calc))
                        else:
                            print('Não conseguirá atingir essa nota pretendida.')
                         
                print('A sua nota final é:\n')
                print(int(nf_MBD))
                #Gráfico
                graph_x(notas_MBD, elementos_MBD)
                #Tabela
                dados_MBD=[elementos_MBD, cot_MBD, datas_MBD, notas_MBD]
                tabela(dados_MBD)
                #Adição dos dados a um ficheiro
                adc_fich(dados_MBD, nomes[2], docente_MBD)
                #Pickle
                #Datas
                with open('datas_MBD.pkl','wb') as f: 
                    pickle.dump(datas_MBD,f)
                f.close()
                #Nota Final
                with open('nota_final_MBD.pkl','wb') as f: 
                    pickle.dump(nf_MBD,f)
                f.close()
                #Notas
                with open('notas_MBD.pkl','wb') as f: 
                    pickle.dump(notas_MBD,f)
                f.close()
                #Cotação
                with open('cot_MBD.pkl','wb') as f: 
                    pickle.dump(cot_MBD,f)
                f.close()
                #Continuação do Programa
                cont()
            else:
                if opc == '4':#Calcular Notas de SD
                    print('\n')#Parágrafo
                    global notas_SD, nf_SD, datas_SD
                    intro(nomes[3], docente_SD,elementos_SD)
                    a=int(input('Quantos elementos de avaliação deseja inserir?\n'))
                    print('\n')#Parágrafo
                    cot_SD=[]
                    notas_SD=[]
                    datas_SD=[]
                    nf_SD=0
                    i=0
                    while i < a:
                        print('Data do Elemento a Introduzir:\n')
                        import datetime
                        ano = int(input('Introduza o ano:\n'))
                        mês = int(input('Introduza o mês:\n'))
                        dia = int(input('Introduza o dia:\n'))
                        date1 = datetime.date(ano, mês, dia)
                        datas_SD.append(date1.__str__())
                        
                        cot_SD.append(float(input('Introduza a percentagem relativa a esse elemento (sem %):\n')))
                        print('\n')#Parágrafo
                        print('Próximo elemento\n')
                        i=i+1
                    i=0
                    for i in range(len(cot_SD)):
                        notas_SD.append(float(input('Introduza a nota:\n')))
                        b=float((cot_SD[i]/100)*notas_SD[i])
                        nf_SD=nf_SD+b
                        i=i+1
                        if i == (a-1) and nf_SD < 10:
                            min=(10-nf_SD)/(cot_SD[-1]/100)
                            if min >20:
                                print('Reprovado à disciplina.')
                                break
                            else:
                                    print('ATENÇÃO! - Para ter aprovação da disciplina com 10 valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(min))
                    
                        if i == (a-1) and nf_SD > 9.5:
                            opc_nota=int(input('Indique o que pretende que seja a sua nota final para ser calculada a nota minima (0 a 20):\n'))
                            opc_nota_calc=(opc_nota - nf_SD)/(cot_SD[-1]/100)
                            if opc_nota_calc <20 and opc_nota_calc >0:
                                print('Para ter aprovação da disciplina com {} valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(opc_nota, opc_nota_calc))
                            else:
                                print('Não conseguirá atingir essa nota pretendida.')
                             
                    print('A sua nota final é.\n')
                    print(int(nf_SD))
                    #Gráfico
                    graph_x(notas_SD, elementos_SD)
                    #Tabelas
                    dados_SD=[elementos_SD, cot_SD, datas_SD, notas_SD]
                    tabela(dados_SD)
                    #Adição dos dados a um ficheiro
                    adc_fich(dados_SD, nomes[3], docente_SD)
                    #Pickle
                    with open('datas_SD.pkl','wb') as f: 
                        pickle.dump(datas_SD,f)
                    f.close()
                    #Nota Final
                    with open('nota_final_SD.pkl','wb') as f: 
                        pickle.dump(nf_SD,f)
                    f.close()
                    #Notas
                    with open('notas_SD.pkl','wb') as f: 
                        pickle.dump(notas_SD,f)
                    f.close()
                    #Cotação
                    with open('cot_SD.pkl','wb') as f: 
                        pickle.dump(cot_SD,f)
                    f.close()
                    #Continuação do Programa
                    cont()
                else:
                    if opc == '5':#Calcular Nota de MAT
                        print('\n')#Parágrafo
                        global notas_MAT, nf_MAT, datas_MAT
                        intro(nomes[4], docente_MAT,elementos_MAT)
                        a=int(input('Quantos elementos de avaliação deseja inserir?\n'))
                        cot_MAT=[]
                        notas_MAT=[] 
                        datas_MAT=[]
                        nf_MAT=0
                        i=0
                        while i < a:
                            print('Data do Elemento a Introduzir:\n')
                            import datetime
                            ano = int(input('Introduza o ano:\n'))
                            mês = int(input('Introduza o mês:\n'))
                            dia = int(input('Introduza o dia:\n'))
                            date1 = datetime.date(ano, mês, dia)
                            datas_MAT.append(date1.__str__())
                            
                            cot_MAT.append(float(input('Introduza a percentagem relativa a esse elemento (sem %):\n')))
                            print('\n')#Parágrafo
                            print('Próximo elemento\n')
                            i=i+1
                        i=0
                        for i in range(len(cot_MAT)):
                            notas_MAT.append(float(input('Introduza a nota:\n')))
                            b=float((cot_MAT[i]/100)*notas_MAT[i])
                            nf_MAT=nf_MAT+b
                            i=i+1
                            if i == (a-1) and nf_MAT < 10:
                                min=(10-nf_MAT)/(cot_MAT[-1]/100)
                                if min >20:
                                    print('Reprovado à disciplina.')
                                    break
                                else:
                                        print('ATENÇÃO! - Para ter aprovação da disciplina com 10 valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(min))
                        
                            if i == (a-1) and nf_MAT > 9.5:
                                opc_nota=int(input('Indique o que pretende que seja a sua nota final para ser calculada a nota minima (0 a 20):\n'))
                                opc_nota_calc=(opc_nota - nf_MAT)/(cot_MAT[-1]/100)
                                if opc_nota_calc <20 and opc_nota_calc >0:
                                    print('Para ter aprovação da disciplina com {} valores precisa de ter no minimo {} valores no próximo item de avaliação.\n'.format(opc_nota, opc_nota_calc))
                                else:
                                    print('Não conseguirá atingir essa nota pretendida.')
                                 
                        print('A sua nota final é:\n')
                        print(int(nf_MAT))
                        #Gráfico
                        graph_x(notas_MAT, elementos_MAT)
                        #Tabela
                        dados_MAT=[elementos_MAT, cot_MAT, datas_MAT,notas_MAT]
                        tabela(dados_MAT)
                        #Adição dos dados a um ficheiro
                        adc_fich(dados_MAT, nomes[4], docente_MAT)
                        #Pickle
                        #Datas
                        with open('datas_MAT.pkl','wb') as f: 
                            pickle.dump(datas_MAT,f)
                        f.close()
                        #Nota Final
                        with open('nota_final_MAT.pkl','wb') as f: 
                            pickle.dump(nf_MAT,f)
                        f.close()
                        #Notas
                        with open('notas_MAT.pkl','wb') as f: 
                            pickle.dump(notas_MAT,f)
                        f.close()
                        #Cotação
                        with open('cot_MAT.pkl','wb') as f: 
                            pickle.dump(cot_MAT,f)
                        f.close()
                        #Continuação do Programa
                        cont()
                    else:
                        if opc != '1' and opc != '2' and opc != '3' and opc != '4' and opc != '5':
                            print('Opção Inválida!\n')
                            menu_calc()

def graph_x(nota, elementos):
    import matplotlib.pyplot as plt
    import numpy as np
    y = nota
    N = len(y)
    x = range(N)
    width = 1/1.5
    plt.bar(x, y, width, color='blue')
    plt.xlabel('Notas')
    plt.ylabel('Elementos de avaliação')
    y_pos = np.arange(len(elementos))
    plt.xticks(y_pos, elementos)
    plt.show()
    
def graph_y(nota, nomes):
    import matplotlib.pyplot as plt
    import numpy as np
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos=np.arange(len(nota))
    ax.barh(y_pos, nota,
            color='green',)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(nomes)
    ax.invert_yaxis()#Começar no primeiro elemento da lista
    ax.set_xlabel('Valores')
    ax.set_title('Notas Finais')
    ax.set_xbound(0,20)
    plt.show()

def tabela(linha):
    for i in range(0,len(linha)):
        for f in range(0,len(linha[i])):
            print('|{0:<16}|'.format(linha[i][f]),end='   ')
        print('\n')#Parágrafo

def intro(disciplina,docente,num):
    print('Calcular a nota de {}.\n'.format(disciplina))
    print('O(s) Docente(s) desta Disciplina:\n{}'.format(docente))
    print('Pela nossa base de dados constamos que existem {} elementos de avaliação.\n'.format(len(num)))
    
def criar_fich():#Função que cria um ficheiro onde é armazenada as informações. Ficheiro .txt com o modo 'w'
    curso=('- Engenharia Informática -')
    ficheiro_a=open('Notas Finais.txt','w') 
    ficheiro_a.write('AVALIAÇÃO CONTÍNUA 1.º ANO/1.º SEM {}\n'.format(curso)) #escreve no ficheiro
    ficheiro_a.write('Iremos dispor os resultados finais das disciplinas.')
    ficheiro_a.write('\n')
    ficheiro_a.close()
    
def adc_fich(lista, disicplina, docente):#Função que adiciona informação aos ficheiros em modo 'a', permitindo manter a informação previamente guardada
    ficheiro_a=open('Notas Finais.txt','a')
    ficheiro_a.write('\n')#Parágrafo
    ficheiro_a.write('Disciplina {}'.format(disicplina)) #escreve no ficheiro o nome atribuido numa variável 'nome'
    ficheiro_a.write('\n')#Parágrafo
    ficheiro_a.write('Docente {}'.format(docente)) #escreve no ficheiro o nome atribuido numa variável 'nome'
    ficheiro_a.write('\n')#Parágrafo
    ficheiro_a.write('\n')#Parágrafo
    for i in range(0,len(lista)): # ciclo i para as linhas da lista
        for j in range(len(lista[i])): # ciclo j para as colunas da lista
            print('|{0:<16}'.format(lista[i][j]),end=' | ',file=ficheiro_a)#print dados guardados nas listas
        # em 24 digitos '{0:16}' 
        # na mesma linha separados com espaços e | (end=' | ')
        print(file=ficheiro_a) 
    ficheiro_a.close()

def ver_fich():#Função para listar as tabelas
    ficheiro_a=open('Notas Finais.txt','r')
    dados=ficheiro_a.read()
    print(dados)
    ficheiro_a.close()
    menu()#chamada da função menu para continuar o programa

#INICIO
introducao()
a=input('É a primeira vez que corre este programa {}? Responda ''"s"'' para sim ou ''"n"'' para não.\n'.format(nome_uti))
if a == 'n':
    import pickle
    #Pickle - Des-serializar e atribuição de variáveis
    #AP
    #Datas
    with open('datas_AP.pkl','rb') as f:
        datas_AP=pickle.load(f)
    f.close()
    #Nota final
    with open('nota_final_AP.pkl','rb') as f:
        nf_AP=pickle.load(f)
    f.close()
    #Notas
    with open('notas_AP.pkl','rb') as f:
        notas_AP=pickle.load(f)
    f.close()
    #Cotação
    with open('cot_AP.pkl','rb') as f:
        cot_AP=pickle.load(f)
    f.close()
    #EDC
    #Datas
    with open('datas_EDC.pkl','rb') as f:
        datas_EDC=pickle.load(f)
    f.close()
    #Nota final
    with open('nota_final_EDC.pkl','rb') as f:
        nf_EDC=pickle.load(f)
    f.close()
    #Notas
    with open('notas_EDC.pkl','rb') as f:
        notas_EDC=pickle.load(f)
    f.close()
    #Cotação
    with open('cot_EDC.pkl','rb') as f:
        cot_EDC=pickle.load(f)
    f.close()
    #MBD
    #Datas
    with open('datas_MBD.pkl','rb') as f:
        datas_MBD=pickle.load(f)
    f.close()
    #Nota final
    with open('nota_final_MBD.pkl','rb') as f:
        nf_MBD=pickle.load(f)
    f.close()
    #Notas
    with open('notas_MBD.pkl','rb') as f:
        notas_MBD=pickle.load(f)
    f.close()
    #Cotação
    with open('cot_MBD.pkl','rb') as f:
        cot_MBD=pickle.load(f)
    f.close()
    #SD
    #Datas
    with open('datas_SD.pkl','rb') as f:
        datas_SD=pickle.load(f)
    f.close()
    #Nota final
    with open('nota_final_SD.pkl','rb') as f:
        nf_SD=pickle.load(f)
    f.close()
    #Notas
    with open('notas_SD.pkl','rb') as f:
        notas_SD=pickle.load(f)
    f.close()
    #Cotação
    with open('cot_SD.pkl','rb') as f:
        cot_SD=pickle.load(f)
    f.close()
    #MAT
    #Datas
    with open('datas_MAT.pkl','rb') as f:
        datas_MAT=pickle.load(f)
    f.close()
    #Nota final
    with open('nota_final_MAT.pkl','rb') as f:
        nf_MAT=pickle.load(f)
    f.close()
    #Notas
    with open('notas_MAT.pkl','rb') as f:
        notas_MAT=pickle.load(f)
    f.close()
    #Cotação
    with open('cot_MAT.pkl','rb') as f:
        cot_MAT=pickle.load(f)
    f.close()
    #Chamada de diferentes funções com uma determinada ordem
    menu()
else:
    if a == 's':
        criar_fich()#Criar o ficheiro onde serão armazenados os dados
        menu()
    else:
        if a != 's' or a != 'n':
            print('Input inválido!\n')
