import streamlit as st
from streamlit_apexcharts import st_apexcharts
import json

def render_dashboard():
    """
    Renders the main dashboard with metrics and charts
    """
    st.header("Dashboard Principal")
    
    # Cards com métricas principais
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Relatórios Gerados", value="0")
    with col2:
        st.metric(label="Tokens Disponíveis", value="10")
    with col3:
        st.metric(label="Oportunidades Identificadas", value="0")
    
    # Gráficos com ApexCharts
    st.subheader("Análise de Atividades")
    
    # Gráfico de barras - Uso por tipo de relatório
    options = {
        "chart": {
            "type": "bar",
            "height": 350
        },
        "plotOptions": {
            "bar": {
                "horizontal": False,
                "columnWidth": "55%",
            },
        },
        "dataLabels": {
            "enabled": False
        },
        "stroke": {
            "show": True,
            "width": 2,
            "colors": ["transparent"]
        },
        "xaxis": {
            "categories": ["Mapa do Negócio", "Relatório Xperience", "Relatório SEO"],
        },
        "yaxis": {
            "title": {
                "text": "Relatórios"
            }
        },
        "fill": {
            "opacity": 1
        },
        "tooltip": {
            "y": {
                "formatter": "function (val) {return val + ' relatórios'}"
            }
        },
        "title": {
            "text": "Relatórios por Tipo",
        }
    }
    
    series = [{
        "name": "Gerados",
        "data": [0, 0, 0]
    }]
    
    st_apexcharts(options, series, height=350)
    
    # Gráfico de área - Tokens ao longo do tempo
    col1, col2 = st.columns(2)
    
    with col1:
        area_options = {
            "chart": {
                "type": "area",
                "height": 350,
                "zoom": {
                    "enabled": False
                }
            },
            "dataLabels": {
                "enabled": False
            },
            "stroke": {
                "curve": "smooth"
            },
            "title": {
                "text": "Uso de Tokens",
            },
            "xaxis": {
                "categories": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun", "Jul"],
            },
            "yaxis": {
                "title": {
                    "text": "Tokens"
                }
            }
        }
        
        area_series = [{
            "name": "Tokens Utilizados",
            "data": [0, 0, 0, 0, 0, 0, 0]
        }]
        
        st_apexcharts(area_options, area_series, height=300)
    
    with col2:
        pie_options = {
            "chart": {
                "type": "pie",
                "height": 350
            },
            "labels": ["Relatórios", "Chat", "Análises"],
            "title": {
                "text": "Distribuição de Uso",
            },
            "responsive": [{
                "breakpoint": 480,
                "options": {
                    "chart": {
                        "width": 200
                    },
                    "legend": {
                        "position": "bottom"
                    }
                }
            }]
        }
        
        pie_series = [70, 20, 10]
        
        st_apexcharts(pie_options, pie_series, height=300)
    
    # Texto informativo
    st.info("""
    Bem-vindo à IA do Empreendedor!
    
    Esta plataforma utiliza Inteligência Artificial para transformar dados em insights estratégicos, 
    ajudando empreendedores a identificar oportunidades de mercado seguindo a teoria do Oceano Azul.
    
    **Comece selecionando um tipo de relatório no menu à esquerda.**
    """) 