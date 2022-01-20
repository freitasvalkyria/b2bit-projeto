# b2bit-projeto
API em que um usuário realiza um cadastro, publica Posts e ver as publicações de outros usuários.

## :hammer: Funcionalidades do projeto
- `Cadastro de usuário`: o usuário consegue efetuar <a href="http://127.0.0.1:8000/api-auth/user/registration/">cadastro no sistema</a> através da API.
- `Autenticação (Login)`: o usuário <a href="http://127.0.0.1:8000/">efetua autenticação</a> no sistema.
- `Faz uma publicação`:  o usuário <a href="http://127.0.0.1:8000/posts/">cria um post</a> (ele deve estar autenticado), a publicação permanece no sistema. Ele (usuário) consegue criar uma publicação, para que possa ser vista por outros usuários do sistema.
- `Feed geral`: no formato JSON, o feed apresenta os <a href="http://127.0.0.1:8000/posts/">últimos 10 posts</a>.
- `Feed personalizado`: o usuário possui feed com apenas as <a href="http://127.0.0.1:8000/api-auth/user/follow/">publicações de usuários selecionados</a>, para que ele possa ter mais controle do seu feed.

## :heavy_check_mark: Tecnologias utilizadas
- `Aplicação em formato REST`
- `Python 3`
- `Django REST Framework`

## :file_folder: Acesso ao projeto
Você pode <a href="https://github.com/freitasvalkyria/b2bit-projeto/tree/main/api">acessar o código fonte do projeto inicial</a>.
