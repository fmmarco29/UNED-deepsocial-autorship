# DeepSocial: Multimodal Authorship & Coordination Detection

[![Code Quality](https://github.com/tu-usuario/deepsocial/actions/workflows/ci.yml/badge.svg)](https://github.com/tu-usuario/deepsocial/actions)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Este repositorio contiene el desarrollo de la **PEC 4** del Máster en Investigación en IA (IAI), enfocado en los objetivos del proyecto **DeepSocial (UNED NLP&IR)**.

## 🎯 Objetivos
- **Dataset Multimodal:** Creación de un conjunto de datos que integra señales de texto, imágenes y metadatos de comportamiento.
- **Authorship Attribution:** Identificación de perfiles pertenecientes a un mismo autor (*sockpuppets*).
- **Behavioral Analysis:** Modelado de patrones de publicación para detectar desinformación organizada y grupos coordinados.

## 🛠️ Stack Tecnológico
- **Lenguaje:** Python 3.11+
- **Gestión de paquetes:** [uv](https://github.com/astral-sh/uv)
- **Modelos:** 
  - NLP: `RoBERTa-base-bne` (Spanish) para estilometría.
  - Vision: `OpenCLIP` para embeddings visuales.
- **MLOps:** `DVC` para versionado de datos, `Ruff` para calidad de código.

## 🚀 Instalación rápida
```bash
# Instalar uv si no lo tienes
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar dependencias
uv sync

# Activar entorno
source .venv/bin/activate
```

## 📂 Estructura del proyecto
- `src/deepsocial/features`: Extractores de señales (Estilometría, Visual, Comportamiento).
- `data/`: Versionado con DVC (raw vs processed).
- `configs/`: Gestión de hiperparámetros con Hydra.

---
*Desarrollado para la convocatoria de investigador del proyecto DeepSocial.*
