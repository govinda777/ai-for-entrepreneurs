# CI/CD para IA do Empreendedor

Este documento descreve a configuração de Integração Contínua (CI) e Entrega Contínua (CD) para o projeto IA do Empreendedor, utilizando provedores gratuitos.

## Visão Geral

O pipeline de CI/CD automatizará os seguintes processos:
- Execução de testes automatizados
- Verificação de qualidade de código
- Build de containers Docker
- Deployment para ambiente de staging e produção

## Provedores Selecionados

### CI/CD

| Provedor | Vantagens | Limitações |
|----------|-----------|------------|
| **GitHub Actions** | Integração nativa com GitHub, workflows YAML, 2000 minutos gratuitos/mês | Limitação de minutos em contas gratuitas |

### Hospedagem

| Provedor | Vantagens | Limitações |
|----------|-----------|------------|
| **Railway** | Deploy automático, integração GitHub, sem inatividade | Limite de 5$ em créditos gratuitos/mês |

### Banco de Dados

| Provedor | Vantagens | Limitações |
|----------|-----------|------------|
| **MySQL** | Banco de dados relacional, fácil configuração | Limite de 1GB de armazenamento |

## Configuração GitHub Actions

### Estrutura de Branches

```
main        # Produção
├── staging # Ambiente de teste
└── dev     # Desenvolvimento
```

### Workflows

Crie os seguintes arquivos na pasta `.github/workflows/`:

#### 1. `ci.yml` (Integração Contínua)

```yaml
name: CI

on:
  push:
    branches: [ dev, staging, main ]
  pull_request:
    branches: [ dev, staging, main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
          
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
          pip install pytest pytest-cov flake8
          
      - name: Lint with flake8
        run: |
          flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
          
      - name: Test with pytest
        run: |
          pytest --cov=./ --cov-report=xml
          
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: true
```

#### 2. `cd-staging.yml` (Deploy para Staging)

```yaml
name: Deploy to Staging

on:
  push:
    branches: [ staging ]
    
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
        
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
          
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: user/ia-empreendedor:staging
          
      - name: Deploy to Railway
        uses: bervProject/railway-deploy@main
        with:
          service: ia-empreendedor-staging
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
```

#### 3. `cd-production.yml` (Deploy para Produção)

```yaml
name: Deploy to Production

on:
  push:
    branches: [ main ]
    
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v2
        
      - name: Login to Docker Hub
        uses: docker/login-action@v2
        with:
          username: ${{ secrets.DOCKERHUB_USERNAME }}
          password: ${{ secrets.DOCKERHUB_TOKEN }}
          
      - name: Build and push
        uses: docker/build-push-action@v4
        with:
          context: .
          push: true
          tags: user/ia-empreendedor:latest
          
      - name: Deploy to Railway
        uses: bervProject/railway-deploy@main
        with:
          service: ia-empreendedor-prod
          railway_token: ${{ secrets.RAILWAY_TOKEN }}
```

## Configuração do Railway

1. Crie uma conta em [railway.app](https://railway.app)
2. Crie um novo projeto
3. Configure:
   - Nome: ia-empreendedor (staging/prod)
   - Integração GitHub
   - Configuração Docker:
     - Root Directory: ./
     - Dockerfile Path: Dockerfile
     - Port: 8501

### Banco de Dados MySQL no Railway

1. Adicione o serviço MySQL ao seu projeto Railway:
   - No dashboard do projeto, clique em "New"
   - Selecione "Database" > "MySQL"
   - Railway configurará automaticamente um banco MySQL

2. Obtenha as credenciais de conexão:
   - Na seção "Variables" do serviço MySQL
   - Railway cria automaticamente as variáveis MYSQL_URL, etc.

## Arquivo Docker

Crie um `Dockerfile` na raiz do projeto:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

E um arquivo `.dockerignore`:

```
.git
.github
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.coverage
htmlcov/
.tox/
.pytest_cache/
```

## Configuração de Variáveis de Ambiente

### GitHub Secrets

Configure as seguintes secrets no seu repositório GitHub:
- `DOCKERHUB_USERNAME`: Seu usuário no Docker Hub
- `DOCKERHUB_TOKEN`: Token de acesso ao Docker Hub
- `RAILWAY_TOKEN`: Token de API do Railway

### Railway Environment Variables

Configure as seguintes variáveis de ambiente no Railway:
- `JWT_SECRET`: Chave secreta para tokens JWT
- `WEB3_PROVIDER_URL`: URL do provedor Web3 (ex: Infura)
- `ENVIRONMENT`: staging ou production

## Monitoramento

Para monitoramento gratuito, recomendamos:
- **Sentry** (free tier): Para monitoramento de erros
- **Railway Dashboard**: Para logs e métricas básicas
- **Uptimerobot**: Para monitoramento de disponibilidade

## Estratégia de Deployment

1. **Desenvolvimento**:
   - Desenvolvedores trabalham em branches de feature
   - Pull requests são abertos para a branch `dev`
   - CI executa testes e análise de código em cada PR

2. **Staging**:
   - Merge de `dev` para `staging` quando features estiverem prontas
   - CD automaticamente faz deploy para ambiente de staging
   - Testes manuais e validação de QA

3. **Produção**:
   - Merge de `staging` para `main` após validação
   - CD automaticamente faz deploy para ambiente de produção
   - Monitoramento de erros e performance

## Considerações sobre Custos

O Railway oferece um plano gratuito com limites, mas considere:
- Manter o consumo dentro do limite de $5 em créditos/mês
- Configurar alertas de uso para evitar cobranças inesperadas
- Considerar a migração para planos pagos à medida que a aplicação cresce

## Próximos Passos

1. Configurar repositório no GitHub
2. Adicionar os workflows de GitHub Actions
3. Configurar projeto no Railway
4. Configurar banco de dados MySQL
5. Configurar variáveis de ambiente
6. Realizar deploy inicial manual para verificar configuração
7. Testar o pipeline de CI/CD completo
8. Configurar monitoramento com Sentry
