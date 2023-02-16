import sqlite3


class AgendaDB:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, name, fone):
        consulta = 'INSERT OR IGNORE INTO agenda (name, fone) VALUES (?, ?)'
        self.cursor.execute(consulta, (name, fone))
        self.conn.commit()

    def editar(self, name, fone, id):
        consulta = 'UPDATE OR IGNORE agenda SET name=?, fone=? WHERE id=?'
        self.cursor.execute(consulta, (name, fone, id))
        self.conn.commit()

    def excluir(self, id):
        conulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(conulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM agenda')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        conulta = 'SELECT * FROM agenda WHERE name LIKE ?'
        self.cursor.execute(conulta, (f'%{valor}%',))

        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = AgendaDB('agenda.db')

    agenda.buscar('luiz')

    agenda.fechar()