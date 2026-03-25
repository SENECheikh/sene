import streamlit as st

st.set_page_config(
    page_title="Portfolio - Cheikh SENE",
    page_icon="📊",
    layout="wide"
)

# ----------- CSS PREMIUM -----------
st.markdown("""
<style>

body {
    background-color: #F5F7FA;
}

/* HEADER */
.hero {
    padding: 80px;
    background: linear-gradient(135deg, #2C6AFF 0%, #3B8DFF 100%);
    border-radius: 15px;
    text-align: center;
    color: white;
    margin-bottom: 40px;
}
.hero h1 {
    font-size: 60px;
    font-weight: 900;
    margin-bottom: -10px;
}
.hero h3 {
    font-size: 22px;
    font-weight: 300;
}

/* TITRES DE SECTION */
.section-title {
    font-size: 36px;
    font-weight: 800;
    margin-top: 40px;
    margin-bottom: 20px;
    color: #1E1E1E;
}

/* CARTES */
.card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #E4E7EB;
    box-shadow: 0 4px 8px rgba(0,0,0,0.04);
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
}
.card h4 {
    font-size: 24px;
    margin-bottom: 8px;
}
.card p {
    font-size: 16px;
    opacity: 0.8;
}

/* FOOTER */
.footer {
    margin-top: 70px;
    padding: 25px;
    text-align: center;
    font-size: 15px;
    opacity: 0.6;
}

</style>
""", unsafe_allow_html=True)

# -------- SIDEBAR --------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Menu :", ["🏠 Accueil", "📚 Projets", "💼 Expériences", "🛠 Compétences", "📞 Contact"])

# -------- ACCUEIL --------
if page == "🏠 Accueil":
    st.markdown("""
    <div class="hero">
        <h1>Cheikh SENE</h1>
        <h3>Data Scientist • Machine Learning • IA • Statistiques avancées</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write("""
    Bienvenue sur mon portfolio professionnel.  
    Je suis spécialisé en Data Science, Machine Learning et analyses statistiques.
    """)


# -------- PROJETS --------
elif page == "📚 Projets":
    st.markdown('<div class="section-title">📚 Mes Projets</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="card">
            <h4>Modélisation prédictive du risque financier</h4>
            <p>Projet de Machine Learning à la CARSAT Nord-Est (Random Forest, XGBoost, Streamlit App).</p>
            https://github.com/SENECheikh🔗 Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h4>Projet NLP – Classification de textes</h4>
            <p>Vectorisation, TF-IDF, modèles de langage avancés pour la classification.</p>
            https://github.com/SENECheikh🔗 Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>Dashboard Streamlit statistique</h4>
            <p>Exploration et visualisation d'indicateurs dynamiques.</p>
            https://github.com/SENECheikh🔗 Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h4>Forecasting / Série temporelles</h4>
            <p>Modèles ARIMA, Prophet & LSTM appliqués à des données réelles.</p>
            https://github.com/SENECheikh🔗 Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)


# -------- EXPÉRIENCES --------
elif page == "💼 Expériences":
    st.markdown('<div class="section-title">💼 Expériences</div>', unsafe_allow_html=True)

    st.subheader("📌 CARSAT Nord-Est — Chargé d'Études Statistiques (2023–2025)")
    st.write("""
    - Développement d’un modèle prédictif (ML)  
    - Automatisation Python  
    - Application Streamlit  
    - Analyses statistiques avancées  
    """)

    st.markdown("---")

    st.subheader("📚 Projets Académiques — MSc Data Management")
    st.write("""
    - Data Science  
    - Économétrie  
    - Visualisation avancée  
    - Feature Engineering  
    """)

# -------- COMPÉTENCES --------
elif page == "🛠 Compétences":
    st.markdown('<div class="section-title">🛠 Compétences</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔹 Machine Learning")
        st.write("""
        - Régression, Classification  
        - NLP  
        - Time Series  
        - Évaluation & Interprétabilité  
        """)

        st.subheader("🔹 Outils")
        st.write("""
        - Python  
        - Git/GitHub  
        - SQL  
        - Streamlit  
        """)

    with col2:
        st.subheader("🔹 Visualisation")
        st.write("""
        - Plotly  
        - Seaborn  
        - Matplotlib  
        """)

        st.subheader("🔹 Statistiques")
        st.write("""
        - Inférentielle  
        - Tests statistiques  
        - Modèles linéaires  
        """)

# -------- CONTACT --------
elif page == "📞 Contact":
    st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)

    st.write("📧 Email : tonemail@example.com")
    st.write("🔗 LinkedIn : https://linkedin.com/in/xxxxx")
    st.write("💻 GitHub : https://github.com/SENECheikh")


# -------- FOOTER --------
st.markdown("""
<div class="footer">
    © 2026 • Portfolio réalisé avec Streamlit
</div>
""", unsafe_allow_html=True)