# ResumAI: Generador Automático de Currículums

ResumAI es un proyecto diseñado para generar automáticamente un currículum optimizado a partir de datos estructurados del candidato (en un archivo Excel) y una oferta de trabajo. El sistema utiliza la API de OpenAI (GPT-4) para procesar la información y generar un CV en formato Markdown, siguiendo instrucciones precisas y asegurando que sólo se utilicen los datos verificados del candidato.

---

## Tabla de Contenidos

- [ResumAI: Generador Automático de Currículums](#resumai-generador-automático-de-currículums)
  - [Tabla de Contenidos](#tabla-de-contenidos)
  - [Descripción](#descripción)
  - [Características](#características)
  - [Estructura del Proyecto](#estructura-del-proyecto)
  - [Requisitos](#requisitos)
  - [Instalación](#instalación)
  - [Uso](#uso)
    - [Ejemplo de uso desde la línea de comandos:](#ejemplo-de-uso-desde-la-línea-de-comandos)
  - [Personalización de Prompts](#personalización-de-prompts)
  - [Notas Adicionales](#notas-adicionales)
  - [Licencia](#licencia)

---

## Descripción

Este proyecto tiene como objetivo automatizar el proceso de generación de un currículum vitae (CV) optimizado para ofertas de trabajo específicas. Se aprovechan dos fuentes principales de datos:

1. **Datos del Candidato:** Un archivo Excel que contiene información detallada (educación, experiencia, proyectos, certificaciones, habilidades, etc.). Los datos se convierten a Markdown mediante un módulo personalizado.
2. **Oferta Laboral:** Un archivo de texto (o PDF convertido a texto) que contiene la descripción del puesto, requisitos y otras características.

El sistema extrae los datos verificados del candidato y, mediante prompts configurados, genera un CV profesional y compatible con sistemas de seguimiento de candidatos (ATS).

---

## Características

- **Integración con la API de OpenAI (GPT-4):** Genera currículums utilizando inteligencia artificial.
- **Entrada de Datos Estructurada:** Los datos del candidato se suministran en un archivo Excel.
- **Prompts Externos:** Los mensajes del sistema y del usuario se encuentran en archivos externos, facilitando actualizaciones y personalización.
- **Conversión de Excel a Markdown:** Uso de un módulo personalizado (`excel_to_markdown`) para convertir la información del Excel a formato Markdown.
- **Soporte para Argumentos de Línea de Comandos:** Permite especificar la ubicación del archivo Excel y la oferta laboral mediante opciones cortas (`-e`, `-o`) y largas (`--excel`, `--offer`).
- **Exportación del CV en Formato Markdown:** El currículum generado se guarda en un archivo Markdown listo para su edición o exportación.

---

## Estructura del Proyecto

```
ResumAI/
├── .env                        # Archivo de configuración con la clave API
├── requirements.txt            # Archivo con todas las dependencias necesarias
├── generate_resume.py          # Script principal para generar el CV
└── src/
    ├── tools/
    │   └── excel_to_markdown.py  # Módulo para convertir Excel a Markdown
    └── prompts/
        ├── system_prompt.txt   # Archivo con el prompt del sistema
        └── user_prompt.txt     # Archivo con el prompt del usuario (con placeholders)
```

---

## Requisitos

- **Python 3.7 o superior**
- **pip** (gestor de paquetes de Python)
- Dependencias listadas en [requirements.txt](requirements.txt)

---

## Instalación

1. **Clona el repositorio o descarga el proyecto.**

2. **Instala las dependencias:**

   Abre la terminal y ejecuta:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configura la clave API de OpenAI:**
   
   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (reemplaza `TU_CLAVE_API` por tu clave real):

   ```env
   OPENAI_API_KEY=TU_CLAVE_API
   ```

4. **Verifica que la estructura del proyecto coincide con la mostrada en [Estructura del Proyecto](#estructura-del-proyecto).**

---

## Uso

El script principal es `generate_resume.py` y genera un currículum optimizado utilizando la información del candidato y la oferta laboral.

### Ejemplo de uso desde la línea de comandos:

Utilizando las opciones cortas `-e` y `-o`:

```bash
python generate_resume.py -e candidate_info.xlsx -o offer.txt
```

También puedes especificar la ruta de salida para el CV generado con la opción `--output`:

```bash
python generate_resume.py -e candidate_info.xlsx -o offer.txt --output generated_resume.md
```

El script realiza los siguientes pasos:
- Convierte el Excel con `excel_to_markdown` a formato Markdown.
- Carga los prompts desde `src/prompts/system_prompt.txt` y `src/prompts/user_prompt.txt`.
- Rellena los placeholders del prompt del usuario con la información del candidato y la oferta laboral.
- Envía la solicitud a la API de OpenAI (modelo GPT-4-turbo).
- Guarda el currículum generado en un archivo Markdown.

---

## Personalización de Prompts

Los mensajes de sistema y de usuario se encuentran en los siguientes archivos:

- **`src/prompts/system_prompt.txt`**  
  Define el rol de la IA y las reglas estrictas que debe seguir (por ejemplo, no inventar datos, uso del idioma de la oferta, etc.).

- **`src/prompts/user_prompt.txt`**  
  Contiene los placeholders `{candidate_info}` y `{job_offer}` que se reemplazarán dinámicamente con la información real.

Puedes editar estos archivos para ajustar el comportamiento de la generación del currículum según tus necesidades.

---

## Notas Adicionales

- **Migración API:** El código está adaptado para funcionar con la versión >= 1.0.0 de la librería `openai`. Si encuentras problemas, asegúrate de tener la versión correcta instalada.
- **Módulo `excel_to_markdown`:** Puedes personalizarlo según la estructura de tu archivo Excel.
- **Seguridad:** Asegúrate de mantener tu archivo `.env` seguro y de no compartirlo públicamente.

---

## Licencia

Este proyecto es de código abierto. Puedes utilizarlo, modificarlo y distribuirlo conforme a los términos de la licencia que elijas.
