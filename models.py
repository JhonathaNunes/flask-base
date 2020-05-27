from banco import bd


class Presenca:
    def __init__(self, email, presenca, resposta, comentarios):
        self.email = email
        self.presenca = presenca
        self.resposta = resposta
        self.comentarios = comentarios

    def gravar(self):
        sql = '''
            insert into presenca
            (email, presenca, resposta, comentarios)
            values (?, ?, ?, ?)
        '''

        bd().execute(sql, [
            self.email,
            self.presenca,
            self.resposta,
            self.comentarios
            ]
        )

        bd().commit()

    @staticmethod
    def recupera_todos():
        sql = '''select * from presenca order by email desc'''
        cur = bd().execute(sql)

        presencas = []
        for email, presenca, resposta, comentarios in cur.fetchall():
            presenca = Presenca(email, presenca, resposta, comentarios)
            presencas.append(presenca)

        return presencas
