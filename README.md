# 📉 Análisis del Impacto Económico: Cierre de Cielo Manufacturing en Tizimín

Un análisis visual y basado en datos sobre el efecto dominó que dejó el cierre de la maquiladora Cielo Manufacturing en la economía local de Tizimín, Yucatán. 

Esta aplicación web interactiva está construida con **Streamlit** y busca dimensionar las pérdidas reales en empleos, salarios mensuales y el daño económico acumulado que afecta directamente a los negocios locales.

---

## 🔍 Hallazgos Principales

El reporte visualiza 5 puntos clave sobre la crisis local:

1. **La brecha de expectativas:** Se prometieron 330 empleos, pero solo promediaron 220. Una diferencia que desde el principio representó un costo invisible.
2. **El dinero que dejó de circular:** Una pérdida directa de **~1.5 millones de MXN al mes** correspondientes a la nómina neta de los trabajadores que se quedaron sin ingresos.
3. **El efecto multiplicador:** En una economía municipal, cada peso circula en restaurantes, transporte y mercados. El golpe real mensual (con un multiplicador de 1.5x) asciende a **más de 2.2 millones de MXN**.
4. **Una bomba de tiempo:** Simulador del daño acumulado mes a mes sin solución. En un año, la pérdida para Tizimín supera los **26 millones de pesos**.
5. **¿Dónde se siente el impacto?** Desglose del gasto familiar promedio (INEGI) para identificar los sectores económicos locales más perjudicados (alimentos, vivienda, transporte).

---

## 🛠️ Tecnologías Utilizadas

- **[Python 3](https://www.python.org/):** Lenguaje principal.
- **[Streamlit](https://streamlit.io/):** Creación de la interfaz web interactiva.
- **[Pandas](https://pandas.pydata.org/):** Limpieza, transformación y estructuración de los datos.
- **[Altair](https://altair-viz.github.io/):** Gráficos estadísticos declarativos y adaptables.
- **[Streamlit Extras](https://arnaudmiribel.github.io/streamlit-extras/):** Mejoras visuales (como `metric_cards` para indicadores resaltados).

---

## 🚀 Cómo ejecutar el proyecto localmente

Sigue estos pasos para correr la aplicación en tu computadora:

1. **Clona el repositorio:**
   ```bash
   git clone https://github.com/Wooz27/economic-impact-maquiladora-cielo-closure-tizimin.git
   cd economic-impact-maquiladora-cielo-closure-tizimin
   ```

2. **Crea un entorno virtual (opcional pero recomendado):**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En macOS/Linux:
   source venv/bin/activate
   ```

3. **Instala las dependencias necesarias:**
   *(Si aún no tienes un `requirements.txt`, puedes instalarlas manualmente)*
   ```bash
   pip install streamlit pandas altair streamlit-extras
   ```

4. **Ejecuta la app:**
   ```bash
   streamlit run main.py
   ```

La aplicación se abrirá automáticamente en tu navegador web en `http://localhost:8501`.

---

## 📊 Fuentes de Datos

- Notas de prensa e historial de empleos: **El Grillo de Yucatán, 2017**
- Distribución de gasto familiar promedio en México: **INEGI (Encuesta Nacional de Ingresos y Gastos de los Hogares, 2025)**
- Cálculo de efecto multiplicador: Estándar para economías municipales locales en México.
