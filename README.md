# 📊 Automatización y Optimización de Reportes Operativos

Pipeline en Python que automatiza la limpieza, transformación y análisis de reportes semanales de atención al cliente — eliminando trabajo manual repetitivo y generando datasets listos para visualizar en Power BI.

---

## 🚀 Resultado

| Métrica | Antes | Después |
|---|---|---|
| ⏱️ Tiempo de procesamiento semanal | ~180 min (manual) | ~20 min (automatizado) |
| 📉 Reducción de tiempo | — | **89% menos** |
| 🎯 Tickets procesados | — | 375 tickets en 3 semanas |
| ⭐ Satisfacción promedio del equipo | — | 4.01 / 5.0 |
| 🕐 Tiempo promedio de atención | — | 17.81 min |

---

## 📈 Visualizaciones en Power BI

### Tiempo Promedio de Atención por Tipo de Incidencia

<img width="812" height="337" alt="Captura de pantalla 2026-03-10 181825" src="https://github.com/user-attachments/assets/10038516-be56-4074-bf8f-3629b39a2b39" />

> Los **Reclamos (19.5 min)** y **Cancelaciones (18.6 min)** superan el promedio general. La línea punteada marca el benchmark del equipo (17.81 min).

---

### Satisfacción Promedio por Agente

<img width="1428" height="623" alt="Captura de pantalla 2026-03-10 180430" src="https://github.com/user-attachments/assets/5f11fd76-74ab-470b-9107-9fd4771c954d" />

> El equipo mantiene una satisfacción consistente entre 3.9 y 4.1 en todos los agentes. **Luis y Marco lideran** con el puntaje más alto.

---

## 🔧 ¿Qué hace este proyecto?

El script `procesar_reportes.py` ejecuta un pipeline completo sobre archivos Excel semanales:

1. **Ingesta** — Lee y concatena todos los `.xlsx` de la carpeta `data/input/`
2. **Normalización de columnas** — Mapea nombres alternativos (`csat`, `satisfaction`, `handling_time`, etc.) al esquema estándar
3. **Limpieza de datos** — Parsea duraciones en distintos formatos (`HH:MM:SS`, `MM:SS`, decimal), imputa valores faltantes con la mediana y estandariza categorías de canal e incidencia
4. **Cálculo de KPIs** — Genera métricas de tiempo de atención, satisfacción, tendencias mensuales y cuellos de botella por canal y tipo
5. **Exportación** — Produce tres archivos de salida listos para consumir

```
data/output/
├── powerbi_dataset.csv     ← Dataset limpio para Power BI
├── kpis_resumen.json       ← KPIs del período
└── reporte_operativo.xlsx  ← Reporte con 4 hojas: KPIs, Tendencias, Incidencias, Cuellos_botella
```

---

## 🛠️ Tecnologías

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-Dashboard-F2C811?style=flat&logo=powerbi&logoColor=black)
![Excel](https://img.shields.io/badge/OpenPyXL-Excel%20I%2FO-217346?style=flat&logo=microsoftexcel&logoColor=white)

| Tecnología | Uso |
|---|---|
| **Python 3.10+** | Lenguaje principal |
| **Pandas** | Limpieza, transformación y análisis de datos |
| **OpenPyXL** | Lectura y escritura de archivos Excel |
| **Power BI Desktop** | Visualización del dataset de salida |
| **JSON** | Exportación de KPIs |

---

## ⚡ Uso rápido

```bash
# Clonar el repositorio
git clone https://github.com/JohanaQuispe/Automatizacion_Optimizacion_Reportes_Operativos.git
cd Automatizacion_Optimizacion_Reportes_Operativos

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar el pipeline con los datos de ejemplo
python procesar_reportes.py

# O especificar rutas personalizadas
python procesar_reportes.py --input-dir ruta/a/excels --output-dir ruta/de/salida
```

Los archivos de salida se generan automáticamente en `data/output/`.

---

## 📁 Estructura del proyecto

```
├── procesar_reportes.py        # Pipeline principal
├── generar_datos_demo.py       # Generador de datos de prueba
├── requirements.txt
├── data/
│   ├── input/                  # Archivos Excel semanales de entrada
│   │   ├── atencion_semana_01.xlsx
│   │   ├── atencion_semana_05.xlsx
│   │   └── atencion_semana_09.xlsx
│   └── output/                 # Resultados generados
│       ├── powerbi_dataset.csv
│       ├── kpis_resumen.json
│       └── reporte_operativo.xlsx
```

---

## 🔄 Flexibilidad del pipeline

El script acepta columnas con nombres distintos gracias a un sistema de alias. Por ejemplo, la columna de satisfacción puede llamarse `satisfaccion`, `csat`, `nivel_satisfaccion` o `satisfaction` — el pipeline la detecta automáticamente.

También soporta duraciones en múltiples formatos:

```
"25"          → 25.0 min
"25:30"       → 25.5 min  (MM:SS)
"1:05:00"     → 65.0 min  (HH:MM:SS)
```

---

*Desarrollado como proyecto de automatización operativa con Python y Power BI.*
