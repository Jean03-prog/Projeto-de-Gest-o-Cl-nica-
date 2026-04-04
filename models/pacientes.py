class Paciente:
    def __init__(self, id, nome, data_nascimento, telefone, email):
        self.id = id
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.telefone = telefone
        self.email = email
    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "data_nascimento": self.data_nascimento,
            "telefone": self.telefone,
            "email": self.email
        }
    @classmethod
    def from_dict(cls, dados):
        return cls (
            dados["id"],
            dados["nome"],
            dados["data_nascimento"],
            dados["telefone"],
            dados["email"]
        )