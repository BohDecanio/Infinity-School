from view import MaterialView
from controller import MaterialController

if __name__ == "__main__":
    view = MaterialView()

    controller = MaterialController(view)

    controller.executar()
