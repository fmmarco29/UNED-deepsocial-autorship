# Health-CIB: Multimodal Authorship & Veracity Detection

[![Code Quality](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions/workflows/ci.yml/badge.svg)](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)

Este repositorio contiene el desarrollo de la PEC 4 del Máster en Investigación en IA (IAI). El proyecto implementa un sistema dual para la detección de **comportamiento coordinado inauténtico** (CIB) y la clasificación de **noticias falsas** (Fake News) en el ámbito de la salud.

## Objetivos
- **Detección de Veracidad:** Clasificación de contenidos de salud mediante modelos transformadores especializados en Fake News (español).
- **Detección de Autoría:** Identificación de identidades vinculadas (*sockpuppets*) mediante estilometría profunda con RoBERTa.
- **Análisis Multimodal:** Detección de coordinación visual en infografías mediante modelos CLIP.
- **Análisis Multifuente:** Estudio de la propagación coordinada entre Twitter/X y Telegram.
- **Modelado Comportamental:** Identificación de ráfagas temporales y sincronización técnica de cuentas.

## Stack Tecnológico
- **Lenguaje:** Python 3.11+
- **Modelos:** 
  - NLP Veracidad: `roberta-base-bne-fake-news-detection`.
  - NLP Estilometría: `roberta-base-bne` (Representación densa).
  - Vision: `OpenCLIP` (Similitud semántica de imágenes).
- **MLOps:** `uv` para gestión de dependencias, `Ruff` para calidad de código y GitHub Actions para CI/CD.

## Estructura del Proyecto
- `src/deepsocial/data`: Motores de adquisición multifuente y protocolos de ingesta.
- `src/deepsocial/features`: Extractores de rasgos (Veracidad, Estilometría, Visual, Comportamiento).
- `src/deepsocial/models`: Motores de fusión de señales y generación de reportes forenses.
- `configs/`: Gestión centralizada de parámetros de investigación.

## Instalación rápida
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv sync
source .venv/bin/activate
```

---
*Investigación académica sobre desinformación y comportamiento coordinado en salud.*
