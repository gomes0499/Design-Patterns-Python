#
# Conceito
# O padrão Factory Method é um padrão de projeto criacional que fornece uma interface para criar objetos em uma superclasse, mas permite que subclasses alterem o tipo de objetos que serão criados. Em outras palavras, o Factory Method delega a responsabilidade de instanciar uma classe para suas subclasses.
#
# Vantagens
# Separação de Responsabilidades: Este padrão separa o código de construção do código que realmente utiliza o objeto. Isso torna o código mais limpo e mais fácil de manter.
#
# Extensibilidade: É fácil adicionar novas classes ao sistema, já que você pode introduzir novas fábricas sem alterar o código existente. Isso segue o Princípio Aberto/Fechado.
#
# Desacoplamento: As classes cliente estão desacopladas das classes que efetivamente implementam a lógica, já que a criação está isolada em um método. Isso facilita a testabilidade e a manutenção.
#
# Polimorfismo: O Factory Method frequentemente utiliza polimorfismo para realizar sua tarefa, o que torna o sistema mais flexível.
#
# Desvantagens
# Complexidade: O padrão pode adicionar complexidade ao código, já que ele introduz uma série de novas subclasses. Isso pode ser um exagero para projetos mais simples.
#
# Acoplamento: Embora o padrão possa reduzir o acoplamento entre o cliente e a implementação, ele pode aumentar o acoplamento entre as subclasses, já que cada nova implementação requer uma nova subclasse de fábrica.
#
# Padrão Overkill: Em alguns casos, o padrão pode ser um "overkill" se a criação do objeto não for complexa e não for provável que mude no futuro.
#
# Identificação Difícil: Às vezes, pode ser difícil identificar antecipadamente quais classes podem ser beneficiadas pelo Factory Method, o que pode levar a refatorações significativas mais tarde.
#
# O Factory Method é uma ferramenta poderosa, mas, como qualquer padrão de projeto, ele tem seus prós e contras. É importante avaliar cuidadosamente se o padrão é apropriado para o problema específico que você está tentando resolver.


from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Lion(Animal):
    def speak(self):
        return "Roar"

class Tiger(Animal):
    def speak(self):
        return "Growl"

class Bear(Animal):
    def speak(self):
        return "Grr"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "Lion":
            return Lion()
        elif animal_type == "Tiger":
            return Tiger()
        elif animal_type == "Bear":
            return Bear()
        else:
            raise ValueError("Invalid animal Type")


factory = AnimalFactory()

animal1 = factory.create_animal("Lion")
print(animal1.speak())

animal2 = factory.create_animal("Tiger")
print(animal2.speak())

animal3 = factory.create_animal("Bear")
print(animal3.speak())
