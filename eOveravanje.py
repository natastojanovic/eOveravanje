import pandas as pd
import json


json_output_path = r"E:\Kepa\output.json"

def generisi_json2(df, json_output_path):
    # Prolazimo kroz sve redove DataFrame-a
    for row in df.itertuples(index=False):
        print(f"Red: {row}")  # Dodajemo ovo da bismo videli svaki red pre nego što ga obradimo

        # Kreiranje rečnika sa svim kolonama i vrednostima iz trenutnog reda
        data = {column: getattr(row, column) for column in df.columns}

        # Zapisivanje podataka u JSON fajl
        with open(json_file, 'a', encoding='utf-8') as jsonf:
            json.dump(data, jsonf, ensure_ascii=False)
            jsonf.write("\n")

    # Uklanjanje razmaka sa početka i kraja naziva kolona
    df.columns = df.columns.str.strip()

    df = df.fillna("")

    df.columns = df.columns.str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
    json_podaci = []
    print(df.to_string())

    for row in df.itertuples(index=False):


        # Pretvori red u JSON objekat

        json_obj = {
            "BrojZahteva": getattr(row, "Broj_zahteva", ""),
            "ZavodniDatumZahteva": getattr(row, "Zavodni_datum_zahteva", ""),
            "UplacenaTaksa": getattr(row, "Uplaćena_taksa_D_ili_N", ""),
            "PodnosilacZahteva": {
                "PravniNaziv": getattr(row, "Podaci_o_podnosiocu_zahteva", ""),
                "MaticniBroj": getattr(row, "Matični_broj_podnosioca", ""),
                "Adresa": getattr(row, "Adresa_podnosioca", ""),
                "Mesto": getattr(row, "Mesto_podnosioca", "")
            },
            "Podaci_o_vlasniku/_korisniku_merila": {
                "Podaci": {
                    "Naziv": getattr(row, "Vlasnik_merila", ""),
                    "MaticniBroj": getattr(row, "Matični_broj_vlasnika", ""),
                    "Adresa": getattr(row, "Adresa_vlasnika", ""),
                    "Mesto": getattr(row, "Mesto_vlasnika", "")
                }
            },
            "BrojZahtevaKodPodnosioca": getattr(row, "Broj_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva", ""),
            "DatumZahtevaKodPodnosioca": getattr(row, "Datum_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva", ""),
            "LokacijaPregleda": {
                "Naziv": getattr(row, "Lokacija_na_kojoj_se_vrši_overavanje-naziv_subjekta;_mesto;_adresa", ""),
                "Adresa": getattr(row, "Adresa_lokacije", ""),
                "Mesto": getattr(row, "Mesto_lokacije", "")
            },
            "ProizvodjacMerila": getattr(row, "Proizvodjač_merila", ""),
            "TipMerila": getattr(row, "Tip_merila", ""),
            "SluzbenaOznaka": getattr(row, "Službena_oznaka_/_Broj_uverenja_/_Broj_sertifikata", ""),
            "SerijskiBrojMerila": getattr(row, "Serijski_broj_merila", ""),
            "NazivMerila": getattr(row, "Naziv_merila", ""),
            "OpsegMeranja": {
                "MinOpseg": getattr(row, "Min_opsega_merenja", ""),
                "MaxOpseg": getattr(row, "Max_opsega_merenja", "")
            },
            "VrstaPregledaMerila": getattr(row, "Vrsta_pregleda_merila_PRV,_PER_ili_V", ""),
            "PlaniraniDatumPregleda": getattr(row, "Planirani_datum_pregleda", ""),
            "VremePocetkaPregleda": getattr(row, "Vreme_početka_pregleda", ""),
            "DatumIzvrsenogPregleda": getattr(row, "Datum_izvršenog_pregleda_/_Datum_overavanja_merila", ""),
            "RezultatPregleda": getattr(row, "Rezultat_pregleda_(overeno/odbijeno)", ""),
            "ImeLicaKojeJeIzvrsiloPregled": getattr(row, "Ime_lica_koje_je_izvršilo_pregled_i_overavanje_merila", ""),
            "Zigovi": {
                "OsnovniZigUtiskivanje": getattr(row, "1)_Osnovni_žig_koji_se_nanosi_utiskivanjem", ""),
                "OsnovniZigNalepnica": getattr(row, "2)_Osnovni_žig_u_obliku_nalepnice", ""),
                "IntervalskiZigUtiskivanje": getattr(row, "3)_Intervalski_žig_koji_se_nanosi_utiskivanjem", ""),
                "IntervalskiZigNalepnica": getattr(row, "4)_Intervalski_žig_u_obliku_nalepnice", ""),
                "IntervalskiZigMeseci": getattr(row, "5)_Intervalski_žig_u_obliku_nalepnice_sa_mesecima", ""),
                "DodatniZigNalepnica": getattr(row, "6)_Dodatni_žig_u_obliku_nalepnice", ""),
                "ZastitniZigUtiskivanje": getattr(row, "7)_Zaštitni_žig_koji_se_nanosi_utiskivanjem", ""),
                "ZastitniZigNalepnica": getattr(row, "8)_Zaštitni_žig_u_obliku_nalepnice", "")

            },
            "BrojIzdatogUverenja": getattr(row, "Broj_izdatog_uverenja_o_overavanju_/_resenja_o_odbijanju", ""),
            "HologramskaNalepnica": getattr(row, "Hologramska_nalepnica", "")
        }


        json_podaci.append(json_obj)

    # Upisivanje JSON fajla sa dobrim formatiranjem i separacijom
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(json_podaci, f, indent=4, ensure_ascii=False, separators=(", ", ": "))


print(f"JSON fajl je uspešno kreiran: {json_output_path}")
