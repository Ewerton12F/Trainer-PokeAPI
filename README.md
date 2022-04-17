# Trainer-PokeAPI 

Esse é um projeto construído com Django Rest Framework para a implementação de uma Restful API seguindo o contrato fornecido em [Trainers API](https://app.swaggerhub.com/apis/fernando.celmer/trainers-api/1.0.0). No projeto também é feito o consumo da API externa [PokéAPI](https://pokeapi.co/).
 
## 🧑‍🏫 Como usar:

Faça [download](https://github.com/Ewerton12F/Trainer-PokeAPI/archive/refs/heads/master.zip) ou clone com o comando:

```sh
$ git clone git@github.com:Ewerton12F/Trainer-PokeAPI.git
```

Acesse o diretório do projeto baixado:
```sh
$ cd Trainer-PokeAPI
```

Crie um ambiente virtual e o ative:
```sh
$ virtualenv venv
$ source venv/bin/activate
```

Instale as dependências necessárias:
```sh
$ pip install -r requirements.txt
```

Faça as migrações:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Execute o servidor:
```sh
$ python manage.py runserver
```

Acesse:
```sh
http://127.0.0.1:8000/trainer/
```


## 🛣️ Roadmap
✅ Ver exemplos de códigos e tutoriais de Django

✅ Entender a documentação [Trainers API](https://app.swaggerhub.com/apis/fernando.celmer/trainers-api/1.0.0).

✅ Entender como funciona as requisições para a API [PokéAPI](https://pokeapi.co/).

✅ Divididir o back-end em 3 camadas

1️⃣ API routes - [urls.py](https://github.com/Ewerton12F/Trainer-PokeAPI/blob/master/api/urls.py)

- Camada responsável pela definição dos endpoints da API e tratamento das requisições e respostas da aplicação.

2️⃣ Services - [views.py](https://github.com/Ewerton12F/Trainer-PokeAPI/blob/master/api/views.py)

- Camada responsável pelas regras de negócios e por fazer a integração entre a camada de dados e a camada de API/Rotas.

3️⃣ Models - [models.py](https://github.com/Ewerton12F/Trainer-PokeAPI/blob/master/api/models.py)

- Camada responsável pela modelagem e acesso aos dados da aplicação.

🚧 Integrar a PokeAPI para salvar os dados da requisição no banco de dados.

🚧 Autenticação com JWT

🚧 Testes com pytest

🚧 Deploy no Heroku

## 🚧 Detalhes:

### Python
1 - A linguagem que eu tenho maior domínio;

2 - Concisa;

3 - Legível.

### Django Rest Framework
1 - Diversas ferramentas incorporadas que facilitam o desenvolvimento

2 - Com poucas linhas de código já é possível ter diversas funcionalidades

### .gitignore
Arquivo .gitignore criado a partir do gitignore.io

### [MIT License](https://choosealicense.com/licenses/mit/)
"A short and simple permissive license with conditions only requiring preservation
of copyright and license notices. Licensed works, modifications, and larger works
may be distributed under different terms and without source code."

---

# Avaliação:
• Boas práticas no tratamento das requisições

• Organização do projeto

• Separação de responsabilidades das lógicas de negócio e apresentação

## Ponto extras
• Implementar o contrato da API fornecido em OpenAPI 3.0

• Implementar autenticação com JWT

• Se possível colocar projeto disponível em um link público para visualização e teste.

• A escolha de tecnologia fica a critério do avaliado, mas uma explicação do motivo da escolha é sempre bem vinda.

• Um resumo de como foi feito o desenvolvimento, bem como um plano para as implementações que gostaria de ter feito.

• Entregue o que você conseguir fazer.