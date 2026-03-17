# 📉 ¿Está en recesión Tizimín? El impacto económico del cierre de Cielo Manufacturing

> *Este proyecto nació de una pregunta incómoda: ¿por qué ningún negocio de Tizimín tenía vacantes?*

---

## ¿Por qué existe este proyecto?

Todo empezó con **Landa** — una plataforma web de empleos que construí para conectar negocios locales con personas en búsqueda de trabajo en Tizimín, Yucatán.

Contacté a más de 200 negocios: 20 de forma física y el resto por WhatsApp. El resultado fue desconcertante — ninguno tenía vacantes. Cero.

Al visitar el centro de la ciudad en viernes de quincena, el panorama era desolador: restaurantes vacíos, negocios sin clientes, calles sin el movimiento que debería tener una ciudad en día de pago.

La pregunta inicial cambió: el problema no era Landa. Era algo más grande.

---

## La hipótesis

En diciembre de 2024, el gobierno federal publicó un decreto que incrementó aranceles hasta el 35% para prendas confeccionadas provenientes de países sin tratado comercial con México, además de ampliar las restricciones al programa IMMEX que regula a las maquiladoras. Esto golpeó a la industria maquiladora en todo el país.

Para Tizimín — una ciudad con una economía históricamente débil y dependiente de pocas fuentes de empleo formal — el golpe fue devastador. **Cielo Manufacturing**, la principal maquiladora local, cerró operaciones dejando a 220 familias sin ingreso directo.

Los comerciantes locales que entrevisté atribuyeron la caída de sus ventas a "la cuesta de enero". Tenían razón en el síntoma, pero no en la causa. Era algo más profundo: **una contracción de mercado**.

**Hipótesis:** El cierre de Cielo Manufacturing retiró aproximadamente 1.5 millones de pesos mensuales del circuito económico de Tizimín, generando un efecto dominó que se siente en todos los sectores — desde el restaurante del centro hasta la farmacia de la esquina.

---

## Metodología

Este análisis combina tres tipos de evidencia:

**1. Investigación periodística**
Revisé notas de El Grillo de Yucatán, Diario de Yucatán y Revista Yucatán para reconstruir la historia de Cielo Manufacturing: su apertura, promesas de empleo, y cierre.

**2. Datos públicos**
- Cifras de empleo: reportes periodísticos de la inauguración (2017)
- Distribución del gasto familiar: ENIGH 2024, INEGI (publicada julio 2025)
- Efecto multiplicador: estimación estándar para economías municipales en México (1.5x)

**3. Observación de campo**
Visité físicamente 20 negocios del centro de Tizimín y contacté a más de 180 adicionales por WhatsApp. Ninguno reportó vacantes activas. En una visita a un restaurante del centro en viernes de quincena, se registraron **0 mesas ocupadas** a las 8-9 PM — una anomalía estadística clara en el día de mayor consumo del mes.

---

## Limitaciones del análisis

Ser honesto con los datos es parte del trabajo:

- **Tizimín no tiene datos municipales públicos confiables.** No existe un registro abierto de empleo formal a nivel municipal. Los datos del IMSS están disponibles solo a nivel estatal.
- **Los cálculos de nómina son estimaciones.** Se basan en el salario promedio reportado en prensa, no en registros oficiales de la empresa.
- **El multiplicador de 1.5x es una aproximación.** Es el rango típico para economías municipales pequeñas en México, pero no existe un cálculo específico para Tizimín.
- **La muestra de campo es pequeña.** 20 visitas físicas no son estadísticamente representativas, pero son evidencia directa y documentada.

Estas limitaciones no invalidan el análisis — lo contextualizan. El objetivo no es precisión milimétrica, sino dimensionar un problema real con los datos disponibles.

---

## 🛠️ Tecnologías utilizadas

| Herramienta | Uso |
|---|---|
| Python 3 | Lenguaje principal |
| Streamlit | Interfaz web interactiva |
| Pandas | Estructuración y cálculo de datos |
| Altair | Visualizaciones estadísticas |
| Streamlit Extras | Componentes visuales adicionales |

---

## 🚀 Cómo ejecutar el proyecto

```bash
git clone https://github.com/Wooz27/economic-impact-maquiladora-cielo-closure-tizimin.git
cd economic-impact-maquiladora-cielo-closure-tizimin
pip install streamlit pandas altair streamlit-extras
streamlit run main.py
```

La app abre en `http://localhost:8501`.

---

## 📚 Referencias

- Grillo de Yucatán. (2017). *La nueva maquiladora Cielo Manufacturing genera 220 empleos en Tizimín*. https://grillodeyucatan.com/2017/05/06/la-nueva-maquiladora-cielo-manufacturing-genera-220-empleos-en-tizimin/

- Revista Yucatán. (2017). *Inauguran maquiladora en Tizimín*. https://www.revistayucatan.com/v1/noticias/inauguran-maquiladora-en-tizimin/

- INEGI. (2025). *Encuesta Nacional de Ingresos y Gastos de los Hogares 2024 (ENIGH) — Presentación de resultados*. https://www.inegi.org.mx/contenidos/programas/enigh/nc/2024/doc/enigh2024_ns_presentacion_resultados.pdf

- Diario de Yucatán. (2023). *Temen cierre de maquiladora en Tizimín*. "https://www.yucatan.com.mx/mexico/2024/12/26/empresas-textiles-alertan-cierre-masivo-por-decreto-de-claudia-sheinbaum-que-dice.html"

- Gobierno de México. (2024, diciembre). *Decreto de aranceles a textiles y modificaciones al programa IMMEX*. Diario Oficial de la Federación.

---

## Sobre este proyecto

Soy estudiante de ciencia de datos en Tizimín, Yucatán. Este análisis forma parte de mi portafolio personal — un intento de aplicar herramientas de datos reales a problemas reales de mi ciudad.

Si tienes datos, correcciones o quieres colaborar, puedes contactarme a través de GitHub.