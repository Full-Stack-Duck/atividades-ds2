from ddd_cidade import CodeDDD
from ddd_cidade_repository import CodeDDDRepository

class CodeDDDService:
    def __init__(self, ddd_cidade_repository: CodeDDDRepository) -> None:
        self.ddd_cidade_repository = ddd_cidade_repository

    def get_ddd(self, ddd: int) -> CodeDDD:
        if(self.ddd_cidade_repository.check_cidade(ddd)):
            return self.ddd_cidade_repository.get_cidade(ddd)
        return None