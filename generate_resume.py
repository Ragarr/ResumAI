import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from src.tools.excel_to_markdown import excel_to_markdown

# Cargar variables desde el archivo .env
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# Función para leer archivos externos
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def main(candidate_excel, job_offer_file, output_path):
    # Cargar prompts desde ficheros externos
    system_prompt = read_file("src/prompts/system_prompt.txt")
    user_prompt_template = read_file("src/prompts/user_prompt.txt")

    # Convertir Excel del candidato a Markdown
    print("🔄 Procesando Excel del candidato...")
    candidate_info = excel_to_markdown(candidate_excel)

    # Leer oferta laboral
    print("🔄 Leyendo oferta laboral...")
    job_offer = read_file(job_offer_file)

    # Formatear el prompt del usuario
    user_prompt = user_prompt_template.format(
        candidate_info=candidate_info,
        job_offer=job_offer
    )

    print("🔄 Generando CV optimizado...")
    # Solicitud a OpenAI (API >= 1.0.0)
    response = client.chat.completions.create(
        model="gpt-4-turbo",  # Ajusta al modelo disponible (ej. gpt-4o)
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.2,
        max_tokens=2000
    )

    # Obtener respuesta generada (CV)
    generated_cv = response.choices[0].message.content

    # Guardar el CV generado en un archivo markdown
    with open(output_path, "w", encoding='utf-8') as f:
        f.write(generated_cv)

    print(f"✅ CV generado exitosamente en: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generar currículum optimizado desde Excel y oferta laboral.")
    parser.add_argument("-e", "--excel", type=str, required=True, help="Ruta al archivo Excel con datos del candidato.")
    parser.add_argument("-o", "--offer", type=str, required=True, help="Ruta al archivo con la descripción del puesto (txt).")
    parser.add_argument("--output", type=str, default="generated_resume.md", help="Ruta de salida para el CV generado.")

    args = parser.parse_args()

    main(args.excel, args.offer, args.output)
