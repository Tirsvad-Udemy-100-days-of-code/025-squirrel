🌐 [English](Usage) · [Dansk](Usage.da) · **Bahasa Melayu**

# Penggunaan

## Jalankan program

Dengan persekitaran maya aktif, dari folder projek:

```bash
python -m squirrel
```

Program membaca `data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv`, mencetak kiraan setiap warna bulu dan menulis `squirrel_count.csv`.

![Larian program](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/raw/branch/main/docs/images/run.png)

Gunakan fail lain dengan `python -m squirrel <fail banci> <fail ringkasan>`. Jika fail banci tidak wujud, program mencetak `Census file not found` dan keluar dengan status 2.

## Jalankan ujian

```bash
python -m pytest
```

![Larian ujian](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/raw/branch/main/docs/images/tests.png)

## Bina dokumentasi sumber

```bash
doxygen Doxyfile
```

Buka `docs/doxygen/html/index.html`.
