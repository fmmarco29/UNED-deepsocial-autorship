# DeepSocial: Multimodal Authorship & Coordination Detection

[![Code Quality](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions/workflows/ci.yml/badge.svg)](https://github.com/fmmarco29/UNED-deepsocial-autorship/actions)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/release/python-3110/)

Este repositorio contiene el desarrollo de la PEC 4 del Máster en Investigación en IA (IAI). El proyecto se centra en la identificación de **identidades vinculadas** (*sockpuppets*) y comportamiento coordinado inauténtico en redes sociales.

## Objetivos
- **Detección de Autoría:** Identificación de perfiles operados por un mismo actor mediante estilometría profunda.
- **Análisis Multimodal:** Comparación de similitud semántica en infografías e imágenes mediante modelos CLIP.
- **Análisis Multifuente:** Estudio de la coordinación cross-platform entre Twitter/X y Telegram.
- **Modelado Comportamental:** Detección de ráfagas temporales y huellas digitales de dispositivos.

## Stack Tecnológico
- **Lenguaje:** Python 3.11+
- **Modelos:** 
  - NLP: `RoBERTa-base-bne` (Spanish Stylometry).
  - Vision: `OpenCLIP` (Image Similarity).
- **MLOps:** `uv` para gestión de dependencias, `Ruff` para calidad de código y GitHub Actions para CI/CD.

## Instalación rápida
```bash
# Instalar uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias
uv sync

# Activar entorno
source .venv/bin/activate
```

## Estructura del Proyecto
- `src/deepsocial/data`: Motores de adquisición multifuente.
- `src/deepsocial/features`: Extractores de rasgos (Estilometría, Visual, Comportamiento).
- `configs/`: Gestión de parámetros de búsqueda y procesamiento.

---
*Investigación académica sobre desinformación en el ámbito de la salud y pseudociencia.*
