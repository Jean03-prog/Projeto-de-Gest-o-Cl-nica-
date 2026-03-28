class Atendimento:
    def __init__(self, id, paciente_id, data, tipo, observacoes, status):
        self.id = id
        self.paciente_id = paciente_id
        self.data = data
        self.tipo = tipo
        self.observacoes = observacoes
        self.status = status
    def to_dict(self):
        return {
            "id": self.id,
            "paciente_id": self.paciente_id,
            "data": self.data,
            "tipo": self.tipo,
            "observacoes": self.observacoes,
            "status": self.status
        }
    @classmethod
    def from_dict(cls, dados):
        return cls (
            dados["id"],
            dados["paciente_id"],
            dados["data"],
            dados["tipo"],
            dados["observacoes"],
            dados["status"]
        )