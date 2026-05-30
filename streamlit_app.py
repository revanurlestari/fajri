import streamlit as st

# =====================================
# CONFIG
# =====================================
st.set_page_config(
    page_title="ThermoVerse",
    page_icon="🌌",
    layout="wide"
)

# =====================================
# CSS FUTURISTIK SUPER UPGRADE (UPDATED COLORS)
# =====================================
st.markdown("""
<style>

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* BACKGROUND (Diubah dari biru ke kombinasi ungu-gelap/magenta) */
.stApp {
    background: linear-gradient(-45deg, #020617, #1e1b4b, #0f172a, #581c87, #3b0764);
    background-size: 500% 500%;
    animation: gradientBG 18s ease infinite;
    color:white;
}

/* ANIMASI BACKGROUND */
@keyframes gradientBG {
    0% {background-position:0% 50%;}
    50% {background-position:100% 50%;}
    100% {background-position:0% 50%;}
}

/* TITLE (Tetap dipertahankan sesuai permintaan) */
.title {
    text-align:center;
    font-size:68px;
    font-weight:900;
    background: linear-gradient(to right,#93c5fd,#dbeafe,#60a5fa);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    text-shadow:0 0 30px rgba(59,130,246,.8);
    animation: floatTitle 3s ease-in-out infinite;
}

@keyframes floatTitle {
    0% {transform:translateY(0px);}
    50% {transform:translateY(-8px);}
    100% {transform:translateY(0px);}
}

.subtitle {
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:35px;
}

/* RESULT CARD */
.result {
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    color:white;
    padding:25px;
    border-radius:22px;
    border:1px solid rgba(255,255,255,0.15);
    box-shadow:0 8px 40px rgba(0,0,0,.35);
    animation: fadeIn 0.7s ease;
    margin-top:20px;
}

/* FADE */
@keyframes fadeIn {
    from {
        opacity:0;
        transform:translateY(20px);
    }
    to {
        opacity:1;
        transform:translateY(0);
    }
}

/* BUTTON (Diubah ke gradasi Ungu ke Pink/Magenta Neon) */
.stButton>button {
    width:100%;
    padding:15px;
    border-radius:18px;
    font-weight:700;
    font-size:16px;
    border:none;
    color:white;
    background: linear-gradient(135deg, #7c3aed, #d946ef);
    box-shadow:0 0 18px rgba(217, 70, 239, 0.5);
    transition:all .3s ease;
}

.stButton>button:hover {
    transform:translateY(-6px) scale(1.02);
    box-shadow:0 0 30px rgba(217, 70, 239, 0.9);
}

/* INPUT */
.stNumberInput input,
.stTextInput input {
    background: rgba(255,255,255,0.08) !important;
    color:black !important;
    border-radius:15px !important;
}

/* LATEX (Diubah ke warna ungu muda/pink pastel soft) */
.katex {
    color:#f5d0fe !important;
    font-size:24px !important;
}

/* INFO BOX */
.stAlert {
    border-radius:18px;
}

/* HEADER (Diubah ke warna ungu muda/pink pastel soft) */
h1,h2,h3 {
    color:#f5d0fe;
}

</style>
""", unsafe_allow_html=True)

# =====================================
# SESSION
# =====================================
if "menu" not in st.session_state:
    st.session_state.menu = None

menu_list = [
    "Hukum 1 Termodinamika",
    "Usaha",
    "Kalor",
    "Entalpi",
    "Hukum Hess",
    "ΔH Reaksi",
    "Energi Gibbs",
    "Entropi",
    "Gas Ideal",
    "Gas Nyata"
]

# =====================================
# HOME
# =====================================
if st.session_state.menu is None:

    st.snow()

    st.markdown("<div class='title'>🌌 ThermoVerse ⚗️</div>", unsafe_allow_html=True)

    st.markdown(
        "<div class='subtitle'>Kalkulator Termodinamika Futuristik + Langkah Penyelesaian Interaktif</div>",
        unsafe_allow_html=True
    )

    cols = st.columns(2)

    for i, m in enumerate(menu_list):
        with cols[i % 2]:
            if st.button(f"⚡ {m}"):
                st.session_state.menu = m
                st.rerun()

# =====================================
# CALCULATOR PAGE
# =====================================
else:

    menu = st.session_state.menu

    if st.button("⬅️ Kembali"):
        st.session_state.menu = None
        st.rerun()

    st.header(f"⚗️ {menu}")
    st.divider()

    # =====================================
    # 1 HUKUM 1 TERMODINAMIKA
    # =====================================
    if menu == "Hukum 1 Termodinamika":

        st.info("""
Hukum 1 Termodinamika menyatakan bahwa energi tidak dapat diciptakan maupun dimusnahkan,
melainkan hanya berubah bentuk.
""")

        st.latex(r"\Delta U = Q - W")

        Q = st.number_input("Q (kJ)", value=0.0)
        W = st.number_input("W (kJ)", value=0.0)

        if st.button("Hitung"):
            hasil = Q - W

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            <b>Rumus:</b><br>
            ΔU = Q − W <br><br>

            <b>Diketahui:</b><br>
            Q = {Q} kJ<br>
            W = {W} kJ<br><br>

            <b>Substitusi:</b><br>
            ΔU = {Q} − {W}<br><br>

            <b>Hasil:</b><br>
            ΔU = <b>{hasil:.3f} kJ</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 2 USAHA
    # =====================================
    elif menu == "Usaha":

        st.info("""
Usaha dalam termodinamika adalah energi yang digunakan sistem
untuk melakukan kerja akibat perubahan volume.
""")

        st.latex(r"W = P \cdot \Delta V")

        P = st.number_input("P (Pa)", value=0.0)
        dV = st.number_input("ΔV (m³)", value=0.0)

        if st.button("Hitung"):

            hasil = P * dV

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            W = P × ΔV <br><br>

            P = {P} Pa<br>
            ΔV = {dV} m³<br><br>

            W = {P} × {dV}<br><br>

            W = <b>{hasil:.3f} J</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 3 KALOR
    # =====================================
    elif menu == "Kalor":

        st.info("""
Kalor adalah energi panas yang berpindah dari benda bersuhu tinggi
ke benda bersuhu rendah.
""")

        st.latex(r"Q = m c \Delta T")

        m = st.number_input("m (g)", value=0.0)
        c = st.number_input("c (J/g°C)", value=0.0)
        dT = st.number_input("ΔT (K)", value=0.0)

        if st.button("Hitung"):

            hasil = m * c * dT

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            Q = m × c × ΔT <br><br>

            m = {m} g<br>
            c = {c} J/g·K<br>
            ΔT = {dT} K<br><br>

            Q = {m} × {c} × {dT}<br><br>

            Q = <b>{hasil:.3f} J</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 4 ENTALPI
    # =====================================
    elif menu == "Entalpi":

        st.info("""
Entalpi adalah total energi panas dalam suatu sistem
pada tekanan tetap.
""")

        st.latex(r"\Delta H = \Delta U + \Delta nRT")

        dU = st.number_input("ΔU", value=0.0)
        dn = st.number_input("Δn", value=0.0)
        T = st.number_input("T (K)", value=0.0)

        R = 0.008314

        if st.button("Hitung"):

            hasil = dU + dn * R * T

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            ΔH = ΔU + ΔnRT <br><br>

            ΔU = {dU}<br>
            Δn = {dn}<br>
            T = {T} K<br>
            R = 0.008314<br><br>

            ΔH = {dU} + ({dn} × 0.008314 × {T})<br><br>

            ΔH = <b>{hasil:.3f} kJ</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 5 HUKUM HESS
    # =====================================
    elif menu == "Hukum Hess":

        st.info("""
Hukum Hess menyatakan bahwa perubahan entalpi total
tidak bergantung pada jalur reaksi.
""")

        st.latex(r"\Delta H = \sum \Delta H")

        data = st.text_input("Masukkan ΔH (pisah koma)", "10,-20,30")

        if st.button("Hitung"):

            arr = [float(x) for x in data.split(",")]

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            Data ΔH = {arr}<br><br>

            ΣΔH = <b>{sum(arr):.3f} kJ</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 6 ΔH REAKSI
    # =====================================
    elif menu == "ΔH Reaksi":

        st.info("""
ΔH reaksi menunjukkan perubahan kalor selama reaksi kimia berlangsung.
""")

        st.latex(r"\Delta H = \sum Hf_{produk} - \sum Hf_{reaktan}")

        p = st.text_input("Produk")
        r = st.text_input("Reaktan")

        if st.button("Hitung") and p and r:

            p = [float(x) for x in p.split(",")]
            r = [float(x) for x in r.split(",")]

            hasil = sum(p) - sum(r)

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            ΣProduk = {sum(p)}<br>
            ΣReaktan = {sum(r)}<br><br>

            ΔH = <b>{hasil:.3f} kJ/mol</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 7 ENERGI GIBBS
    # =====================================
    elif menu == "Energi Gibbs":

        st.info("""
Energi Gibbs digunakan untuk menentukan apakah suatu reaksi
berlangsung spontan atau tidak.
""")

        st.latex(r"\Delta G = \Delta H - T\Delta S")

        dH = st.number_input("ΔH", value=0.0)
        T = st.number_input("T", value=0.0)
        dS = st.number_input("ΔS", value=0.0)

        if st.button("Hitung"):

            hasil = dH - T * dS

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            ΔG = ΔH − TΔS <br><br>

            ΔH = {dH}<br>
            T = {T}<br>
            ΔS = {dS}<br><br>

            ΔG = <b>{hasil:.3f} kJ</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 8 ENTROPI
    # =====================================
    elif menu == "Entropi":

        st.info("""
Entropi adalah ukuran tingkat ketidakteraturan suatu sistem.
""")

        st.latex(r"\Delta S = Q/T")

        Q = st.number_input("Q", value=0.0)
        T = st.number_input("T", value=0.0)

        if st.button("Hitung"):

            if T == 0:
                st.error("T tidak boleh 0")

            else:

                hasil = Q / T

                st.balloons()

                st.markdown(f"""
                <div class='result'>

                <h3>Langkah Penyelesaian</h3>

                ΔS = Q / T <br><br>

                Q = {Q}<br>
                T = {T}<br><br>

                ΔS = <b>{hasil:.3f} kJ/K</b>

                </div>
                """, unsafe_allow_html=True)

    # =====================================
    # 9 GAS IDEAL
    # =====================================
    elif menu == "Gas Ideal":

        st.info("""
Gas ideal adalah model gas teoritis yang partikel-partikelnya
tidak memiliki gaya tarik dan tumbukannya elastis sempurna.
""")

        st.latex(r"PV = nRT")

        n = st.number_input("n", value=0.0)
        T = st.number_input("T", value=0.0)
        V = st.number_input("V", value=0.0)

        R = 0.0821

        if st.button("Hitung"):

            P = (n * R * T) / V if V != 0 else 0

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            P = nRT / V <br><br>

            n = {n}<br>
            T = {T}<br>
            V = {V}<br>
            R = 0.0821<br><br>

            P = <b>{P:.3f} atm</b>

            </div>
            """, unsafe_allow_html=True)

    # =====================================
    # 10 GAS NYATA
    # =====================================
    elif menu == "Gas Nyata":

        st.info("""
Gas nyata adalah gas yang memperhitungkan volume partikel
dan gaya tarik antar molekul.
""")

        st.latex(r"(P+\frac{an^2}{V^2})(V-nb)=nRT")

        n = st.number_input("n", value=0.0)
        T = st.number_input("T", value=0.0)
        V = st.number_input("V", value=0.0)
        a = st.number_input("a", value=0.0)
        b = st.number_input("b", value=0.0)

        if st.button("Hitung"):

            R = 0.0821

            P = ((n * R * T) / (V - n * b)) - ((a * n**2) / (V**2))

            st.balloons()

            st.markdown(f"""
            <div class='result'>

            <h3>Langkah Penyelesaian</h3>

            Persamaan Van der Waals<br><br>

            P = <b>{P:.3f} atm</b>

            </div>
            """, unsafe_allow_html=True)
