import pandas as pd
import json

# Putanja do izlaznog JSON fajla
output_json_path = r"E:\Kepa\output.json"

Broj_zahteva = None
Zavodni_datum_zahteva = None
Uplacena_taksa = None

Podaci_o_podnosiocu_zahteva = None
Naziv_podnosioca_zahteva=None
Maticni_broj_podnosioca_zahteva=None
Adresa_podnosioca_zahteva=None
Mesto_podnosioca_zahteva=None

Podaci_o_vlasniku_korisniku_merila = None
Naziv_vlasnika=None
Maticni_broj_vlasnika=None
Adresa_vlasnika=None
Mesto_vlasnika=None

Broj_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva = None
Datum_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva = None

Lokacija_na_kojoj_se_vrsi_overavanje = None
Naziv_objekta=None
Adresa_lokacije=None
Mesto_lokacije=None

Proizvodjac_merila = None
Tip_merila = None
Sluzbena_oznaka_Broj_uverenja_Broj_sertifikata = None
Serijski_broj_merila = None
Naziv_merila = None
Min_opsega_merenja = None
Max_opsega_merenja = None
Vrsta_pregleda_merila = None
Planirani_datum_pregleda = None
Vreme_pocetka_pregleda = None
Datum_izvrsenog_pregleda_Datum_overavanja_merila = None
Rezultat_pregleda_overeno_odbijeno = None
Ime_lica_koje_je_izvrsilo_pregled_i_overavanje_merila = None
Osnovni_zig_koji_se_nanosi_utiskivanjem = None
Osnovni_zig_u_obliku_nalepnice = None
Intervalski_zig_koji_se_nanosi_utiskivanjem = None
Intervalski_zig_u_obliku_nalepnice = None
Intervalski_zig_u_obliku_nalepnice_sa_mesecima = None
Dodatni_zig_u_obliku_nalepnice = None
Zastitni_zig_koji_se_nanosi_utiskivanjem = None
Zastitni_zig_u_obliku_nalepnice = None
Broj_izdatog_uverenja_o_overavanju_resenja_o_odbijanju = None
Hologramska_nalepnica = None


def generisi_json(df, json_output_path):

    df.columns = df.columns.str.strip()

    json_podaci = []

    for index, row in df.iterrows():
        row_dict = {col: row[col] for col in df.columns}


        Broj_zahteva = row_dict["Broj zahteva"]
        Zavodni_datum_zahteva = row_dict["Zavodni datum zahteva"]
        Uplacena_taksa = row_dict["Uplaćena taksa (D ili N)"].strip().upper() == "D"

        Podaci_o_podnosiocu_zahteva = row_dict["Podaci o podnosiocu zahteva"]
        Naziv_podnosioca_zahteva = Podaci_o_podnosiocu_zahteva
        Maticni_broj_podnosioca_zahteva = None
        Adresa_podnosioca_zahteva = None
        Mesto_podnosioca_zahteva = None

        Podaci_o_vlasniku_korisniku_merila = row_dict["Podaci o vlasniku/ korisniku merila"]
        Naziv_vlasnika, Adresa_vlasnika, Mesto_vlasnika=Podaci_o_vlasniku_korisniku_merila.split("; ")

        Broj_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva = row_dict["Broj  pod kojim je zahtev zaveden kod podnosioca zahteva"]
        Datum_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva = row_dict["Datum pod kojim je zahtev zaveden kod podnosioca zahteva"]

        Lokacija_na_kojoj_se_vrsi_overavanje = row_dict["Lokacija na kojoj se vrši overavanje-naziv subjekta; mesto; adresa"]
        Naziv_objekta, Adresa_lokacije, Mesto_lokacije=Lokacija_na_kojoj_se_vrsi_overavanje.split("; ")

        Proizvodjac_merila = row_dict["Proizvodjač merila"]
        Tip_merila = row_dict["Tip merila"]
        Sluzbena_oznaka_Broj_uverenja_Broj_sertifikata = row_dict["Službena oznaka / Broj uverenja / Broj sertifikata"]
        Serijski_broj_merila = row_dict["Serijski broj merila"]
        Naziv_merila = row_dict["Naziv merila"]
        Min_opsega_merenja = row_dict["Min opsega merenja"]
        Max_opsega_merenja = row_dict["Max opsega merenja"]
        Vrsta_pregleda_merila = row_dict["Vrsta pregleda merila PRV,  PER ili V (PRV-ako je prvi; PER- ako je periodični; V- ako je vanredni pregled)"]
        Planirani_datum_pregleda = row_dict["Planirani datum pregleda"]
        Vreme_pocetka_pregleda = row_dict["Vreme početka pregleda"]
        Datum_izvrsenog_pregleda_Datum_overavanja_merila = row_dict["Datum izvršenog pregleda / Datum overavanja merila"]
        Rezultat_pregleda_overeno_odbijeno = row_dict["Rezultat pregleda (overeno/odbijeno)"]
        Ime_lica_koje_je_izvrsilo_pregled_i_overavanje_merila = row_dict["Ime lica koje je izvršilo  pregled i overavanje merila"]
        Osnovni_zig_koji_se_nanosi_utiskivanjem = row_dict["1) Osnovni žig koji se nanosi utiskivanjem"]
        Osnovni_zig_u_obliku_nalepnice = row_dict["2) Osnovni žig u obliku nalepnice"]
        Intervalski_zig_koji_se_nanosi_utiskivanjem = row_dict["3) Intervalski žig koji se nanosi utiskivanjem"]
        Intervalski_zig_u_obliku_nalepnice = row_dict["4) Intervalski žig u obliku nalepnice"]
        Intervalski_zig_u_obliku_nalepnice_sa_mesecima = row_dict["5) Intervalski žig u obliku nalepnice sa mesecima"]
        Dodatni_zig_u_obliku_nalepnice = row_dict["6) Dodatni žig u obliku nalepnice"]
        Zastitni_zig_koji_se_nanosi_utiskivanjem = row_dict["7) Zaštitni žig koji se nanosi utiskivanjem"]
        Zastitni_zig_u_obliku_nalepnice = row_dict["8) Zaštitni žig u obliku nalepnice"]
        Broj_izdatog_uverenja_o_overavanju_resenja_o_odbijanju = row_dict["Broj izdatog uverenja o overavanju / resenja o odbijanju"]
        Hologramska_nalepnica = row_dict["Hologramska nalepnica"]

        json_obj = {
            "BrojZahteva": Broj_zahteva,
            "ZavodniDatumZahteva": Zavodni_datum_zahteva,
            "UplacenaTaksa": Uplacena_taksa,
            "PodnosilacZahteva": {
                "PravniNaziv": Podaci_o_podnosiocu_zahteva,
                "MaticniBroj": Maticni_broj_podnosioca_zahteva,
                "Adresa": Adresa_podnosioca_zahteva,
                "Mesto": Mesto_podnosioca_zahteva
            },
            "Podaci_o_vlasniku/_korisniku_merila": {
                    "Naziv": Naziv_vlasnika,
                    "MaticniBroj": Maticni_broj_vlasnika,
                    "Adresa": Adresa_vlasnika,
                    "Mesto": Mesto_vlasnika
            },
            "BrojZahtevaKodPodnosioca": Broj_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva,
            "DatumZahtevaKodPodnosioca": Datum_pod_kojim_je_zahtev_zaveden_kod_podnosioca_zahteva,
            "LokacijaPregleda": {
                "Naziv": Naziv_objekta,
                "Adresa": Adresa_lokacije,
                "Mesto": Mesto_lokacije
            },
            "ProizvodjacMerila": Proizvodjac_merila,
            "TipMerila": Tip_merila,
            "SluzbenaOznaka": Sluzbena_oznaka_Broj_uverenja_Broj_sertifikata,
            "SerijskiBrojMerila": Serijski_broj_merila,
            "NazivMerila": Naziv_merila,
            "MinOpsegMerenja": Min_opsega_merenja,
            "MaxOpsegMerenja": Max_opsega_merenja,
            "VrstaPregledaMerila": Vrsta_pregleda_merila,
            "PlaniraniDatumPregleda": Planirani_datum_pregleda,
            "VremePocetkaPregleda": Vreme_pocetka_pregleda,
            "DatumIzvrsenogPregleda": Datum_izvrsenog_pregleda_Datum_overavanja_merila,
            "RezultatPregleda": Rezultat_pregleda_overeno_odbijeno,
            "ImeLicaKojeJeIzvrsiloPregled": Ime_lica_koje_je_izvrsilo_pregled_i_overavanje_merila,
            "OsnovniZigUtiskivanje": Osnovni_zig_koji_se_nanosi_utiskivanjem,
            "OsnovniZigNalepnica": Osnovni_zig_u_obliku_nalepnice,
            "IntervalskiZigUtiskivanje": Intervalski_zig_koji_se_nanosi_utiskivanjem,
            "IntervalskiZigNalepnica": Intervalski_zig_u_obliku_nalepnice,
            "IntervalskiZigMeseci": Intervalski_zig_u_obliku_nalepnice_sa_mesecima,
            "DodatniZigNalepnica": Dodatni_zig_u_obliku_nalepnice,
            "ZastitniZigUtiskivanje": Zastitni_zig_koji_se_nanosi_utiskivanjem,
            "ZastitniZigNalepnica": Zastitni_zig_u_obliku_nalepnice,
            "BrojIzdatogUverenja": Broj_izdatog_uverenja_o_overavanju_resenja_o_odbijanju,
            "HologramskaNalepnica": Hologramska_nalepnica
        }

        json_podaci.append(json_obj)

    # Upisivanje JSON fajla sa dobrim formatiranjem i separacijom
    with open(json_output_path, "w", encoding="utf-8") as f:
        json.dump(json_podaci, f, indent=4, ensure_ascii=False, separators=(", ", ": "))


    print(f"JSON fajl je uspešno kreiran: {json_output_path}")
