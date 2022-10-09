

# from array import array




class ColumnLayout:

    Index = 0
    Cost = 0
    ActiveRows=[]
    

# class Scp:

#     Columns:[ColumnLayout]
#     Rows = []


class Instance:

    Column = 0
    Row = 0
    lista=[]
    Columns = [ColumnLayout()]
    Columns.clear()
    # aux=ColumnLayout()
    # aux.Index=1
    # aux.Cost=2
    # aux.ActiveRows=[]
    # # aux2=ColumnLayout()
    # Columns.append(aux)
    # aux2=ColumnLayout()
    # aux2.Index=3
    # aux2.Cost=2
    # aux2.ActiveRows=[]
    # Columns.append(aux2)
    # aux2.ActiveRows.append(7)
    # Columns[0].ActiveRows=[2]
    # Columns[1].ActiveRows=[4]
    # print()
    # Rows = array()
    Instancia = open('instance/scp41.txt')

    def getInstance(self):
        cont = 0
        # print(Instancia.read())
        # Instancia = Instancia.read()
        Lines = self.Instancia.readline().split(' ')
        # line = lines.split(' ')
        # for line in lines:
        self.Row = int(Lines[1])
        self.Column = int(Lines[2])
        # print(Row)
        # print(Column)
        self.getColumns()
        self.getActiveRow()
        # print(self.Columns[1].Index)
        # print(self.Columns[3].Index)
        # print(self.Columns[4].Index)
        # if (self.Columns[0].ActiveRows==self.Columns[1].ActiveRows):
        #     print('Eooooooo')
        for column in self.Columns:
            print('Indice:', column.Index, ' Costo:', column.Cost, ' Active Rows: ',column.ActiveRows)
        #     # print(cont)
        #     # cont=cont+1
        #     print(column)
# print(column.Cost)

    def getColumns(self):
        cont = 0
        # aux:
        for Column in range(self.Column):
            Line = self.Instancia.readline()
            Elements = Line.split(' ')
            for Element in Elements:
                if Element.isdigit():
                    # self.Columns.append(Element)
                    # Aux:ColumnLayout
                    Aux = ColumnLayout()
                    cont = cont+1
                    Aux.Index = cont
                    Aux.Cost = int(Element)
                    Aux.ActiveRows=[]
                    # print(Aux.Cost)cl
                    # self.Columns.__add__()
                    self.Columns.append(Aux)
                    # self.addColumns(Aux)
                    # self.Columns.append(Aux)
                    # print(self.Columns[cont].Index)
                    # self.Columns[Column].Index = Column+1
                    # self.Columns[Column].Cost = int(Element)
            if cont == self.Column:
                break

    def getActiveRow(self):
        for Row in range(200):
            Line = self.Instancia.readline()
            cantColumns = int(Line.split(' ')[1])
            # print(cantColumns)
            cont = 0
            while cont < cantColumns:
                Line = self.Instancia.readline()
                Elements=Line.split(' ')
                for Element in Elements:
                    if Element.isdigit():
                        row=Row+1
                        cont=cont+1
                        self.Columns[int(Element)-1].ActiveRows.append(row)
                        print('Adding Row ',row , ' To ',Element)
    

if __name__ == "__main__":
    Instancia = Instance()
    Instancia.getInstance()
