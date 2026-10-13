🌐 [English](Description) · [Dansk](Description.da) · **Bahasa Melayu**

# Penerangan

## Apa yang dilakukan program

Program mengikut langkah dalam pelajaran:

1. `read_csv` membaca fail banci.
2. `count_by_fur_color` mengira pemerhatian Gray, Cinnamon dan Black.
3. `build_summary` menukar kiraan kepada baris ringkasan.
4. `write_csv` menulis ringkasan ke `squirrel_count.csv`.

Pada fail banci 2018 hasilnya ialah Gray 2473, Cinnamon 392 dan Black 103. Pemerhatian tanpa warna bulu tidak dikira dalam mana-mana satu.

## Mengapa tidak menggunakan Pandas

Pelajaran menggunakan Pandas. Projek ini hanya menggunakan pustaka standard Python (`csv` dan `collections.Counter`) supaya tiada apa-apa untuk dipasang bagi menjalankannya. Keputusan itu direkodkan sebagai ADR-0001 dalam repositori.

## Susun atur

| Laluan | Kandungan |
| --- | --- |
| `src/squirrel/census.py` | Empat langkah di atas |
| `src/squirrel/cli.py` | Baris perintah, `python -m squirrel` |
| `src/squirrel/constants.py` | Semua pemalar, ditakrif sekali |
| `tests/` | Ujian pytest |
| `docs/` | Kes perniagaan, pelan, model, rekod semakan |

## Kualiti

Setiap dokumen dan kod disemak berdasarkan senarai semak rangka kerja SQA dan QC dalam mod autonomi: penyemak ialah pengganti AI, jadi semakan itu tidak bebas.
