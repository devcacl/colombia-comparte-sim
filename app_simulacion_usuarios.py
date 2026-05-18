import random
from typing import Dict, List, Tuple

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st


PRIMARY = "#0033A0"
SECONDARY = "#FCD116"
ACCENT = "#CE1126"
GREEN = "#2E7D32"
ORANGE = "#E65100"
RED = "#B71C1C"
INK = "#172033"
MUTED = "#667085"
SURFACE = "#F6F8FC"


ESTADOS_INFO: Dict[str, str] = {
    "S0": "Página de inicio de Colombia Comparte",
    "S1": "Selección de perfil (Emprendedor)",
    "S2": "Formulario de registro – datos personales",
    "S3": "Formulario de registro – datos del emprendimiento",
    "S4": "Carga de documentos requeridos",
    "S5": "Verificación de requisitos previos",
    "S6": "Selección de sector económico",
    "S7": "Descripción del proyecto / idea de negocio",
    "S8": "Selección de categoría de apoyo",
    "S9": "Revisión de términos y condiciones",
    "S10": "Envío de solicitud de registro",
    "S11": "Confirmación por correo electrónico",
    "S12": "Activación de cuenta",
    "S13": "Inicio de sesión post-registro",
    "S14": "Panel principal del emprendedor",
    "S15": "Error en datos personales (corrección)",
    "S16": "Error al cargar documentos (reintento)",
    "S17": "Duda en selección de sector (vuelve atrás)",
    "S18": "Lectura de preguntas frecuentes (FAQ)",
    "S19": "Chat de soporte en línea",
    "S20": "Abandono en datos personales",
    "S21": "Abandono en carga de documentos",
    "S22": "Abandono en selección de sector",
    "S23": "Abandono en términos y condiciones",
    "S24": "Error de sistema / timeout",
    "S25": "Reintento tras error de sistema",
    "S26": "Validación de NIT / cédula",
    "S27": "Registro de datos bancarios opcionales",
    "S28": "REGISTRO EXITOSO – Emprendedor activo",
    "S29": "FALLO DEFINITIVO – No puede completar registro",
}

ESTADOS = list(ESTADOS_INFO.keys())
ESTADOS_EXITO = ["S28"]
ESTADOS_ABANDONO = ["S20", "S21", "S22", "S23"]
ESTADOS_ERROR = ["S24", "S29"]
ESTADOS_SEGUIMIENTO = ["S18", "S19", "S25", "S27"]
ESTADOS_FINALES = ESTADOS_EXITO + ESTADOS_ABANDONO + ESTADOS_ERROR


RECORRIDOS: List[List[str]] = [
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S13", "S14", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S13", "S27", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S17", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S18", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S3", "S17", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S18", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S18", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S15", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S16", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S15", "S2", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S16", "S4", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S15", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S16", "S4", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S24", "S25", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S3", "S6", "S7", "S8", "S24", "S25", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S24", "S25", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S19", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S19", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S3", "S6", "S7", "S8", "S4", "S9", "S10", "S11", "S12", "S13", "S28"],
    ["S0", "S1", "S18", "S2", "S3", "S17", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S13", "S14", "S27", "S28"],
    ["S0", "S1", "S19", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S15", "S2", "S26", "S3", "S17", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S24", "S25", "S9", "S10", "S11", "S12", "S13", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S16", "S19", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S18", "S1", "S2", "S15", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S10", "S27", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S20"],
    ["S0", "S1", "S2", "S15", "S20"],
    ["S0", "S1", "S2", "S26", "S20"],
    ["S0", "S1", "S18", "S2", "S20"],
    ["S0", "S1", "S2", "S19", "S20"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S21"],
    ["S0", "S1", "S2", "S3", "S6", "S7", "S8", "S4", "S16", "S21"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S21"],
    ["S0", "S1", "S2", "S3", "S4", "S21"],
    ["S0", "S1", "S2", "S26", "S3", "S4", "S16", "S21"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S22"],
    ["S0", "S1", "S2", "S3", "S17", "S22"],
    ["S0", "S1", "S2", "S3", "S6", "S22"],
    ["S0", "S18", "S1", "S2", "S3", "S6", "S22"],
    ["S0", "S1", "S2", "S3", "S17", "S6", "S22"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S23"],
    ["S0", "S1", "S2", "S3", "S6", "S7", "S8", "S4", "S5", "S9", "S23"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S9", "S23"],
    ["S0", "S1", "S2", "S15", "S2", "S3", "S6", "S7", "S8", "S9", "S23"],
    ["S0", "S1", "S2", "S24", "S25", "S24", "S29"],
    ["S0", "S1", "S2", "S26", "S24", "S25", "S24", "S29"],
    ["S0", "S1", "S2", "S3", "S6", "S7", "S8", "S4", "S24", "S25", "S24", "S29"],
    ["S0", "S1", "S2", "S15", "S19", "S20"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S16", "S19", "S21"],
    ["S0", "S1", "S2", "S19", "S24", "S25", "S29"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S24", "S29"],
    ["S0", "S1", "S2", "S3", "S4", "S16", "S4", "S21"],
    ["S0", "S1", "S2", "S3", "S6", "S22"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S16", "S4", "S5", "S9", "S10", "S11", "S12", "S28"],
    ["S0", "S1", "S2", "S26", "S3", "S6", "S7", "S8", "S4", "S16", "S4", "S5", "S9", "S10", "S11", "S12", "S13", "S28"],
]


def state_type(code: str) -> str:
    if code == "S0":
        return "inicial"
    if code in ESTADOS_EXITO:
        return "final exitoso"
    if code in ESTADOS_ABANDONO:
        return "final negativo"
    if code in ESTADOS_ERROR:
        return "error"
    if code in ESTADOS_SEGUIMIENTO:
        return "seguimiento"
    return "intermedio"


def inject_css() -> None:
    st.markdown(
        f"""
        <style>
            .stApp {{
                background: linear-gradient(180deg, #ffffff 0%, {SURFACE} 100%);
                color: {INK};
            }}
            [data-testid="stSidebar"] {{
                background: linear-gradient(180deg, {PRIMARY} 0%, #061B55 100%);
            }}
            [data-testid="stSidebar"] * {{
                color: #ffffff !important;
            }}
            h1, h2, h3 {{
                color: {INK};
                letter-spacing: 0;
            }}
            .hero {{
                background: #ffffff;
                border-left: 8px solid {SECONDARY};
                border-radius: 8px;
                padding: 1rem 1.25rem;
                box-shadow: 0 10px 28px rgba(15, 23, 42, .08);
                margin-bottom: 1rem;
            }}
            .hero h1 {{
                margin: 0 0 .25rem 0;
                font-size: 2rem;
            }}
            .hero p {{
                margin: 0;
                color: {MUTED};
            }}
            .metric-card {{
                background: #ffffff;
                border: 1px solid #E5E7EB;
                border-radius: 8px;
                padding: .95rem;
                box-shadow: 0 8px 22px rgba(15, 23, 42, .06);
                min-height: 108px;
            }}
            .metric-card small {{
                color: {MUTED};
                font-weight: 700;
                text-transform: uppercase;
            }}
            .metric-card strong {{
                display: block;
                color: {PRIMARY};
                font-size: 1.65rem;
                margin-top: .25rem;
            }}
            .recommendation {{
                background: #ffffff;
                border: 1px solid #E7EEF8;
                border-left: 8px solid {ACCENT};
                border-radius: 8px;
                padding: 1rem 1.2rem;
                box-shadow: 0 8px 22px rgba(15, 23, 42, .06);
            }}
            .pill {{
                display: inline-block;
                border-radius: 999px;
                padding: .22rem .58rem;
                font-weight: 700;
                font-size: .78rem;
                background: #EEF4FF;
                color: {PRIMARY};
            }}
            div[data-testid="stDataFrame"] {{
                border: 1px solid #E5E7EB;
                border-radius: 8px;
                overflow: hidden;
            }}
            .stButton > button {{
                background: {PRIMARY};
                color: white;
                border: 0;
                border-radius: 8px;
                font-weight: 800;
            }}
            .stButton > button:hover {{
                background: #061B55;
                color: white;
                border: 0;
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def estados_dataframe() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "Código": code,
                "Nombre": description.split(" – ")[0],
                "Descripción": description,
                "Tipo de estado": state_type(code),
            }
            for code, description in ESTADOS_INFO.items()
        ]
    )


def recorridos_dataframe() -> pd.DataFrame:
    rows = []
    for index, recorrido in enumerate(RECORRIDOS, start=1):
        final = recorrido[-1]
        rows.append(
            {
                "Recorrido": f"R{index:02d}",
                "Códigos": " → ".join(recorrido),
                "Resultado": clasificar(final),
                "Estado final": final,
                "Descripción final": ESTADOS_INFO[final],
                "Número de pasos": len(recorrido),
            }
        )
    return pd.DataFrame(rows)


def construir_matriz_conteos() -> pd.DataFrame:
    matriz = pd.DataFrame(0, index=ESTADOS, columns=ESTADOS, dtype=int)
    for recorrido in RECORRIDOS:
        for actual, siguiente in zip(recorrido[:-1], recorrido[1:]):
            if actual in ESTADOS and siguiente in ESTADOS:
                matriz.loc[actual, siguiente] += 1
    return matriz


def construir_matriz_probabilidades(matriz_conteos: pd.DataFrame) -> pd.DataFrame:
    return matriz_conteos.div(matriz_conteos.sum(axis=1), axis=0).fillna(0)


def aplicar_mejoras(matriz_prob: pd.DataFrame) -> pd.DataFrame:
    matriz_mejorada = matriz_prob.copy()

    if "S24" in ESTADOS and matriz_mejorada.loc["S24"].sum() > 0:
        matriz_mejorada.loc["S24", "S25"] = 0.90
        matriz_mejorada.loc["S24", "S29"] = 0.10
        total = matriz_mejorada.loc["S24"].sum()
        if total > 0:
            matriz_mejorada.loc["S24"] /= total

    if "S16" in ESTADOS and matriz_mejorada.loc["S16"].sum() > 0:
        s16_row = matriz_mejorada.loc["S16"].copy()
        s16_row["S21"] = max(0, s16_row["S21"] - 0.17)
        s16_row["S4"] = s16_row["S4"] + 0.17
        total = s16_row.sum()
        if total > 0:
            s16_row /= total
        matriz_mejorada.loc["S16"] = s16_row

    return matriz_mejorada


def simular_usuario(matriz_prob: pd.DataFrame, max_pasos: int, estado_inicial: str = "S0") -> List[str]:
    estado_actual = estado_inicial
    recorrido_sim = [estado_actual]

    for _ in range(max_pasos):
        if estado_actual in ESTADOS_FINALES:
            break
        probs = matriz_prob.loc[estado_actual]
        if probs.sum() == 0:
            break
        siguiente = np.random.choice(matriz_prob.columns, p=probs.values)
        recorrido_sim.append(str(siguiente))
        estado_actual = str(siguiente)

    return recorrido_sim


def clasificar(estado_final: str) -> str:
    if estado_final in ESTADOS_EXITO:
        return "Éxito"
    if estado_final in ESTADOS_ABANDONO:
        return "Abandono"
    return "Error"


def ejecutar_simulacion(n_usuarios: int, max_pasos: int, seed: int, matriz_prob: pd.DataFrame) -> pd.DataFrame:
    random.seed(seed)
    np.random.seed(seed)
    resultados = []

    for i in range(n_usuarios):
        rec = simular_usuario(matriz_prob, max_pasos=max_pasos)
        ef = rec[-1]
        resultados.append(
            {
                "usuario": i + 1,
                "recorrido": " → ".join(rec),
                "estado_final": ef,
                "descripcion": ESTADOS_INFO.get(ef, ef),
                "categoria": clasificar(ef),
                "num_pasos": len(rec),
            }
        )

    return pd.DataFrame(resultados)


def calcular_kpis(df_resultados: pd.DataFrame) -> Dict[str, float]:
    n = max(len(df_resultados), 1)
    seguimiento = df_resultados["recorrido"].str.contains("S18|S19|S25|S27", regex=True).sum()
    return {
        "Éxito": (df_resultados["categoria"] == "Éxito").sum() / n * 100,
        "Abandono": (df_resultados["categoria"] == "Abandono").sum() / n * 100,
        "Error": (df_resultados["categoria"] == "Error").sum() / n * 100,
        "Seguimiento pendiente": seguimiento / n * 100,
        "Promedio de pasos": df_resultados["num_pasos"].mean(),
    }


def detectar_estado_critico(df_resultados: pd.DataFrame) -> Tuple[str, int, pd.DataFrame]:
    no_exitosos = df_resultados[df_resultados["categoria"] != "Éxito"]
    if no_exitosos.empty:
        return "Sin estado crítico", 0, pd.DataFrame()

    dist = no_exitosos["estado_final"].value_counts().reset_index()
    dist.columns = ["Estado", "Usuarios"]
    dist["Descripción"] = dist["Estado"].map(ESTADOS_INFO)
    dist["Categoría"] = dist["Estado"].map(clasificar)
    top = dist.iloc[0]
    label = f"{top['Estado']} – {top['Descripción']}"
    return label, int(top["Usuarios"]), dist


def recomendacion_estado_critico(estado_critico: str) -> str:
    if estado_critico.startswith("S24"):
        return (
            "Implementar guardado automático del progreso del formulario y mensajes claros de recuperación "
            "cuando ocurra un error de sistema. Esto evita que el usuario pierda información por timeout y "
            "reduce la probabilidad de fallo definitivo desde S24."
        )
    if estado_critico.startswith("S21"):
        return (
            "Simplificar la carga de documentos: aceptar más formatos, reducir el tamaño máximo exigido, "
            "mostrar ejemplos visuales y permitir guardar documentos parcialmente antes de continuar."
        )
    if estado_critico.startswith("S20"):
        return (
            "Reducir fricción en datos personales: validar campos en tiempo real, explicar por qué se pide "
            "cada dato y ofrecer ayuda visible antes de que el usuario abandone."
        )
    if estado_critico.startswith("S22"):
        return (
            "Mejorar la selección de sector económico con buscador, ejemplos de sectores y recomendación "
            "asistida según la descripción del emprendimiento."
        )
    if estado_critico.startswith("S23"):
        return (
            "Resumir términos y condiciones en lenguaje claro, destacar puntos clave y permitir lectura "
            "por secciones para reducir abandono al final del proceso."
        )
    return (
        "Priorizar el monitoreo del punto crítico detectado y comparar el cambio contra la matriz mejorada "
        "propuesta en el cuaderno original."
    )


def render_header() -> None:
    st.markdown(
        """
        <div class="hero">
            <h1>Simulación – Colombia Comparte</h1>
            <p>Flujo de registro de emprendedores con cadenas de Márkov, basado únicamente en el cuaderno original.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_metric(label: str, value: str) -> None:
    st.markdown(
        f"""
        <div class="metric-card">
            <small>{label}</small>
            <strong>{value}</strong>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_dashboard(df_resultados: pd.DataFrame) -> None:
    kpis = calcular_kpis(df_resultados)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        render_metric("Éxito", f"{kpis['Éxito']:.1f}%")
    with col2:
        render_metric("Abandono", f"{kpis['Abandono']:.1f}%")
    with col3:
        render_metric("Error", f"{kpis['Error']:.1f}%")
    with col4:
        render_metric("Seguimiento pendiente", f"{kpis['Seguimiento pendiente']:.1f}%")
    with col5:
        render_metric("Promedio de pasos", f"{kpis['Promedio de pasos']:.2f}")

    conteos = df_resultados["categoria"].value_counts().reset_index()
    conteos.columns = ["Categoría", "Usuarios"]
    colors = {"Éxito": GREEN, "Abandono": ORANGE, "Error": RED}

    col_a, col_b = st.columns([1.1, 1])
    with col_a:
        fig = px.bar(
            conteos,
            x="Categoría",
            y="Usuarios",
            color="Categoría",
            text="Usuarios",
            color_discrete_map=colors,
            title="Resultados generales de la simulación",
        )
        fig.update_traces(textposition="outside", marker_line_width=0)
        fig.update_layout(showlegend=False, plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=20, r=20, t=55, b=20))
        st.plotly_chart(fig, use_container_width=True)

    with col_b:
        fig = px.pie(
            conteos,
            names="Categoría",
            values="Usuarios",
            hole=0.58,
            color="Categoría",
            color_discrete_map=colors,
            title="Distribución porcentual",
        )
        fig.update_layout(plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=20, r=20, t=55, b=20))
        st.plotly_chart(fig, use_container_width=True)

    fig_steps = px.histogram(
        df_resultados,
        x="num_pasos",
        color="categoria",
        color_discrete_map=colors,
        nbins=18,
        title="Distribución de pasos por usuario",
        labels={"num_pasos": "Número de pasos", "categoria": "Categoría"},
    )
    fig_steps.add_vline(x=kpis["Promedio de pasos"], line_dash="dash", line_color=PRIMARY)
    fig_steps.update_layout(plot_bgcolor="white", paper_bgcolor="white", margin=dict(l=20, r=20, t=55, b=20))
    st.plotly_chart(fig_steps, use_container_width=True)


def render_modelo(matriz_conteos: pd.DataFrame, matriz_prob: pd.DataFrame) -> None:
    st.subheader("Estados del modelo")
    st.dataframe(estados_dataframe(), use_container_width=True, hide_index=True)

    st.subheader("Recorridos base de usuarios")
    st.dataframe(recorridos_dataframe(), use_container_width=True, hide_index=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Matriz de conteos")
        st.dataframe(matriz_conteos, use_container_width=True)
    with col2:
        st.subheader("Matriz de probabilidades")
        st.dataframe(matriz_prob.style.format("{:.2%}"), use_container_width=True)


def render_simulacion(df_resultados: pd.DataFrame) -> None:
    st.subheader("Vista previa de la simulación")
    st.dataframe(df_resultados.head(12), use_container_width=True, hide_index=True)

    st.subheader("Resultados completos")
    st.dataframe(df_resultados, use_container_width=True, hide_index=True)
    st.download_button(
        "Descargar resultados CSV",
        data=df_resultados.to_csv(index=False).encode("utf-8-sig"),
        file_name="resultados_simulacion_colombia_comparte.csv",
        mime="text/csv",
        use_container_width=True,
    )


def render_mejora(df_resultados: pd.DataFrame, matriz_prob: pd.DataFrame, n_usuarios: int, max_pasos: int, seed: int) -> None:
    st.subheader("Estado crítico y propuesta de mejora")
    estado_critico, n_critico, dist = detectar_estado_critico(df_resultados)

    col1, col2 = st.columns([0.8, 1.2])
    with col1:
        st.markdown(
            f"""
            <div class="metric-card">
                <small>Estado más crítico</small>
                <strong style="font-size:1.18rem">{estado_critico}</strong>
                <p style="color:{MUTED}; margin:.5rem 0 0 0;">Usuarios no exitosos en este estado: {n_critico}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            f"""
            <div class="recommendation">
                <span class="pill">Recomendación del modelo</span>
                <p style="margin:.8rem 0 0 0; color:{INK};">{recomendacion_estado_critico(estado_critico)}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    if not dist.empty:
        st.dataframe(dist, use_container_width=True, hide_index=True)

    st.subheader("Escenario mejorado del cuaderno")
    matriz_mejorada = aplicar_mejoras(matriz_prob)
    df_mejorado = ejecutar_simulacion(n_usuarios, max_pasos, seed + 1, matriz_mejorada)
    base = df_resultados["categoria"].value_counts().rename("Antes")
    mejorado = df_mejorado["categoria"].value_counts().rename("Después")
    comparativa = pd.concat([base, mejorado], axis=1).fillna(0).astype(int).reset_index()
    comparativa.columns = ["Categoría", "Antes", "Después"]
    comparativa["Diferencia"] = comparativa["Después"] - comparativa["Antes"]
    st.dataframe(comparativa, use_container_width=True, hide_index=True)

    fig = go.Figure()
    fig.add_trace(go.Bar(name="Antes", x=comparativa["Categoría"], y=comparativa["Antes"], marker_color=PRIMARY))
    fig.add_trace(go.Bar(name="Después", x=comparativa["Categoría"], y=comparativa["Después"], marker_color=SECONDARY))
    fig.update_layout(
        barmode="group",
        title="Comparativa antes vs. después de las mejoras",
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(l=20, r=20, t=55, b=20),
    )
    st.plotly_chart(fig, use_container_width=True)


def main() -> None:
    st.set_page_config(page_title="Colombia Comparte | Simulación", page_icon=":bar_chart:", layout="wide")
    inject_css()

    matriz_conteos = construir_matriz_conteos()
    matriz_prob = construir_matriz_probabilidades(matriz_conteos)

    with st.sidebar:
        st.markdown("## Colombia Comparte")
        st.caption("Flujo: Registro de emprendedores")
        n_usuarios = st.slider("Número de usuarios a simular", 10, 5000, 1000, step=10)
        max_pasos = st.slider("Número máximo de pasos por usuario", 5, 80, 40, step=1)
        seed = st.number_input("Semilla aleatoria", min_value=1, max_value=999999, value=2026, step=1)
        ejecutar = st.button("Ejecutar simulación", use_container_width=True)

        st.markdown("---")
        seccion = st.radio("Barra de navegación", ["Dashboard", "Modelo", "Simulación", "Mejora"], index=0)
        st.markdown("---")
        st.caption("Datos tomados del notebook original ProyectoFinalSimulacion.ipynb.")

    render_header()

    if "df_resultados" not in st.session_state or ejecutar:
        st.session_state.df_resultados = ejecutar_simulacion(n_usuarios, max_pasos, seed, matriz_prob)
        st.session_state.config = {"usuarios": n_usuarios, "max_pasos": max_pasos, "seed": seed}

    df_resultados = st.session_state.df_resultados
    config = st.session_state.config
    st.info(
        f"Configuración actual: {config['usuarios']} usuarios, "
        f"{config['max_pasos']} pasos máximos, semilla {config['seed']}. "
        f"Modelo base: {len(ESTADOS)} estados y {len(RECORRIDOS)} recorridos."
    )

    if seccion == "Dashboard":
        render_dashboard(df_resultados)
    elif seccion == "Modelo":
        render_modelo(matriz_conteos, matriz_prob)
    elif seccion == "Simulación":
        render_simulacion(df_resultados)
    else:
        render_mejora(df_resultados, matriz_prob, config["usuarios"], config["max_pasos"], config["seed"])


if __name__ == "__main__":
    main()
