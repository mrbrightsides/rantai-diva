import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="RANTAI DIVA",
    page_icon="💃",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/pwYe3ox.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **ETHIKA** adalah modul Ethics & Bias Checker yang dirancang untuk mendeteksi ketidakseimbangan dataset dan mengevaluasi fairness model secara sederhana dan interaktif. Modul ini tidak hanya memberikan flag dan indikator bias, tetapi juga mengedukasi mahasiswa dengan refleksi kritis tentang dampak sosial dan etis dari bias AI, menjadikan pembelajaran responsible AI lebih hidup dan kontekstual dalam ekosistem Web3.
    
    ---
    #### 🔮 Vision Statement
    
    Menjadi modul etika AI terpercaya yang memberdayakan mahasiswa dan pengembang untuk menciptakan model machine learning yang adil, bertanggung jawab, dan berakar pada nilai-nilai sosial, hukum, dan moral, guna membangun teknologi yang layak dan bermanfaat bagi semua lapisan masyarakat.

    ---
    ### 🧩 STC Ecosystem
    
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [DataHub](https://stc-data.streamlit.app/)

    ---
    ### ☂ RANTAI Communities
    
    1. [Learn3](https://learn3.streamlit.app/)
    2. [BlockPedia](https://blockpedia.streamlit.app/)
    3. [Diva](https://rantai-diva.streamlit.app/)
    4. [Nexus](https://rantai-nexus.streamlit.app/)
    5. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    6. [Business Intelligence](https://rantai-busi.streamlit.app/)
    7. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    8. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/rantai-diva)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

def embed_iframe(src, hide_top_px=72, height=800):
    components.html(f"""
    <div style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:{height + hide_top_px}px; border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>
    """, height=height)

# URL Ohara
iframe_url = "https://ohara.ai/mini-apps/4e2fb7dc-1821-43bb-afdc-be3db1d12b74"

# Panggil fungsi
embed_iframe(iframe_url, hide_top_px=110, height=800)
