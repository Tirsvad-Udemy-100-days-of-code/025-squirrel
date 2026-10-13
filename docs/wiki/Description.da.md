🌐 [English](Description) · **Dansk** · [Bahasa Melayu](Description.ms)

# Beskrivelse

## Hvad programmet gør

Programmet følger lektionens trin:

1. `read_csv` læser optællingsfilen.
2. `count_by_fur_color` tæller observationerne af Gray, Cinnamon og Black.
3. `build_summary` gør tallene til rækkerne i en opsummering.
4. `write_csv` skriver opsummeringen til `squirrel_count.csv`.

På optællingsfilen fra 2018 er resultatet Gray 2473, Cinnamon 392 og Black 103. Observationer uden pelsfarve tælles ikke med i nogen af dem.

## Hvorfor ikke Pandas

Lektionen bruger Pandas. Dette projekt bruger kun Pythons standardbibliotek (`csv` og `collections.Counter`), så der ikke er noget at installere for at køre det. Beslutningen er beskrevet som ADR-0001 i repositoryet.

## Opbygning

| Sti | Indhold |
| --- | --- |
| `src/squirrel/census.py` | De fire trin ovenfor |
| `src/squirrel/cli.py` | Kommandolinjen, `python -m squirrel` |
| `src/squirrel/constants.py` | Alle konstanter, defineret ét sted |
| `tests/` | pytest-testene |
| `docs/` | Business case, plan, modeller, reviewposter |

## Kvalitet

Alle dokumenter og al kode er gennemgået mod tjeklisterne i SQA- og QC-frameworket i autonom tilstand: reviewer er en AI-stedfortræder, så reviewene er ikke uafhængige.
