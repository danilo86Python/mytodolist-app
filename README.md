# 📝 MyTodolist App — Gerenciador de Tarefas em FreeSimpleGUI

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Interface](https://img.shields.io/badge/UI-FreeSimpleGUI-9cf)
![Status](https://img.shields.io/badge/status-Em_desenvolvimento-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

> **MyTodolist App** é uma aplicação simples e funcional desenvolvida em **Python** com **FreeSimpleGUI**, projetada para desktop.  
> O aplicativo permite **adicionar, editar e excluir tarefas**, salvando os dados automaticamente em um arquivo externo.

---

## 🧠 Sobre o projeto

O **MyTodolist App** foi criado para oferecer uma experiência prática e direta na gestão de tarefas.  
Ele permite ao usuário:
- ➕ **Adicionar** novas tarefas através de um campo de texto.  
- ✏️ **Editar** uma tarefa já existente.  
- 🗑️ **Excluir** tarefas concluídas ou desnecessárias.  

Todas as alterações são salvas automaticamente em um arquivo de texto (`todos.txt`), garantindo que nenhuma informação seja perdida entre execuções.

---

## 🧩 Estrutura do projeto

```
mytodolist-app/
├── dist/              # Pasta com o executável do app (.exe)
├── gui.py             # Interface gráfica (FreeSimpleGUI)
├── functions.py       # Manipulação de dados (ler/gravar tarefas)
├── cli.py             # Backend funcional da aplicação
├── exe.py             # Personalização do executável
├── add.png            # Ícone do botão "Adicionar"
├── edit.png           # Ícone do botão "Editar"
├── complete.png       # Ícone do botão "Excluir"
├── todos.txt          # Arquivo de texto com as tarefas salvas
├── requirements.txt   # Dependências Python
└── readme.md          # Documentação do projeto
```

---

## ⚙️ Instalação e execução (modo desenvolvedor)

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/danilo86Python/mytodolist-app.git
   cd mytodolist-app
   ```

2. **Crie o ambiente virtual:**
   ```bash
   python -m venv venv
   venv\Scripts\activate     # (Windows)
   source venv/bin/activate  # (Linux/Mac)
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o aplicativo:**
   ```bash
   python gui.py
   ```

---

## 💾 Executável pronto (modo usuário final)

Na pasta **`dist`**, há um arquivo **`.exe`** que permite executar o app **sem precisar do Python instalado**.

Para usar:
1. Baixe a pasta `dist/` e o arquivo `todos.txt`.  
2. Coloque-os no mesmo diretório.  
3. Execute o arquivo `.exe`.  

---

## 🛠️ Tecnologias utilizadas

- **Python 3.13+**
- **FreeSimpleGUI**
- **PyInstaller**
- **Manipulação de arquivos (.txt)**

---

## 🚧 Status do projeto

> 🟡 Aplicativo em desenvolvimento.  
> Novos recursos e melhorias visuais serão adicionados em futuras versões.

---

## 📜 Licença

Distribuído sob a **Licença MIT**.  
Este projeto é de código aberto e pode ser utilizado livremente para fins educacionais e de aprendizado.

---

## 👨‍💻 Autor

**Danilo Santos**  
🐙 [GitHub](https://github.com/danilo86Python)  
🌐 [Repositório do Projeto](https://github.com/danilo86Python/mytodolist-app.git)

---

⭐ Se este projeto foi útil para você, deixe uma estrela no repositório!
