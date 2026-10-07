#!/usr/bin/env python3
"""Zuglói Sasok statikus oldalgenerátor.

A közös fejléc/lábléc itt van egy helyen; futtatás: python3 build.py
Minden oldal a repó gyökerébe íródik (.html).
"""
from pathlib import Path

ROOT = Path(__file__).parent
SITE = "Zuglói Sasok"
EMAIL = "info@zugloisasok.hu"
PHONE = "06 30 841 6818"
PHONE_TEL = "+36308416818"
ADDRESS = "1145 Budapest, Columbus u. 54/B"

NAV = [
    ("index.html", "Kezdőlap", []),
    ("misszio.html", "Egyesület", [
        ("misszio.html", "Misszió"),
        ("vezetok.html", "Vezetők"),
        ("edzoink.html", "Edzőink"),
    ]),
    ("csapatok.html", "Csapatok", [
        ("csapatok.html", "Utánpótlás"),
        ("nb2.html", "NB II"),
    ]),
    ("hirek.html", "Hírek", []),
]


def nav_html(active):
    out = []
    for href, label, subs in NAV:
        is_active = active == href or any(active == s for s, _ in subs)
        cur = ' aria-current="page"' if is_active else ""
        if subs:
            sub = "".join(f'<li><a href="{s}">{l}</a></li>' for s, l in subs)
            out.append(f'<li class="has-sub"><a href="{href}"{cur}>{label}</a><ul class="sub">{sub}</ul></li>')
        else:
            out.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    cur = ' aria-current="page"' if active == "kapcsolat.html" else ""
    out.append(f'<li class="nav-cta"><a href="kapcsolat.html"{cur}>Kapcsolat</a></li>')
    return "".join(out)


LOGO = f'<a class="logo" href="index.html" aria-label="{SITE} – kezdőlap"><span class="logo__mark">ZS</span><span class="logo__text">Zuglói Sasok<small>Sportegyesület · 1998</small></span></a>'


def page(slug, title, desc, body):
    html = f"""<!doctype html>
<html lang="hu">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} – {SITE}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600&family=Open+Sans:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
<header class="site-header">
  <div class="container site-header__inner">
    {LOGO}
    <button class="nav-toggle" aria-label="Menü" aria-expanded="false"><span></span><span></span><span></span></button>
    <nav class="nav" aria-label="Fő navigáció"><ul>{nav_html(slug)}</ul></nav>
  </div>
</header>
<main>
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        {LOGO}
        <p style="margin-top:18px">1998 óta adunk szervezett keretek között sportolási lehetőséget a kosárlabdát szerető zuglói lányoknak és fiúknak.</p>
      </div>
      <div>
        <h4>Egyesület</h4>
        <ul><li><a href="misszio.html">Misszió</a></li><li><a href="vezetok.html">Vezetők</a></li><li><a href="edzoink.html">Edzőink</a></li></ul>
      </div>
      <div>
        <h4>Csapatok</h4>
        <ul><li><a href="csapatok.html">Utánpótlás</a></li><li><a href="nb2.html">NB II</a></li><li><a href="hirek.html">Hírek</a></li></ul>
      </div>
      <div>
        <h4>Kapcsolat</h4>
        <ul>
          <li>{ADDRESS}</li>
          <li><a href="tel:{PHONE_TEL}">{PHONE}</a> <small>(H–P 10–16)</small></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li><a href="https://www.facebook.com/zugloisasok/" target="_blank" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span id="year">2026</span> Zuglói Sasok Sportegyesület. Minden jog fenntartva.</span>
      <span>Hajrá Sasok! Szárnyaljatok!</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>
"""
    (ROOT / slug).write_text(html, encoding="utf-8")


def page_hero(crumb, title, lead):
    return f"""<section class="page-hero"><div class="container">
  <div class="breadcrumb"><a href="index.html">Kezdőlap</a> / {crumb}</div>
  <h1>{title}</h1><p>{lead}</p>
</div></section>"""


CTA = f"""<section class="cta"><div class="container cta__inner">
  <div><h2>Gyere, próbáld ki!</h2><p>Várjuk a kosárlabdát szerető lányokat és fiúkat minden korosztályban.</p></div>
  <a class="btn" href="kapcsolat.html">Jelentkezem</a>
</div></section>"""

COACHES = [
    ("Ronkay László", "Elnök, szakmai igazgató", ["Előkészítő"]),
    ("Sárosi Judit", "Edző", ["Előkészítő"]),
    ("Mészáros Márton", "Edző", ["U11", "U12"]),
    ("Babik Barnabás", "Edző", ["U14", "U15", "U16B"]),
    ("Kőszegi Adorján", "Edző", ["U14", "U15", "U16B"]),
    ("Szabó Máté", "Edző", ["U16"]),
    ("Hirschler Máté", "Edző", ["U18"]),
]


def initials(name):
    return "".join(p[0] for p in name.split()[:2])


def person(name, role, tags):
    t = "".join(f'<span class="tag">{x}</span>' for x in tags)
    return f'<div class="person reveal"><div class="avatar">{initials(name)}</div><h3>{name}</h3><div class="role">{role}</div>{t}</div>'


POSTS = [
    ("kettos-gyozelem-a-kenguru-kupa-4-fordulojaban.html", "Kenguru Kupa", "Kettős győzelem a Kenguru Kupa 4. fordulójában",
     "Két magabiztos sikerrel zártuk a fordulót: a Keresztúri Méhecskék és a Budapest Blazers ellen is nyertünk."),
    ("hajra-sasok-szarnyaljatok.html", "Szurkolók", "„Hajrá Sasok! Szárnyaljatok!”",
     "A lelátó végig mögöttünk állt – a buzdítás már az első feldobásnál felcsendült."),
]


def post_card(href, cat, title, excerpt):
    return f"""<article class="post reveal"><a href="{href}" class="post__thumb" aria-hidden="true" tabindex="-1"></a>
<div class="post__body"><div class="post__meta">{cat}</div><h3>{title}</h3><p>{excerpt}</p>
<a class="post__link" href="{href}">Tovább olvasom →</a></div></article>"""


# ---------------- Kezdőlap ----------------
page("index.html", "Kezdőlap", "A Zuglói Sasok Sportegyesület 1998 óta neveli a zuglói kosárlabdázókat.", f"""
<section class="hero"><div class="container"><div class="hero__inner">
  <span class="eyebrow">Zuglói Sasok Sportegyesület · 1998</span>
  <h1>Kosárlabda <em>Zuglóban</em>,<br>szárnyalásra készen</h1>
  <p>Előkészítőtől az U18-ig és a felnőtt NB II-ig – szervezett, szakmailag megalapozott kosárlabda lányoknak és fiúknak.</p>
  <div class="hero__actions"><a class="btn btn--accent" href="kapcsolat.html">Jelentkezés edzésre</a><a class="btn btn--ghost" href="csapatok.html">Csapataink</a></div>
</div></div></section>

<div class="container"><div class="stats">
  <div class="stat reveal"><strong>1998</strong><span>óta működünk</span></div>
  <div class="stat reveal"><strong>{len(COACHES)}</strong><span>elhivatott edző</span></div>
  <div class="stat reveal"><strong>5</strong><span>partner iskola</span></div>
  <div class="stat reveal"><strong>NB II</strong><span>felnőtt csapat</span></div>
</div></div>

<section class="section"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">Rólunk</span>
    <h2>Több mint egy edzés</h2>
    <p class="lead">Egyesületünket 1998-ban alapítottuk azzal a céllal, hogy a kosárlabdát szerető gyerekeknek – lányoknak és fiúknak egyaránt – szervezett keretek között adjunk sportolási lehetőséget a világ egyik legnépszerűbb sportágában.</p>
    <p>Kiemelt feladatunk az utánpótlás-nevelés: a tehetséges gyerekek felkutatása, tudásuk megfelelő szintre emelése és sportpályafutásuk segítése.</p>
    <a class="btn btn--outline" href="misszio.html">Misszióink</a>
  </div>
  <div class="panel reveal">
    <h3>Zuglói partneriskoláink</h3>
    <ul>
      <li>Herman Ottó Általános Iskola</li>
      <li>Jókai Mór Általános Iskola</li>
      <li>Kaffka Margit Általános Iskola</li>
      <li>Németh Imre Általános Iskola</li>
      <li>Széchenyi István Általános Iskola</li>
    </ul>
  </div>
</div></section>

<section class="section section--soft"><div class="container">
  <div class="center reveal"><span class="eyebrow">Miért a Sasok?</span><h2>Amit nálunk kapsz</h2></div>
  <div class="grid grid--3" style="margin-top:40px">
    <div class="card reveal"><div class="card__icon">🏀</div><h3>Korosztályos csapatok</h3><p>Előkészítő csoportoktól az U18-ig minden korosztálynak megvan a helye, egészen a felnőtt NB II-es csapatig.</p></div>
    <div class="card reveal"><div class="card__icon">🎓</div><h3>Szakképzett edzők</h3><p>Tapasztalt edzői stábunk korosztályonként, egyénre szabottan fejleszti a játékosokat.</p></div>
    <div class="card reveal"><div class="card__icon">🤝</div><h3>Erős partnerségek</h3><p>Szakmai együttműködés a Budapest Honvéd kosárlabda-akadémiájával és öt zuglói általános iskolával.</p></div>
  </div>
</div></section>

<section class="section"><div class="container">
  <div class="reveal" style="display:flex;justify-content:space-between;align-items:end;flex-wrap:wrap;gap:16px">
    <div><span class="eyebrow">Hírek</span><h2 style="margin:0">Legfrissebb híreink</h2></div>
    <a class="btn btn--outline" href="hirek.html">Összes hír</a>
  </div>
  <div class="grid grid--2" style="margin-top:36px">{''.join(post_card(*p) for p in POSTS)}</div>
</div></section>
{CTA}
""")

# ---------------- Misszió ----------------
page("misszio.html", "Misszió", "A Zuglói Sasok Sportegyesület küldetése.", page_hero("Egyesület / Misszió", "Misszió", "Miért dolgozunk nap mint nap a zuglói kosárlabdáért.") + f"""
<section class="section"><div class="container split">
  <div class="reveal">
    <span class="eyebrow">Küldetésünk</span>
    <h2>Kosárlabda minden gyereknek</h2>
    <p class="lead">A Zuglói Sasok Sportegyesületet 1998-ban alapítottuk azzal a céllal, hogy a kosárlabdát szerető gyerekeknek – lányoknak és fiúknak egyaránt – szervezett keretek között biztosítsunk sportolási lehetőséget a világ egyik legnépszerűbb sportágában.</p>
    <p>Fontos feladatunk a kosárlabda-utánpótlás nevelése, a tehetséges gyermekek felkutatása, tudásuk megfelelő szintre fejlesztése és sportpályafutásuk elősegítése.</p>
  </div>
  <div class="panel reveal">
    <h3>Céljaink</h3>
    <ul>
      <li>Szervezett sportolási lehetőség lányoknak és fiúknak</li>
      <li>Tehetségek felkutatása és fejlesztése</li>
      <li>Sportpályafutások támogatása</li>
      <li>A kosárlabda népszerűsítése a XIV. kerületi iskolákban</li>
    </ul>
  </div>
</div></section>
<section class="section section--soft"><div class="container">
  <div class="center reveal"><span class="eyebrow">Értékeink</span><h2>Amiben hiszünk</h2></div>
  <div class="grid grid--4" style="margin-top:40px">
    <div class="card reveal"><div class="card__icon">💪</div><h3>Kitartás</h3><p>Edzésről edzésre építkezünk, türelemmel és alázattal.</p></div>
    <div class="card reveal"><div class="card__icon">🤝</div><h3>Csapat</h3><p>Együtt nyerünk és együtt tanulunk a vereségekből.</p></div>
    <div class="card reveal"><div class="card__icon">⭐</div><h3>Tehetség</h3><p>Minden gyerekben meglátjuk a benne rejlő lehetőséget.</p></div>
    <div class="card reveal"><div class="card__icon">🏫</div><h3>Közösség</h3><p>Zuglói iskolákkal és családokkal közösen dolgozunk.</p></div>
  </div>
</div></section>
<section class="section"><div class="container center reveal">
  <span class="eyebrow">Partnerség</span><h2>Szakmai együttműködés</h2>
  <p class="lead">Szakmai partnerkapcsolatban állunk a Budapest Honvéd kosárlabda-akadémiájával, valamint együttműködési rendszert építettünk ki a XIV. kerület több általános iskolájával: a Herman Ottó, a Jókai Mór, a Kaffka Margit, a Németh Imre és a Széchenyi István Általános Iskolával.</p>
</div></section>
{CTA}
""")

# ---------------- Vezetők ----------------
page("vezetok.html", "Vezetők", "A Zuglói Sasok Sportegyesület vezetői.", page_hero("Egyesület / Vezetők", "Vezetők", "Az egyesület irányításáért felelős csapat.") + f"""
<section class="section"><div class="container">
  <div class="grid grid--2" style="max-width:820px;margin:0 auto">
    {person("Ronkay László", "Elnök, szakmai igazgató", ["Szakmai irányítás"])}
    {person("Tóth Andrea", "Operatív vezető", ["Szervezés", "Ügyintézés"])}
  </div>
</div></section>
{CTA}
""")

# ---------------- Edzőink ----------------
page("edzoink.html", "Edzőink", "A Zuglói Sasok edzői korosztályonként.", page_hero("Egyesület / Edzőink", "Edzőink", "Elhivatott szakemberek minden korosztály mellett.") + f"""
<section class="section"><div class="container">
  <div class="grid grid--4">{''.join(person(*c) for c in COACHES)}</div>
</div></section>
{CTA}
""")

# ---------------- Csapatok ----------------
TEAMS = [
    ("Előkészítő", "Ronkay László, Sárosi Judit", "Játékos ismerkedés a kosárlabdával a legkisebbeknek."),
    ("U11 – U12", "Mészáros Márton", "Alapok, labdakezelés, csapatjáték."),
    ("U14 – U16B", "Babik Barnabás, Kőszegi Adorján", "Technikai és taktikai fejlődés, bajnoki szereplés."),
    ("U16", "Szabó Máté", "Versenyszerű felkészítés a kadett korosztályban."),
    ("U18", "Hirschler Máté", "Átvezetés a felnőtt kosárlabdába."),
    ("Felnőtt NB II", "", "A Sasok felnőtt férfi csapata az NB II-ben."),
]
rows = "".join(f"<tr><td><strong>{t}</strong></td><td>{c or '–'}</td><td>{d}</td></tr>" for t, c, d in TEAMS)
page("csapatok.html", "Csapatok", "A Zuglói Sasok korosztályos csapatai.", page_hero("Csapatok", "Csapataink", "Előkészítőtől a felnőtt NB II-ig.") + f"""
<section class="section"><div class="container">
  <div class="grid grid--3">
    {''.join(f'<div class="card reveal"><div class="card__icon">🏀</div><h3>{t}</h3><p>{d}</p></div>' for t, _, d in TEAMS)}
  </div>
</div></section>
<section class="section section--soft"><div class="container">
  <div class="reveal"><span class="eyebrow">Áttekintés</span><h2>Korosztályok és edzők</h2></div>
  <div class="table-wrap reveal" style="margin-top:24px"><table>
    <thead><tr><th>Csapat</th><th>Edző</th><th>Leírás</th></tr></thead><tbody>{rows}</tbody>
  </table></div>
</div></section>
<section class="section"><div class="container split">
  <div class="reveal"><span class="eyebrow">Edzéshelyszín</span><h2>Ahol edzünk</h2>
    <p class="lead">Utánpótlás-edzéseink fő helyszíne a Németh Imre Általános Iskola tornaterme.</p>
    <p><strong>1148 Budapest, Lengyel utca 23.</strong></p>
    <a class="btn btn--outline" href="kapcsolat.html">Edzésidőpontok egyeztetése</a></div>
  <iframe class="map reveal" loading="lazy" title="Németh Imre Általános Iskola" src="https://www.google.com/maps?q=1148+Budapest,+Lengyel+utca+23&output=embed"></iframe>
</div></section>
{CTA}
""")

# ---------------- NB II ----------------
page("nb2.html", "NB II", "A Zuglói Sasok felnőtt NB II-es csapata.", page_hero("Csapatok / NB II", "NB II", "Felnőtt férfi csapatunk bemutatkozása.") + f"""
<section class="section"><div class="container split">
  <div class="reveal"><span class="eyebrow">Felnőtt csapat</span><h2>A Sasok az NB II-ben</h2>
    <p class="lead">Felnőtt férfi csapatunk az NB II-ben szerepel – itt mutatkoznak be utánpótlásunk legjobbjai a felnőtt mezőnyben.</p>
    <p>Az aktuális tabellát, sorsolást és eredményeket a magyar kosárlabda-szövetség (MKOSZ) oldalán követheted.</p>
    <a class="btn btn--accent" href="https://mkosz.hu" target="_blank" rel="noopener">Eredmények – MKOSZ</a></div>
  <div class="panel reveal"><h3>Gyere szurkolni!</h3><ul>
    <li>Kövesd a csapatot a bajnokságban</li><li>Biztasd a Sasokat a lelátón</li><li>Hajrá Sasok! Szárnyaljatok!</li></ul></div>
</div></section>
{CTA}
""")

# ---------------- Hírek ----------------
page("hirek.html", "Hírek", "A Zuglói Sasok hírei, eredményei.", page_hero("Hírek", "Hírek", "Eredmények, beszámolók és események az egyesület életéből.") + f"""
<section class="section"><div class="container">
  <div class="grid grid--3">{''.join(post_card(*p) for p in POSTS)}</div>
</div></section>
""")

page(POSTS[0][0], POSTS[0][2], POSTS[0][3], page_hero('<a href="hirek.html">Hírek</a>', POSTS[0][2], "Kenguru Kupa · 4. forduló") + """
<section class="section"><div class="container article">
  <p class="lead">A Kenguru Kupa 4. fordulójában két győzelemmel gazdagodtunk a csoportmérkőzések során.</p>
  <div class="score"><span>Zuglói Sasok</span><b>79 : 46</b><span>Keresztúri Méhecskék</span></div>
  <div class="score"><span>Zuglói Sasok</span><b>67 : 38</b><span>Budapest Blazers</span></div>
  <p>A Budapest Blazers elleni találkozón Varga András 18, Bohács Bence 14 ponttal vette ki a részét a sikerből.</p>
  <p>Gratulálunk a csapatnak és az edzőknek! Hajrá Sasok!</p>
  <p><a class="btn btn--outline" href="hirek.html">← Vissza a hírekhez</a></p>
</div></section>
""")

page(POSTS[1][0], POSTS[1][2], POSTS[1][3], page_hero('<a href="hirek.html">Hírek</a>', POSTS[1][2], "Szurkolók") + """
<section class="section"><div class="container article">
  <p class="lead">A labda feldobásának pillanatában felcsendült a lelátón: „Hajrá Sasok! Szárnyaljatok!”</p>
  <p>A tét mindkét csapat játékán érződött: a játékosok keményen küzdöttek, sok hibával, de óriási lelkesedéssel. Köszönjük szurkolóinknak, hogy végig mögöttünk álltak!</p>
  <p><a class="btn btn--outline" href="hirek.html">← Vissza a hírekhez</a></p>
</div></section>
""")

# ---------------- Kapcsolat ----------------
page("kapcsolat.html", "Kapcsolat", "Lépj kapcsolatba a Zuglói Sasok Sportegyesülettel.", page_hero("Kapcsolat", "Kapcsolat", "Kérdésed van, vagy jelentkeznél edzésre? Írj nekünk!") + f"""
<section class="section"><div class="container split" style="align-items:start">
  <div class="reveal">
    <span class="eyebrow">Elérhetőségek</span><h2>Zuglói Sasok Sportegyesület</h2>
    <ul class="contact-list">
      <li><span class="ic">📍</span><div><strong>Cím</strong>{ADDRESS}</div></li>
      <li><span class="ic">📞</span><div><strong>Telefon</strong><a href="tel:{PHONE_TEL}">{PHONE}</a><br><small>Hétköznap 10:00–16:00</small></div></li>
      <li><span class="ic">✉️</span><div><strong>E-mail</strong><a href="mailto:{EMAIL}">{EMAIL}</a></div></li>
      <li><span class="ic">🏀</span><div><strong>Edzéshelyszín</strong>Németh Imre Általános Iskola, 1148 Budapest, Lengyel utca 23.</div></li>
    </ul>
  </div>
  <form class="card reveal" action="mailto:{EMAIL}" method="post" enctype="text/plain">
    <h3>Üzenetküldés</h3>
    <div class="row"><div><label for="nev">Név</label><input id="nev" name="Név" required></div>
    <div><label for="email">E-mail</label><input id="email" type="email" name="E-mail" required></div></div>
    <label for="tema">Téma</label>
    <select id="tema" name="Téma"><option>Jelentkezés edzésre</option><option>Általános kérdés</option><option>Támogatás, partnerség</option></select>
    <label for="uzenet">Üzenet</label><textarea id="uzenet" name="Üzenet" rows="5" required></textarea>
    <button class="btn btn--accent" type="submit">Küldés</button>
  </form>
</div></section>
<section class="section section--soft" style="padding-top:0;background:none"><div class="container">
  <iframe class="map" loading="lazy" title="Zuglói Sasok – térkép" src="https://www.google.com/maps?q=1145+Budapest,+Columbus+utca+54/B&output=embed"></iframe>
</div></section>
""")

print("Kész.")
