from deep_translator import GoogleTranslator
import speech_recognition as sr
import keyboard
import pyttsx3

# Dicionário de idiomas suportados.
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

#Reconhece a fala e retorna a frase capturada no idioma especificado.
def reconhecer_fala(rec, language):
    while True:
        with sr.Microphone() as mic:
            rec.adjust_for_ambient_noise(mic)
            print("Pressione 'r' para começar a escutar.")
            keyboard.wait('r')
            print("Escutando...")
            audio = rec.listen(mic)
            print("Parando a escuta...")
        try:
            Frase = rec.recognize_google(audio, language=language)
            print(f"Você disse: {Frase}")
            print("Confirme se a transcrição está correta (sim/não): ")
            confirmacao = input().strip().lower()
            if confirmacao == "sim":
                return Frase
            else:
                print("Por favor, fale novamente.")
        except sr.UnknownValueError:
            print("Não foi possível entender o áudio. Por favor, tente novamente.")
        except sr.RequestError as e:
            print(f"Erro ao solicitar resultados do serviço de reconhecimento de fala: {e}")
            return None
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return None

#Fala o texto traduzido com a pyttsx3.        
def falar_traducao(engine, texto):
    engine.say(texto)
    engine.runAndWait()

#Captura o idioma de origem via áudio.
def source_do_audio():
    rec = sr.Recognizer()
    print("Diga o idioma de origem (por exemplo, inglês, português): ")
    id_source = reconhecer_fala(rec, "pt").lower()
    
    if id_source in Linguagens_suportadas:
        return Linguagens_suportadas[id_source]
    else:
        print("Desculpe, o idioma não é suportado ou não foi reconhecido.")
        return None

#Traduz texto digitado pelo usuário e oferece a opção de ouvir a tradução.
def traduzir_txt():
    text = input("Digite o texto que você deseja traduzir: ")
    linguagem_target = input("Digite o idioma de destino: ").strip().lower()

    if linguagem_target in Linguagens_suportadas:
        codigo_target = Linguagens_suportadas[linguagem_target]
        txt_traduzido = GoogleTranslator(target=codigo_target).translate(text)
        print(f"Tradução para {linguagem_target.capitalize()}: {txt_traduzido}")
        
        # Perguntar se o usuário deseja ouvir a tradução
        falar_S_ou_N = input("Deseja ouvir a tradução em áudio? (sim/não): ").strip().lower()
        if falar_S_ou_N == 'sim':
            engine = pyttsx3.init()
            falar_traducao(engine, txt_traduzido)
    else:
        print("Desculpe, o idioma não é suportado ou não foi reconhecido.")

#Traduz áudio um capturado do usuário.
def traduzir_audio():
    rec = sr.Recognizer()
    engine = pyttsx3.init()

    source = source_do_audio()

    if source:
        print("Diga algo para traduzir:")
        text = reconhecer_fala(rec, source)

        linguagem_target = input("Digite o idioma de destino: ").strip().lower()

        if linguagem_target in Linguagens_suportadas:
            codigo_target = Linguagens_suportadas[linguagem_target]
            txt_traduzido = GoogleTranslator(source=source, target=codigo_target).translate(text)
            print(f"Tradução para {linguagem_target.capitalize()}: {txt_traduzido}")
            
            # Perguntar se o usuário deseja ouvir a tradução
            falar_S_ou_N = input("Deseja ouvir a tradução em áudio? (sim/não): ").strip().lower()
            if falar_S_ou_N == 'sim':
                engine = pyttsx3.init()
                falar_traducao(engine, txt_traduzido)
        else:
            print("Desculpe, o idioma não é suportado ou não foi reconhecido.")
    else:
        print("Idioma de origem não reconhecido.")

#Função principal para mostrar o menu e processar as entradas do usuário.
def main():
    while True:
        print("\n[1] Traduzir\n[2] Lista de Idiomas\n[3] Sair")
        comando = input("Digite o comando: ").strip()

        if comando == '1':
            while True:
                print("Como quer traduzir?")
                opcao = input("[1] Texto\n[2] Áudio\n[3] Voltar\n").strip()

                if opcao == '1':
                    traduzir_txt()
                elif opcao == '2':
                    traduzir_audio()
                elif opcao == '3':
                    break
                else:
                    print("Opção inválida. Tente novamente.")
        elif comando == '2':
            print("\nIdiomas disponíveis:")
            for lingua in Linguagens_suportadas:
                print(f"- {lingua.capitalize()}")
        elif comando == '3':
            print("Encerrando o programa...")
            break
        else:
            print("Comando inválido. Tente novamente.")

if __name__ == "__main__":
    main()
