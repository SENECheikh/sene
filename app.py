
import streamlit as st
from streamlit_extras.colored_header import colored_header
from streamlit_extras.card import card

# ------------------------------
# CONFIGURATION
# ------------------------------
st.set_page_config(
    page_title="Portfolio - Cheikh SENE",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# STYLE CUSTOM
# ------------------------------
st.markdown("""
    <style>
    .big-title {
        font-size: 60px;
        font-weight: 900;
        text-align: center;
        color: #2C6AFF;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        margin-top: -15px;
        color: #333;
    }
    .section-title {
        font-size: 35px;
        font-weight: 800;
        padding-top: 30px;
        color: #2C2C2C;
    }
    .card-container {
        display: flex;
        flex-wrap: wrap;
        gap: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------------------
# SIDEBAR NAV
# ------------------------------
st.sidebar.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=50)
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio("Aller vers :", [
    "🏠 Accueil",
    "📚 Projets",
    "💼 Expériences",
    "🛠 Compétences",
    "📞 Contact"
])

# ------------------------------
# PAGE : ACCUEIL
# ------------------------------
if page == "🏠 Accueil":
    st.markdown('<div class="big-title">Cheikh SENE</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Data Scientist • Machine Learning • IA • Statistique avancée</div>', unsafe_allow_html=True)

    colored_header(label="", description="", color_name="blue-70")

    st.write("""
    Bienvenue sur mon portfolio interactif.  
    Je suis passionné par la Data Science, le Machine Learning, les analyses statistiques 
    et la création de solutions intelligentes.  
    """)

    st.success("👉 Explore mes projets, expériences et mes compétences via le menu à gauche !")

# ------------------------------
# PAGE : PROJETS
# ------------------------------
elif page == "📚 Projets":
    st.markdown('<div class="section-title">📚 Mes Projets</div>', unsafe_allow_html=True)

    card(
        title="Modélisation prédictive du risque financier – CARSAT Nord-Est",
        text="Modèle supervisé (XGBoost, Random Forest), preprocessing, analyse des risques, dashboard complet.",
        url="https://github.com/SENECheikh"
    )

    card(
        title="Application Streamlit de pilotage statistique",
        text="Dashboard interactif avec filtres dynamiques, graphiques, indicateurs clés.",
        url="https://github.com/SENECheikh"
    )

    card(
        title="Projets Machine Learning (NLP, Classification, Forecasting)",
        text="Ensemble de notebooks ML démontrant mon expertise Python + Data Science.",
        url="https://github.com/SENECheikh"
    )

# ------------------------------
# PAGE : EXPÉRIENCES
# ------------------------------
elif page == "💼 Expériences":
    st.markdown('<div class="section-title">💼 Mes Expériences</div>', unsafe_allow_html=True)

    st.subheader("📌 CARSAT Nord-Est — Chargé d'Études Statistiques")
    st.write("""
    2023 – 2025  
    - Modélisation prédictive (Machine Learning)  
    - Analyses statistiques avancées  
    - Automatisations Python  
    - Développement d’une application Streamlit  
    - Études d’impact financier  
    """)

    st.markdown("---")

    st.subheader("📘 Projets Académiques — MSc Data Management / CEPOPP")
    st.write("""
    - Visualisation avancée  
    - Data Cleaning & Feature Engineering  
    - Économétrie appliquée  
    - Machine Learning supervisé & non supervisé  
    """)

# ------------------------------
# PAGE : COMPÉTENCES
# ------------------------------
elif page == "🛠 Compétences":
    st.markdown('<div class="section-title">🛠 Compétences</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔹 Machine Learning")
        st.write("""
        - Régression, Classification  
        - NLP, vectorisation, TF-IDF  
        - Time Series (ARIMA, LSTM)  
        - Interprétabilité des modèles  
        """)

        st.subheader("🔹 Langages & Outils")
        st.write("""
        - Python (Pandas, NumPy, Scikit-learn)
        - Streamlit
        - Git/GitHub
        - SQL
        """)

    with col2:
        st.subheader("🔹 Visualisation")
        st.write("""
        - Matplotlib, Seaborn, Plotly  
        - Dashboards interactifs  
        """)

        st.subheader("🔹 Autres")
        st.write("""
        - Statistiques avancées  
        - Feature Engineering  
        - Data Cleaning  
        """)

# ------------------------------
# PAGE : CONTACT
# ------------------------------
elif page == "📞 Contact":
    st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)

    st.write("📧 Email : tonemail@example.com")
    st.write("🔗 LinkedIn : https://linkedin.com/in/xxxx")
    st.write("💻 GitHub : https://github.com/SENECheikh")

    st.success("Merci de visiter mon portfolio 🙌")
