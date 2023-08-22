# Conceito
# O padrão Singleton é um padrão de projeto criacional que garante que uma classe tenha apenas uma instância e fornece um ponto de acesso global para essa instância. Isso é útil quando exatamente um objeto é necessário para coordenar ações no sistema. O padrão é frequentemente usado para representar coisas como gerenciadores de configuração, conexões de rede, e gerenciadores de recursos, entre outros.
#
# Vantagens
# Instância Única: Garante que uma classe tenha apenas uma instância, o que pode economizar memória e recursos computacionais.
#
# Acesso Global: Fornece um ponto de acesso global, o que pode ser útil para operações de coordenação em diferentes partes do sistema.
#
# Inicialização Preguiçosa: A instância é geralmente criada quando é necessária pela primeira vez, o que pode melhorar o desempenho e o uso de recursos.
#
# Substituição Facilitada: Como há apenas uma instância, substituir essa instância afeta todo o sistema, o que pode ser útil para alterar comportamentos globalmente (por exemplo, mudar de um sistema de logging para outro).
#
# Desvantagens
# Global State: O Singleton frequentemente age como um estado global, o que pode ser problemático para o teste e pode levar a um acoplamento indesejado entre classes.
#
# Violação do Princípio da Responsabilidade Única: A classe Singleton frequentemente lida com a própria criação e com a lógica de negócios, o que viola o Princípio da Responsabilidade Única.
#
# Dificuldade de Subclasse: Extender uma classe Singleton pode ser complicado.
#
# Testabilidade: Testar classes que dependem de Singletons pode ser complicado, já que os testes podem acabar interferindo uns nos outros devido ao estado compartilhado.
#
# Concorrência: Em ambientes multithread, garantir que uma classe seja Singleton pode exigir mecanismos de bloqueio que podem afetar o desempenho.
#
# Pode Encorajar o Uso Indevido: A facilidade de implementação e uso pode encorajar os desenvolvedores a usá-lo para tudo, o que pode levar a problemas de design.

import json

class ConfigurationManager:
    _instance = None
    def __new__(cls, config_file=None):
        if cls._instance is None:
            print("Carregando configurações...")
            cls._instance = super(ConfigurationManager, cls).__new__(cls)
            if config_file:
                with open(config_file, "r") as f:
                    cls._instance.config_data = json.load(f)
            else:
                cls._instance.config_data = {}
        return cls._instance


    def get(self, key, default=None):
        return self.config_data.get(key, default)

    def set(self, key, value):
        self.config_data[key] = value

config1 = ConfigurationManager("config.json")

db_host = config1.get("db_host")
print(f"db_host: {db_host}")

config2 = ConfigurationManager()

db_host = config2.get("db_host")
print(f"db_host: {db_host}")

print(config1 is config2)
