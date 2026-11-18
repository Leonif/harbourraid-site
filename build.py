"""Builds the Harbour Raid site (GitHub Pages): a landing page, privacy policy and support in Ukrainian and English.

  python3 -I build.py

Pages are plain self-contained HTML; edit the texts here and rebuild.
"""
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = "https://leonif.github.io/harbourraid-site"
EMAIL = "leonif1@gmail.com"
UPDATED = {"uk": "18 листопада 2026", "en": "18 November 2026"}

CSS = """
:root { --bg:#0d1820; --panel:#13222c; --line:#243843; --fg:#f1e6c5; --muted:#9fb2b8; --amber:#e9b949; --red:#e2604a;
  --sans: system-ui, -apple-system, "Segoe UI", Roboto, sans-serif; --mono: ui-monospace, "SF Mono", Menlo, Consolas, monospace; color-scheme: dark; }
* { box-sizing: border-box; }
html, body { margin: 0; }
body { background: var(--bg); color: var(--fg); font: 16px/1.6 var(--sans); padding: 32px max(16px, env(safe-area-inset-right, 0px)) 64px max(16px, env(safe-area-inset-left, 0px)); }
main { max-width: 760px; margin: 0 auto; display: flex; flex-direction: column; gap: 28px; }
header { display: flex; align-items: center; gap: 16px; flex-wrap: wrap; }
header img { width: 64px; height: 64px; border-radius: 14px; }
.brand { display: flex; flex-direction: column; min-width: 0; }
.kicker { font: 600 12px var(--mono); letter-spacing: .12em; text-transform: uppercase; color: var(--amber); }
h1 { font-size: 30px; line-height: 1.15; margin: 2px 0 0; text-wrap: balance; }
h2 { font-size: 19px; margin: 0 0 6px; }
p, li { color: var(--fg); max-width: 68ch; }
p { margin: 0 0 10px; }
ul { margin: 0; padding-left: 20px; display: flex; flex-direction: column; gap: 4px; }
a { color: var(--amber); }
a:focus-visible { outline: 2px solid var(--amber); outline-offset: 2px; }
nav { display: flex; flex-wrap: wrap; gap: 6px 18px; font: 600 13px var(--mono); letter-spacing: .06em; text-transform: uppercase; }
nav a { text-decoration: none; color: var(--muted); }
nav a[aria-current] { color: var(--fg); border-bottom: 2px solid var(--red); }
section { background: var(--panel); border: 1px solid var(--line); border-radius: 10px; padding: 18px 20px; }
.hero { padding: 0; overflow: hidden; }
.hero img { display: block; width: 100%; height: auto; }
.muted { color: var(--muted); font-size: 14px; }
table { border-collapse: collapse; width: 100%; }
td { padding: 6px 10px 6px 0; border-bottom: 1px solid var(--line); vertical-align: top; }
tr:last-child td { border-bottom: 0; }
td:first-child { font: 13px var(--mono); color: var(--amber); white-space: nowrap; }
.wrap { overflow-x: auto; }
footer { color: var(--muted); font-size: 13px; }
"""

T = {
    "uk": {
        "lang": "uk", "other": "en", "other_name": "English",
        "tagline": "Аркадний шутер: небо і море",
        "nav": [("index", "Гра"), ("support", "Підтримка"), ("privacy", "Приватність")],
        "index_title": "Harbour Raid - аркадний шутер для Mac",
        "index": """
<section class="hero"><img src="../hero.jpg" width="1280" height="800" alt="Harbour Raid: камуфляжний літак атакує ворожу гавань - авіаносець, лінкор і катер у вогні біля тропічного берега"></section>
<section><h2>Три рубежі, один літак</h2>
<p>Harbour Raid - аркадний вертикальний шутер для Mac. Ви пілот одного літака проти цілої оборони: винищувачів у небі, танків і гармат на землі, кораблів у морі.</p>
<ul><li>Пальмовий рубіж: гай, бази, залізниця і бронепоїзд.</li><li>Морський рубіж: конвой, авіаносець, острови-батареї і підводний човен.</li><li>Портовий рубіж: гирло річки, лінкори, форт на молу і гавань.</li></ul></section>
<section><h2>Без зайвого</h2>
<p>Перший рівень безкоштовний, повна гра - одна покупка назавжди. Без реклами, без підписок, без облікових записів. Гра працює без інтернету й анонімно рахує, як проходять рівні, без особистих даних. Інтерфейс українською та англійською.</p>
<p class="muted">Незабаром у Mac App Store. Потрібна macOS 13 або новіша.</p></section>""",
        "support_title": "Підтримка - Harbour Raid",
        "support": """
<section><h2>Зв'язок</h2>
<p>Питання, помилка чи побажання - напишіть на <a href="mailto:{email}">{email}</a>. Вкажіть версію гри і macOS, а якщо щось зламалось - що саме ви робили перед цим.</p></section>
<section><h2>Керування</h2><div class="wrap"><table>
<tr><td>Миша</td><td>Рух літака; під час польоту курсор схований і захоплений</td></tr>
<tr><td>Ліва кнопка</td><td>Вогонь (утримувати)</td></tr>
<tr><td>Права кнопка</td><td>Бомба</td></tr>
<tr><td>Стрілки / WASD</td><td>Рух</td></tr>
<tr><td>Space / Z</td><td>Вогонь (утримувати)</td></tr>
<tr><td>X / B</td><td>Бомба</td></tr>
<tr><td>P / Esc</td><td>Пауза; миша звільняється</td></tr>
<tr><td>1 / 2</td><td>Вимкнути або ввімкнути ефекти / музику</td></tr>
</table></div></section>
<section><h2>Часті питання</h2>
<p><strong>Як змінити мову?</strong> Меню - Налаштування - Мова. Доступні українська та англійська.</p>
<p><strong>Курсор зник і не рухається.</strong> Під час польоту гра захоплює мишу. Натисніть P або Esc - пауза поверне курсор.</p>
<p><strong>Де зберігаються рекорди?</strong> Лише на вашому Mac, у даних гри. Якщо видалити гру разом з її даними, рекорди зникнуть.</p>
<p><strong>Що дає покупка «Повна гра»?</strong> Рівні 2 і 3 та всі майбутні рівні, назавжди. Якщо перевстановили гру, у меню «Повна гра» натисніть «Відновити покупку».</p>
<p><strong>На чому працює?</strong> macOS 13 або новіша, Mac з Apple silicon або Intel.</p></section>""",
        "privacy_title": "Політика приватності - Harbour Raid",
        "privacy": """
<section><h2>Коротко</h2><p>Harbour Raid не збирає особистих даних. У грі немає облікових записів, реклами і трекінгу. Єдине, що гра надсилає, - анонімна статистика про те, як проходять рівні.</p></section>
<section><h2>Анонімна статистика</h2>
<p>Щоб розуміти, де гра заскладна чи нудна, вона надсилає сервісу <a href="https://telemetrydeck.com/privacy/">TelemetryDeck</a> такі події: запуск гри, початок рівня, перемога, поразка, вихід із рівня, втрата літака, відкриття екрана «Повна гра».</p>
<ul><li>Разом із подією йдуть: версія гри, версія macOS, мова інтерфейсу, номер рівня й ділянки, номер спроби, рахунок, кількість життів і пройдена частина рівня.</li><li>Ідентифікатор - випадковий рядок, створений на вашому Mac. Перед відправкою він хешується, а сервіс хешує його ще раз. Він не пов'язаний з Apple ID, іменем чи поштою.</li><li>Ім'я, пошта, Apple ID, вміст вашого Mac чи дані про оплату не надсилаються.</li></ul>
<p>Ці дані не використовуються для реклами і не передаються нікому, крім TelemetryDeck як обробника. Без інтернету гра працює так само, просто нічого не надсилає.</p></section>
<section><h2>Що зберігається на вашому Mac</h2>
<ul><li>Рекорди і відкриті рівні.</li><li>Налаштування: мова, звук, музика.</li><li>Випадковий ідентифікатор установлення для анонімної статистики.</li><li>Технічна статистика вильотів (влучання, рахунок, тривалість) - файл у даних гри, який використовується лише для налагодження балансу і нікуди не надсилається.</li></ul>
<p>Ці дані лежать тільки в контейнері гри на вашому пристрої. Щоб їх видалити, видаліть гру разом з її даними.</p></section>
<section><h2>Покупка</h2><p>Завантаження гри і покупку повної версії обробляє Apple через Mac App Store за власною політикою приватності. Розробник не отримує ваших платіжних чи особистих даних.</p></section>
<section><h2>Діти</h2><p>Гра не збирає особистих даних ні в кого, зокрема й у дітей.</p></section>
<section><h2>Зміни і зв'язок</h2><p>Якщо політика зміниться, нова редакція з'явиться на цій сторінці з новою датою. Питання - на <a href="mailto:{email}">{email}</a>.</p></section>""",
        "updated": "Оновлено", "footer": "Harbour Raid. Незалежна гра.",
    },
    "en": {
        "lang": "en", "other": "uk", "other_name": "Українська",
        "tagline": "Arcade shooter: sky and sea",
        "nav": [("index", "Game"), ("support", "Support"), ("privacy", "Privacy")],
        "index_title": "Harbour Raid - an arcade shooter for Mac",
        "index": """
<section class="hero"><img src="../hero.jpg" width="1280" height="800" alt="Harbour Raid: a camouflaged plane attacks an enemy harbour - a carrier, a battleship and a burning patrol boat off a tropical coast"></section>
<section><h2>Three fronts, one plane</h2>
<p>Harbour Raid is an arcade vertical shooter for Mac. You fly one plane against a whole defence line: fighters in the air, tanks and guns on the ground, warships at sea.</p>
<ul><li>Palm Front: a grove, bases, a railway and an armoured train.</li><li>Sea Front: a convoy, an aircraft carrier, island batteries and a submarine.</li><li>Harbour Front: a river mouth, battleships, a fort on the mole and the harbour.</li></ul></section>
<section><h2>Nothing extra</h2>
<p>The first level is free; the full game is one purchase for good. No ads, no subscriptions, no accounts. The game works offline and anonymously counts how levels are played, with no personal data. Interface in Ukrainian and English.</p>
<p class="muted">Coming soon to the Mac App Store. Requires macOS 13 or later.</p></section>""",
        "support_title": "Support - Harbour Raid",
        "support": """
<section><h2>Contact</h2>
<p>A question, a bug or a wish - write to <a href="mailto:{email}">{email}</a>. Please include the game and macOS versions and, if something broke, what you were doing just before.</p></section>
<section><h2>Controls</h2><div class="wrap"><table>
<tr><td>Mouse</td><td>Moves the plane; the cursor is hidden and captured in flight</td></tr>
<tr><td>Left button</td><td>Fire (hold)</td></tr>
<tr><td>Right button</td><td>Bomb</td></tr>
<tr><td>Arrows / WASD</td><td>Move</td></tr>
<tr><td>Space / Z</td><td>Fire (hold)</td></tr>
<tr><td>X / B</td><td>Bomb</td></tr>
<tr><td>P / Esc</td><td>Pause; the mouse is released</td></tr>
<tr><td>1 / 2</td><td>Switch effects / music off or on</td></tr>
</table></div></section>
<section><h2>Common questions</h2>
<p><strong>How do I change the language?</strong> Menu - Settings - Language. Ukrainian and English are available.</p>
<p><strong>The cursor is gone and will not move.</strong> The game captures the mouse in flight. Press P or Esc: the pause gives the cursor back.</p>
<p><strong>Where are my best scores kept?</strong> Only on your Mac, in the game's data. Deleting the game with its data removes them.</p>
<p><strong>What does the Full game purchase give?</strong> Levels 2 and 3 and every future level, for good. After a reinstall, open Full game in the menu and press Restore purchase.</p>
<p><strong>What does it run on?</strong> macOS 13 or later, a Mac with Apple silicon or Intel.</p></section>""",
        "privacy_title": "Privacy Policy - Harbour Raid",
        "privacy": """
<section><h2>In short</h2><p>Harbour Raid collects no personal data. The game has no accounts, ads or tracking. The only thing it sends is anonymous statistics about how levels are played.</p></section>
<section><h2>Anonymous statistics</h2>
<p>To see where the game is too hard or dull, it sends these events to <a href="https://telemetrydeck.com/privacy/">TelemetryDeck</a>: game launched, level started, level won, game over, level left, plane lost, the Full game screen opened.</p>
<ul><li>Each event carries the game version, the macOS version, the interface language, the level and its section, the attempt number, the score, the lives left and how far into the level you were.</li><li>The identifier is a random string created on your Mac. It is hashed before it is sent, and the service hashes it again. It is not tied to your Apple ID, name or email.</li><li>Your name, email, Apple ID, the contents of your Mac and payment details are never sent.</li></ul>
<p>This data is not used for advertising and is shared with no one except TelemetryDeck as the processor. Offline, the game works the same and simply sends nothing.</p></section>
<section><h2>What is kept on your Mac</h2>
<ul><li>Best scores and unlocked levels.</li><li>Settings: language, sound, music.</li><li>A random installation identifier for the anonymous statistics.</li><li>Technical sortie statistics (hits, score, duration) - a file in the game's data used only for balance tuning; it is never sent anywhere.</li></ul>
<p>This data stays in the game's container on your device. To remove it, delete the game together with its data.</p></section>
<section><h2>Purchase</h2><p>Downloading the game and buying the full version are handled by Apple through the Mac App Store under Apple's own privacy policy. The developer receives none of your payment or personal data.</p></section>
<section><h2>Children</h2><p>The game collects no personal data from anyone, children included.</p></section>
<section><h2>Changes and contact</h2><p>If this policy changes, the new version will appear on this page with a new date. Questions: <a href="mailto:{email}">{email}</a>.</p></section>""",
        "updated": "Updated", "footer": "Harbour Raid. An independent game.",
    },
}


def page(lang, name):
    t = T[lang]
    nav = "".join(f'<a href="{n}.html"{" aria-current=\"page\"" if n == name else ""}>{label}</a>' for n, label in t["nav"])
    nav += f'<a href="../{t["other"]}/{name}.html" hreflang="{t["other"]}">{t["other_name"]}</a>'
    title = t[name + "_title"]
    body = t[name].format(email=EMAIL)
    return f"""<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{title}">
<link rel="canonical" href="{BASE}/{lang}/{name}.html">
<link rel="alternate" hreflang="{t['other']}" href="{BASE}/{t['other']}/{name}.html">
<link rel="icon" href="../icon.png">
<style>{CSS}</style>
</head>
<body>
<main>
<header><img src="../icon.png" alt="" width="64" height="64"><div class="brand"><span class="kicker">{t['tagline']}</span><h1>{title.split(' - ')[0]}</h1></div></header>
<nav>{nav}</nav>
{body}
<footer>{t['updated']}: {UPDATED[lang]} · {t['footer']}</footer>
</main>
</body>
</html>
"""


for lang in T:
    (HERE / lang).mkdir(exist_ok=True)
    for name in ("index", "support", "privacy"):
        (HERE / lang / f"{name}.html").write_text(page(lang, name), encoding="utf-8")
# The root sends visitors to the Ukrainian page; English is one click away.
(HERE / "index.html").write_text(f"""<!DOCTYPE html>
<html lang="uk"><head><meta charset="UTF-8"><title>Harbour Raid</title>
<meta http-equiv="refresh" content="0; url=uk/index.html"><link rel="canonical" href="{BASE}/uk/index.html"></head>
<body><p><a href="uk/index.html">Harbour Raid - українською</a> · <a href="en/index.html">in English</a></p></body></html>
""", encoding="utf-8")
print("built", sum(1 for _ in HERE.rglob("*.html")), "pages")
