"""Subclass of FrameFixacao, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db

# Implementing FrameVolumes
class FrameFixacao(guiperfumes.FrameFixacao):
	def __init__( self, parent ):
		guiperfumes.FrameFixacao.__init__( self, parent )
		self.atualizarGrid()

	# Handlers for FrameVolumes events.
	def fecharFrame( self, event ):
		self.Show(False)

	def adicionarFixacao( self, event ):
		nome=self.txtNome.GetValue() #Recupera o conteúdo da caixa de texto
		db.inserirFixacao(nome) #Chama a função inserir Fixação do arquivo db.py
		#Exibe uma mensagem ao usuário confirmado o sucesso na inserção
		wx.MessageBox(message="Fixação Inserida com Sucesso!",caption="SisPerfumes",style=wx.OK,parent=self)
		self.atualizarGrid()#Atualiza o grid com a relação de marcas

	# Essa função é chamada quando o usuário edita o conteúdo de uma célula do meu grid
	def atualizarFixacao( self, event ):
		nome_fixacao=self.gridFixacoes.GetCellValue(event.GetRow(),event.GetCol()) #Recupera a descrição do fixacao editado
		if (nome_fixacao): #Se o conteúdo não for vazio, faça
			id_fixacao=int(self.gridFixacoes.GetCellValue(event.GetRow(),0))#Pegue na linha editada, o conteúdo da primeira coluna
			db.atualizarFixacao(id_fixacao, nome_fixacao) #Chame a função para atualizar uma Fixacão
			wx.MessageBox(message="Fixação Atualizado com Sucesso!",caption="SysPerfumes",style=wx.OK,parent=self)

	def atualizarGrid(self):
		if (self.gridFixacoes.GetNumberRows()>0):
			self.gridFixacoes.DeleteRows(0,self.gridFixacoes.GetNumberRows()) #Limpa a tabela
		fixacao=db.listarFixacao() #Chama a função listar fixações, retornando a lista de fixações existentes
		for fixacao in fixacao:
			self.gridFixacoes.AppendRows(1)#Adiciona uma linha em branco
			self.gridFixacoes.SetCellValue(self.gridFixacoes.GetNumberRows()-1,0,str(fixacao[0])) #adicione o id da fixação
			self.gridFixacoes.SetCellValue(self.gridFixacoes.GetNumberRows() - 1, 1, fixacao[1]) #adiciona a descrição da fixação
			self.gridFixacoes.SetReadOnly(self.gridFixacoes.GetNumberRows() - 1, 0, True) #Informa que a coluna 0(ID) é somente leitura



