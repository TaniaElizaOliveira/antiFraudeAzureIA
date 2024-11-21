
# AntiFraudeAzureIA

Este é um projeto desenvolvido para detectar fraudes utilizando a inteligência artificial do **Azure Cognitive Services**. O sistema realiza o upload de imagens de cartões de crédito, valida as informações e identifica se o cartão é válido ou inválido.

## 📋 Funcionalidades

- **Upload de Imagens**: Permite o envio de imagens de cartões de crédito.
- **Análise com Azure AI**: Utiliza o serviço **Document Intelligence** do Azure para extrair e validar informações de cartões de crédito.
- **Interface Intuitiva**: Desenvolvido com **Streamlit**, proporcionando uma interface amigável.
- **Armazenamento em Azure Blob Storage**: As imagens são armazenadas de forma segura na nuvem.

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Streamlit**: Interface interativa.
- **Azure Blob Storage**: Armazenamento de arquivos.
- **Azure AI Document Intelligence**: Para validação e extração de informações dos cartões.
- **Bibliotecas**:
  - `azure-ai-formrecognizer`
  - `azure-storage-blob`
  - `streamlit`
  - `python-dotenv`

---

## ⚙️ Instalação e Configuração

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/AntiFraudeAzureIA.git
cd AntiFraudeAzureIA

