from ddd_cidade import CodeDDD

class CodeDDDRepository:
    def __init__(self) -> None:
        self.codes_ddd: CodeDDD = []

    def add_cidade(self, cidade: CodeDDD) -> None:
        self.codes_ddd.append(cidade)

    def get_cidade(self, ddd: int) -> CodeDDD:
        for cidade in self.codes_ddd:
            if(ddd == cidade.ddd):
                return cidade

    def check_cidade(self, ddd: int) -> bool:
        for cidade in self.codes_ddd:
            if(ddd == cidade.ddd):
                return True
        return False

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20}\n"
        tabela = formatText.format("DDD", "Cidade")

        for cidade in self.codes_ddd:
            tabela += formatText.format(cidade.ddd, cidade.cidade)
        return tabela
