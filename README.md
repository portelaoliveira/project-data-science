<!-- @import "tutorial/style.html" -->

# Ciência de Dados

### O que é?

- É você usar os dados/informações do negócio para extrair informações valiosas e ajudar na tomada de decisão.
- De forma simples e o que é usado em muitas empresas -> É você resolver um desafio da empresa/do negócio usando os dados disponíveis
- O certo seria: Ciência de Dados tá preocupado em resolver os desafios do negócio e saber o que fazer no futuro, fazer alguma previsão que vai ajudar a tomar o rumo da empresa e o Business Intelligence tá em descrever como as coisas funcionaram/funcionaram até aqui

### Diferença de Ciência de Dados e Machine Learning

- Machine Learning faz parte da Ciência de Dados, é um modelo disponível para ajudar a prever alguma coisa.

### Onde podemos aplicar Ciência de Dados

- Em qualquer empresa basicamente, afinal, todas as empresas tem dados disponíveis.
- Mas na prática, podemos aplicar em todo lugar porque o objetivo é resolver um desafio do negócio usando dados. Então em qualquer empresa que você consiga usar os dados disponíveis para resolver um desafio da empresa, você pode aplicar Ciência de Dados

### Como funciona um Projeto de Ciência de Dados na prática

São várias etapas importantes, de forma bem completa:

1. Entendimento do Desafio que você quer resolver
2. Entendimento da Empresa/Área
3. Extração/Obtenção de Dados
4. Ajustes de Dados (Limpeza de Dados)
5. Análise Exploratória
6. Modelagem + Algoritmos
7. Interpretação dos Resultados
8. Deploy/Produção

### Onde o Python entra no meio disso tudo?

O Python é a ferramenta que vai te permitir fazer isso tudo, desde o 3 até o 8

### Projetos de Ciência de Dados Completo

- [Recomendação -> Kaggle] (https://www.kaggle.com/)

# Projeto Airbnb Rio - Ferramenta de Previsão de Preço de Imóvel para pessoas comuns 

### Contexto

No Airbnb, qualquer pessoa que tenha um quarto ou um imóvel de qualquer tipo (apartamento, casa, chalé, pousada, etc.) pode ofertar o seu imóvel para ser alugado por diária. Você cria o seu perfil de host (pessoa que disponibiliza um imóvel para aluguel por diária) e cria o anúncio do seu imóvel.

Nesse anúncio, o host deve descrever as características do imóvel da forma mais completa possível, de forma a ajudar os locadores/viajantes a escolherem o melhor imóvel para eles (e de forma a tornar o seu anúncio mais atrativo)

Existem dezenas de personalizações possíveis no seu anúncio, desde quantidade mínima de diária, preço, quantidade de quartos, até regras de cancelamento, taxa extra para hóspedes extras, exigência de verificação de identidade do locador, etc.

### Nosso objetivo

Construir um modelo de previsão de preço que permita uma pessoa comum que possui um imóvel possa saber quanto deve cobrar pela diária do seu imóvel. Ou ainda, para o locador comum, dado o imóvel que ele está buscando, ajudar a saber se aquele imóvel está com preço atrativo (abaixo da média para imóveis com as mesmas características) ou não.

### O que temos disponível, inspirações e créditos

As bases de dados foram retiradas do site kaggle: https://www.kaggle.com/allanbruno/airbnb-rio-de-janeiro

Caso queira uma outra solução, podemos olhar como referência a solução do usuário Allan Bruno do kaggle no Notebook: https://www.kaggle.com/allanbruno/helping-regular-people-price-listings-on-airbnb

Você vai perceber semelhanças entre a solução que vamos desenvolver aqui e a dele, mas também algumas diferenças significativas no processo de construção do projeto.

- As bases de dados são os preços dos imóveis obtidos e suas respectivas características em cada mês.
- Os preços são dados em reais (R$)
- Temos bases de abril de 2018 a maio de 2020, com exceção de junho de 2018 que não possui base de dados

### Expectativas Iniciais

- Acredito que a sazonalidade pode ser um fator importante, visto que meses como dezembro costumam ser bem caros no RJ
- A localização do imóvel deve fazer muita diferença no preço, já que no Rio de Janeiro a localização pode mudar completamente as características do lugar (segurança, beleza natural, pontos turísticos)
- Adicionais/Comodidades podem ter um impacto significativo, visto que temos muitos prédios e casas antigos no Rio de Janeiro

Vamos descobrir o quanto esses fatores impactam e se temos outros fatores não tão intuitivos que são extremamente importantes.

<!--

![](./tutorial/img/tela_principal.png)

<p class="legend"> Figura 1: Tela principal. </p> -->
