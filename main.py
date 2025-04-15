
import pandas as pd
import json

from eOveravanje import generisi_json2

# Putanja do Excel fajla
file_path = r"E:\Kepa\OT 038 EWG DOO BEOGRAD EOT 01.08.-15.08.2024.xlsx"

# Putanja do izlaznog JSON fajla
output_json_path = r"E:\Kepa\output.json"

# Funkcija za citanje Excel fajla i generisanje JSON-a
try:
    # Ucitavanje Excel fajla sa ispravnim zaglavljem
    df = pd.read_excel(file_path, header=1)  # Preskace prvi red, nije bitan
    print(df.head(20))  # Prikazuje prvih 20 redova
    print(df.columns)  # Prikazuje tacne nazive kolona
    # Prolazimo kroz sve kolone i razdvajamo podatke sa ';' separatorom
    for col in df.columns:
        df[col] = df[col].apply(lambda x: x.split(';') if isinstance(x, str) and ';' in x else x)

    # Zamenjuje NaN vrednosti sa praznim stringom
    df = df.fillna("")
    generisi_json2(df, output_json_path)

except Exception as e:
    print(f"Došlo je do greške: {e}")

