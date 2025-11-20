# auto-login
# 🤖 Bot de Login Automático (RPA)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![Edge WebDriver](https://img.shields.io/badge/Browser-Edge-0078D7?style=for-the-badge&logo=microsoft-edge&logoColor=white)
![Status](https://img.shields.io/badge/Status-Funcional-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

> **Automação profissional de login em portais web utilizando Selenium WebDriver e Python.**

---

## 📄 Descrição

Este projeto é uma solução completa de **RPA (Robotic Process Automation)** para realizar login de forma **automática, segura e confiável**.

### Principais Diferenciais:

- ✅ **Segurança:** Uso de variáveis de ambiente para proteger credenciais, sem senhas hardcoded.  
- ✅ **Estabilidade:** Implementação de *Explicit Waits* (`WebDriverWait`) para evitar erros de elementos não carregados.  
- ✅ **Persistência:** O navegador permanece aberto após a execução (`detach: True`) para verificação humana ou continuação do fluxo.  
- ✅ **Modularidade:** Código organizado em funções, fácil de expandir para outros portais.  

---

## 🚀 Tecnologias Utilizadas

- **Python 3.14+**  
- **Selenium WebDriver 4+**  
- **Microsoft Edge WebDriver**  
- **Biblioteca OS** (Gerenciamento de variáveis de ambiente)  

---

## ⚙️ Pré-requisitos

Antes de iniciar, você precisa ter instalado:

1. [Python](https://www.python.org/downloads/)  
2. Navegador **Microsoft Edge**  
3. Git  

---

## 🔧 Instalação e Uso

### 1. Clone o repositório
```bash
git clone https://github.com/jhonileon-alves/auto-login.git
cd auto-login
```

### 2. Crie um ambiente virtual (Opcional, mas recomendado)
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências
```bash
pip install selenium
```

### 4. Configure as Credenciais
**Windows (PowerShell)**:
```powershell
$env:TEST_USER="seu_usuario"
$env:TEST_PASS="sua_senha"
```

**Windows (CMD)**:
```cmd
set TEST_USER=seu_usuario
set TEST_PASS=sua_senha
```

**Linux / Mac**:
```bash
export TEST_USER="seu_usuario"
export TEST_PASS="sua_senha"
```

### 5. Execute o Bot
```bash
python main.py
```

---

## 🧠 Estrutura do Código

O script principal utiliza **WebDriverWait** para garantir estabilidade na automação:

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Espera explícita para garantir carregamento do elemento
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.NAME, 'user')))
```

---

## 🤝 Contribuição

Sinta-se à vontade para fazer **fork**, abrir **issues** ou submeter **pull requests**.  

---

## 👨‍💻 Autor

**Jhoni Leon**  
- [GitHub](https://github.com/jhonileon-alves)  
- Email: [jhoni.leon.alves@gamil.com](mailto:jhoni.leon.alves@gamil.com)  
