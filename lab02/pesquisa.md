# 🧪Laboratório 02 — Estratégias e Níveis de Teste na Prática


## Domínio:
    Sistema de Transferências Bancárias Instantâneas do Banco do Brasil (Gateway Pix).


## Sumário

├── [1. Teste de Unidade (Unit Testing)](#1-teste-de-unidade-unit-testing)<br>
│   └── [1.1 Verificação de lógica atômica em componente/classe isolada](#11---verificacao-de-logica-atomica-em-componenteclasse-isolada-validacao-de-chave-pix-cpf)<br>
│<br>
├── [2. Teste de Integração (Integration Testing)](#2-teste-de-integracao-integration-testing)<br>
│   ├── [2.1 Integração Não Incremental (Big Bang)](#21---integracao-nao-incremental-big-bang)<br>
│   ├── [2.2 Integração Incremental Top-Down (Descendente) com uso de Stubs](#22---integracao-incremental-top-down-descendente-com-uso-de-stubs)<br>
│   ├── [2.3 Integração Incremental Bottom-Up (Ascendente) com uso de Drivers](#23---integracao-incremental-bottom-up-ascendente-com-uso-de-drivers)<br>
│   ├── [2.4 Teste de Fumaça (Smoke Testing)](#24---teste-de-fumaca-smoke-testing)<br>
│   └── [2.5 Teste de Regressão](#25---teste-de-regressao)<br>
│<br>
├── [3. Teste de Validação (Validation Testing)](#3-teste-de-validacao-validation-testing)<br>
│   ├── [3.1 Critérios de Aceitação (User Acceptance Testing)](#31---criterios-de-aceitacao-user-acceptance-testing---uat)<br>
│   ├── [3.2 Teste Alfa (Alpha Testing)](#32---teste-alfa-alpha-testing)<br>
│   └── [3.3 Teste Beta (Beta Testing)](#33---teste-beta-beta-testing)<br>
│<br>
└── [4. Teste de Sistema (System Testing)](#4-teste-de-sistema-system-testing)<br>
    ├── [4.1 Teste de Recuperação (Recovery Testing)](#41---teste-de-recuperacao-recovery-testing)<br>
    ├── [4.2 Teste de Segurança (Security Testing)](#42---teste-de-seguranca-security-testing)<br>
    ├── [4.3 Teste de Estresse (Stress Testing)](#43---teste-de-estresse-stress-testing)<br>
    └── [4.4 Teste de Desempenho (Performance Testing)](#44---teste-de-desempenho-performance-testing)

<br>


## 1. Teste de Unidade (Unit Testing)

### 1.1 — Verificação de Lógica Atômica em Componente/Classe Isolada (Validação de Chave Pix CPF)

1. Diagrama de Classes UML

    O diagrama abaixo ilustra o teste de unidade focado na classe isolada **ValidadorChavePix**, responsável por verificar atomicamente se uma string é um CPF válido, sem nenhuma dependência de banco de dados ou redes externas.

    ```mermaid
            classDiagram
        class ValidadorChavePix {
            +validarCPF(chave: String) Boolean
            -calcularDigitoVerificador(base: String) int
        }
        class ValidadorChavePixTest {
            -validador: ValidadorChavePix
            +setup() void
            +testValidarCPF_ComSucesso() void
            +testValidarCPF_Invalido_DeveRetornarFalso() void
            +testValidarCPF_FormatoErrado_DeveRetornarFalso() void
        }
        ValidadorChavePixTest ..> ValidadorChavePix : <<instantiates and tests>>
    ```

    Visualização PlantUml

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte e cole no seu renderizador de preferência.


2. Código-fonte do Diagrama (Mermaid e PlantUML)

    Código-fonte Mermaid

    ```mermaid
        classDiagram
        class ValidadorChavePix {
            +validarCPF(chave: String) Boolean
            -calcularDigitoVerificador(base: String) int
        }
        class ValidadorChavePixTest {
            -validador: ValidadorChavePix
            +setup() void
            +testValidarCPF_ComSucesso() void
            +testValidarCPF_Invalido_DeveRetornarFalso() void
            +testValidarCPF_FormatoErrado_DeveRetornarFalso() void
        }
        ValidadorChavePixTest ..> ValidadorChavePix : <<instantiates and tests>>
    ```

    Código-fonte PlantUml

    ```mermaid
        @startuml
        skinparam classAttributeIconSize 0

        class ValidadorChavePix {
            +validarCPF(chave: String): Boolean
            -calcularDigitoVerificador(base: String): int
        }

        class ValidadorChavePixTest {
            -validador: ValidadorChavePix
            +setup(): void
            +testValidarCPF_ComSucesso(): void
            +testValidarCPF_Invalido_DeveRetornarFalso(): void
            +testValidarCPF_FormatoErrado_DeveRetornarFalso(): void
        }

        ValidadorChavePixTest ..> ValidadorChavePix : <<instantiates and tests>>
        @enduml
    ```

3. Explicação Textual do Cenário:

    **Contexto:** No desenvolvimento do ecossistema do Gateway Pix do Banco do Brasil, o componente de cadastro e roteamento precisa garantir que os dados de entrada inseridos pelo usuário sejam estruturalmente íntegros antes de qualquer chamada de rede ao DICTA (Banco Central). A validação do formato de chaves Pix baseadas em CPF é uma operação puramente matemática (cálculo dos dígitos verificadores) e de correspondência de padrão de string.

    **Como a abordagem de Teste de Unidade Isolada é aplicada:**

     * **Classe Real** sob Teste (Alvo): A classe utilitária ValidadorChavePix é o componente sob teste. Ela opera de forma 100% isolada e sem estado interno complexo. Seu método público validarCPF(String) aciona o método privado calcularDigitoVerificador(String) para executar o algoritmo oficial de validação de CPF.
    
     * **Classe de Teste:** A classe ValidadorChavePixTest atua como a suite de testes automatizada (usando frameworks como JUnit). No método setup(), o componente alvo é instanciado na memória RAM.

     * **Cenários Testados e Objetivo:** O objetivo é testar a lógica matemática de forma atômica contra diferentes entradas (Input/Output). O método testValidarCPF_ComSucesso() injeta um CPF estruturalmente correto e valida o retorno verdadeiro. Os métodos testValidarCPF_Invalido_DeveRetornarFalso() e testValidarCPF_FormatoErrado_DeveRetornarFalso() testam CPFs com dígitos incorretos e strings com letras ou comprimentos errados, respectivamente.

     * **Tipo de Defeito que Visa Revelar:** Erros de lógica matemática na rotina do algoritmo de verificação (ex.: erro de indexação no laço for que multiplica os pesos dos dígitos), falhas no tratamento de strings nulas ou vazias, e comportamentos inesperados ao processar CPFs compostos por números repetidos (ex.: "111.111.111-11"), que passam no cálculo tradicional mas são inválidos.


## 2. Teste de Integração (Integration Testing)

### 2.1 — Integração Não Incremental (Big Bang)

1. Diagrama de Classes UML

    O diagrama ilustra o cenário onde todos os módulos desenvolvidos em paralelo são unificados e testados de uma única vez.

    ```mermaid
    classDiagram
        class PixAPI {
            +processarTransferencia(req: Request) Response
        }
        class MotorDeFraude {
            +analisarRisco(conta: String, valor: double) Boolean
        }
        class ValidadorDeSaldo {
            +reservarSaldo(conta: String, valor: double) Boolean
        }
        class ConectorSPI {
            +liquidarNoBacen(dados: Transacao) Boolean
        }
        class SuiteTesteBigBang {
            +testarFluxoCompletoDoSistema() void
        }
        SuiteTesteBigBang ..> PixAPI : <<chama>>
        PixAPI --> MotorDeFraude : <<integra com>>
        PixAPI --> ValidadorDeSaldo : <<integra com>>
        PixAPI --> ConectorSPI : <<integra com>>
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    classDiagram
        class PixAPI {
            +processarTransferencia(req: Request) Response
        }
        class MotorDeFraude {
            +analisarRisco(conta: String, valor: double) Boolean
        }
        class ValidadorDeSaldo {
            +reservarSaldo(conta: String, valor: double) Boolean
        }
        class ConectorSPI {
            +liquidarNoBacen(dados: Transacao) Boolean
        }
        class SuiteTesteBigBang {
            +testarFluxoCompletoDoSistema() void
        }
        SuiteTesteBigBang ..> PixAPI : <<chama>>
        PixAPI --> MotorDeFraude : <<integra com>>
        PixAPI --> ValidadorDeSaldo : <<integra com>>
        PixAPI --> ConectorSPI : <<integra com>>
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    skinparam classAttributeIconSize 0

    class PixAPI {
        +processarTransferencia(req: Request): Response
    }
    class MotorDeFraude {
        +analisarRisco(conta: String, valor: double): Boolean
    }
    class ValidadorDeSaldo {
        +reservarSaldo(conta: String, valor: double): Boolean
    }
    class ConectorSPI {
        +liquidarNoBacen(dados: Transacao): Boolean
    }
    class SuiteTesteBigBang {
        +testarFluxoCompletoDoSistema(): void
    }

    SuiteTesteBigBang ..> PixAPI
    PixAPI --> MotorDeFraude
    PixAPI --> ValidadorDeSaldo
    PixAPI --> ConectorSPI
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: As equipes terminaram o desenvolvimento inicial das quatro frentes do Gateway Pix. Em vez de testar as conexões passo a passo, a gerência decide realizar um teste unificado, implantando a PixAPI, o MotorDeFraude, o ValidadorDeSaldo e o ConectorSPI juntos em um ambiente de homologação.
    Como a abordagem Big Bang é aplicada:

    * Módulos sob Teste: Todos os componentes do ecossistema são acoplados simultaneamente.
    * Execução: A classe SuiteTesteBigBang dispara uma requisição de transferência completa para a PixAPI.processarTransferencia(). A requisição trafega em cascata por todos os componentes reais até a simulação da ponta final.
    * Tipo de Defeito que Visa Revelar: Incompatibilidades generalizadas de interface (ex.: PixAPI passa o valor como String, mas o MotorDeFraude espera Double), estouros de timeout cascateados ou falhas de configuração de dependências de infraestrutura que impedem os sistemas de se comunicarem. Nota: Se o teste falhar, isolar o culpado nesta abordagem torna-se altamente complexo devido ao emaranhado de interações simultâneas.


### 2.2 — Integração Incremental Top-Down (Descendente) com uso de Stubs

1. Diagrama de Classes UML

O diagrama exibe o teste focado na camada superior do sistema de transferência, onde as dependências inferiores de infraestrutura ou parceiros externos ainda não estão prontas e são substituídas por dublês de teste passivos (Stubs).

    Visualização Mermaid

    ```mermaid
    classDiagram
        class TransferenciaPixService {
            -gatewayBacen: IGatewayBacen
            +enviarOrdem(transacao: Transacao) Boolean
        }
        <<interface>> IGatewayBacen
        class IGatewayBacen {
            +liquidar(t: Transacao) Boolean
        }
        class GatewayBacenStub {
            -simularFalha: Boolean
            +setSimularFalha(b: Boolean) void
            +liquidar(t: Transacao) Boolean
        }
        class TesteTopDownService {
            +testEnviarOrdem_ComSucessoBacen() void
            +testEnviarOrdem_ComErroBacen() void
        }
        TransferenciaPixService --> IGatewayBacen : <<uses>>
        GatewayBacenStub ..|> IGatewayBacen : <<implements>>
        TesteTopDownService ..> TransferenciaPixService : <<instantiates and tests>>
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    classDiagram
        class TransferenciaPixService {
            -gatewayBacen: IGatewayBacen
            +enviarOrdem(transacao: Transacao) Boolean
        }
        <<interface>> IGatewayBacen
        class IGatewayBacen {
            +liquidar(t: Transacao) Boolean
        }
        class GatewayBacenStub {
            -simularFalha: Boolean
            +setSimularFalha(b: Boolean) void
            +liquidar(t: Transacao) Boolean
        }
        class TesteTopDownService {
            +testEnviarOrdem_ComSucessoBacen() void
            +testEnviarOrdem_ComErroBacen() void
        }
        TransferenciaPixService --> IGatewayBacen : <<uses>>
        GatewayBacenStub ..|> IGatewayBacen : <<implements>>
        TesteTopDownService ..> TransferenciaPixService : <<instantiates and tests>>
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    skinparam classAttributeIconSize 0

    interface IGatewayBacen {
        +liquidar(t: Transacao): Boolean
    }

    class TransferenciaPixService {
        -gatewayBacen: IGatewayBacen
        +enviarOrdem(transacao: Transacao): Boolean
    }

    class GatewayBacenStub {
        -simularFalha: Boolean
        +setSimularFalha(b: Boolean): void
        +liquidar(t: Transacao): Boolean
    }

    class TesteTopDownService {
        +testEnviarOrdem_ComSucessoBacen(): void
        +testEnviarOrdem_ComErroBacen(): void
    }

    TransferenciaPixService --> IGatewayBacen
    GatewayBacenStub ..|> IGatewayBacen
    TesteTopDownService ..> TransferenciaPixService
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: O time de negócios do BB implementou a lógica central de orquestração financeira na classe TransferenciaPixService (Alto Nível). No entanto, o canal de comunicação criptografado e seguro com o Banco Central (IGatewayBacen) está sendo construído por outra equipe e não está operacional.
    Como a abordagem Top-Down com Stubs é aplicada:

    * Classe Real de Alto Nível sob Teste: A classe TransferenciaPixService é validada primeiro de forma descendente.
    * Uso de Stub: Cria-se a classe GatewayBacenStub implementando a interface contratual. Ela não envia dados para a rede real; simplesmente possui uma lógica estática programada em memória para retornar true imediatamente ou false se setSimularFalha(true) for acionado pela classe de teste.
    * Tipo de Defeito que Visa Revelar: Falhas de fluxo de controle na classe de alto nível (ex.: o TransferenciaPixService não capturar ou tratar incorretamente o retorno negativo do stub de liquidação, gerando um crash interno em vez de notificar o usuário).


### 2.3 — Integração Incremental Bottom-Up (Ascendente) com uso de Drivers

1. Diagrama de Classes UML

O diagrama exibe o teste focado na base da pirâmide (camadas de infraestrutura ou serviços de baixo nível), utilizando um executor de testes ativo (Driver) para simular as camadas de negócio superiores que ainda não existem.

Visualização Mermaid

    ```mermaid
    classDiagram
        class RepositorioLedgerPix {
            +gravarLancamentoLog(id: String, v: double) void
        }
        class DriverTesteLedger {
            -repositorio: RepositorioLedgerPix
            +executarSimulacaoCargaGravacao() void
        }
        DriverTesteLedger ..> RepositorioLedgerPix : <<drives and tests>>
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    classDiagram
        class RepositorioLedgerPix {
            +gravarLancamentoLog(id: String, v: double) void
        }
        class DriverTesteLedger {
            -repositorio: RepositorioLedgerPix
            +executarSimulacaoCargaGravacao() void
        }
        DriverTesteLedger ..> RepositorioLedgerPix : <<drives and tests>>
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    skinparam classAttributeIconSize 0

    class RepositorioLedgerPix {
        +gravarLancamentoLog(id: String, v: double): void
    }

    class DriverTesteLedger {
        -repositorio: RepositorioLedgerPix
        +executarSimulacaoCargaGravacao(): void
    }

    DriverTesteLedger ..> RepositorioLedgerPix
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: A camada de persistência de dados de altíssima performance, responsável por gravar o histórico imutável das transações Pix (RepositorioLedgerPix), foi concluída. Como ela fica na base do software (baixo nível) e as telas do aplicativo ou APIs do BB que chamam essa gravação ainda não foram desenvolvidas, a integração precisa ocorrer de baixo para cima.

    Como a abordagem Bottom-Up com Drivers é aplicada:

    * Classe Real de Baixo Nível sob Teste: O alvo do teste é o RepositorioLedgerPix.
    * Uso de Driver: Desenvolve-se um programa de teste ativo chamado DriverTesteLedger. Esse Driver atua simulando o comportamento que as APIs superiores teriam, bombardeando o método gravarLancamentoLog com dados, garantindo que o banco de dados aguente a escrita imediata.
    * Tipo de Defeito que Visa Revelar: Erros de concorrência na escrita em banco de dados, falhas de mapeamento objeto-relacional, estouro de conexões do pool de dados da base técnica e vazamento de memória sob volume constante de inserções.


### 2.4 — Teste de Fumaça (Smoke Testing)

1. Diagrama de Classes UML

O diagrama ilustra uma suíte ágil que faz chamadas rápidas de ponta a ponta nas principais artérias do ecossistema do Gateway Pix para avaliar a estabilidade básica da build (versão gerada).

1. Visualização Mermaid

    ```mermaid
    classDiagram
        class MonitorSaudePix {
            +verificarStatusProvedores() String
        }
        class ConectorSPI {
            +checarConexaoBacen() Boolean
        }
        class ValidadorDeSaldo {
            +checarBancoDisponivel() Boolean
        }
        class SuiteSmokeTest {
            +executarVerificacaoRapidaBuild() void
        }
        SuiteSmokeTest ..> MonitorSaudePix : <<triggers healthcheck>>
        MonitorSaudePix --> ConectorSPI : <<pings>>
        MonitorSaudePix --> ValidadorDeSaldo : <<pings>>
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    classDiagram
        class MonitorSaudePix {
            +verificarStatusProvedores() String
        }
        class ConectorSPI {
            +checarConexaoBacen() Boolean
        }
        class ValidadorDeSaldo {
            +checarBancoDisponivel() Boolean
        }
        class SuiteSmokeTest {
            +executarVerificacaoRapidaBuild() void
        }
        SuiteSmokeTest ..> MonitorSaudePix : <<triggers healthcheck>>
        MonitorSaudePix --> ConectorSPI : <<pings>>
        MonitorSaudePix --> ValidadorDeSaldo : <<pings>>
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    skinparam classAttributeIconSize 0

    class MonitorSaudePix {
        +verificarStatusProvedores(): String
    }
    class ConectorSPI {
        +checarConexaoBacen(): Boolean
    }
    class ValidadorDeSaldo {
        +checarBancoDisponivel(): Boolean
    }
    class SuiteSmokeTest {
        +executarVerificacaoRapidaBuild(): void
    }

    SuiteSmokeTest ..> MonitorSaudePix
    MonitorSaudePix --> ConectorSPI
    MonitorSaudePix --> ValidadorDeSaldo
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: No fluxo de integração contínua (CI/CD) do Banco do Brasil, sempre que um desenvolvedor faz uma alteração no código do Gateway Pix, uma nova build é gerada. Antes de enviar essa versão para os analistas de teste ou servidores de validação complexa, um script rápido precisa rodar para verificar se a build não está "pegando fogo" (inoperante).

    Como a abordagem de Teste de Fumaça é aplicada:

    * Componentes Envolvidos: A suite de testes invoca o método principal de monitoramento (MonitorSaudePix.verificarStatusProvedores()).
    * Operação: O teste faz chamadas rápidas não destrutivas (ex.: pings de conectividade com as pontas do Bacen via ConectorSPI.checarConexaoBacen() e checagem de conexão do banco de dados via ValidadorDeSaldo.checarBancoDisponivel()).
    * Tipo de Defeito que Visa Revelar: Erros graves que inviabilizam qualquer teste posterior, como falhas catastróficas de inicialização do servidor, arquivos de propriedades/credenciais de banco ausentes na compilação ou portas de rede trancadas por regras de firewall locais.

### 2.5 — Teste de Regressão

1. Diagrama de Classes UML

O diagrama demonstra como um conjunto preexistente de testes é rodado novamente após uma modificação ou correção em uma classe específica (GerenciadorDeChaves) para assegurar que partes antigas e consolidadas do sistema não foram danificadas.

Visualização Mermaid

    ```mermaid
    classDiagram
        class GerenciadorDeChaves {
            +buscarChave(chave: String) String
            +removerChave(chave: String) Boolean
        }
        class SuiteTestesRegressaoChaves {
            -componente: GerenciadorDeChaves
            +testRegressao_BuscarChaveExistente() void
            +testRegressao_ExclusaoChaveLogica() void
        }
        SuiteTestesRegressaoChaves ..> GerenciadorDeChaves : <<re-runs tests against modified component>>
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    classDiagram
        class GerenciadorDeChaves {
            +buscarChave(chave: String) String
            +removerChave(chave: String) Boolean
        }
        class SuiteTestesRegressaoChaves {
            -componente: GerenciadorDeChaves
            +testRegressao_BuscarChaveExistente() void
            +testRegressao_ExclusaoChaveLogica() void
        }
        SuiteTestesRegressaoChaves ..> GerenciadorDeChaves : <<re-runs tests against modified component>>
    ```

    Código-fonte PlantUML

    ```mermaid
        @startuml
        skinparam classAttributeIconSize 0

        class GerenciadorDeChaves {
            +buscarChave(chave: String): String
            +removerChave(chave: String): Boolean
        }

        class SuiteTestesRegressaoChaves {
            -componente: GerenciadorDeChaves
            +testRegressao_BuscarChaveExistente(): void
            +testRegressao_ExclusaoChaveLogica(): void
        }

        SuiteTestesRegressaoChaves ..> GerenciadorDeChaves
        @enduml
    ```
    
3. Explicação Textual do Cenário:
    
    **Contexto:** O componente GerenciadorDeChaves passou por uma refatoração de código para otimizar o tempo de resposta em consultas a chaves do tipo chave aleatória (EVP). Embora a alteração tenha sido pontual, o medo da equipe é que essa alteração tenha quebrado acidentalmente o comportamento antigo e estável de busca de chaves do tipo e-mail ou CPF, ou o mecanismo de exclusão.

    Como a abordagem de teste de regressão é aplicada:

     * Fluxo de Execução: Logo após a alteração no código do método buscarChave(), a suite de automação dispara a execução completa do bloco SuiteTestesRegressaoChaves.

     * Verificação: O teste executa novamente cenários que já funcionavam antes da alteração (como testRegressao_ExclusaoChaveLogica()), avaliando se o comportamento esperado permanece idêntico.

     * Tipo de Defeito que Visa Revelar: Efeitos colaterais indesejados introduzidos por manutenções ou correções de bugs (ex.: a otimização alterou a forma como as strings limpam espaços em branco, quebrando acidentalmente as consultas de chaves Pix baseadas em e-mails que possuem caracteres especiais).



## 3. Teste de Validação (Validation Testing)

### 3.1 — Critérios de Aceitação (User Acceptance Testing - UAT)

1. Diagrama de Componentes UML

    Os testes de aceitação validam se o sistema entrega o valor de negócio esperado sob a ótica dos critérios definidos pelo Product Owner (PO) e analistas de conformidade do Banco Central.

    Seguem exemplos de diagramas que ilustram a aplicação deste conceito no cenário proposto.

    Visualização Mermaid

    ```mermaid
    componentDiagram
        component [App BB (Canal do Cliente)] as App
        component [Motor Pix (Validador de Regras)] as Motor
        component [Sistema de Notificações (Push/SMS)] as Notificacao
        
        App --> Motor : 1. Solicita transferência com Chave Inválida
        Motor --> App : 2. Retorna Código de Erro "CHAVE_NAO_ENCONTRADA"
        Motor --> Notificacao : 3. Registra Log de Tentativa Inválida
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    graph TD
        App[App BB Canal do Cliente] -->|1. Solicita transferência com Chave Inválida| Motor[Motor Pix Validador de Regras]
        Motor -->|2. Retorna Erro CHAVE_NAO_ENCONTRADA| App
        Motor -->|3. Registra Log de Tentativa| Notificacao[Sistema de Notificações]
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    [App BB (Canal do Cliente)] as App
    [Motor Pix (Validador de Regras)] as Motor
    [Sistema de Notificações (Push/SMS)] as Notificacao

    App -> Motor : 1. Solicita transferência com Chave Inválida
    Motor -> App : 2. Retorna Código de Erro "CHAVE_NAO_ENCONTRADA"
    Motor -> Notificacao : 3. Registra Log de Tentativa Inválida
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: O Product Owner do Banco do Brasil estabeleceu um Critério de Aceitação mandatório (baseado nas circulares do Bacen): "Se um cliente tentar iniciar um Pix para uma chave inexistente, o sistema deve recusar a operação imediatamente na tela, exibindo uma mensagem clara para evitar fraudes ou transferências erradas, sem permitir o avanço para a digitação da senha."

    Como a abordagem de Critérios de Aceitação (UAT) é aplicada:

    * Componentes Envolvidos: A interface do App BB aciona o componente central Motor Pix.
    * Operação: O analista de UAT (ou um script BDD automatizado) força o cenário de negócio enviando uma requisição com uma chave sabidamente falsa. O teste valida se o comportamento fim-a-fim atende à regra escrita na especificação, verificando se o Motor Pix gerou o código de erro exato (CHAVE_NAO_ENCONTRADA) e bloqueou o avanço do fluxo.
    * Tipo de Defeito que Visa Revelar: Divergências entre o software construído e a regra de negócio desejada (ex.: o programador permitiu o avanço para a tela de senha mesmo com a chave inválida, ou exibiu uma mensagem genérica de erro de sistema "Internal Error 500" em vez da mensagem amigável de chave inexistente).



### 3.2 — Teste Alfa (Alpha Testing)

1. Diagrama de Arquitetura/Componentes UML

    O teste Alfa é realizado internamente pela própria equipe de tecnologia e funcionários selecionados do Banco do Brasil, utilizando um ambiente controlado que simula o ecossistema de produção.

    Visualização Mermaid

    ```mermaid
    graph LR
        subgraph Lab_Interno_BB [Ambiente Controlado Interno - Lab BB]
            Funcionario[Funcionário do BB / Tester Interno] -->|Usa App Interno| GatewayAlfa[Gateway Pix - Build Alfa]
            GatewayAlfa -->|Consulta Massa de Dados Fictícia| BancoFalso[(Banco de Dados de Homologação)]
        end
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    graph LR
        subgraph Lab_Interno_BB [Ambiente Controlado Interno - Lab BB]
            Funcionario[Funcionário do BB / Tester Interno] -->|Usa App Interno| GatewayAlfa[Gateway Pix - Build Alfa]
            GatewayAlfa -->|Consulta Massa de Dados Fictícia| BancoFalso[(Banco de Dados de Homologação)]
        end
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    skinparam packageStyle rectangle

    rectangle "Ambiente Controlado Interno - Lab BB" {
        [Funcionário do BB / Tester] as Funcionario
        [Gateway Pix (Build Alfa)] as GatewayAlfa
        database "Banco de Dados de Homologação" as BancoFalso
        
        Funcionario -> GatewayAlfa : Usa App Interno (Dispositivo do Lab)
        GatewayAlfa -> BancoFalso : Consulta Massa de Dados Fictícia
    }
    @enduml
    ```


3. Explicação Textual do Cenário

    Contexto: O novo módulo de agendamento de Pix recorrente do Banco do Brasil está pronto para validação. Antes de expor o sistema a clientes reais na loja de aplicativos, o BB libera uma versão especial em um laboratório interno para que os próprios engenheiros e funcionários da instituição usem o serviço em cenários do dia a dia.

    Como a abordagem de Teste Alfa é aplicada:

    * Execução: O grupo interno de funcionários utiliza smartphones de teste fornecidos pelo laboratório do BB, conectados à rede privada da instituição (Intranet), transacionando contas correntes simuladas com saldos fictícios.
    * Objetivo: Identificar bugs evidentes de usabilidade, travamentos de tela ou inconsistências no fluxo que passaram pelos testes automatizados anteriores, sob uma perspectiva humana de uso do produto, porém sem risco operacional.
    * Tipo de Defeito que Visa Revelar: Falhas de fluxo de navegação, travamentos da interface gráfica (UI) ao alternar telas rapidamente, problemas na câmera do celular ao tentar ler o QR Code estático do Lab, ou quebras de validação de campo que tornam o uso confuso ou impossível.


### 3.3 — Teste Beta (Beta Testing)

1. Diagrama de Arquitetura/Componentes UML

    O teste Beta abre o sistema para um grupo selecionado de clientes reais do banco fora do ambiente controlado do BB, operando diretamente na infraestrutura de produção com dinheiro real, mas de forma limitada.

    Visualização Mermaid

    ```mermaid
    graph LR
        subgraph Infraestrutura_Real [Ambiente de Produção do Banco do Brasil]
            ClienteBeta[Cliente Real do BB Grupo Piloto] -->|Acessa Funcionalidade Oculta| GatewayBeta[Gateway Pix - Feature Flag Ativa]
            GatewayBeta -->|Liquida com Dinheiro de Verdade| SPIReal((Sistema do Banco Central - SPI Real))
        end
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    graph LR
        subgraph Infraestrutura_Real [Ambiente de Produção do Banco do Brasil]
            ClienteBeta[Cliente Real do BB Grupo Piloto] -->|Acessa Funcionalidade Oculta| GatewayBeta[Gateway Pix - Feature Flag Ativa]
            GatewayBeta -->|Liquida com Dinheiro de Verdade| SPIReal((Sistema do Banco Central - SPI Real))
        end
    ```

    Visualização PlantUML

    ```mermaid
    @startuml
    skinparam packageStyle rectangle

    rectangle "Ambiente de Produção do Banco do Brasil" {
        [Cliente Real (Grupo Piloto)] as ClienteBeta
        [Gateway Pix (Feature Flag Ativa)] as GatewayBeta
        cloud "Banco Central (SPI Real)" as SPIReal
        
        ClienteBeta -> GatewayBeta : Acessa Funcionalidade Oculta
        GatewayBeta -> SPIReal : Liquida com Dinheiro de Verdade
    }
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: O Banco do Brasil quer lançar uma nova modalidade de Pix parcelado no app. Após passar com sucesso pelo Teste Alfa interno, a funcionalidade é implantada em produção, mas escondida por uma chave de ativação (Feature Flag). O banco seleciona 1% da sua base de correntistas reais (Grupo Piloto/Beta Testers) para usar a novidade em suas rotinas reais de pagamento.

    Como a abordagem de Teste Beta é aplicada:

    * Execução: O sistema monitora o comportamento desses usuários em produção. Os clientes realizam pagamentos reais em maquininhas de cartão ou sites de e-commerce na rua, operando com seus próprios saldos bancários.
    * Coleta de Feedback: O banco disponibiliza um canal direto de suporte e telemetria automatizada no app para receber relatórios de falhas de hardware e feedbacks de usabilidade coletados de surpresa no "mundo real".
    * Tipo de Defeito que Visa Revelar: Falhas de compatibilidade que só ocorrem na imensa variedade de aparelhos do mercado (ex.: a câmera de um modelo específico de smartphone chinês de um cliente não consegue focar o QR Code sob luz solar), instabilidades causadas por oscilações nas redes de operadoras de telefonia móvel (3G/4G/5G), ou comportamentos inesperados do usuário que a equipe de engenharia não conseguiu prever no laboratório.



## 4. Teste de Sistema (System Testing)

### 4.1 — Teste de Recuperação (Recovery Testing)

1. Diagrama de Sequência UML

    O diagrama ilustra o comportamento do ecossistema quando o banco de dados principal de transações sofre uma queda abrupta de energia ou hardware, avaliando a capacidade de reconexão e a ativação automática da réplica (Failover).

    Visualização Mermaid

    ```mermaid
    sequenceDiagram
        autonumber
        participant App as Aplicativo BB
        participant Gateway as Gateway Pix API
        participant DB_Princ as Banco de Dados (Principal)
        participant DB_Repl as Banco de Dados (Réplica Failover)
        
        App->>Gateway: efetuarPagamento(dados)
        Note over Gateway,DB_Princ: [PONTO DE INJEÇÃO DE FALHA: Queda do BD]
        Gateway-xDB_Princ: gravarTransacao(t) (FALHA / TIMEOUT)
        Gateway->>Gateway: dispararMecanismoFailover()
        Gateway->>DB_Repl: conectarReplicasAlternativas()
        DB_Repl-->>Gateway: Conexão Estabelecida (Sucesso)
        Gateway->>DB_Repl: gravarTransacao(t)
        DB_Repl-->>Gateway: Transação Gravada com Sucesso
        Gateway-->>App: Resposta 200 OK (Pagamento Efetuado)
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)## Código-fonte Mermaid

    ```mermaid
    sequenceDiagram
        autonumber
        participant App as Aplicativo BB
        participant Gateway as Gateway Pix API
        participant DB_Princ as Banco de Dados (Principal)
        participant DB_Repl as Banco de Dados (Réplica Failover)
        
        App->>Gateway: efetuarPagamento(dados)
        Note over Gateway,DB_Princ: [PONTO DE INJEÇÃO DE FALHA: Queda do BD]
        Gateway-xDB_Princ: gravarTransacao(t) (FALHA / TIMEOUT)
        Gateway->>Gateway: dispararMecanismoFailover()
        Gateway->>DB_Repl: conectarReplicasAlternativas()
        DB_Repl-->>Gateway: Conexão Estabelecida (Sucesso)
        Gateway->>DB_Repl: gravarTransacao(t)
        DB_Repl-->>Gateway: Transação Gravada com Sucesso
        Gateway-->>App: Resposta 200 OK (Pagamento Efetuado)
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    autonumber

    actor "Aplicativo BB" as App
    participant "Gateway Pix API" as Gateway
    database "Banco de Dados (Principal)" as DB_Princ
    database "Banco de Dados (Réplica Failover)" as DB_Repl

    App -> Gateway : efetuarPagamento(dados)
    note over Gateway, DB_Princ : [PONTO DE INJEÇÃO DE FALHA: Queda do BD]
    Gateway -x DB_Princ : gravarTransacao(t) (FALHA / TIMEOUT)

    Gateway -> Gateway : dispararMecanismoFailover()
    Gateway -> DB_Repl : conectarReplicasAlternativas()
    DB_Repl --> Gateway : Conexão Estabelecida (Sucesso)

    Gateway -> DB_Repl : gravarTransacao(t)
    DB_Repl --> Gateway : Transação Gravada com Sucesso
    Gateway --> App : Resposta 200 OK (Pagamento Efetuado)
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: O Banco Central do Brasil exige alta disponibilidade em transações instantâneas. O sistema do BB precisa ser resiliente e capaz de se recuperar automaticamente de falhas de hardware ou indisponibilidade de infraestrutura sem perder transações financeiras no meio do caminho.

    Como a abordagem de Teste de Recuperação é aplicada:

    * Injeção de Falha: Durante a execução de um lote de transações simuladas, o engenheiro de testes ou uma ferramenta de engenharia do caos (como o Chaos Mesh) força a queda do nó de base de dados principal (Banco de Dados (Principal)), desconectando os cabos de rede virtuais ou desligando o servidor.
    * Ação do Sistema: O Gateway Pix API detecta a perda de conectividade e aciona o método dispararMecanismoFailover(). O sistema deve restabelecer conexões automaticamente direcionando as novas escritas para o Banco de Dados (Réplica Failover).
    * Tipo de Defeito que Visa Revelar: Defeitos no gerenciamento do pool de conexões (ex.: o sistema trava tentando se conectar infinitamente ao banco morto em vez de desistir e chavear para a réplica), falhas de sincronismo de transações não salvas que geram corrupção ou duplicação de saldo na virada dos servidores, ou lentidão excessiva no processo de chaveamento automático excedendo os tempos de limite aceitáveis.

### 4.2 — Teste de Segurança (Security Testing)

    1. Diagrama de Sequência UML

    O diagrama simula uma tentativa maliciosa de ataque de injeção de parâmetros modificados para desviar dinheiro de outra conta, avaliando o comportamento das defesas de criptografia e barramento do gateway.

    Visualização Mermaid

    ```mermaid
    sequenceDiagram
        autonumber
        actor Hacker as Usuário Malicioso (Hacker)
        participant WAF as Firewall de Aplicação (WAF / API Gateway)
        participant Auth as Validador OAuth2 / Assinatura
        participant Core as Core Pix Backend
        
        Hacker->>WAF: Envia requisição Pix alterando ContaOrigem do payload (Manipulação de Parâmetros)
        WAF->>WAF: Analisa payload contra assinaturas de injeção (XSS/SQLi)
        WAF->>Auth: Encaminha para checar assinatura digital do payload
        Auth->>Auth: Validar assunatura com Token mTLS do usuário
        Note over Auth: [Falha: Token de acesso não bate com a chave privada de origem]
        Auth-->>WAF: Retorna Erro 401 (Acesso não Autorizado / Assinatura Inválida)
        WAF-->>Hacker: Retorna HTTP Status 403 Forbidden (Transação Rejeitada)
        WAF->>WAF: Dispara Alerta no SIEM (Segurança Operacional)
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

    2. Código-fonte do Diagrama (Mermaid e PlantUML)

    Código-fonte Mermaid

    ```mermaid
    sequenceDiagram
        autonumber
        actor Hacker as Usuário Malicioso (Hacker)
        participant WAF as Firewall de Aplicação (WAF / API Gateway)
        participant Auth as Validador OAuth2 / Assinatura
        participant Core as Core Pix Backend
        
        Hacker->>WAF: Envia requisição Pix alterando ContaOrigem do payload (Manipulação de Parâmetros)
        WAF->>WAF: Analisa payload contra assinaturas de injeção (XSS/SQLi)
        WAF->>Auth: Encaminha para checar assinatura digital do payload
        Auth->>Auth: Validar assunatura com Token mTLS do usuário
        Note over Auth: [Falha: Token de acesso não bate com a chave privada de origem]
        Auth-->>WAF: Retorna Erro 401 (Acesso não Autorizado / Assinatura Inválida)
        WAF-->>Hacker: Retorna HTTP Status 403 Forbidden (Transação Rejeitada)
        WAF->>WAF: Dispara Alerta no SIEM (Segurança Operacional)
    ```

    Código-fonte PlantUML

    ```mermaid
    @startuml
    autonumber

    actor "Usuário Malicioso (Hacker)" as Hacker
    participant "Firewall de Aplicação (WAF)" as WAF
    participant "Validador OAuth2 / Assinatura" as Auth
    participant "Core Pix Backend" as Core

    Hacker -> WAF : Envia requisição alterando ContaOrigem no payload
    WAF -> WAF : Analisa payload contra assinaturas de injeção
    WAF -> Auth : Encaminha para checar assinatura digital
    Auth -> Auth : Validar assinatura com Token mTLS do usuário
    note over Auth : [Falha: Token não bate com a chave privada de origem]

    Auth --> WAF : Retorna Erro 401 (Assinatura Inválida)
    WAF --> Hacker : Retorna HTTP Status 403 Forbidden
    WAF -> WAF : Dispara Alerta no SIEM (Segurança)
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: O Gateway Pix trafega bilhões de reais diariamente e é alvo constante de cibercriminosos. Um dos ataques mais comuns é a adulteração de requisições de rede capturadas, na tentativa de alterar dados do payload (como a conta corrente debitada) antes que a transação chegue ao servidor central do Banco do Brasil.

    Como a abordagem de Teste de Segurança é aplicada:

    * Execução do Ataque Simulado (Pentest): A equipe de segurança ofensiva (Red Team) simula requisições forjadas diretamente nas rotas expostas da API. Eles interceptam a chamada de um aplicativo legítimo e modificam os parâmetros internos do JSON (ex.: trocam a conta que vai pagar pela conta de uma vítima), disparando o envio para o WAF.
    * Verificação de Defesa: O teste avalia se o barramento de segurança (Validador OAuth2 / Assinatura) barra a requisição de forma imediata porque a chave criptográfica mTLS ou os tokens de sessão (JWT) gerados no início não assinam digitalmente as alterações feitas no payload malicioso.
    * Tipo de Defeito que Visa Revelar: Falhas de Broken Object Level Authorization (BOLA), que permitem a um usuário manipular IDs de recursos de terceiros; ausência de validação de criptografia de ponta a ponta; falhas de vazamento de dados confidenciais em logs do sistema (Sensitive Data Exposure) ou portas com políticas frouxas de CORS e cabeçalhos HTTP inseguros.


### 4.3 — Teste de Estresse (Stress Testing)

1. Diagrama de Componentes UML

    O diagrama de componentes representa a infraestrutura sob um teste de bombardeio volumétrico massivo de dados (muito além da capacidade nominal projetada) para analisar como o sistema falha e se ele quebra graciosamente ou de forma catastrófica.

    Visualização Mermaid

    ```mermaid
    graph TD
        Injetor[Injetor de Carga - JMeter / Gatling] -->|Dispara 150.000 req/seg simulando picos extremos| API[Gateway Pix API Load Balancer]
        API -->|Estrangulamento de Recursos| Fila[Fila de Mensageria - Kafka / RabbitMQ]
        
        subgraph Servidores_BB [Cluster Elastic Kubernetes Service]
            Fila --> Pod1[Pod Operacional 1]
            Fila -.->|POD CAIU: Falha por falta de Memória OOM| Pod2[Pod Operacional 2]
        end
        
        API -.->|Circuito Aberto Circuit Breaker: Retorna Erro Amigável| Injetor
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)

    Código-fonte Mermaid

    ```mermaid
    graph TD
        Injetor[Injetor de Carga - JMeter / Gatling] -->|Dispara 150.000 req/seg simulando picos extremos| API[Gateway Pix API Load Balancer]
        API -->|Estrangulamento de Recursos| Fila[Fila de Mensageria - Kafka / RabbitMQ]
        
        subgraph Servidores_BB [Cluster Elastic Kubernetes Service]
            Fila --> Pod1[Pod Operacional 1]
            Fila -.->|POD CAIU: Falha por falta de Memória OOM| Pod2[Pod Operacional 2]
        end
        
        API -.->|Circuito Aberto Circuit Breaker: Retorna Erro Amigável| Injetor
    ```

    Visualização PlantUML

    ```mermaid
    @startuml
    skinparam packageStyle rectangle

    [Injetor de Carga (JMeter / Gatling)] as Injetor
    [Gateway Pix API (Load Balancer)] as API
    [Fila de Mensageria (Kafka)] as Fila

    rectangle "Cluster Kubernetes (Servidores BB)" {
        [Pod Operacional 1] as Pod1
        [Pod Operacional 2 (POD CAIU: Memória OOM)] as Pod2
    }

    Injetor -> API : Dispara 150.000 req/seg (Pico Extremo)
    API -> Fila : Estrangulamento de Recursos
    Fila --> Pod1
    Fila -.> Pod2

    API -.> Injetor : [Circuit Breaker Aberto: Erro Amigável 429]
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: O Banco do Brasil planeja a infraestrutura do Gateway Pix para aguentar picos normais de mercado. No entanto, no fechamento da Black Friday ou nos minutos finais do pagamento de lotes de restituição do Imposto de Renda, a carga de usuários simultâneos pode subir de forma exponencial. O teste de estresse força o sistema até o seu limite físico para entender quando ele para de funcionar.

    Como a abordagem de Teste de Estresse é aplicada:

    * Ação do Teste: Utilizando ferramentas como Apache JMeter ou Gatling (Injetor de Carga), a equipe dispara volumetrias massivas (ex.: 150.000 requisições por segundo), um número propositalmente 3 vezes maior do que a capacidade máxima planejada para o cluster de servidores do banco.
    * Comportamento Avaliado: O objetivo não é ver se o sistema responde rápido, mas sim avaliar como ele quebra. Espera-se que mecanismos como o Circuit Breaker (Disjuntor de Código) abram na Gateway Pix API, parando de sufocar os servidores internos e passando a responder os clientes com um erro amigável "Sistema sobrecarregado, tente novamente em instantes (HTTP 429)", protegendo a integridade dos dados na base.
    * Tipo de Defeito que Visa Revelar: Desmoronamento catastrófico do sistema (ex.: estouro generalizado de memória RAM nos servidores — Out Of Memory / OOM), travamento permanente de threads, indisponibilidade em cascata onde a queda de um microsserviço derruba todos os outros por falta de tratamento de lentidão, ou corrupção de dados por interrupção abrupta de conexões inacabadas.


### 4.4 — Teste de Desempenho (Performance Testing)

1. Diagrama de Sequência UML

    O diagrama mapeia as métricas de tempo de resposta (SLA) de cada componente envolvido em uma transação Pix bem-sucedida sob carga normal e controlada para identificar gargalos e latências.

    Visualização Mermaid

    ```mermaid
    sequenceDiagram
        autonumber
        participant App as App BB (Cliente)
        participant Gateway as Gateway Pix API
        participant AntiFraude as Motor AntiFraude
        participant Core as Core Bancário
        
        App->>Gateway: Envia Requisição Pix (0ms)
        activate Gateway
        Gateway->>AntiFraude: analisarRisco(transacao) (Latência Alvo: < 200ms)
        activate AntiFraude
        AntiFraude-->>Gateway: Risco Baixo / Aprovado (+180ms)
        deactivate AntiFraude
        
        Gateway->>Core: debitaEfetivaSaldo(valores) (Latência Alvo: < 500ms)
        activate Core
        Core-->>Gateway: Debitado com Sucesso (+420ms)
        deactivate Core
        
        Gateway-->>App: Transação Confirmada (Tempo Total: 600ms)
        deactivate Gateway
        Note over App,Gateway: SLA Aceitável Bacen: < 2000ms (2 segundos)
    ```

    Visualização PlantUML

    Para visualizar no PlantUML, copie a sintaxe textual fornecida na seção seguinte.

2. Código-fonte do Diagrama (Mermaid e PlantUML)

    Código-fonte Mermaid

    ```mermaid
    sequenceDiagram
        autonumber
        participant App as App BB (Cliente)
        participant Gateway as Gateway Pix API
        participant AntiFraude as Motor AntiFraude
        participant Core as Core Bancário
        
        App->>Gateway: Envia Requisição Pix (0ms)
        activate Gateway
        Gateway->>AntiFraude: analisarRisco(transacao) (Latência Alvo: < 200ms)
        activate AntiFraude
        AntiFraude-->>Gateway: Risco Baixo / Aprovado (+180ms)
        deactivate AntiFraude
        
        Gateway->>Core: debitaEfetivaSaldo(valores) (Latência Alvo: < 500ms)
        activate Core
        Core-->>Gateway: Debitado com Sucesso (+420ms)
        deactivate Core
        
        Gateway-->>App: Transação Confirmada (Tempo Total: 600ms)
        deactivate Gateway
        Note over App,Gateway: SLA Aceitável Bacen: < 2000ms (2 segundos)
    ```

    Visualização PlantUML

    ```mermaid
    @startuml
    autonumber

    participant "App BB (Cliente)" as App
    participant "Gateway Pix API" as Gateway
    participant "Motor AntiFraude" as AntiFraude
    participant "Core Bancário" as Core

    App -> Gateway : Envia Requisição Pix (0ms)
    activate Gateway

    Gateway -> AntiFraude : analisarRisco(transacao) (Alvo: < 200ms)
    activate AntiFraude
    AntiFraude --> Gateway : Risco Baixo / Aprovado (+180ms)
    deactivate AntiFraude

    Gateway -> Core : debitaEfetivaSaldo(valores) (Alvo: < 500ms)
    activate Core
    Core --> Gateway : Debitado com Sucesso (+420ms)
    deactivate Core

    Gateway --> App : Transação Confirmada (Tempo Total: 600ms)
    deactivate Gateway

    note over App, Gateway : SLA Aceitável Bacen: < 2000ms (2 segundos)
    @enduml
    ```

3. Explicação Textual do Cenário

    Contexto: O Banco Central estipula rígidas metas de tempo para a consolidação de transferências via Pix (idealmente processadas em menos de 2 segundos de ponta a ponta). O teste de desempenho serve para medir se o sistema opera eficientemente dentro desses parâmetros de tempo e consumo de recursos de hardware sob cargas de trabalho estáveis e previsíveis.

    Como a abordagem de Teste de Desempenho é aplicada:

    * Execução da Medição: Um script executa uma carga constante de transações equivalente ao fluxo médio real esperado para um dia comum no banco (ex.: 25.000 requisições simultâneas por minuto). Ferramentas de monitoramento (como o APM Dynatrace, Datadog ou Prometheus) colhem as métricas de tempo de resposta.
    * Mapeamento de Gargalos: O teste mede individualmente o tempo que o Gateway Pix API leva para orquestrar as frentes, a latência de análise do Motor AntiFraude (180ms) e o tempo de débito em conta no Core Bancário (420ms), consolidando um tempo total de processamento interno de 600ms (bem abaixo da exigência do regulador).
    * Tipo de Defeito que Visa Revelar: Identificação de gargalos na infraestrutura (ex.: consultas lentas a bancos de dados por falta de índices bem planejados), consumo exagerado de CPU ou vazamentos lentos de memória que degradam o desempenho ao longo das horas, má configuração de roteamento de rede que adiciona latência desnecessária, e trechos de código pouco otimizados (como loops redundantes).