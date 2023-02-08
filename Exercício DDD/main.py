from ddd_cidade import CodeDDD
from ddd_cidade_repository import CodeDDDRepository
from ddd_cidade_service import CodeDDDService
from ui import UI
from ui_console import UIConsole

ddd_cidade_repository = CodeDDDRepository()

ddd75 = CodeDDD(75, "Feira de Santana")

ddd_cidade_repository.add_cidade(ddd75)

ddd_cidade_service = CodeDDDService(ddd_cidade_repository)
ui = UI(ddd_cidade_service)
ui_console = UIConsole(ui)

while (True):
    print(ddd_cidade_repository)
    resultado = ui_console.get_busca_ddd()
    if(resultado == "DDD não encontrado... "):
        break