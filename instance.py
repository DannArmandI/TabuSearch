" Clases para cargar y almacenar la instancia "


class ColumnLayout:
    " Clases para cargar y almacenar la instancia "
    index = 0
    cost = 0
    active_rows = []


# class Scp:

#     Columns:[ColumnLayout]
#     Rows = []


class Instance:
    " Clases para cargar y almacenar la instancia "
    column = 0
    row = 0
    lista = []
    columns = [ColumnLayout()]
    columns.clear()
    instancia = open('instance/scp41.txt', encoding='UTF-8')

    def set_instance(self):
        " Clases para cargar y almacenar la instancia "
        # cont = 0
        # print(Instancia.read())
        # Instancia = Instancia.read()
        lines = self.instancia.readline().split(' ')
        # line = lines.split(' ')
        # for line in lines:
        self.row = int(lines[1])
        self.column = int(lines[2])
        # print(Row)
        # print(Column)
        self.set_columns()
        self.set_rows()
        # print(self.Columns[1].Index)
        # print(self.Columns[3].Index)
        # print(self.Columns[4].Index)
        # if (self.Columns[0].ActiveRows==self.Columns[1].ActiveRows):
        #     print('Eooooooo')
        for column in self.columns:
            print('Indice:', column.index, ' Costo:', column.cost,
                  ' Active Rows: ', column.active_rows)
        #     # print(cont)
        #     # cont=cont+1
        #     print(column)
# print(column.Cost)

    def set_columns(self):
        " Clases para cargar y almacenar la instancia "
        cont = 0
        # aux:
        while 1:
            line = self.instancia.readline()
            elements = line.split(' ')
            for element in elements:
                if element.isdigit():
                    # self.Columns.append(Element)
                    # Aux:ColumnLayout
                    aux = ColumnLayout()
                    cont = cont+1
                    aux.index = cont
                    aux.cost = int(element)
                    aux.active_rows = []
                    # print(Aux.Cost)cl
                    # self.Columns.__add__()
                    self.columns.append(aux)
                    # self.addColumns(Aux)
                    # self.Columns.append(Aux)
                    # print(self.Columns[cont].Index)
                    # self.Columns[Column].Index = Column+1
                    # self.Columns[Column].Cost = int(Element)
            if cont == self.column:
                break

    def set_rows(self):
        " Clases para cargar y almacenar la instancia "
        for row in range(200):
            line = self.instancia.readline()
            cant_columns = int(line.split(' ')[1])
            # print(cantColumns)
            cont = 0
            while cont < cant_columns:
                line = self.instancia.readline()
                elements = line.split(' ')
                for element in elements:
                    if element.isdigit():
                        row_aux = row+1
                        cont = cont+1
                        self.columns[int(element) -
                                     1].active_rows.append(row_aux)
                        print('Adding Row ', row, ' To ', element)
