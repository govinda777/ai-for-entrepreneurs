#!/bin/bash

# Cores para output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

echo -e "${YELLOW}Configurando ambiente de desenvolvimento para IA do Empreendedor...${NC}"

# Verificar se Python 3.10+ está instalado
python_version=$(python3 --version 2>&1 | awk '{print $2}')
required_version="3.10.0"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then 
    echo -e "${RED}Python 3.10 ou superior é necessário. Versão atual: $python_version${NC}"
    exit 1
fi

echo -e "${GREEN}Python $python_version encontrado.${NC}"

# Verificar se pip está instalado
if ! command -v pip3 &> /dev/null; then
    echo -e "${RED}pip3 não encontrado. Por favor, instale o pip.${NC}"
    exit 1
fi

echo -e "${GREEN}pip3 encontrado.${NC}"

# Criar ambiente virtual
echo -e "${YELLOW}Criando ambiente virtual...${NC}"
python3 -m venv venv
if [ $? -ne 0 ]; then
    echo -e "${RED}Falha ao criar ambiente virtual.${NC}"
    exit 1
fi

# Ativar ambiente virtual
echo -e "${YELLOW}Ativando ambiente virtual...${NC}"
source venv/bin/activate
if [ $? -ne 0 ]; then
    echo -e "${RED}Falha ao ativar ambiente virtual.${NC}"
    exit 1
fi

# Atualizar pip
echo -e "${YELLOW}Atualizando pip...${NC}"
pip install --upgrade pip

# Instalar dependências
echo -e "${YELLOW}Instalando dependências...${NC}"
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo -e "${RED}Falha ao instalar dependências.${NC}"
    exit 1
fi

# Criar arquivo .env a partir do exemplo se não existir
if [ ! -f .env ]; then
    echo -e "${YELLOW}Criando arquivo .env a partir do exemplo...${NC}"
    cp .env.example .env
    echo -e "${GREEN}Arquivo .env criado. Por favor, atualize as variáveis conforme necessário.${NC}"
else
    echo -e "${GREEN}Arquivo .env já existe.${NC}"
fi

# Instalar NLTK data
echo -e "${YELLOW}Instalando dados NLTK...${NC}"
python -m nltk.downloader punkt stopwords wordnet
if [ $? -ne 0 ]; then
    echo -e "${RED}Falha ao baixar dados NLTK.${NC}"
    exit 1
fi

# Instalar pré-requisitos adicionais (Redis e MongoDB)
echo -e "${YELLOW}Verificando pré-requisitos adicionais...${NC}"
echo -e "${GREEN}Verifique se você tem MongoDB e Redis instalados localmente ou configurados em contêineres.${NC}"

echo -e "${GREEN}Ambiente de desenvolvimento configurado com sucesso!${NC}"
echo -e "${GREEN}Para ativar o ambiente, execute:${NC} source venv/bin/activate"
echo -e "${GREEN}Para iniciar o app Streamlit, execute:${NC} streamlit run app.py" 