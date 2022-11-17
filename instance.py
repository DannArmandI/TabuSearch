" Clases para cargar y almacenar la instancia "


class ColumnLayout:
    " Clases para cargar y almacenar la instancia "
    index = 0
    cost = 0
    active_rows = []


class Instance:
    " Clases para cargar y almacenar la instancia "
    column = 0
    row = 0
    columns = [ColumnLayout()]
    columns.clear()
    instancia = open('instance/scp41.txt', encoding='UTF-8')

    def set_instance(self):
        " Clases para cargar y almacenar la instancia "
        lines = self.instancia.readline().split(' ')
        self.row = int(lines[1])
        self.column = int(lines[2])
        self.set_columns()
        self.set_active_rows()


    def set_columns(self):
        " Clases para cargar y almacenar la instancia "
        cont = 0
        while 1:
            line = self.instancia.readline()
            elements = line.split(' ')
            for element in elements:
                if element.isdigit():
                    aux = ColumnLayout()
                    cont = cont+1
                    aux.index = cont
                    aux.cost = int(element)
                    aux.active_rows = []
                    self.columns.append(aux)
            if cont == self.column:
                break

    def set_active_rows(self):
        " Clases para cargar y almacenar la instancia "
        for row in range(200):
            line = self.instancia.readline()
            cant_columns = int(line.split(' ')[1])
            cont = 0
            while cont < cant_columns:
                line = self.instancia.readline()
                elements = line.split(' ')
                for element in elements:
                    if element.isdigit():
                        cont = cont+1
                        self.columns[int(element) -
                                     1].active_rows.append(row)

    def print_instance(self):
        "asdasd"
        for column in self.columns:
            print('Indice:', column.index, ' Costo:', column.cost,
                  ' Active Rows: ', column.active_rows)
