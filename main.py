import pandas as pd
import json
from eOveravanje import generisi_json


def main():
    print("=== eOveravanje - JSON Generator ===")

    excel_path = input("Unesi punu putanju do Excel fajla: ").strip('"')
    json_output_path = input("Unesi gde da se sačuva JSON fajl: ").strip('"')

    try:
        df = pd.read_excel(excel_path, header=1)
        df = df.where(pd.notna(df), None)
        generisi_json(df, json_output_path)
        print(f"✅ JSON fajl je uspešno sačuvan na: {json_output_path}")
    except Exception as e:
        print(f"❌ Došlo je do greške: {e}")


if __name__ == "__main__":
    main()
