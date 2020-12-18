import sqlite3
path=r'D:\Projeto_Devs_Web_(GitHub)\IFRN\SisPerfume'
#O nome do banco criado foi dbperfumes-v2.db. Se você criar com outro nome, troque aqui
banco=sqlite3.connect(path+r'\dbperfumes-v2.db')
'''
Essa função insere um marca no banco de dados, recebendo como parâmetro o nome da marca
'''
def inserirMarca(nome_marca):
    sql="insert into Marcas (nome) values('{0}')".format(nome_marca)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
'''
Essa função atualiza uma marca no banco de dados, recebendo como parâmetros
o id e o nome. O id é necessário para ser usado na instrução update
'''
def atualizarMarca(id,nome):
    sql="update Marcas set nome='{0}' where id={1}".format(nome,id)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()
'''
Essa função localiza uma marca pelo seu nome, partindo do pressuposto que não
existirão marcas com nomes iguais
'''
def localizarMarcaPorNome(nome):
    sql="select * from Marcas where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    marca=cursor.fetchone()
    cursor.close()
    return marca
'''
Essa função retorna uma lista Python com todas as marcas cadastradas no banco de dados,
trazendo o id o nome da marca
'''
def listarMarca():
    sql="select * from Marcas"
    cursor=banco.cursor()
    cursor.execute(sql)
    marcas=cursor.fetchall()
    cursor.close()
    return marcas
'''
Essa função retorna uma lista Python contendo o nome de todas marcas,
ordenadas pelo nome
'''
def listarMarcaNome():
    sql="select nome from Marcas order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_marcas=cursor.fetchall()
    cursor.close()
    marcas=[]
    for nome_marca in nome_marcas:
        marcas.append(nome_marca[0])
    return marcas

def inserirVolume(nome_volume):
    sql="insert into Volumes (nome) values('{0}')".format(nome_volume)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()

def atualizarVolume(id,nome):
    sql="update Volumes set nome='{0}' where id={1}".format(nome,id)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()

def listarVolume():
    sql="select * from Volumes"
    cursor=banco.cursor()
    cursor.execute(sql)
    volumes=cursor.fetchall()
    cursor.close()
    return volumes

def listarVolumeNome():
    sql="select nome from Volumes order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_volumes=cursor.fetchall()
    cursor.close()
    volumes=[]
    for nome_volume in nome_volumes:
        volumes.append(nome_volume[0])
    return volumes

def localizarVolumePorNome(nome):
    sql="select * from Volumes where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    volume=cursor.fetchone()
    cursor.close()
    return volume

def inserirFixacao(nome):
    sql="insert into Fixacoes (nome) values('{0}')".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()

def atualizarFixacao(id,nome):
    sql="update Fixacoes set nome='{0}' where id={1}".format(nome,id)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()

def listarFixacao():
    sql="select * from Fixacoes"
    cursor=banco.cursor()
    cursor.execute(sql)
    fixacao=cursor.fetchall()
    cursor.close()
    print(len(fixacao))
    return fixacao

def localizarFixacaoPorNome(nome):
    sql="select * from Fixacoes where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    fixacao=cursor.fetchone()
    cursor.close()
    return fixacao

def listarFixacaoNome():
    sql="select nome from Fixacoes order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_fixacoes=cursor.fetchall()
    cursor.close()
    fixacoes=[]
    for nome_fixacao in nome_fixacoes:
        fixacoes.append(nome_fixacao[0])
    return fixacoes

def inserirEssencia(nome):
    sql="insert into Essencias (nome) values('{0}')".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()

def atualizarEssencia(id,nome):
    sql="update Essencias set nome='{0}' where id={1}".format(nome,id)
    cursor=banco.cursor()
    cursor.execute(sql)
    banco.commit()
    cursor.close()

def listarEssencia():
    sql="select * from Essencias"
    cursor=banco.cursor()
    cursor.execute(sql)
    essencia=cursor.fetchall()
    cursor.close()
    print(len(essencia))
    return essencia

def localizarEssenciaPorNome(nome):
    sql="select * from Essencias where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    essencia=cursor.fetchone()
    cursor.close()
    return essencia

def listarEssenciaNome():
    sql="select nome from Essencias order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_essencias=cursor.fetchall()
    cursor.close()
    essencias=[]
    for nome_essencia in nome_essencias:
        essencias.append(nome_essencia[0])
    return essencias

def vincularEssenciaPerfume():
    sql="SELECT * FROM Perfumes AS P JOIN Essencias AS E ON P.ID = E.ID"
    cursor=banco.cursor()
    cursor.execute(sql)
    essencia_perfume=cursor.fetchall()
    cursor.close()
    print(len(essencia_perfume))
    return essencia_perfume

def listarEssencia_Perfume():
    sql="select * from Essencia_Perfume"
    cursor=banco.cursor()
    cursor.execute(sql)
    essenciaP=cursor.fetchall()
    cursor.close()
    print(len(essenciaP))
    return essenciaP

def localizarPerfumePorNome(nome):
    sql="select * from Perfumes where nome='{0}'".format(nome)
    cursor=banco.cursor()
    cursor.execute(sql)
    perfume=cursor.fetchone()
    cursor.close()
    return perfume

def salvarVinculo(listaEssencia_Perfume):
    cursor=banco.cursor()
    for essencia_perfume in listaEssencia_Perfume: #For percorre a lista de perfumes, inserindo ou atualizando, um por um
        sql=''
        #Se essencia_perfume[0] for vazio, ou seja, o id, significa que temos que incliuir o registro
        if essencia_perfume[0]=='':
            #As funções localizar buscam o id do perfume e essência, de forma a garantir a integridade do banco de dados
            sql="insert into essencia_perfume (id_perfume,id_essencia) values({0},{1})".format(essencia_perfume[0],essencia_perfume[1])

        #Caso contrário, devemos atualizar
        else:
            sql="update essencia_perfume set id_perfume={0},id_esencia={1} where id={0}".format(essencia_perfume[0],essencia_perfume[1])
        try:
            cursor.execute(sql) #Executo a instrução, se der um erro, retorna a mensagem de erro
        except sqlite3.Error as e:
            return False,"Erro ao salvar essencia_perfume: "+e.args[0]
    banco.commit() #Se tudo correr bem, confirma as alterações no banco
    cursor.close() #Fecha a conexão
    return True,None #Retorna dizendo que deu certo salvar a lista de perfumes



'''
Essa função lista todos os perfumes, trazendo as informações completas e relacionadas com as outras tabelas,
de forma que a lista final tem os segintes campos: id do Perfume, nome do perfume, quantidade do perfume,
nome do volume, nome da marca e nome da fixação
'''

def listarPerfumes():
    sql='''
        select Perfumes.id, Perfumes.nome,Perfumes.quantidade,Volumes.nome,Marcas.nome,Fixacoes.nome from 
        Perfumes inner join Volumes on Perfumes.id_volume=Volumes.id 
        inner join Marcas on Perfumes.id_marca=Marcas.id inner join Fixacoes on Perfumes.id_fixacao=Fixacoes.id
    '''
    cursor=banco.cursor()
    cursor.execute(sql)
    perfumes=cursor.fetchall()
    return perfumes

def listarPerfumesID():
    sql="select id from Perfumes order by id"
    cursor=banco.cursor()
    cursor.execute(sql)
    id_perfumes=cursor.fetchall()
    cursor.close()
    ids=[]
    for id_perfume in id_perfumes:
        ids.append(id_perfume[0])
    return ids

def listarPerfumesNome():
    sql="select nome from Perfumes order by nome"
    cursor=banco.cursor()
    cursor.execute(sql)
    nome_perfumes=cursor.fetchall()
    cursor.close()
    perfumes=[]
    for nome_perfume in nome_perfumes:
        perfumes.append(nome_perfume[0])
    return perfumes

'''
Essa função é a mais complexa do nosso programa. Ela recebe como parâmetro uma lista de perfumes,
que virá do FramePerfumes. Essa lista deve conter 6 elementos:
listaPerfumes[0]--> id do perfume. Se for vazio, significa que iremos inserir
listaPerfumes[1]--> Nome do Perfume
listaPerfumes[2]--> Quantidade do Perfume
listaPerfumes[3]--> Nome do Volume
listaPerfumes[4]--> Nome da Marca
listaPerfumes[5]-->Nome da Fixação

'''
def salvarPerfumes(listaPerfumes):
    cursor=banco.cursor()
    for perfume in listaPerfumes: #For percorre a lista de perfumes, inserindo ou atualizando, um por um
        sql=''
        #Se perfume[0] for vazio, ou seja, o id, significa que temos que incliuir o registro
        if perfume[0]=='':
            #As funções localizar buscam o id do volume, marca e fixacao, de forma a garantir a integridade do banco de dados
            sql="insert into perfumes (nome,quantidade,id_volume,id_marca,id_fixacao) " \
                "values('{0}',{1},{2},{3},{4})".format(perfume[1],perfume[2],localizarVolumePorNome(perfume[3])[0],
                                                       localizarMarcaPorNome(perfume[4])[0],
                                                       localizarFixacaoPorNome(perfume[5])[0])
        #Caso contrário, devemos atualizar
        else:
            sql="update perfumes set nome='{1}',quantidade={2},id_volume={3}," \
                "id_marca={4},id_fixacao={5} where id={0}".format(perfume[0],perfume[1],perfume[2],
                                                                  localizarVolumePorNome(perfume[3])[0],
                                                                  localizarMarcaPorNome(perfume[4])[0],
                                                                  localizarFixacaoPorNome(perfume[5])[0])
        try:
            cursor.execute(sql) #Executo a instrução, se der um erro, retorna a mensagem de erro
        except sqlite3.Error as e:
            return False,"Erro ao salvar perfume: "+e.args[0]
    banco.commit() #Se tudo correr bem, confirma as alterações no banco
    cursor.close() #Fecha a conexão
    return True,None #Retorna dizendo que deu certo salvar a lista de perfumes