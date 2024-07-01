from deep_translator import GoogleTranslator

def traduzir_txt():
    Linguagens_suportadas = {
        "inglês": "en",
        "português": "pt",
        "espanhol": "es",
        "francês": "fr",
        "alemão": "de",
        "italiano": "it",
        "japonês": "ja",
        "chinês": "zh",
        "russo": "ru"
    }
    print("[1] Traduzir\n[2] Lista de Idiomas\n[3] Sair")
    while True:
        comando = input("\nDigite o comando: ").strip()
        if comando == '1':
            text = input("Digite o texto que você deseja traduzir: ")
            linguagem_target = input("Digite o idioma de destino: ").strip().lower()
            if linguagem_target in Linguagens_suportadas:
                codigo_target = Linguagens_suportadas[linguagem_target]
                txt_traduzido = GoogleTranslator(target=codigo_target).translate(text)
                print(f"Tradução para {linguagem_target.capitalize()}: {txt_traduzido}")
            else:
                print("Desculpe, o idioma não é suportado ou não foi reconhecido.")
        if comando == '2':
            print()
            print("Idiomas disponíveis:")
            for ling in Linguagens_suportadas:
                print(f"- {ling.capitalize()}")
        if comando == '3':
            print("Encerrando o programa...")
            break

traduzir_txt()
