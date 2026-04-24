# Health-CIB: Multimodal Authorship & Veracity Detection

[![Code Quality](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions/workflows/ci.yml/badge.svg)](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)

Este repositorio contiene el desarrollo de la PEC 4 del Máster en Investigación en IA (IAI). El proyecto implementa un sistema dual para la detección de **Comportamiento Coordinado Inauténtico (CIB)** y la clasificación de **Fake News** en salud.

### Conceptos Clave

#### 1. CIB (Coordinated Inauthentic Behavior)
El **CIB** se refiere a campañas organizadas donde grupos de cuentas o páginas colaboran de forma síncrona para engañar a los usuarios sobre su identidad o sus objetivos. El sistema analiza la **coordinación técnica** (ráfagas temporales, sincronización de dispositivos y reutilización de imágenes) entre múltiples plataformas.

#### 2. Fake News (Detección de Veracidad)
Las **Fake News** o noticias falsas son contenidos creados deliberadamente para desinformar. En este estudio, nos centramos en el ámbito de la **salud y la pseudociencia**. El sistema utiliza modelos de lenguaje (Transformers) ajustados para clasificar la veracidad del mensaje, contrastándolo con patrones lingüísticos típicos de la desinformación en español.

## Objetivos del Proyecto
- **Análisis de Veracidad:** Detección de Fake News en salud mediante el modelo `roberta-base-bne-fake-news-detection`.
- **Detección de CIB:** Identificación de patrones de coordinación técnica y ráfagas de actividad síncrona.
- **Identidades Vinculadas (Sockpuppets):** Vinculación de cuentas en **Twitter/X** y **Telegram** mediante estilometría profunda.
- **Análisis Multimodal:** Comparación de similitud semántica en infografías mediante modelos CLIP.

## Estructura del Sistema
- `src/deepsocial/data`: Motores de ingesta y alineación de fuentes multifuente.
- `src/deepsocial/features`: Extractores de rasgos (Veracidad, Estilometría, Visual CLIP, Comportamiento).
- `src/deepsocial/models`: Motor de fusión de señales y generación de reportes forenses.

## Instalación rápida
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
source .venv/bin/activate
```

---
*Investigación académica sobre desinformación y comportamiento coordinado en salud.*
