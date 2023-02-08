from ddd_cidade import CodeDDD
from ddd_cidade_service import CodeDDDService

class UI:
    def __init__(self, ddd_cidade_service: CodeDDDService) -> None:
        self.ddd_cidade_service = ddd_cidade_service

    def busca_ddd(self, ddd: int) -> str:
        cidade = self.ddd_cidade_service.get_ddd(ddd)
        if(cidade == None):
            return "Esse DDD não existe..."
        return f"DDD pertence a: {cidade}"