# Diferenças entre Abstract Factory e Factory Method
# Número de Produtos: O Factory Method é utilizado para criar um tipo de produto, enquanto o Abstract Factory é usado para criar famílias de produtos relacionados.
#
# Complexidade: O Abstract Factory é geralmente mais complexo de implementar, pois envolve múltiplas classes e interfaces.
#
# Flexibilidade: O Abstract Factory é mais flexível e pode ser facilmente estendido para incluir novos tipos de produtos na família.
#
# Nível de Abstração: O Abstract Factory opera em um nível de abstração mais alto, lidando com famílias de objetos relacionados, enquanto o Factory Method lida com a criação de um único tipo de objeto.
#
# Ambos os padrões têm o objetivo de desacoplar o cliente da criação de objetos, mas eles são usados em cenários diferentes.

from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def paint(self):
        pass
class Window(ABC):
    @abstractmethod
    def paint(self):
        pass

class WindowsButton(Button):
    def paint(self):
        return "Render a button in a Windows style"

class MacOSButton(Button):
    def paint(self):
        return "Render a button in a MacOS style"

class WindowsWindow(Window):
    def paint(self):
        return "Render a window in a Windows style"

class MacOSWindow(Window):
    def paint(self):
        return "Render a window in a MacOS style"

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self):
        pass

    @abstractmethod
    def create_window(self):
        pass

class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_window(self):
        return MacOSWindow()

# Client code
def gui_elements(factory: GUIFactory):
    button = factory.create_button()
    window = factory.create_window()
    print(button.paint())
    print(window.paint())

# Usando a fábrica do Windows
windows_factory = WindowsFactory()
gui_elements(windows_factory)

# Usando a fábrica do MacOS
macos_factory = MacOSFactory()
gui_elements(macos_factory)
