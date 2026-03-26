
import streamlit as st

# ----------------------- CONFIG -----------------------
st.set_page_config(
    page_title="Portfolio - Cheikh SENE",
    page_icon="📊",
    layout="wide"
)

# ----------------------- CSS -----------------------
st.markdown("""
<style>

body {
    background-color: #F5F7FA;
    font-family: 'Segoe UI', Roboto, sans-serif;
}

/* HERO */
.hero {
    padding: 70px;
    background: linear-gradient(135deg, #2C6AFF 0%, #3B8DFF 100%);
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 50px;
}
.hero h1 {
    font-size: 55px;
    font-weight: 900;
}
.hero h3 {
    font-size: 22px;
    font-weight: 300;
}

/* SECTION TITLES */
.section-title {
    font-size: 36px;
    font-weight: 800;
    margin-top: 40px;
    margin-bottom: 20px;
}

/* CARD STYLE */
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
    box-shadow: 0 10px 22px rgba(0,0,0,0.10);
}
.card h4 {
    font-size: 22px;
    margin-bottom: 8px;
}

/* FOOTER */
.footer {
    margin-top: 70px;
    padding: 25px;
    text-align: center;
    opacity: 0.6;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------- SIDEBAR -----------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Menu :",
    ["🏠 Accueil", "📚 Projets", "💼 Expériences", "🎓 Formations", "🛠 Compétences", "📞 Contact"]
)

# ----------------------- ACCUEIL -----------------------
if page == "🏠 Accueil":

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("cheikh.png", width=260)

    with col2:
        st.markdown("""
            <div class="hero">
                <h1>Cheikh SENE</h1>
                <h3>Data Scientist • Chargé d'Études Statistiques</h3>
            </div>
        """, unsafe_allow_html=True)

        st.write("""
        Bienvenue sur mon portfolio professionnel.  
        Je suis spécialisé en **Data Science**, **Machine Learning**, **Statistiques avancées**,  
        ainsi que dans la **visualisation de données et le reporting décisionnel**.
        """)

# ----------------------- PROJETS -----------------------
elif page == "📚 Projets":
    st.markdown('<div class="section-title">📚 Mes Projets</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <h4>Modélisation prédictive du risque financier</h4>
            <p>Projet ML réalisé à la CARSAT Nord‑Est : Random Forest, XGBoost, Streamlit App.</p>
            ⭐ Priorisation des contrôles et réduction du risque.
            <br><a href="https://github.com/SENECheikh">Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h4>NLP – Classification de textes</h4>
            <p>Vectorisation, TF‑IDF, pipelines ML, modèles avancés.</p>
            <a href="https://github.com/SENECheikh">Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <h4>Dashboard statistique dynamique</h4>
            <p>Indicateurs, visualisations et exploration interactive.</p>
            <a href="https://github.com/SENECheikh">Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card">
            <h4>Time Series Forecasting</h4>
            <p>ARIMA, Prophet & LSTM appliqués à des données réelles.</p>
            <a href="https://github.com/SENECheikh">Voir sur GitHub</a>
        </div>
        """, unsafe_allow_html=True)

# ----------------------- EXPÉRIENCES -----------------------
elif page == "💼 Expériences":
    st.markdown('<div class="section-title">💼 Expériences</div>', unsafe_allow_html=True)

    st.subheader("📌 CARSAT Nord‑Est — Chargé d'Études Statistiques (2023–2025)")
    st.write("""
    - Analyses statistiques : performance, qualité, risque  
    - Automatisation : Python, SQL, Excel  
    - Tableaux de bord Power BI & reporting décisionnel  
    - Nettoyage, extraction et fiabilisation des données  
    - Production d'indicateurs clés pour les directions métier  
    """)

    st.subheader("📌 Projet de fin d’études — Modélisation prédictive (2025)")
    st.write("""
    - Modèle prédictif du **risque financier des dossiers**  
    - Sélection de variables, interprétation, importance des features  
    - Déploiement d’un outil Streamlit pour les contrôleurs  
    - Gains : meilleure priorisation, maîtrise du risque, gain de temps  
    """)

# ----------------------- FORMATIONS -----------------------
elif page == "🎓 Formations":
    st.markdown('<div class="section-title">🎓 Formations</div>', unsafe_allow_html=True)

    st.subheader("🎓 MSc Data Management — Aivancity Paris (2023–2025)")
    st.write("""
    - Machine Learning, Big Data, Cloud Azure  
    - Databricks, DataViz, Éthique & gouvernance des données  
    """)

    st.subheader("🎓 Master 2 – Économie Appliquée — Université de Lille (2021–2023)")
    st.write("""
    - Économétrie : panel, séries temporelles  
    - Statistiques avancées et politiques publiques  
    """)

# ----------------------- COMPÉTENCES -----------------------
elif page == "🛠 Compétences":
    st.markdown('<div class="section-title">🛠 Compétences</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🤖 Machine Learning")
        st.write("""
        - Régression, Classification  
        - NLP  
        - Séries temporelles  
        - Interprétabilité des modèles  
        """)

        st.subheader("🧰 Outils & Développement")
        st.write("""
        - Python (pandas, numpy, sklearn, statsmodels)  
        - SQL  
        - Git / GitHub  
        - Streamlit  
        """)

    with col2:
        st.subheader("📊 Visualisation & BI")
        st.write("""
        - Power BI (DAX, dashboards dynamiques)  
        - Excel avancé  
        - Matplotlib, Seaborn, Plotly  
        """)

        st.subheader("📈 Statistiques & Économétrie")
        st.write("""
        - Tests statistiques  
        - Modèles linéaires  
        - Données de panel  
        """)

# ----------------------- CONTACT -----------------------
elif page == "📞 Contact":
    st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)

    st.write("📧 Email : senecheikh31@gmail.com")
    st.write("📱 Téléphone : 06 52 75 68 61")
    st.write("📍 Localisation : Nancy / France entière")
    st.write("💼 LinkedIn : https://linkedin.com/in/xxxxx")
    st.write("💻 GitHub : https://github.com/SENECheikh")

    # Bouton pour télécharger le CV
    with open("CV_Cheikh_SENE.pdf", "rb") as cv_file:
        st.download_button(
            label="📄 Télécharger mon CV",
            data=cv_file,
            file_name="CV_Cheikh_SENE.pdf",
            mime="application/pdf"
        )

# ----------------------- FOOTER -----------------------
st.markdown("""
    <div class="footer">
        © 2026 • Portfolio réalisé avec Streamlit
    </div>
""", unsafe_allow_html=True)
