<p align="center">
  <img src="https://img.shields.io/badge/навыки-35-brightgreen?style=for-the-badge&logo=shield&logoColor=white" alt="Навыки">
  <img src="https://img.shields.io/badge/фреймворки-6-blue?style=for-the-badge" alt="Фреймворки">
  <img src="https://img.shields.io/badge/лицензия-MIT-green?style=for-the-badge" alt="Лицензия">
  <img src="https://img.shields.io/badge/язык-🇷🇺%20English-blueviolet?style=for-the-badge" alt="Язык">
</p>

<h1 align="center">MiMoCode Skills</h1>

<p align="center">
  <b>35 готовых навыков для AI-агентов — кибербезопасность, дизайн, инженерные процессы, IoT/hardware security, frontend-дизайн</b><br>
  Адаптировано из <a href="https://github.com/garrytan/gstack">gstack</a>, <a href="https://github.com/affaan-m/ECC">ECC</a>, <a href="https://github.com/bergside/typeui">TypeUI</a>, <a href="https://github.com/emilkowalski/skills">emilkowalski/skills</a>, <a href="https://github.com/Leonxlnx/taste-skill">taste-skill</a>, <a href="https://github.com/pbakaus/impeccable">impeccable</a>, <a href="https://github.com/BrownFineSecurity/iothackbot">IoTHackBot</a> и репозиториев безопасности
</p>

<p align="center">
  <a href="#быстрый-старт">Быстрый старт</a> •
  <a href="#каталог-навыков">Навыки</a> •
  <a href="#использование">Использование</a> •
  <a href="#рабочие-процессы">Workflow'ы</a> •
  <a href="#источники">Источники</a> •
  <a href="README_EN.md">English</a>
</p>

---

## Что это?

Коллекция из **35 структурированных навыков**, которые дают AI-агентам специализированные возможности:

### Категории навыков

**Кибербезопасность и инжиниринг:**
- **Ревью кода** с оценкой уверенности и классификацией серьёзности
- **Систематический дебаггинг** с анализом корневой причины
- **QA тестирование** с оценкой здоровья и триажем
- **Безопасный аудит** с чеклистами OWASP/WCAG
- **Пентест** с методологией PTES
- **Реагирование на инциденты** с плейбуками NIST/SANS
- **Угрозы и хантинг** с MITRE ATT&CK маппингом
- **TDD процессы** с циклами RED/GREEN/REFACTOR
- **CSO** — инфраструктурный аудит безопасности с OWASP Top 10 + STRIDE

**Frontend-дизайн и UX:**
- **Design Engineering** — полная философия UI, анимации, springs, gestures, компоненты (emilkowalski)
- **Review Animations** — строгий ревью анимаций с 10 non-negotiable стандартами
- **Animation Vocabulary** — глоссарий терминов для описания эффектов
- **Taste Engineering** — антислоп с 3 дизайн-дайлами, anti-AI-tell правилами, redesign протоколом (taste-skill)
- **Premium Visual Design** — агентский уровень: double-bezel, magnetic hover, cinematic motion
- **Minimalist UI** — editorial минимализм, warm monochrome, Notion/Linear стиль
- **Industrial Brutalist UI** — Swiss typographic + military terminal эстетика
- **Impeccable** — production-grade дизайн с 23 командами, brand/product регистрами
- **Redesign Existing** — аудит и апгрейд существующих проектов
- **Full Output Enforcement** — запрет на truncation, полный вывод кода

**Дизайн-системы и UI/UX:**
- **Design System** — универсальные принципы иерархии, отступов, типографики
- **Design Audit** — ревью UI против принципов дизайна

**IoT/Hardware Security:**
- Анализ прошивок (apktool, jadx)
- JTAG/UART отладка (picocom, jtagprobe)
- Сетевой анализ (nmap, iotnet, wsdiscovery)
- Android реверс-инжиниринг (apktool, jadx)
- Telnet/Serial оболочки

**Инженерные процессы:**
- **Поиск перед кодом** — исследование перед написанием
- **Инцидент-респонс** — NIST SP 800-61 / SANS PICERL
- **Threat Hunting** — гипотезо-управляемое расследование

---

## Проверяемый локальный каталог / Verified local catalog

Теперь в репозитории есть CLI на Python 3.10+ для поиска и выборочной установки действительно существующих навыков. Он не запускает инструкции навыков, не использует интернет и не перезаписывает существующие папки.

```bash
python scripts/skill_catalog.py --list
python scripts/skill_catalog.py --search design --json
python scripts/skill_catalog.py --install design-engineering code-review --dest ~/.codex/skills --dry-run
python scripts/skill_catalog.py --install design-engineering code-review --dest ~/.codex/skills
```

Проверка frontmatter и локальной установки: `python -m pip install 'PyYAML>=6,<7'`, затем `python -m unittest discover -s tests -p 'test_*.py' -v`. Для разных AI-ассистентов директория skills может отличаться. Не выполняйте команды из сторонних skill-файлов без проверки источника и разрешений.

## Быстрый старт (ручная установка)

### Вариант 1: Клонировать целиком

```bash
git clone https://github.com/Samuraiprm/mimocode-skills.git ~/.mimocode/skills/
```

### Вариант 2: Копировать отдельные навыки

```bash
# Только frontend-дизайн навыки
cp -r ~/.mimocode/skills/taste-engineering ~/.mimocode/skills/
cp -r ~/.mimocode/skills/design-engineering ~/.mimocode/skills/
cp -r ~/.mimocode/skills/impeccable ~/.mimocode/skills/
# ... и так далее

# Только IoT навыки
cp -r iot-* ~/.mimocode/skills/
```

### Вариант 3: Клонировать вручную

```bash
cd ~/.mimocode/skills/
git clone https://github.com/Samuraiprm/mimocode-skills.git temp/
cp -r temp/*/ .
rm -rf temp/
```

---

## Каталог навыков

### Frontend-дизайн

| Навык | Описание | Источник |
|-------|----------|----------|
| `design-engineering` | UI polish, анимации, springs, gestures, компоненты, perf, a11y | [emilkowalski/skills](https://github.com/emilkowalski/skills) |
| `review-animations` | Строгий ревью анимаций: 10 стандартов, escalation triggers, verdict | [emilkowalski/skills](https://github.com/emilkowalski/skills) |
| `animation-vocabulary` | Глоссарий: описание эффекта -> точный термин | [emilkowalski/skills](https://github.com/emilkowalski/skills) |
| `taste-engineering` | Антислоп: 3 дайла, brief inference, anti-AI-tell, redesign protocol | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `premium-visual-design` | Агентский уровень: double-bezel, magnetic hover, cinematic motion | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `minimalist-ui` | Editorial минимализм: warm monochrome, typographic contrast | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `industrial-brutalist-ui` | Swiss typographic + military terminal: rigid grids, CRT scanlines | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `impeccable` | Production-grade: 23 команды, brand/product регистры, 45 правил | [pbakaus/impeccable](https://github.com/pbakaus/impeccable) |
| `redesign-existing` | Аудит и апгрейд: typography, color, layout, a11y, компоненты | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |
| `full-output-enforcement` | Запрет на truncation, полный вывод, banned placeholder-паттерны | [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) |

### Безопасность и инжиниринг

| Навык | Описание | Источник |
|-------|----------|----------|
| `code-review` | Ревью PR: SQL safety, race conditions, trust boundaries | gstack |
| `code-audit` | Безопасный аудит кода: статический анализ, уязвимости | gstack |
| `investigate` | Систематический дебаггинг: root cause analysis | gstack |
| `qa-test` | QA тестирование: 3 уровня (Quick/Standard/Exhaustive) | gstack |
| `review` | Pre-landing ревью: structural issues, scope drift | gstack |
| `tdd-workflow` | TDD: RED/GREEN/REFACTOR циклы | ECC |
| `search-first` | Исследование перед кодом: поиск существующих решений | ECC |
| `verification-loop` | Build -> Type Check -> Lint -> Test -> Security | ECC |
| `security-review` | Чеклисты: auth, input handling, API, secrets | gstack |
| `cso` | Инфраструктурный аудит: OWASP Top 10 + STRIDE | gstack |

### Безопасность и инциденты

| Навык | Описание | Источник |
|-------|----------|----------|
| `pentest` | PTES: recon, scanning, exploitation, post-exploitation | PTES |
| `incident-response` | NIST SP 800-61 / SANS PICERL: detection -> recovery | NIST/SANS |
| `threat-hunting` | MITRE ATT&CK: гипотезы, IOC, detection engineering | MITRE |

### Дизайн-системы

| Навык | Описание | Источник |
|-------|----------|----------|
| `design-system` | Универсальные принципы: иерархия, отступы, типографика | TypeUI |
| `design-audit` | Ревью UI: hierarchy, spacing, typography, accessibility | TypeUI |

### IoT/Hardware Security

| Навык | Описание | Инструмент |
|-------|----------|------------|
| `iot-apktool` | Декомпиляция Android APK/IPK | apktool |
| `iot-jadx` | Анализ Java/Dex исходников | jadx |
| `iot-jtagprobe` | JTAG/UART отладка и дамп памяти | jtagprobe |
| `iot-picocom` | Serial/UART терминал | picocom |
| `iot-nmap` | Сетевое сканирование и обнаружение | nmap |
| `iot-iotnet` | UPnP/SSDP обнаружение устройств | iotnet |
| `iot-wsdiscovery` | WS-Discovery протокол | wsdiscovery |
| `iot-ffind` | Поиск и анализ файлов прошивок | ffind |
| `iot-chipsec` | Анализ чипов и hardware security | chipsec |
| `iot-telnetshell` | Telnet/Serial оболочки | telnetshell |

---

## Использование

### В Claude Code / Cursor / Codex

Навыки автоматически загружаются из `~/.mimocode/skills/`. Просто опишите задачу:

```
Проведи code review этого PR с фокусом на SQL injection
```

```
Создай landing page с использованием taste-engineering
```

```
Проведи аудит безопасности этого endpoint
```

### Ручной вызов навыка

```
/impeccable critique landing
```

```
/impeccable polish settings
```

### Выбор конкретного навыка

```
Используй design-engineering для ревью анимаций в этом компоненте
```

---

## Рабочие процессы

### Frontend Design Pipeline

```
1. taste-engineering → brief inference, дизайн-дайлы
2. design-engineering → анимации, компоненты, perf
3. review-animations → ревью motion-кода
4. impeccable → production-grade финальный пасс
```

### Security Audit Pipeline

```
1. code-audit → статический анализ
2. security-review → чеклисты OWASP
3. pentest → методология PTES
4. incident-response → плейбуки NIST/SANS
```

### Redesign Pipeline

```
1. redesign-existing → аудит текущего состояния
2. taste-engineering → новые дизайн-дайлы
3. design-engineering → компоненты и motion
4. impeccable → финальный polish
```

### IoT Security Pipeline

```
1. iot-nmap → обнаружение устройств
2. iot-iotnet / iot-wsdiscovery → UPnP/WS-Discovery
3. iot-apktool / iot-jadx → анализ прошивок
4. iot-jtagprobe / iot-picocom → hardware отладка
```

---

## Источники

### Оригинальные репозитории

| Репозиторий | Описание | Навыков взято |
|-------------|----------|---------------|
| [emilkowalski/skills](https://github.com/emilkowalski/skills) | Skills for Design Engineers | 3 |
| [Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill) | Anti-Slop Frontend Framework | 7 |
| [pbakaus/impeccable](https://github.com/pbakaus/impeccable) | Frontend Design Guidance | 1 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | Engineering workflows | 6 |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | Engineering best practices | 3 |
| [bergside/typeui](https://github.com/bergside/typeui) | Design system principles | 2 |
| [BrownFineSecurity/iothackbot](https://github.com/BrownFineSecurity/iothackbot) | IoT security tools | 9 |

### Стандарты и фреймворки

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [NIST SP 800-61](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final)
- [SANS PICERL](https://www.sans.org/white-papers/incident-handlers-handbook/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [PTES](http://www.pentest-standard.org/)
- [WCAG 2.1](https://www.w3.org/TR/WCAG21/)

---

## Структура файла

```
mimocode-skills/
├── README.md              # Русская версия
├── README_EN.md           # Английская версия
├── LICENSE                # MIT License
├── QUICKSTART.md          # Быстрый старт (рус)
├── QUICKSTART_EN.md       # Быстрый старт (англ)
│
├── design-engineering/    # emilkowalski/skills
│   └── SKILL.md
├── taste-engineering/     # Leonxlnx/taste-skill
│   └── SKILL.md
├── impeccable/            # pbakaus/impeccable
│   └── SKILL.md
├── review-animations/     # emilkowalski/skills
│   └── SKILL.md
├── animation-vocabulary/  # emilkowalski/skills
│   └── SKILL.md
├── premium-visual-design/ # Leonxlnx/taste-skill
│   └── SKILL.md
├── minimalist-ui/         # Leonxlnx/taste-skill
│   └── SKILL.md
├── industrial-brutalist-ui/ # Leonxlnx/taste-skill
│   └── SKILL.md
├── redesign-existing/     # Leonxlnx/taste-skill
│   └── SKILL.md
├── full-output-enforcement/ # Leonxlnx/taste-skill
│   └── SKILL.md
│
├── code-audit/            # gstack
├── code-review/           # gstack
├── investigate/           # gstack
├── qa-test/               # gstack
├── review/                # gstack
├── security-review/       # gstack
├── cso/                   # gstack
│
├── tdd-workflow/          # ECC
├── search-first/          # ECC
├── verification-loop/     # ECC
│
├── design-system/         # TypeUI
├── design-audit/          # TypeUI
│
├── pentest/               # PTES
├── incident-response/     # NIST/SANS
├── threat-hunting/        # MITRE
│
├── iot-apktool/           # IoTHackBot
├── iot-jadx/
├── iot-jtagprobe/
├── iot-picocom/
├── iot-nmap/
├── iot-iotnet/
├── iot-wsdiscovery/
├── iot-ffind/
├── iot-chipsec/
└── iot-telnetshell/
```

---

## Лицензия

[MIT License](LICENSE) - можно свободно использовать, модифицировать и распространять.

---

## Вклад

Приветствуются PR с новыми навыками или улучшениями существующих. Каждый навык должен:
- Иметь `SKILL.md` с YAML frontmatter (`name`, `description`)
- Быть самодостаточным (не зависеть от других навыков)
- Иметь четкие триггеры использования
- Содержать пошаговый workflow
