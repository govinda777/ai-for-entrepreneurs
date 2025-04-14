import streamlit as st
import os
from dotenv import load_dotenv

# Import components
from app.components.dashboard import render_dashboard
from app.components.business_map import render_business_map
from app.components.chat import render_chat
from app.components.web3_auth import render_auth_component
from app.components.advanced_charts import render_advanced_dashboard

# Carregar variáveis de ambiente
load_dotenv()

# Configuração da página
st.set_page_config(
    page_title="IA do Empreendedor",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Função para configuração de estilo CSS
def load_css():
    st.markdown("""
    <style>
    .main .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    
    h1, h2, h3 {
        color: #1E3A8A;
    }
    
    .stButton button {
        background-color: #1E3A8A;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
    }
    
    .stButton button:hover {
        background-color: #1E40AF;
    }
    
    .css-1y4p8pa {
        padding-top: 0rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Carregar CSS
load_css()

# Título principal
st.title("IA do Empreendedor")
st.subheader("Transformando dados em insights estratégicos")

# Sidebar
with st.sidebar:
    st.image("assets/wireframe.jpeg", width=250)
    st.title("Menu Principal")
    
    # Opções do menu
    menu = st.radio(
        "Selecione uma opção:",
        [
            "Dashboard",
            "Dashboard Avançado",
            "Mapa do Seu Negócio",
            "Relatório Xperience",
            "Relatório SEO",
            "Configurações",
        ],
    )
    
    # Componente de autenticação Web3
    render_auth_component()

# Chat box na lateral direita (fixado em todas as páginas)
chat_container = st.container()

# Conteúdo principal baseado na seleção do menu
if menu == "Dashboard":
    render_dashboard()
    
elif menu == "Dashboard Avançado":
    render_advanced_dashboard()
    
elif menu == "Mapa do Seu Negócio":
    render_business_map()

elif menu == "Relatório Xperience":
    st.header("Relatório Xperience (Oceano Azul)")
    st.markdown("""
    O Relatório Xperience utiliza os princípios da estratégia do Oceano Azul para identificar 
    oportunidades inexploradas de mercado e criar novos espaços onde a concorrência é irrelevante.
    """)
    
    # Formulário para o Relatório Xperience
    with st.form("form_relatorio_xperience"):
        st.subheader("Produtos e Serviços")
        produtos = st.text_area("Produtos/Serviços Atuais (um por linha)")
        
        st.subheader("Diferenciação")
        diferenciais = st.text_area("Diferenciais Competitivos Atuais")
        
        st.subheader("Cliente-Alvo")
        dores = st.text_area("Principais Dores do Cliente-Alvo")
        
        st.subheader("Objetivos")
        objetivos = st.text_area("Objetivos Estratégicos")
        
        if st.form_submit_button("Gerar Relatório Xperience"):
            st.success("Esta funcionalidade será implementada em breve!")

elif menu == "Relatório SEO":
    st.header("Relatório SEO")
    st.markdown("""
    O Relatório SEO analisa sua presença digital e fornece recomendações para 
    melhorar seu posicionamento nos motores de busca e aumentar o tráfego do seu site.
    """)
    
    # Formulário para o Relatório SEO
    with st.form("form_relatorio_seo"):
        st.subheader("Informações do Site")
        url = st.text_input("URL do Site")
        
        st.subheader("Palavras-chave")
        keywords = st.text_area("Palavras-chave Alvo (uma por linha)")
        
        st.subheader("Concorrência Digital")
        concorrentes_digitais = st.text_area("Concorrentes Digitais (um por linha)")
        
        st.subheader("Marketing Digital")
        canais = st.multiselect(
            "Canais de Marketing Utilizados",
            ["SEO Orgânico", "Google Ads", "Facebook Ads", "Instagram", "LinkedIn", "Email Marketing", "Outros"]
        )
        
        if st.form_submit_button("Gerar Relatório SEO"):
            st.success("Esta funcionalidade será implementada em breve!")

elif menu == "Configurações":
    st.header("Configurações")
    
    # Tabs para diferentes configurações
    tab1, tab2, tab3 = st.tabs(["Perfil", "Tokens", "API"])
    
    with tab1:
        st.subheader("Perfil do Usuário")
        st.text_input("Nome")
        st.text_input("Email")
        st.text_input("Empresa")
        if st.button("Salvar Perfil"):
            st.success("Esta funcionalidade será implementada em breve!")
    
    with tab2:
        st.subheader("Tokens Xperience")
        st.metric("Tokens Disponíveis", "10")
        st.button("Comprar Tokens")
    
    with tab3:
        st.subheader("Configurações de API")
        st.text_input("API Key", type="password")
        st.checkbox("Ativar Modo Debug")
        if st.button("Salvar Configurações"):
            st.success("Esta funcionalidade será implementada em breve!")

# Renderizar o componente de chat na lateral direita
with chat_container:
    render_chat()

# Rodapé
st.markdown("---")
st.markdown("© 2023 IA do Empreendedor | Desenvolvido com ❤️ para Empreendedores") 