from deep_translator import GoogleTranslator

tradutor = GoogleTranslator(source="auto", target="en")

texto = input("digite aqui o que vc quer traduzir: ")

traducao = tradutor.translate(texto)

print(f"Sua frase em traduzida é \"{traducao}\"")