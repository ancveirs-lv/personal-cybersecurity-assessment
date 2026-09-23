# Personīgās kiberdrošības pašnovērtējums ikvienam

**Latviski** · [English](README.md)

**24 jautājumu divvalodu pašnovērtējums · globāls angļu pamats · latviešu versija**

Šis ir praktisks pašnovērtējuma materiāls, nevis drošības garantija, juridisks atzinums vai incidentu reaģēšanas palīdzības aizstājējs.

Repozitorijs ir **nepilnību-pārvēršanas-darbībās instruments**, nevis tests, kas ar vienu skaitli paziņo, ka cilvēks vai organizācija ir “droša”.

## Modelis

`ietvars → joma → jautājums → atbildes stāvoklis → nepilnība → ieteiktā darbība → atkārtots novērtējums`

## Atbilžu modelis

`UNKNOWN → NOT_IN_PLACE → PARTIAL → CONSISTENT → VERIFIED`

Nezināmās zonas paliek redzamas. Projekts apzināti **nerada** vienu kopējo drošības, atbilstības vai brieduma skaitli.

## Ātra palaišana

```bash
python3 scripts/validate.py
python3 scripts/render.py --check
python3 -m unittest discover -s tests -v
python3 scripts/assess.py examples/answers.example.json
```

Repozitorija rīki nevienu pašnovērtējuma atbildi nekur nenosūta.

## Struktūra

- `data/assessment.en.json` — kanoniskais globālais angļu novērtējums;
- `data/assessment.lv.json` — latviešu versija;
- `data/sources.json` — oficiālo avotu reģistrs;
- `docs/` — deterministiski ģenerētas anketas;
- `scripts/assess.py` — lokāls nepilnību/darbību pārskata ģenerators;
- `scripts/validate.py` un `scripts/render.py` — validācijas līgumi;
- `tests/` — regresijas testi.

## Avoti un adaptācija

Jautājumi ir oriģināls projekta formulējums, kas balstīts reģistrētajos avotos. Atsauces norāda sasaisti vai pamatojumu, nevis oficiālu avota formulējumu vai apstiprinājumu.

## Versijas statuss

`v0.1.0` ir **pilota bāzes versija** pārskatīšanai un kalibrēšanai pirms stabilas 1.0 versijas.

## Autors

**Zigmārs Ancveirs** — tehnoloģiju vadītājs, programmatūras inženieris un neatkarīgs kiberdrošības pētnieks.

## Licence

Dokumentācija un novērtējuma dati: **CC BY 4.0**. Kods un automatizācija: **MIT**.
