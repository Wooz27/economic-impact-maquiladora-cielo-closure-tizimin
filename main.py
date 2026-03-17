import streamlit as st 
import pandas as pd 
import altair as alt
from streamlit_extras.metric_cards import style_metric_cards

# ==========================================
# FUNCIONES AUXILIARES
# ==========================================
def fmt_moneda(valor):
    return f"${valor:,.0f}"

# ==========================================
# FUNCIÓN PRINCIPAL DE LA APP
# ==========================================
def main():

    # Configuración de página de Streamlit
    st.set_page_config(
        page_title="El cierre de Cielo Manufacturing: ¿está en recesión Tizimín?",
        page_icon="📉",
        layout="centered",
    )

    # ==========================================
    # VARIABLES BASE Y CÁLCULOS PRINCIPALES
    # Cifras usadas a lo largo de todo el análisis
    # ==========================================

    # Cifras de empleo y economía
    trabajadores_prometidos=int(330)
    trabajadores_maximos = int(270)
    trabajadores_reales = int(220)
    sueldo_promedio = 8000
    descuentos_estimado = 0.15
    multiplicador_derrama = 1.5
    
    # Cálculos derivados
    descuento_por_t = sueldo_promedio * descuentos_estimado
    sueldo_por_t = sueldo_promedio - descuento_por_t
    sueldo_total_mensual = trabajadores_reales * sueldo_por_t
    perdida_con_derrama_mensual = sueldo_total_mensual * multiplicador_derrama
    perdida_con_derrama_anual = perdida_con_derrama_mensual * 12

    #consumo por familia segun el Innegi 2025: https://www.inegi.org.mx/contenidos/programas/enigh/nc/2024/doc/enigh2024_ns_presentacion_resultados.pdf
    alimentos_bebidas_tabaco = 37.7
    transporte_comunicaciones = 19.5
    educación_esparcimiento = 9.6   
    vivienda_servicios = 9.1
    cuidados_personales = 7.8
    enseres_domésticos = 6.3
    vestido_calzado= 3.8
    salud = 3.4
    otros = 2.4





    # ==========================================
    # ENCABEZADO Y DESCRIPCIÓN CONTEXTUAL
    # ==========================================
    st.title("El cierre de Cielo Manufacturing: ¿está en recesión Tizimín?")
    st.write("")
    st.markdown("""🚨 **No es solo una maquiladora vacía.** Es un golpe directo al bolsillo de todo Tizimín.
    Hablamos de casi **1.5 millones de pesos mensuales** que desaparecieron de golpe de restaurantes, farmacias, mercados y transporte.
    Desliza para ver el verdadero efecto dominó 👇""")


    # ==========================================
    # SECCIÓN 1: BRECHA DE EMPLEOS PROMETIDOS VS REALES
    # Compara visualmente los empleos prometidos, máximos y reales.
    # ==========================================
    st.divider()

    st.subheader("1. Lo prometido vs lo real")
    st.markdown("""
    📉 **Promesas que se quedaron cortas.** Se anunciaron 330 empleos con bombo y platillo.
    ¿La realidad? Solo promediaron 220. Esa brecha de 110 empleos fantasma fue el primer costo invisible para la ciudad.
    """)

    #Tabla y gráfica
    df = pd.DataFrame({
        "Clasificación": ["Prometidos", "Máximos", "Reales"],
        "Total de trabajadores": [trabajadores_prometidos, trabajadores_maximos, trabajadores_reales],
    })

    df = df.sort_values(by="Total de trabajadores", ascending=True)
    print(df)

    #grafica de altair
    grafica_cap = alt.Chart(df).mark_bar().encode(
        x = alt.X("Clasificación", sort='y', axis=alt.Axis(labelAngle=0)),
        y = alt.Y ("Total de trabajadores")
    )

    st.altair_chart(grafica_cap, width="stretch")

    st.caption("Fuente: El Grillo de Yucatán, 2017.")

    st.divider()
    # ==========================================
    # SECCIÓN 2: EL DINERO QUE DEJÓ DE CIRCULAR
    # Muestra los cálculos de sueldos netos y la nómina total mensual.
    # ==========================================
    
    st.subheader("2. El dinero que dejó de circular")

    st.markdown("""
    💸 **La llave que se cerró.** Con ingresos netos de unos 6,800 MXN por trabajador,
    la nómina inyectaba cerca de **1,496,000 MXN mensuales** directo a la ciudad.
    Ese es el efectivo que literalmente dejó de llegar a las manos de los comerciantes locales.
    """)
    st.write("")
    col1,col2,col3,col4 = st.columns([1,1,1,1.3])

    col1.metric(label="Sueldo Bruto", value=fmt_moneda(sueldo_promedio))
    col2.metric(label="Descuento Estimado", value=f"{descuentos_estimado*100}%")
    col3.metric(label="Sueldo Neto", value=fmt_moneda(sueldo_por_t))
    col4.metric(label="Nómina Mensual", value=fmt_moneda(sueldo_total_mensual))
    style_metric_cards(
        background_color="#4F4F4F",
        box_shadow = True,
        border_color = "#ffffff",
        border_radius_px= 20,
        border_size_px= 2,

        )

    st.caption("Fuente: Cálculos propios basados en datos de El Grillo de Yucatán, 2017.")
    st.divider()


    # ==========================================
    # SECCIÓN 3: EFECTO MULTIPLICADOR DE LA DERRAMA
    # Explica cómo la circulación de dinero incrementa el daño económico.
    # ==========================================
    
    st.subheader("3. El efecto multiplicador: por qué el daño es mayor de lo que aparenta")
    st.markdown(f"""
    🔄 **El efecto dominó.** Un billete no se queda quieto: el trabajador paga las tortillas 🌯, el de la tienda le paga al proveedor 🚚, y así sigue la cadenita.

    <div style="color: inherit;">
    Por eso, el golpe real para Tizimín no es de {fmt_moneda(sueldo_total_mensual)},
    sino que se dispara a <b>{fmt_moneda(sueldo_total_mensual * multiplicador_derrama)} mensuales</b>. 
    </div>
    ¡Todos acabamos perdiendo!
    """, unsafe_allow_html=True)

    df_derrama = pd.DataFrame({
        "Concepto":["Impacto Directo", "Impacto total con derrama"],
        "monto": [sueldo_total_mensual, sueldo_total_mensual * multiplicador_derrama],
        "color": ["#eff780", "#ff160e"]
    })

    grafica_derrama = alt.Chart(df_derrama).mark_bar().encode(
        x = alt.X("Concepto", sort='y', axis=alt.Axis(labelAngle=0)),
        y = alt.Y("monto", axis=alt.Axis(title="Monto en MXN")),
        color= alt.Color("color:N", scale=None, legend=None, )
    )
    st.altair_chart(grafica_derrama, width="stretch")

    st.caption("Fuente: Cálculos propios basados en datos de El Grillo de Yucatán, 2017 y multiplicadores típicos para economías municipales en México.")

    st.divider()    
    # ==========================================
    # SECCIÓN 4: EL DAÑO ACUMULADO A LO LARGO DEL TIEMPO
    # Muestra cómo el impacto económico crece mes a mes sin solución.
    # ==========================================

    st.subheader("4. El daño acumulado a lo largo del tiempo")
    st.markdown("""
    ⏳ **Una bomba de tiempo.** El problema no terminó el día que apagaron las máquinas.
    Cada mes que pasa sin recuperar esos empleos, el hoyo económico crece.
    Mira cómo se acumula la pérdida en un año sin soluciones:
                """)
    
    df_meses= pd.DataFrame({
        "meses desde el cierre": ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
        "impacto_acumulado": [sueldo_total_mensual * multiplicador_derrama * (i+1) for i in range(12)]
    })

    grafica_mes = alt.Chart(df_meses).mark_line(point=True).encode(
        x = alt.X("meses desde el cierre:O",sort='y', axis=alt.Axis(labelAngle=0), ),
        y = alt.Y("impacto_acumulado", axis=alt.Axis(title="Millones perdidos"))
    )
    st.altair_chart(grafica_mes, width="stretch")

    col1, col2,col3 = st.columns([1.3,1.3,1.1])

    col1 = col1.metric(label="Impacto acumulado a 6 meses", value=fmt_moneda(df_meses["impacto_acumulado"][5]))
    col2 = col2.metric(label="Impacto acumulado a 12 meses", value=fmt_moneda(df_meses["impacto_acumulado"][11]))
    col3.markdown("""
    💥 **En un año sin solución, el daño económico para Tizimín superaría los 26 millones de pesos.**
    """)
    st.divider()
    # ==========================================
    # SECCIÓN 5: ¿DÓNDE SE SIENTE EL IMPACTO?
    # ==========================================

    st.subheader("5. ¿Dónde se siente el impacto?")

    st.markdown("""
    🛒 **¿A qué tipo de negocios les pega más fuerte?** 
    Cuando las familias se quedan sin empleo, los recortes afectan a todos los sectores. Según el INEGI (2025), así se divide el presupuesto de un hogar en porcentajes. 
    
    *En otras palabras: de cada 100 pesos que los ex-trabajadores dejaron de gastar, así se repartía la pérdida entre los negocios locales:*
    """)
    df_gastos = pd.DataFrame({
        "Gastos":["Alimentos, bebidas y tabaco", 
                  "Transporte y comunicaciones", "Educación y esparcimiento",
                  "Vivienda y servicios", "Cuidados personales", "Enseres domésticos", "Vestido y calzado", "Salud", "Otros"],
        "Porcentaje": [alimentos_bebidas_tabaco, transporte_comunicaciones,
                        educación_esparcimiento, vivienda_servicios, cuidados_personales, enseres_domésticos, vestido_calzado, salud, otros]
        
    })

    grafica_gastos = alt.Chart(df_gastos).mark_arc().encode(
        theta=alt.Theta(field="Porcentaje", type="quantitative"),
        color=alt.Color(field="Gastos", type="nominal"),
        tooltip=["Gastos", "Porcentaje"]
    ).properties(
        title="Distribución del gasto familiar promedio en México (INEGI, 2025)"
    )

    st.altair_chart(grafica_gastos, width="stretch")

    st.dataframe(df_gastos,
                 hide_index=True,)

    st.subheader("De los porcentajes a los pesos reales")

    st.markdown("""
    📉 **De la estadística a la caja registradora:** Los porcentajes del INEGI pueden ser solo números fríos, pero si los cruzamos con el dinero total que dejó de entrar a Tizimín cada mes, la realidad es otra.
    
    La tiendita de la esquina, el panadero o la farmacia no resienten "porcentajes", resienten billetes que ya no entran en sus negocios. 
    
    Al aplicar esos hábitos de gasto al impacto económico total (con todo y efecto dominó), aquí calculamos **cuánto dinero crudo está perdiendo Tizimín cada mes, sector por sector:**
    """)
    
    filtro_tiemp = st.radio("¿Quieres ver la pérdida mensual o anual?", options=["Mensual", "Anual"])
    df_impacto_sectores = pd.DataFrame({
        "Sector":["Alimentos, bebidas y tabaco", 
                  "Transporte y comunicaciones", "Educación y esparcimiento",
                  "Vivienda y servicios", "Cuidados personales", "Enseres domésticos", "Vestido y calzado", "Salud", "Otros"
                  ],
                  "perdida_mensual_mxn": [perdida_con_derrama_mensual * (alimentos_bebidas_tabaco/100),
                                                    perdida_con_derrama_mensual * (transporte_comunicaciones/100),
                                                    perdida_con_derrama_mensual * (educación_esparcimiento/100),
                                                    perdida_con_derrama_mensual * (vivienda_servicios/100),
                                                    perdida_con_derrama_mensual * (cuidados_personales/100),
                                                    perdida_con_derrama_mensual * (enseres_domésticos/100),
                                                    perdida_con_derrama_mensual * (vestido_calzado/100),
                                                    perdida_con_derrama_mensual * (salud/100),
                                                    perdida_con_derrama_mensual * (otros/100)],
                                                    
                                                    "perida_anual_mxn": [perdida_con_derrama_anual * (alimentos_bebidas_tabaco/100),
                                                    perdida_con_derrama_anual * (transporte_comunicaciones/100),
                                                    perdida_con_derrama_anual * (educación_esparcimiento/100),
                                                    perdida_con_derrama_anual * (vivienda_servicios/100),
                                                    perdida_con_derrama_anual * (cuidados_personales/100),
                                                    perdida_con_derrama_anual * (enseres_domésticos/100),
                                                    perdida_con_derrama_anual * (vestido_calzado/100),
                                                    perdida_con_derrama_anual * (salud/100),
                                                    perdida_con_derrama_anual * (otros/100)]
                                                    })
    
    if filtro_tiemp == "Mensual":
        grafica_impacto_sectores = alt.Chart(df_impacto_sectores).mark_bar().encode(
        y= alt.Y("Sector", sort='x', axis=alt.Axis(labelAngle=0)),
        x= alt.X("perdida_mensual_mxn", axis=alt.Axis(title="Pérdida mensual estimada (MXN)")),
        color= alt.Color("Sector:N", legend=None, scale=alt.Scale(scheme="category20")
        ))
        
        st.altair_chart(grafica_impacto_sectores, width="stretch")
    else:
        grafica_impacto_sectores_anual = alt.Chart(df_impacto_sectores).mark_bar().encode(
        y= alt.Y("Sector", sort='x', axis=alt.Axis(labelAngle=0)),
        x= alt.X("perida_anual_mxn", axis=alt.Axis(title="Pérdida anual estimada (MXN)")),
        color= alt.Color("Sector:N", legend=None, scale=alt.Scale(scheme="category20")
        ))
        
        st.altair_chart(grafica_impacto_sectores_anual, width="stretch")
    

    st.warning("""
    👁️‍🗨️ **Dato real desde las calles:** Al visitar restaurantes locales del centro en plena quincena de marzo (ya pasada la cuesta de enero), se notaban **prácticamente vacíos**. 
    Tomando en cuenta que la maquiladora cerró en diciembre de 2025, el golpe a los bolsillos locales ya no es solo teoría en gráficas: **literalmente se siente en la calle.**
    """)
    st.dataframe(df_impacto_sectores
                 
                 .assign(perdida_mensual_mxn=lambda x: x["perdida_mensual_mxn"].apply(fmt_moneda))
                 .assign(perida_anual_mxn=lambda x: x["perida_anual_mxn"].apply(fmt_moneda))
                ,hide_index=True
                 )
    st.divider()
    #6. Conclusiones y referencias
    st.subheader("6. Conclusiones y referencias")
    st.markdown("""
    En resumen: **el cierre de Cielo Manufacturing no es "solo el problema de los exempleados".** Es una herida abierta en la economía de todo Tizimín. 
    
    Cada día que pasa sin recuperar esos empleos formales, **es un día de pérdidas** para la señora de los tamales, el taxista, el tendero y el mercado completo. Las cifras no mienten: el agujero de **26 millones al año** no se tapa solo. 
    
    ¿Qué sigue para Tizimín? ¿Las autoridades están viendo estas cifras? 
    Es momento de exigir y buscar soluciones reales antes de que la recesión local ahogue a los negocios que aún resisten.
    """)
    
    referencias = pd.DataFrame({
        "Fuente":["Revista Yucatán. (2017)",
                "INEGI. (2025)", 
                "Diario de Yucatán. (2023)", 
                "El Grillo de Yucatán. (2017)",
                "Diario Oficial de la Federación." ],
        "Descripción":["Anuncio del cierre de Cielo Manufacturing y cifras iniciales de empleo.",
                    "Encuesta Nacional de Ingresos y Gastos de los Hogares (ENIGH) 2024, resultados publicados en 2025.",
                    "Reportaje sobre el impacto económico del cierre de la maquiladora en Tizimín, con testimonios locales.",
                    "Cifras detalladas sobre el número de trabajadores prometidos, máximos y reales en Cielo Manufacturing.",
                    "Información oficial sobre la fecha y condiciones del cierre de la planta, así como cualquier apoyo gubernamental anunciado."
                    ],
        "url":["https://www.revistayucatan.com/v1/noticias/inauguran-maquiladora-en-tizimin/",
               "https://www.inegi.org.mx/contenidos/programas/enigh/nc/2024/doc/enigh2024_ns_presentacion_resultados.pdf",
               "https://www.yucatan.com.mx/mexico/2024/12/26/empresas-textiles-alertan-cierre-masivo-por-decreto-de-claudia-sheinbaum-que-dice.html",
               "https://grillodeyucatan.com/2017/05/06/la-nueva-maquiladora-cielo-manufacturing-genera-220-empleos-en-tizimin/",
                "https://canaintex.org.mx/decreto-por-el-que-se-modifica-la-tarifa-de-la-ley-de-los-impuestos-generales-de-importacion-y-de-exportacion-y-el-decreto-para-el-fomento-de-la-industria-manufacturera-maquiladora-y-de-servicios-de/"
                 ]
    })

    st.info("👋 **Sobre el autor:** Este trabajo fue hecho por Reynaldo Manzanilla, estudiante de Data Science en IEU Puebla. El objetivo es concientizar sobre el impacto económico del cierre de la maquiladora Cielo Manufacturing en Tizimín, Yucatán. Las cifras y análisis se basan en datos públicos y cálculos propios.")

    with st.expander("📚 Ver Referencias y Fuentes de Datos"):
        st.markdown("Para quienes quieran profundizar, aquí están las fuentes clave que respaldan los hallazgos de este estudio.")
        st.dataframe(
            referencias,
            hide_index=True,
            column_config={
                "url": st.column_config.LinkColumn("Enlace al documento")
            }
        )


# ==========================================
# PUNTO DE ENTRADA AL SCRIPT
# ==========================================
if __name__ == "__main__":
    main()