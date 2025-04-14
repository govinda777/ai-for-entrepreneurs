import streamlit as st
from streamlit_elements import elements, dashboard, mui, html

def render_auth_component():
    """
    Renders Web3 authentication component with Metamask integration
    """
    with st.sidebar:
        st.sidebar.markdown("---")
        st.sidebar.subheader("Conectar Wallet")
        
        # Interface simples para conexão da wallet
        if "wallet_connected" not in st.session_state:
            st.session_state.wallet_connected = False
            st.session_state.wallet_address = None
        
        if not st.session_state.wallet_connected:
            if st.sidebar.button("Login com Metamask", use_container_width=True):
                # Aqui seria implementada a conexão real com Metamask via Web3
                # Por enquanto, simular a conexão para demonstração
                st.session_state.wallet_connected = True
                st.session_state.wallet_address = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F"
                st.rerun()
        else:
            st.sidebar.success(f"Wallet conectada")
            st.sidebar.code(f"{st.session_state.wallet_address[:6]}...{st.session_state.wallet_address[-4:]}")
            
            # Mostrar saldo de tokens (simulado)
            st.sidebar.metric("Tokens Xperience", "10 XP")
            
            # Botão para desconectar
            if st.sidebar.button("Desconectar", use_container_width=True):
                st.session_state.wallet_connected = False
                st.session_state.wallet_address = None
                st.rerun()
        
        st.sidebar.markdown("---")

def render_advanced_auth():
    """
    Renders advanced Web3 authentication using streamlit-elements (Material UI)
    This is a more sophisticated UI for the wallet connection
    """
    # Só usar esta função se específico para mostrar usos avançados de UI
    # com streamlit-elements
    with elements("web3_auth_elements"):
        # Criar um layout de dashboard
        with dashboard.Grid(numberCols=1, autoSize=False, draggableHandle=".draggable"):
            # Bloco de autenticação com Material UI
            with dashboard.Item("wallet_auth", 0, 0, 1, 2):
                with mui.Card(sx={"display": "flex", "flexDirection": "column", "p": 2, "borderRadius": 2, "boxShadow": 3}):
                    mui.CardHeader(title="Autenticação Web3", className="draggable")
                    
                    with mui.CardContent:
                        if "wallet_connected" not in st.session_state or not st.session_state.wallet_connected:
                            mui.Typography("Conecte sua wallet para acessar recursos exclusivos.")
                            with mui.Stack(direction="row", spacing=2, sx={"mt": 2}):
                                mui.Button("Conectar Metamask", variant="contained", color="primary")
                                mui.Button("WalletConnect", variant="outlined")
                        else:
                            mui.Typography("Wallet conectada:")
                            mui.Typography(
                                f"{st.session_state.wallet_address[:6]}...{st.session_state.wallet_address[-4:]}", 
                                sx={"fontWeight": "bold", "my": 1}
                            )
                            mui.Divider(sx={"my": 1})
                            with mui.Box(sx={"display": "flex", "alignItems": "center", "justifyContent": "space-between"}):
                                mui.Typography("Tokens Xperience:", sx={"fontWeight": "bold"})
                                mui.Typography("10 XP", sx={"color": "primary.main", "fontWeight": "bold"})
                            mui.Button("Desconectar", variant="outlined", color="error", sx={"mt": 2}) 