# 🎙️ Tradutor de Voz e Texto Multilíngue

Um tradutor interativo em Python que reconhece fala, traduz texto ou áudio entre vários idiomas e pode reproduzir a tradução em voz alta.  

## 🚀 Funcionalidades
- 🎧 **Reconhecimento de fala** usando o microfone (via `speech_recognition`).  
- 🌍 **Tradução automática** com o `deep_translator` (Google Translate).  
- 🔊 **Síntese de voz** com `pyttsx3` para ouvir o resultado da tradução.  
- 🧠 **Suporte a múltiplos idiomas**, incluindo inglês, português, espanhol, francês, alemão, italiano, japonês, chinês e russo.  
- 🖱️ Interface simples por terminal, com menus interativos e controle via teclado.

## 🧩 Dependências
Instale os pacotes necessários com:
```bash
pip install deep-translator speechrecognition keyboard pyttsx3
```

> 💡 É necessário ter o **microfone configurado** corretamente para usar o modo de tradução por voz.

## 🕹️ Como usar
Execute o programa:
```bash
python tradutor.py
```

Escolha uma das opções do menu:
1. **Traduzir** → escolha entre texto ou áudio.  
2. **Lista de idiomas** → mostra todos os idiomas suportados.  
3. **Sair** → encerra o programa.  

Durante o uso:
- Pressione **“r”** para começar a gravar no modo de áudio.  
- Confirme a transcrição antes da tradução.  
- Escolha se deseja **ouvir a tradução em voz alta**.  

## 📚 Exemplo de uso
```
[1] Traduzir
[2] Lista de Idiomas
[3] Sair
Digite o comando: 1
Como quer traduzir?
[1] Texto
[2] Áudio
[3] Voltar
```

## 🛠️ Autor
Desenvolvido em Python para fins de estudo e demonstração de reconhecimento de fala, tradução e síntese de voz.
