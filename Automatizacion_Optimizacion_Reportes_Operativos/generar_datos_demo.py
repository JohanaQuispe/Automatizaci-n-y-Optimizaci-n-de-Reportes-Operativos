from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

incidencias = [
    "Error técnico",
    "Problema de facturación",
    "Consulta general",
    "Reclamo",
    "Cancelación de servicio",
]
canales = ["whatsapp", "telefono", "email", "chat"]
estados = ["Cerrado", "En proceso", "Cerrado", "Cerrado"]


def create_week_df(start_date: str, n: int, week_name: str) -> pd.DataFrame:
    base = pd.to_datetime(start_date)
    fechas = [base + pd.Timedelta(days=int(x)) for x in rng.integers(0, 7, size=n)]
    duraciones = rng.normal(18, 7, n).clip(3, 65)
    satisfaccion = rng.normal(4.1, 0.7, n).clip(1, 5)

    df = pd.DataFrame(
        {
            "ID": [f"{week_name}-{i:04d}" for i in range(1, n + 1)],
            "Fecha_Atencion": fechas,
            "Agente": rng.choice(["Ana", "Luis", "Camila", "José", "Marco"], n),
            "Canal": rng.choice(canales, n),
            "Incidencia": rng.choice(incidencias, n, p=[0.28, 0.23, 0.24, 0.17, 0.08]),
            "Duracion": [f"00:{int(x):02d}:{int((x%1)*60):02d}" for x in duraciones],
            "CSAT": np.round(satisfaccion, 1),
            "Estado": rng.choice(estados, n),
        }
    )

    # Insertar valores nulos para simular limpieza
    null_idx = rng.choice(df.index, size=max(1, n // 20), replace=False)
    df.loc[null_idx, "CSAT"] = np.nan

    return df


def main() -> None:
    out = Path("data/input")
    out.mkdir(parents=True, exist_ok=True)

    create_week_df("2025-01-06", 120, "W01").to_excel(out / "atencion_semana_01.xlsx", index=False)
    create_week_df("2025-02-03", 130, "W05").to_excel(out / "atencion_semana_05.xlsx", index=False)
    create_week_df("2025-03-03", 125, "W09").to_excel(out / "atencion_semana_09.xlsx", index=False)
    print("✅ Datos demo generados en data/input")


if __name__ == "__main__":
    main()