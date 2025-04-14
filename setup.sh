#!/bin/bash

# Cores para output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}### Configurando IA do Empreendedor ###${NC}"

# Verificar se Python está instalado
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Python 3 não está instalado. Por favor, instale o Python 3.9 ou superior.${NC}"
    exit 1
fi

# Verificar versão do Python
python_version=$(python3 --version | awk '{print $2}')
if [[ "$(echo $python_version | cut -d '.' -f 1,2)" < "3.9" ]]; then
    echo -e "${RED}A versão do Python é $python_version. É necessário Python 3.9 ou superior.${NC}"
    exit 1
fi

echo -e "${GREEN}Versão do Python: $python_version${NC}"

# Criar ambiente virtual se não existir
if [ ! -d "venv" ]; then
    echo -e "${YELLOW}Criando ambiente virtual...${NC}"
    python3 -m venv venv
    echo -e "${GREEN}Ambiente virtual criado com sucesso!${NC}"
else
    echo -e "${GREEN}Ambiente virtual já existe.${NC}"
fi

# Ativar ambiente virtual
echo -e "${YELLOW}Ativando ambiente virtual...${NC}"
source venv/bin/activate
echo -e "${GREEN}Ambiente virtual ativado!${NC}"

# Instalar dependências
echo -e "${YELLOW}Instalando dependências...${NC}"
pip install --upgrade pip
pip install -r requirements.txt
echo -e "${GREEN}Dependências instaladas com sucesso!${NC}"

# Criar arquivos de pacote necessários
echo -e "${YELLOW}Criando estrutura de pacotes...${NC}"
mkdir -p app/components
mkdir -p app/api
mkdir -p app/blockchain
mkdir -p app/core
mkdir -p app/data
mkdir -p app/models
mkdir -p app/utils

# Criar arquivos __init__.py
if [ ! -f "app/__init__.py" ]; then
    echo '"""App package initialization."""' > app/__init__.py
    echo -e "${GREEN}Criado app/__init__.py${NC}"
else
    echo -e "${GREEN}app/__init__.py já existe.${NC}"
fi

if [ ! -f "app/components/__init__.py" ]; then
    echo '"""Components package initialization."""' > app/components/__init__.py
    echo -e "${GREEN}Criado app/components/__init__.py${NC}"
else
    echo -e "${GREEN}app/components/__init__.py já existe.${NC}"
fi

# Criar .env se não existir
if [ ! -f ".env" ] && [ -f ".env.example" ]; then
    echo -e "${YELLOW}Criando arquivo .env a partir do modelo...${NC}"
    cp .env.example .env
    echo -e "${GREEN}Arquivo .env criado com sucesso!${NC}"
    echo -e "${YELLOW}Edite o arquivo .env com suas configurações.${NC}"
elif [ ! -f ".env" ]; then
    echo -e "${YELLOW}Criando arquivo .env vazio...${NC}"
    touch .env
    echo -e "${GREEN}Arquivo .env criado!${NC}"
    echo -e "${YELLOW}Edite o arquivo .env com suas configurações.${NC}"
else
    echo -e "${GREEN}Arquivo .env já existe.${NC}"
fi

echo -e "${BLUE}### Configuração concluída ###${NC}"
echo -e "${GREEN}Para executar a aplicação, use:${NC}"
echo -e "${YELLOW}streamlit run app.py${NC}" 