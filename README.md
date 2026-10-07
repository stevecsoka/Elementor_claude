# Zuglói Sasok – megújított weboldal

A https://zugloisasok.hu megújított, statikus HTML másolata aloldalakkal.

## Oldalak
- `index.html` – Kezdőlap
- `misszio.html`, `vezetok.html`, `edzoink.html` – Egyesület
- `csapatok.html`, `nb2.html` – Csapatok
- `hirek.html` + cikkoldalak – Hírek
- `kapcsolat.html` – Kapcsolat

## Szerkesztés
- Közös fejléc/lábléc és tartalom: `build.py` → futtatás: `python3 build.py`
- Színek és betűtípusok: `assets/css/style.css` tetején, a `:root` változókban
  (`--brand-primary`, `--brand-accent`, `--font-heading`, `--font-body`).
