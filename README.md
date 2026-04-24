# Health-CIB: Multimodal Authorship & Veracity Detection

[![Code Quality](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions/workflows/ci.yml/badge.svg)](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)

Este repositorio contiene el desarrollo de la PEC 4 del Máster en Investigación en IA (IAI). El proyecto implementa un sistema para la detección de **Comportamiento Coordinado Inauténtico (CIB)** y la clasificación de **noticias falsas** en salud.

### ¿Qué es CIB (Coordinated Inauthentic Behavior)?
El **CIB** se refiere a campañas organizadas donde grupos de cuentas o páginas colaboran de forma síncrona para engañar a los usuarios sobre su identidad o sus objetivos. En este proyecto, el foco no es solo el contenido del mensaje, sino la **coordinación técnica** entre múltiples autores en diferentes plataformas.

## Objetivos del Proyecto
- **Detección de CIB:** Identificación de patrones de coordinación técnica, ráfagas temporales y sincronización de dispositivos.
- **Identidades Vinculadas (Sockpuppets):** Uso de estilometría profunda (RoBERTa) para vincular cuentas aparentemente independientes.
- **Análisis Multimodal y Multifuente:** Alineación de señales de **Twitter/X** y **Telegram** mediante similitud semántica visual (CLIP) y lingüística.
- **Clasificación de Veracidad:** Detección de Fake News en salud mediante modelos transformadores SOTA.

## Estructura del Sistema
- `src/deepsocial/data`: Motores de ingesta y alineación de fuentes (X + Telegram).
- `src/deepsocial/features`: Extractores de rasgos (Estilometría, Visual CLIP, Comportamiento Temporal, Veracidad).
- `src/deepsocial/models`: Motor de fusión de señales y generación de informes de riesgo.

## Instalación rápida
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
source .venv/bin/activate
```

---
*Investigación académica sobre desinformación y comportamiento coordinado en el ámbito de la salud.*
