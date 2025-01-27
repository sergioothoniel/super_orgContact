## Google People API Integration

### Descrição do Projeto

Este projeto é um aplicativo web desenvolvido com Vue.js no frontend e Flask no backend. Ele permite que os usuários façam login com sua conta Google, conectem-se à Google People API e visualizem as conexões (contatos) associadas à sua conta.

### Funcionalidades Principais

- Login com conta Google utilizando o protocolo OAuth2.
- Geração e utilização de tokens de acesso para interagir com a Google People API.
- Exibição de conexões em uma tabela, agrupando informações por domínio de e-mail.

### Instruções para execução local

#### Backend

- Criar um projeto no Google Cloud para acessar o `People API`
- Criar `IDs do cliente OAuth 2.0`, inserindo a URI de redirecionamento `http://localhost:5173/contactslist`
- Faça o download do arquivo JSON do cliente OAuth para a pasta `backend` com o nome `credentiasl.json`
- Crie um ambiente virtual com `python -m venv venv`
- Acesso o ambiente virtual com `source venv/Scripts/activate` (ou `source venv/bin/activate`)
- Instale as dependências com `pip install -r requirements.txt`
- Execute o servidor com `python app.p`

#### Frontend

- Instale as dependências da pasta `app` com `npm i`
- Execute o comando `npm run dev` para rodar loacalmente na porta 5173
- Acesse o app pelo seu navegador
