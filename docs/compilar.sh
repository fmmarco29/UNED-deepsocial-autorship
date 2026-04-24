#!/bin/bash
# =======================================================
# Compilación automática LaTeX + Biber (UNED / TFM)
# Autor: Fernando Martínez Marco
# Fecha: 2025
# Versión: SEGURA (no borra .bib, .tex ni .pdf)
# =======================================================

echo "🧠 Compilador LaTeX + Biber (versión interactiva y segura)"
echo "----------------------------------------------------------"

# Solicita el nombre del archivo .tex
read -p "📄 Introduce el nombre del archivo principal (sin .tex): " DOC

# Verifica si el archivo existe
if [ ! -f "$DOC.tex" ]; then
    echo "❌ Error: No se encontró el archivo '$DOC.tex' en el directorio actual."
    exit 1
fi

echo "🚀 Iniciando compilación de '$DOC.tex' ..."
echo "------------------------------------------"

# 1️⃣ Primera compilación LaTeX (genera .bcf)
pdflatex -interaction=nonstopmode "$DOC.tex"

# 2️⃣ Compilación de bibliografía con Biber
biber "$DOC"

# 3️⃣ Segunda compilación para integrar las citas
pdflatex -interaction=nonstopmode "$DOC.tex"

# 4️⃣ Tercera compilación para ajustar referencias cruzadas
pdflatex -interaction=nonstopmode "$DOC.tex"

# 5️⃣ Limpieza opcional (archivos auxiliares)
read -p "🧹 ¿Deseas eliminar los archivos auxiliares (.aux, .log, .bcf, etc.)? [s/n]: " LIMPIAR
if [[ "$LIMPIAR" == "s" || "$LIMPIAR" == "S" ]]; then
    echo "🧽 Eliminando archivos auxiliares..."
    # Lista segura: solo archivos auxiliares conocidos
    AUX_FILES=(
        "$DOC.aux" "$DOC.bbl" "$DOC.bcf" "$DOC.blg" "$DOC.log" "$DOC.out"
        "$DOC.run.xml" "$DOC.toc" "$DOC.lof" "$DOC.lot" "$DOC.lol"
        "$DOC.acn" "$DOC.glo" "$DOC.ist" "$DOC.fls" "$DOC.fdb_latexmk"
        "$DOC.synctex.gz" "$DOC.nav" "$DOC.snm" "$DOC.vrb"
        "$DOC.idx" "$DOC.ilg" "$DOC.ind" "$DOC.brf"
    )

    for f in "${AUX_FILES[@]}"; do
        if [ -f "$f" ]; then
            rm -f "$f"
        fi
    done

    echo "✅ Archivos auxiliares eliminados correctamente."
    echo "⚠️  Archivos principales conservados: $DOC.tex, $DOC.pdf, *.bib"
fi

echo "🎓 Compilación completada con éxito."
echo "📘 Documento final generado: $DOC.pdf"

