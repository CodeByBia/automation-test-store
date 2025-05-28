# automation-test-store
Este é um projeto de automatização para o curso de Testes de Software da empresa Softex

Este projeto utiliza **Python**, **Behave** (BDD) e **Selenium** para automação de testes.

## 🛠️ Pré-requisitos

- Python 3.x
- pip
- Google Chrome (ou outro navegador)
- ChromeDriver (ou outro driver compatível com o navegador)

## ⚙️ Como configurar o ambiente

### 1. Clone o repositório

```bash
git clone <URL-do-repositório>
cd <nome-do-repositório>
```
### 2. Crie e ative o ambiente virtual
Windows
```bash
python -m venv venv
venv\Scripts\activate
```
Linux/MacOS
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Como executar os testes
Para rodar todos os testes:
```bash
behave
```
Para rodar testes com uma tag específica:
```bash
behave -t "@test"
```
