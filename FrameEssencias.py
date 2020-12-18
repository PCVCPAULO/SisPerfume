"""Subclass of FrameEssencias, which is generated by wxFormBuilder."""

import wx
import guiperfumes
import db

# Implementing FrameEssencias
class FrameEssencias(guiperfumes.FrameEssencias):
	def __init__( self, parent ):
		guiperfumes.FrameEssencias.__init__( self, parent )
		self.atualizarGrid()

	# Handlers for FrameEssencias events.
	def fecharFrame( self, event ):
		self.Show(False)

	def adicionarEssencia( self, event ):
		nome=self.txtNome.GetValue() #Recupera o conteúdo da caixa de texto
		db.inserirEssencia(nome)    #Chama a função inserir Essencia do arquivo db.py
		#Exibe uma mensagem ao usuário confirmado o sucesso na inserção
		wx.MessageBox(message="Essência Inserida com Sucesso!",caption="SisPerfumes",style=wx.OK,parent=self)
		self.atualizarGrid()#Atualiza o grid com a relação de Essências

	# Essa função é chamada quando o usuário edita o conteúdo de uma célula do meu grid
	def atualizarEssencia( self, event ):
		nome_essencia=self.gridEssencias.GetCellValue(event.GetRow(),event.GetCol()) #Recupera a descrição da Essência editado
		if (nome_essencia): #Se o conteúdo não for vazio, faça
			id_essencia=int(self.gridEssencias.GetCellValue(event.GetRow(),0))#Pegue na linha editada, o conteúdo da primeira coluna
			db.atualizarEssencia(id_essencia, nome_essencia) #Chame a função para atualizar uma Essência
			wx.MessageBox(message="Essência Atualizado com Sucesso!",caption="SysPerfumes",style=wx.OK,parent=self)

	def atualizarGrid(self):
		if (self.gridEssencias.GetNumberRows()>0):
			self.gridEssencias.DeleteRows(0,self.gridEssencias.GetNumberRows()) #Limpa a tabela
		essencias=db.listarEssencia() #Chama a função listar Essências, retornando a lista de Essências existentes
		for essencias in essencias:
			self.gridEssencias.AppendRows(1)#Adiciona uma linha em branco
			self.gridEssencias.SetCellValue(self.gridEssencias.GetNumberRows()-1,0,str(essencias[0])) #adicione o id da Essência
			self.gridEssencias.SetCellValue(self.gridEssencias.GetNumberRows() - 1, 1, essencias[1]) #adiciona a descrição da Essência
			self.gridEssencias.SetReadOnly(self.gridEssencias.GetNumberRows() - 1, 0, True) #Informa que a coluna 0(ID) é somente leitura


