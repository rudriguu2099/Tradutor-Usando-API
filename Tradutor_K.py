from deep_translator import GoogleTranslator

def traduzir_txt():
    Linguagens_suportadas = {
        "english": "en",
        "portuguese": "pt",
        "spanish": "es",
        "french": "fr",
        "german": "de",
        "italian": "it",
        "japanese": "ja",
        "chinese": "zh",
        "russian": "ru"
    }
    
    text = input("Digite o texto que você deseja traduzir: ")

    print("Idiomas disponíveis:")
    for ling in Linguagens_suportadas:
        print(f"- {ling.capitalize()}")

    linguagem_target = input("Digite o idioma de destino (em inglês): ").strip().lower()

    if linguagem_target in Linguagens_suportadas:
        codigo_target = Linguagens_suportadas[linguagem_target]
        txt_traduzido = GoogleTranslator(target=codigo_target).translate(text)
        print(f"Tradução para {linguagem_target.capitalize()}: {txt_traduzido}")
    else:
        print("Desculpe, o idioma não é suportado ou não foi reconhecido.")

traduzir_txt()
