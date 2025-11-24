import streamlit as st

st.set_page_config(page_title="Assistant pain levain", layout="centered")

st.title("🍞 Assistant pain au levain")

st.markdown(
    """
Recette de base (pour 1000 g de farine) :

- **Farine** : 1000 g  
- **Eau totale** : 800 g  
- **Levain** : 320 g  
- **Sel** : 22 g  

Hydratation ~80 %, levain à ~32 %, sel à ~2,2 %.
"""
)

# -----------------------------
# Paramètres de la recette
# -----------------------------

BASE_FLOUR = 1000  # g
BASE_WATER = 800   # g
BASE_LEVAIN = 320  # g
BASE_SALT = 22     # g

# Pour le levain (pour 1000 g de farine)
BASE_CHEF = 80
BASE_R1_FLOUR = 50
BASE_R1_WATER = 30
BASE_R2_FLOUR = 100
BASE_R2_WATER = 60

# Eau dans la pâte : 750 g au départ, le reste en bassinage
BASE_WATER_INITIAL = 750

st.sidebar.header("Paramètres")
flour_choice = st.sidebar.selectbox(
    "Quantité de farine (g)",
    [500, 1000, 1850, 2000, 3600],
    index=1,
    format_func=lambda x: f"{x} g"
)

# Facteur d'échelle (par rapport à la recette de base)
scale = flour_choice / BASE_FLOUR

# Ingrédients principaux
water_total = round(BASE_WATER * scale)
levain_total = round(BASE_LEVAIN * scale)
salt = round(BASE_SALT * scale)

water_initial = round(BASE_WATER_INITIAL * scale)
water_bassinage = water_total - water_initial

# Détails levain
chef = round(BASE_CHEF * scale)
r1_flour = round(BASE_R1_FLOUR * scale)
r1_water = round(BASE_R1_WATER * scale)
r2_flour = round(BASE_R2_FLOUR * scale)
r2_water = round(BASE_R2_WATER * scale)

st.markdown(f"## Ingrédients pour **{flour_choice} g** de farine")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Pâte finale")
    st.write(f"- 🧺 Farine : **{flour_choice} g**")
    st.write(f"- 💧 Eau totale FROIDE : **{water_total} g**")
    st.write(f"  - dont eau de départ : **{water_initial} g**")
    st.write(f"  - eau en bassinage : **{water_bassinage} g**")
    st.write(f"- 🧪 Levain prêt à l'emploi : **{levain_total} g**")
    st.write(f"- 🧂 Sel : **{salt} g**")

with col2:
    st.markdown("### Construction du levain")
    st.write(f"- Levain chef : **{chef} g**")
    st.write("1er rafraîchi :")
    st.write(f"  - Farine : **{r1_flour} g**")
    st.write(f"  - Eau : **{r1_water} g**")
    st.write("2ᵉ rafraîchi :")
    st.write(f"  - Farine : **{r2_flour} g**")
    st.write(f"  - Eau : **{r2_water} g**")
    st.info("Quand le levain est au **max de pousse**, tu comptes ~3 h à 27°C.")

st.markdown("---")
st.markdown("## Protocole détaillé")

st.markdown(
    f"""
### 1. Préparation du levain (à 27°C)

1. Prendre **{chef} g** de levain chef.
2. **1er rafraîchi**  
   - Ajouter **{r1_flour} g** de farine et **{r1_water} g** d'eau.  
   - Mélanger, laisser pousser **2–3 h** à ~27°C.
3. **2ᵉ rafraîchi**  
   - Ajouter **{r2_flour} g** de farine et **{r2_water} g** d'eau.  
   - Laisser pousser à nouveau jusqu'à ce que le levain soit **au maximum de sa pousse** (en pratique ~3 h à 27°C).

Tu dois obtenir environ **{levain_total} g** de levain prêt à l'emploi.

---

### 2. Mélange et pétrissage

1. Dans un grand bol, **mélanger le levain** (**{levain_total} g**) avec **{water_initial} g** d'eau.
2. Ajouter les **{flour_choice} g** de farine et pétrir jusqu'à obtenir une pâte homogène.
3. Ajouter le sel (**{salt} g**) et le **reste de l'eau** (**{water_bassinage} g**) en bassinage, petit à petit, jusqu'à absorption complète.

---

### 3. Pointage et froid

1. Faire quelques **rabats** pendant la première heure (toutes les 20–30 min par exemple).
2. Laisser la pâte encore reposer pour que la **1ʳᵉ heure** totale se fasse à ~27°C.
3. Mettre ensuite la pâte **au frigo** pour une fermentation lente, entre **12 et 18 h**.

---

### 4. Façonnage et apprêt

1. Sortir du frigo, **façonner directement** (miche, bâtard, etc.).
2. Laisser l'apprêt **2–3 h à 27°C**.

---

### 5. Cuisson en cocotte

1. Préchauffer le four avec la cocotte à **250–270°C** (au moins 30–45 min).
2. Déposer délicatement le pâton façonné dans la cocotte chaude, grigner.
3. **Cuisson :**
   - **30 min** avec couvercle à **250°C**.
   - Puis **30 min** sans couvercle à **220°C**.
4. Optionnel : laisser sécher quelques minutes four entrouvert si tu veux une croûte plus sèche.

---

Tu peux ajuster la liste des quantités de farine dans la barre latérale (500, 1000, 1850, 2000, 3600 g).  
Il suffit de modifier le tableau `[500, 1000, 1850, 2000, 3600]` dans le code pour coller à tes habitudes.
"""
)
