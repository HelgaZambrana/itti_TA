# E-commerce Analytics Challenge

## Descripción

Análisis end-to-end de cuatro datasets de e-commerce para generar 
insights accionables sobre retención de clientes, rendimiento de ventas, 
percepción de producto y predicción de recompra.

---

## Datasets

| Dataset | Fuente | Uso |
|---|---|---|
| eCommerce_Dataset.csv | [Kaggle / UCI](https://www.kaggle.com/datasets/carrie1/ecommerce-data) | Cohortes y análisis de ventas |
| events.csv | [Kaggle / Retailrocket](https://www.kaggle.com/datasets/retailrocket/ecommerce-dataset) | Análisis de funnel |
| Musical_instruments_reviews.csv | [Kaggle / Amazon](https://www.kaggle.com/datasets/eswarchandt/amazon-music-reviews) | NLP y sentiment analysis |
| Instacart/*.csv | [Kaggle / Instacart](https://www.kaggle.com/datasets/psparks/instacart-market-basket-analysis) | Feature engineering y modelo predictivo |

> Los datasets no están incluidos en el repositorio. Descargarlos 
> desde los links anteriores y ubicarlos en `data/` respetando 
> la estructura indicada.

---

## Estructura del proyecto
```
data/                         # datasets locales 
│   └── Instacart/
notebooks/
│   ├── 01_eda.ipynb          # calidad de datos y decisiones de limpieza
│   ├── 02_cohorts_sales.ipynb  # análisis de cohortes y ventas
│   ├── 03_nlp_sentiment.ipynb  # sentiment analysis con VADER
│   ├── 04_feature_engineering.ipynb  # features de comportamiento (Instacart)
│   ├── 05_predictive_model.ipynb     # Logistic Regression + XGBoost + SHAP
│   └── 06_business_impact.ipynb      # oportunidades de negocio cuantificadas
outputs/                      # gráficos y datasets intermedios generados
src/
│   └── utils.py              # paths y configuración global
requirements.txt
```
---

## Contenido por notebook

| Notebook | Tarea del challenge | Contenido |
|---|---|---|
| 01_eda | Exploración inicial | Calidad de datos, decisiones de limpieza y visualizaciones por dataset |
| 02_cohorts_sales | Análisis de cohortes + análisis de ventas | Heatmap de retención mensual, top productos por revenue, mercados internacionales |
| 03_nlp_sentiment | Sentiment del cliente | VADER scoring, análisis de discrepancias rating vs. sentiment, wordclouds |
| 04_feature_engineering | Preparación del modelo | 10 features de comportamiento por usuario desde historial de Instacart |
| 05_predictive_model | Modelo predictivo | Logistic Regression baseline, XGBoost, curvas ROC, SHAP values, análisis de umbral |
| 06_business_impact | Impacto en el negocio | Tres oportunidades cuantificadas con propuestas de acción y métricas de éxito |

---

## Oportunidades de negocio identificadas

**1. Programa de retención temprana**
El análisis de cohortes muestra que ninguna cohorte supera el 37% de 
retención en el primer mes post-compra. Recuperar el 10% de los clientes 
perdidos en ese período representa £688K en revenue potencial.
Acción: programa de onboarding de 30 días con email a los 7 días 
y descuento de reactivación a los 25 días si no hubo segunda compra.
Métrica de éxito: retención en período 1 >= 30%.

**2. Expansión en mercados de alto valor**
Netherlands, Australia y Japan tienen un ticket promedio 6x superior 
al de UK (£116–£121 vs £19) con volumen de transacciones bajo, 
señal de mercados con demanda existente no desarrollada.
Acción: localización de plataforma y campañas de performance marketing 
focalizadas en los tres mercados.
Métrica de éxito: incremento de transacciones del 50% manteniendo AOV >= £100.

**3. Optimización del funnel de conversión**
El cuello de botella está en view > addtocart (2,69%), no en 
addtocart > transaction (31,07%). Mejorar la conversión end-to-end 
del 0,83% al 4% representa 44448 compradores adicionales.
Acción: A/B testing de páginas de producto y remarketing a usuarios 
con 3 o más vistas sin conversión.
Métrica de éxito: conversión view > addtocart >= 4% en páginas intervenidas.

---

## Cómo reproducir el análisis

```bash
git clone https://github.com/HelgaZambrana/itti_TA.git
cd itti_TA
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Descargar los datasets desde los links de la tabla anterior y ubicarlos en `data/`.
Ejecutar los notebooks en orden del 01 al 06.

---

## Decisiones de diseño

**Asignación de datasets por tarea:** cada dataset se asignó a la tarea 
para la que tiene mayor afinidad estructural. Instacart para el modelo 
predictivo por su campo `reordered` y su historial de pedidos por usuario. 
Amazon Reviews para NLP por ser el único dataset con texto libre. 
E-commerce para cohortes por tener `CustomerID` e `InvoiceDate`. 
Retailrocket para análisis de funnel por sus eventos de comportamiento.

**Redefinición del target:** el target original (al menos un producto 
reordenado) generaba 93% de positivos. Se redefinió como tasa de reorden >= 0.5 en el pedido de train, resultando en un dataset balanceado 
(66,65% / 33,35%) sobre el que el modelo puede aprender patrones reales.

**CustomerID nulos en e-commerce:** el 24,93% de registros no tiene 
`CustomerID`. En lugar de excluirlos globalmente se generaron dos versiones 
del dataset: `df_clean` para análisis de producto y ventas, `df_customers` 
para análisis que requieren identificar al cliente.

---

## Hallazgos principales

- **Retención:** ninguna cohorte supera el 37% de retención en período 1. 
  La cohorte de diciembre 2010 muestra un pico de 50,3% en período 11 
  (noviembre 2011) explicado por estacionalidad navideña.
- **Ventas:** REGENCY CAKESTAND 3 TIER lidera revenue (£174K) con ticket 
  alto (£12,57/u), en contraste con productos de volumen masivo como 
  MEDIUM CERAMIC TOP STORAGE JAR (£1,05/u).
- **Funnel:** el drop crítico está en view > addtocart (2.69%). 
  Una vez en el carrito, el 31,07% completa la compra.
- **Sentiment:** el 89,4% de las reseñas tiene sentiment positivo. 
  Las reseñas negativas concentran vocabulario de precio y calidad 
  percibida ("cheap", "problem", "better").
- **Modelo:** ROC-AUC de 0,79. `reorder_rate` es el predictor dominante. 
  XGBoost mejora marginalmente sobre Logistic Regression (0,004 AUC).