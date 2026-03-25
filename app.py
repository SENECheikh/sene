
import streamlit as st

# ------------------------------
# CONFIG PAGE
# ------------------------------
st.set_page_config(
    page_title="Portfolio - Cheikh SENE",
    page_icon="📊",
    layout="wide"
)

# ------------------------------
# CUSTOM STYLE
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
    margin-top: 40px;
    color: #2C2C2C;
}
.project-card {
    padding: 20px;
    border-radius: 10px;
    background-color: #F7F9FC;
    border: 1px solid #E2E6EB;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# SIDEBAR
# ------------------------------
st.sidebar.title("📌 Navigation")

page = st.sidebar.radio("Aller vers :", [
    "🏠 Accueil",
    "📚 Projets",
    "💼 Expériences",
    "🛠 Compétences",
    "📞 Contact"
])

# ------------------------------
# ACCUEIL
# ------------------------------
if page == "🏠 Accueil":
    st.markdown('<div class="big-title">Cheikh SENE</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Data Scientist • Machine Learning • IA • Statistique avancée</div>', unsafe_allow_html=True)

    st.write("""
    Bienvenue sur mon portfolio interactif.  
    Je suis passionné par la Data Science, le Machine Learning, les analyses statistiques 
    et la création de solutions intelligentes.
    """)

    st.success("👉 Explore mes projets, expériences et compétences via le menu à gauche !")

# ------------------------------
# PROJETS
# ------------------------------
elif page == "📚 Projets":
    st.markdown('<div class="section-title">📚 Mes Projets</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
    <h3>Modélisation prédictive du risque financier – CARSAT Nord-Est</h3>
    <p>Modèles XGBoost, Random Forest, preprocessing, analyse des risques, dashboard complet.</p>
    <a href="https://github.com/SENECheikh" target="_blank">🔗 Voir sur GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
    <h3>Application Streamlit de pilotage statistique</h3>
    <p>Dashboard interactif avec filtres dynamiques, graphiques et indicateurs clés.</p>
    <a href="https://github.com/SENECheikh" target="_blank">🔗 Voir sur GitHub</a>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="project-card">
    <h3>Projets Machine Learning (NLP, Classification, Forecasting)</h3>
    <p>Ensemble de notebooks ML démontrant mes compétences Python + Data Science.</p>
    <a href="https://github.com/SENECheikh" target="_blank">🔗 Voir sur GitHub</a>
    </div>
    """, unsafe_allow_html=True)

# ------------------------------
# EXPÉRIENCES
# ------------------------------
elif page == "💼 Expériences":
    st.markdown('<div class="section-title">💼 Mes Expériences</div>', unsafe_allow_html=True)

    st.subheader("📌 CARSAT Nord-Est — Chargé d'Études Statistiques (2023–2025)")
    st.write("""
    - Modélisation prédictive  
    - Statistiques avancées  
    - Automatisations Python  
    - Application Streamlit  
    - Études d’impact financier  
    """)

    st.markdown("---")

    st.subheader("📘 Projets Académiques – MSc Data Management / CEPOPP")
    st.write("""
    - Machine Learning supervisé & non supervisé  
    - Visualisation avancée  
    - Feature Engineering  
    - Économétrie appliquée  
    """)

# ------------------------------
# COMPÉTENCES
# ------------------------------
elif page == "🛠 Compétences":
    st.markdown('<div class="section-title">🛠 Compétences</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🔹 Machine Learning")
        st.write("""
        - Régression  
        - Classification  
        - NLP  
        - Séries temporelles  
        """)

        st.subheader("🔹 Outils & Langages")
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
        - Matplotlib  
        - Seaborn  
        """)

        st.subheader("🔹 Autres")
        st.write("""
        - Statistiques  
        - Feature Engineering  
        - Nettoyage de données  
        """)

# ------------------------------
# CONTACT
# ------------------------------
elif page == "📞 Contact":
    st.markdown('<div class="section-title">📞 Contact</div>', unsafe_allow_html=True)

    st.write("📧 Email : tonemail@example.com")
    st.write("🔗 LinkedIn : https://linkedin.com/in/xxxx")
    st.write("💻 GitHub : https://github.com/SENECheikh")

    st.success("Merci de visiter mon portfolio 🙌")
