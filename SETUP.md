# Configuração do Ambiente de Desenvolvimento

Este guia descreve como configurar o ambiente de desenvolvimento para o projeto IA do Empreendedor.

## Pré-requisitos

- Python 3.10 ou superior
- pip (gerenciador de pacotes Python)
- MongoDB (localmente ou via Docker)
- Redis (localmente ou via Docker)

## Instalação no macOS/Linux

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/ai-for-entrepreneurs.git
   cd ai-for-entrepreneurs
   ```

2. Execute o script de setup:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

3. Ative o ambiente virtual:
   ```bash
   source venv/bin/activate
   ```

4. Configure o arquivo `.env` com suas variáveis de ambiente (o script cria automaticamente um arquivo a partir do exemplo).

5. Inicie o aplicativo:
   ```bash
   streamlit run app.py
   ```

## Instalação no Windows

1. Clone o repositório:
   ```cmd
   git clone https://github.com/seu-usuario/ai-for-entrepreneurs.git
   cd ai-for-entrepreneurs
   ```

2. Execute o script de setup:
   ```cmd
   setup.bat
   ```

3. Ative o ambiente virtual:
   ```cmd
   venv\Scripts\activate
   ```

4. Configure o arquivo `.env` com suas variáveis de ambiente (o script cria automaticamente um arquivo a partir do exemplo).

5. Inicie o aplicativo:
   ```cmd
   streamlit run app.py
   ```

## Configuração Manual (Alternativa)

Se preferir configurar manualmente, siga estes passos:

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   ```

2. Ative o ambiente virtual:
   - macOS/Linux: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Instale dados NLTK:
   ```bash
   python -m nltk.downloader punkt stopwords wordnet
   ```

5. Crie um arquivo `.env` baseado no `.env.example`:
   ```bash
   cp .env.example .env
   ```

6. Edite o arquivo `.env` com suas configurações específicas.

## Configuração do MongoDB e Redis

### MongoDB

#### Usando Docker:

```bash
docker run -d -p 27017:27017 --name mongodb mongo:latest
```

#### Instalação local:

- macOS (com Homebrew): `brew install mongodb-community`
- Ubuntu/Debian: `sudo apt install -y mongodb`
- Windows: Baixe o instalador MSI em [MongoDB Download Center](https://www.mongodb.com/try/download/community)

### Redis

#### Usando Docker:

```bash
docker run -d -p 6379:6379 --name redis redis:latest
```

#### Instalação local:

- macOS (com Homebrew): `brew install redis`
- Ubuntu/Debian: `sudo apt install -y redis-server`
- Windows: Siga as instruções em [Redis Windows](https://github.com/microsoftarchive/redis/releases)

## Estrutura de Diretórios

```
ai-for-entrepreneurs/
├── app/
│   ├── api/           # Endpoints da API REST
│   ├── blockchain/    # Integração com blockchain 
│   ├── components/    # Componentes da UI Streamlit
│   ├── core/          # Funcionalidades principais da aplicação
│   ├── data/          # Modelos e manipulação de dados
│   ├── models/        # Modelos ML/AI
│   └── utils/         # Funções utilitárias
├── assets/            # Recursos como imagens e arquivos estáticos
├── .env.example       # Exemplo de configuração de variáveis de ambiente
├── app.py             # Aplicativo Streamlit principal
├── requirements.txt   # Dependências do projeto
├── setup.bat          # Script de setup para Windows
└── setup.sh           # Script de setup para macOS/Linux
```

## Verificação da Instalação

Para verificar se o ambiente foi configurado corretamente:

1. Ative o ambiente virtual
2. Execute:
   ```bash
   streamlit hello
   ```

Se uma demo do Streamlit aparecer no navegador, a instalação está correta.

## Solução de Problemas

### Erro ao instalar dependências com pip

Se você encontrar erros ao instalar pacotes, tente atualizar o pip:
```bash
pip install --upgrade pip
```

### Problemas com o MongoDB ou Redis

Verifique se os serviços estão rodando:
- MongoDB: `mongo --eval "db.version()"`
- Redis: `redis-cli ping` (deve retornar "PONG")

### Outras questões

Para outros problemas, verifique os logs ou abra uma issue no repositório. 