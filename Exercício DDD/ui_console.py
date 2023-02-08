from ui import UI

class UIConsole:
    def __init__(self, ui: UI) -> None:
        self.ui = ui

    def get_busca_ddd(self) -> None:
        busca_ddd = input("Digite o ddd que você deseja buscar: ")
        resultado = self.ui.busca_ddd(int(busca_ddd))
        print(resultado)
        return resultado