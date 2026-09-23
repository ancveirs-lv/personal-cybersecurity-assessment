# Personīgās kiberdrošības pašnovērtējums ikvienam

> Šis ir praktisks pašnovērtējuma materiāls, nevis drošības garantija, juridisks atzinums vai incidentu reaģēšanas palīdzības aizstājējs.

## Atbilžu stāvokļi

- `UNKNOWN` — Neesmu pārliecināts: Pašreizējā prakse nav zināma.
- `NOT_IN_PLACE` — Nav ieviests: Aizsardzības prakse attiecīgajās situācijās nav ieviesta.
- `PARTIAL` — Daļēji / nekonsekventi: Prakse ir ieviesta tikai daļai attiecīgo kontu, ierīču vai situāciju.
- `CONSISTENT` — Konsekventi ieviests: Prakse tiek konsekventi piemērota attiecīgajās situācijās.
- `VERIFIED` — Pārbaudīts vai testēts: Prakse nesen ir pārbaudīta vai testēta.
- `NOT_APPLICABLE` — Nav attiecināms: Punkts patiešām neattiecas uz personas situāciju; nepieciešams pamatojums.

## Novērtējums

### Konti un autentifikācija

#### P01

Svarīgiem kontiem tiek izmantotas unikālas paroles vai passkey, nevis atkārtoti lietotas paroles.

**Ieteiktā darbība:** Sāc ar galveno e-pastu un banku; novērs atkārtoti lietotas paroles.

**Avoti:** `nist_sp800_63b`, `ncsc_top_tips`

#### P02

Parolēm, kas jāglabā, tiek izmantots paroļu pārvaldnieks vai līdzvērtīga droša metode.

**Ieteiktā darbība:** Izmanto aizsargātu paroļu glabātuvi un aizsargā tās kontu.

**Avoti:** `nist_sp800_63b`, `ncsc_top_tips`

#### P03

Svarīgiem kontiem, kur iespējams, ir ieslēgta daudzfaktoru vai pret pikšķerēšanu noturīga autentifikācija.

**Ieteiktā darbība:** Vispirms ieslēdz passkey vai stipru MFA augstas ietekmes kontiem.

**Avoti:** `nist_sp800_63b`, `ncsc_top_tips`

#### P04

Atkopšanas kanāli, atkopšanas kodi un aktīvās sesijas ir aktuālas un manā kontrolē.

**Ieteiktā darbība:** Pārskati atkopšanas kanālus un noņem novecojušas sesijas un ierīces.

**Avoti:** `nist_sp800_63b`

### Ierīces un programmatūra

#### P05

Telefoni un datori izmanto ekrāna bloķēšanu un netiek atstāti brīvi pieejami.

**Ieteiktā darbība:** Ieslēdz piemērotu ierīces bloķēšanu un saprātīgu automātiskās bloķēšanas laiku.

**Avoti:** `ncsc_top_tips`

#### P06

Operētājsistēmas, pārlūki un svarīgas lietotnes savlaicīgi saņem drošības atjauninājumus.

**Ieteiktā darbība:** Kur piemērots, ieslēdz automātiskos atjauninājumus un uzstādi neieviestos drošības atjauninājumus.

**Avoti:** `ncsc_top_tips`

#### P07

Iebūvētie drošības aizsardzības līdzekļi ir ieslēgti, un es zinu, vai ierīce vairs netiek atbalstīta.

**Ieteiktā darbība:** Pārbaudi drošības iestatījumus un identificē neatbalstītas ierīces.

**Avoti:** `ncsc_top_tips`

#### P08

Vecas, pazaudētas vai pārdotas ierīces ir atvienotas no svarīgiem kontiem un apstrādātas droši.

**Ieteiktā darbība:** Pārskati uzticamo ierīču sarakstus un pirms nodošanas droši dzēs ierīces.

**Avoti:** `nist_sp800_63b`

### Dati un rezerves kopijas

#### P09

Svarīgiem fotoattēliem, dokumentiem un citiem datiem ir rezerves kopija ārpus galvenās ierīces.

**Ieteiktā darbība:** Datiem, kuru zudums būtu vissāpīgākais, izveido rezerves kopiju atsevišķā aizsargātā vietā.

**Avoti:** `ncsc_top_tips`

#### P10

Es esmu pārbaudījis, ka vismaz vienu svarīgu rezerves kopiju tiešām var atjaunot.

**Ieteiktā darbība:** Atjauno testa failu vai kopiju un fiksē, kas izdevās.

**Avoti:** `ncsc_top_tips`

#### P11

Sensitīvi faili un mākoņkrātuves ir aizsargātas ar atbilstošiem konta un koplietošanas iestatījumiem.

**Ieteiktā darbība:** Pārskati mākoņkoplietošanas saites, tiesības un konta aizsardzību.

**Avoti:** `ncsc_top_tips`

#### P12

Es neglabāju paroles, atkopšanas kodus vai sensitīvus noslēpumus brīvi nolasāmās piezīmēs vai ziņās.

**Ieteiktā darbība:** Pārvieto atklāti glabātus noslēpumus uz aizsargātu glabātuvi un dzēs nevajadzīgās kopijas.

**Avoti:** `nist_sp800_63b`

### Krāpšana un pārbaude

#### P13

Negaidīta steidzamība, slepenība vai emocionāls spiediens liek man apstāties pirms rīcības.

**Ieteiktā darbība:** Pieprasījumiem par naudu vai piekļuves datiem izmanto apzinātu pauzes noteikumu.

**Avoti:** `ncsc_top_tips`

#### P14

Svarīgām darbībām es pats atveru oficiālo pakalpojumu, nevis uzticos saitei ziņā.

**Ieteiktā darbība:** Bankas un konta izmaiņām pats atver zināmo oficiālo pakalpojumu.

**Avoti:** `ncsc_top_tips`

#### P15

Neparastus pieprasījumus no zināmiem cilvēkiem vai organizācijām es pārbaudu citā kanālā.

**Ieteiktā darbība:** Pirms rīcības izmanto atsevišķi zināmu saziņas kanālu.

**Avoti:** `ncsc_top_tips`

#### P16

Es neinstalēju attālinātās piekļuves programmas un nedalos ar verifikācijas kodiem pēc negaidīta zvanītāja vai ziņas norādes.

**Ieteiktā darbība:** Negaidītu attālinātās piekļuves vai kodu izpaušanas pieprasījumu uztver kā apstāšanās signālu.

**Avoti:** `nist_sp800_63b`, `ncsc_top_tips`

### Tīkli, lietotnes un koplietošana

#### P17

Mājas rūterim/Wi-Fi ir aktuāli drošības iestatījumi un nav noklusējuma administratora piekļuves datu.

**Ieteiktā darbība:** Pārskati rūtera administratora piekļuves datus, atjauninājumu statusu un bezvadu drošības režīmu.

**Avoti:** `ncsc_top_tips`

#### P18

Es nesaglabāju paroles un neatstāju atvērtas sesijas koplietotās vai publiskās ierīcēs.

**Ieteiktā darbība:** Koplietotās ierīcēs nesaglabā piekļuves datus un pilnībā izraksties.

**Avoti:** `ncsc_top_tips`

#### P19

Es periodiski pārskatu lietotņu atļaujas un noņemu nevajadzīgas piekļuves.

**Ieteiktā darbība:** Pārskati atrašanās vietas, kontaktu, mikrofona, kameras un kontu atļaujas.

**Avoti:** `ncsc_top_tips`

#### P20

Es izmantoju aizsargājošu DNS vai līdzvērtīgu tīkla aizsardzību, ja tas ir piemēroti un pieejams.

**Ieteiktā darbība:** Apsver uzticamu aizsargājošu DNS pakalpojumu; Latvijā izvērtē CERT.LV/NIC.LV DNS ugunsmūri.

**Avoti:** `certlv_dns`

### Incidenti un atkopšanas gatavība

#### P21

Es zinu pirmās darbības, kas jāveic svarīga konta kompromitācijas gadījumā.

**Ieteiktā darbība:** Pieraksti īsu atkopšanas secību: atgūsti kontroli, nomaini vai atsauc piekļuves datus un pārskati atkopšanas iestatījumus.

**Avoti:** `nist_sp800_63b`

#### P22

Es zinu, kā pēc aizdomām par kompromitāciju atsaukt vecas sesijas, ierīces vai piekļuves datus.

**Ieteiktā darbība:** Atrodi galvenā e-pasta sesiju/ierīču pārvaldības sadaļu, pirms tā kļūst vajadzīga.

**Avoti:** `nist_sp800_63b`

#### P23

Es zinu, kur ziņot par kiberincidentiem vai krāpšanu un kad finansiāla zaudējuma gadījumā jāsazinās arī ar banku vai policiju.

**Ieteiktā darbība:** Saglabā oficiālos ziņošanas un bankas kontaktus pirms incidenta.

**Avoti:** `certlv_services`

#### P24

Pēc drošības incidenta es pārbaudu, kas vēl var būt skarts, nevis salaboju tikai redzamo simptomu.

**Ieteiktā darbība:** Pārbaudi saistītos kontus, atkopšanas kanālus, maksājumu metodes un skartās ierīces.

**Avoti:** `nist_sp800_63b`, `ncsc_top_tips`
