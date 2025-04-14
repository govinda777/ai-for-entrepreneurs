import streamlit as st
from streamlit_elements import elements, dashboard, mui, html, nivo

def render_advanced_dashboard():
    """
    Renders an advanced dashboard using streamlit-elements with draggable components
    and Nivo charts (more sophisticated than ApexCharts)
    """
    # Define height
    dashboard_height = 900
    
    # Create a dashboard layout
    with elements("advanced_dashboard"):
        # Dashboard layout with Material UI
        with dashboard.Grid(numberCols=12, rowHeight=40, draggableHandle=".draggable"):
            # Header card
            with dashboard.Item("header", 0, 0, 12, 2):
                with mui.Paper(sx={"p": 2, "display": "flex", "flexDirection": "column", "borderRadius": 3}):
                    mui.Typography("IA do Empreendedor - Dashboard Avançado", 
                                  variant="h5", 
                                  className="draggable",
                                  sx={"mb": 1, "fontWeight": "bold", "color": "#1E3A8A"})
                    mui.Typography("Visão detalhada do seu negócio com métricas e insights em tempo real", 
                                  variant="subtitle1", 
                                  color="textSecondary")
            
            # Metric cards
            with dashboard.Item("metrics_1", 0, 2, 4, 3):
                with mui.Paper(sx={"p": 2, "display": "flex", "flexDirection": "column", "borderRadius": 3}):
                    mui.Typography("Relatórios Gerados", className="draggable", sx={"fontWeight": "bold"})
                    with mui.Box(sx={"display": "flex", "alignItems": "center"}):
                        mui.Typography("0", variant="h3", sx={"my": 2, "fontWeight": "bold", "color": "#1E3A8A"})
                        mui.Typography("/10", sx={"ml": 1, "color": "text.secondary"})
                    mui.LinearProgress(variant="determinate", value=0, sx={"mb": 1})
                    mui.Typography("Nenhum relatório gerado ainda", variant="body2", color="text.secondary")
            
            with dashboard.Item("metrics_2", 4, 2, 4, 3):
                with mui.Paper(sx={"p": 2, "display": "flex", "flexDirection": "column", "borderRadius": 3}):
                    mui.Typography("Tokens Disponíveis", className="draggable", sx={"fontWeight": "bold"})
                    with mui.Box(sx={"display": "flex", "alignItems": "center"}):
                        mui.Typography("10", variant="h3", sx={"my": 2, "fontWeight": "bold", "color": "#1E3A8A"})
                        mui.Typography("XP", sx={"ml": 1, "color": "text.secondary"})
                    mui.LinearProgress(variant="determinate", value=100, sx={"mb": 1})
                    mui.Typography("Tokens para uso em relatórios e análises", variant="body2", color="text.secondary")
            
            with dashboard.Item("metrics_3", 8, 2, 4, 3):
                with mui.Paper(sx={"p": 2, "display": "flex", "flexDirection": "column", "borderRadius": 3}):
                    mui.Typography("Oportunidades Identificadas", className="draggable", sx={"fontWeight": "bold"})
                    with mui.Box(sx={"display": "flex", "alignItems": "center"}):
                        mui.Typography("0", variant="h3", sx={"my": 2, "fontWeight": "bold", "color": "#1E3A8A"})
                    mui.LinearProgress(variant="determinate", value=0, sx={"mb": 1})
                    mui.Typography("Sem oportunidades identificadas ainda", variant="body2", color="text.secondary")
            
            # Bar chart
            with dashboard.Item("bar_chart", 0, 5, 6, 8):
                with mui.Paper(sx={"p": 2, "display": "flex", "flexDirection": "column", "height": "100%", "borderRadius": 3}):
                    mui.Typography("Uso por Tipo de Relatório", className="draggable", sx={"fontWeight": "bold", "mb": 2})
                    
                    data = [
                        {
                            "relatório": "Mapa do Negócio",
                            "Gerados": 0,
                            "GeradosColor": "hsl(240, 70%, 50%)",
                            "Pendentes": 2,
                            "PendentesColor": "hsl(240, 20%, 80%)",
                        },
                        {
                            "relatório": "Relatório Xperience",
                            "Gerados": 0,
                            "GeradosColor": "hsl(240, 70%, 50%)",
                            "Pendentes": 3,
                            "PendentesColor": "hsl(240, 20%, 80%)",
                        },
                        {
                            "relatório": "Relatório SEO",
                            "Gerados": 0,
                            "GeradosColor": "hsl(240, 70%, 50%)",
                            "Pendentes": 1,
                            "PendentesColor": "hsl(240, 20%, 80%)",
                        },
                    ]
                    
                    # Nivo Bar Chart
                    nivo.Bar(
                        data=data,
                        keys=["Gerados", "Pendentes"],
                        indexBy="relatório",
                        margin={"top": 50, "right": 130, "bottom": 50, "left": 60},
                        padding=0.3,
                        valueScale={"type": "linear"},
                        indexScale={"type": "band", "round": True},
                        colors={"scheme": "blues"},
                        borderColor={"from": "color", "modifiers": [["darker", 1.6]]},
                        axisTop=None,
                        axisRight=None,
                        axisBottom={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": "Tipo de Relatório",
                            "legendPosition": "middle",
                            "legendOffset": 32,
                        },
                        axisLeft={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": "Quantidade",
                            "legendPosition": "middle",
                            "legendOffset": -40,
                        },
                        enableGridY=True,
                        labelSkipWidth=12,
                        labelSkipHeight=12,
                        labelTextColor={"from": "color", "modifiers": [["darker", 1.6]]},
                        legends=[
                            {
                                "dataFrom": "keys",
                                "anchor": "bottom-right",
                                "direction": "column",
                                "justify": False,
                                "translateX": 120,
                                "translateY": 0,
                                "itemsSpacing": 2,
                                "itemWidth": 100,
                                "itemHeight": 20,
                                "itemDirection": "left-to-right",
                                "itemOpacity": 0.85,
                                "symbolSize": 20,
                                "effects": [
                                    {
                                        "on": "hover",
                                        "style": {
                                            "itemOpacity": 1
                                        }
                                    }
                                ]
                            }
                        ],
                        role="application",
                        ariaLabel="Uso por Tipo de Relatório",
                        barAriaLabel={"enabled": True, "format": lambda e: e["id"] + ": " + e["value"] + " no " + e["indexValue"]}
                    )
            
            # Pie chart
            with dashboard.Item("pie_chart", 6, 5, 6, 4):
                with mui.Paper(sx={"p": 2, "display": "flex", "flexDirection": "column", "height": "100%", "borderRadius": 3}):
                    mui.Typography("Distribuição de Uso", className="draggable", sx={"fontWeight": "bold", "mb": 2})
                    
                    # Data for pie chart
                    data = [
                        {
                            "id": "Relatórios",
                            "label": "Relatórios",
                            "value": 70,
                            "color": "hsl(240, 70%, 50%)"
                        },
                        {
                            "id": "Chat",
                            "label": "Chat",
                            "value": 20,
                            "color": "hsl(240, 40%, 50%)"
                        },
                        {
                            "id": "Análises",
                            "label": "Análises",
                            "value": 10,
                            "color": "hsl(240, 10%, 50%)"
                        }
                    ]
                    
                    # Nivo Pie Chart
                    nivo.Pie(
                        data=data,
                        margin={"top": 40, "right": 80, "bottom": 80, "left": 80},
                        innerRadius=0.5,
                        padAngle=0.7,
                        cornerRadius=3,
                        activeOuterRadiusOffset=8,
                        borderWidth=1,
                        borderColor={"from": "color", "modifiers": [["darker", 0.2]]},
                        arcLinkLabelsSkipAngle=10,
                        arcLinkLabelsTextColor="grey",
                        arcLinkLabelsThickness=2,
                        arcLinkLabelsColor={"from": "color"},
                        arcLabelsSkipAngle=10,
                        arcLabelsTextColor={"from": "color", "modifiers": [["darker", 2]]},
                        legends=[
                            {
                                "anchor": "bottom",
                                "direction": "row",
                                "justify": False,
                                "translateX": 0,
                                "translateY": 56,
                                "itemsSpacing": 0,
                                "itemWidth": 100,
                                "itemHeight": 18,
                                "itemTextColor": "#999",
                                "itemDirection": "left-to-right",
                                "itemOpacity": 1,
                                "symbolSize": 18,
                                "symbolShape": "circle",
                                "effects": [
                                    {
                                        "on": "hover",
                                        "style": {
                                            "itemTextColor": "#000"
                                        }
                                    }
                                ]
                            }
                        ]
                    )
            
            # Line Chart (Market Trends)
            with dashboard.Item("line_chart", 6, 9, 6, 4):
                with mui.Paper(sx={"p": 2, "display": "flex", "flexDirection": "column", "height": "100%", "borderRadius": 3}):
                    mui.Typography("Tendências de Mercado", className="draggable", sx={"fontWeight": "bold", "mb": 2})
                    
                    line_data = [
                        {
                            "id": "Seu Mercado",
                            "color": "hsl(240, 70%, 50%)",
                            "data": [
                                { "x": "Jan", "y": 150 },
                                { "x": "Fev", "y": 170 },
                                { "x": "Mar", "y": 180 },
                                { "x": "Abr", "y": 160 },
                                { "x": "Mai", "y": 190 },
                                { "x": "Jun", "y": 210 },
                                { "x": "Jul", "y": 220 }
                            ]
                        },
                        {
                            "id": "Média do Setor",
                            "color": "hsl(200, 70%, 50%)",
                            "data": [
                                { "x": "Jan", "y": 200 },
                                { "x": "Fev", "y": 220 },
                                { "x": "Mar", "y": 210 },
                                { "x": "Abr", "y": 240 },
                                { "x": "Mai", "y": 250 },
                                { "x": "Jun", "y": 260 },
                                { "x": "Jul", "y": 270 }
                            ]
                        }
                    ]
                    
                    # Nivo Line Chart
                    nivo.Line(
                        data=line_data,
                        margin={"top": 50, "right": 110, "bottom": 50, "left": 60},
                        xScale={"type": "point"},
                        yScale={"type": "linear", "min": "auto", "max": "auto"},
                        yFormat=" >-.2f",
                        curve="cardinal",
                        axisTop=None,
                        axisRight=None,
                        axisBottom={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": "Mês",
                            "legendOffset": 36,
                            "legendPosition": "middle"
                        },
                        axisLeft={
                            "tickSize": 5,
                            "tickPadding": 5,
                            "tickRotation": 0,
                            "legend": "Crescimento",
                            "legendOffset": -40,
                            "legendPosition": "middle"
                        },
                        colors={"scheme": "category10"},
                        pointSize=10,
                        pointColor={"theme": "background"},
                        pointBorderWidth=2,
                        pointBorderColor={"from": "serieColor"},
                        pointLabelYOffset=-12,
                        useMesh=True,
                        legends=[
                            {
                                "anchor": "bottom-right",
                                "direction": "column",
                                "justify": False,
                                "translateX": 100,
                                "translateY": 0,
                                "itemsSpacing": 0,
                                "itemDirection": "left-to-right",
                                "itemWidth": 80,
                                "itemHeight": 20,
                                "itemOpacity": 0.75,
                                "symbolSize": 12,
                                "symbolShape": "circle",
                                "symbolBorderColor": "rgba(0, 0, 0, .5)",
                                "effects": [
                                    {
                                        "on": "hover",
                                        "style": {
                                            "itemBackground": "rgba(0, 0, 0, .03)",
                                            "itemOpacity": 1
                                        }
                                    }
                                ]
                            }
                        ]
                    ) 