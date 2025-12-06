# Password Security Analyzer

Ferramenta Python para análise de segurança de senhas e verificação de vazamentos.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![Security](https://img.shields.io/badge/Security-Password_Checker-red.svg)
![API](https://img.shields.io/badge/API-HaveIBeenPwned-green.svg)

## Funcionalidades

- **Análise de força de senhas** - Baseada em múltiplos critérios
- **Verificação de vazamentos** - Consulta à API do Have I Been Pwned
- **Feedback detalhado** - Recomendações para melhorar a senha
- **Modo interativo** - Para testes e demonstrações
- **Proteção de privacidade** - Usa hash SHA-1 (nunca envia a senha completa)

## Tecnologias

- **Python 3.6+**
- **Requests** - Para chamadas à API
- **Hashlib** - Para hashing seguro de senhas
- **Have I Been Pwned API** - Base de dados de vazamentos

## Instalação

```bash
# Clone o repositório
git clone https://github.com/Erickmateus10/password-security-tool.git

# Entre na pasta
cd password-security-tool

# Instale as dependências
pip install -r requirements.txt
```

## Como Usar

### Modo Interativo
```bash
python password_checker.py
```

### Analisar uma senha específica
```bash
python password_checker.py --senha "sua_senha_aqui"
```

## Exemplo de Saída

```
📊 ANÁLISE DE FORÇA:
   • Nível: 🔒 FORTE
   • Pontuação: 6/6
   • Critérios atendidos: 5/5

🔍 VERIFICANDO VAZAMENTOS...
   ✅ Esta senha não foi encontrada em vazamentos conhecidos
```

## Casos de Uso

- **Usuários comuns** - Verificar segurança de suas senhas
- **Administradores de sistema** - Validar políticas de senha
- **Desenvolvedores** - Implementar verificações em aplicações
- **Conscientização** - Educar sobre segurança de credenciais

## Como Funciona a Verificação de Vazamentos

1. A senha é convertida em **hash SHA-1**
2. Apenas os **5 primeiros caracteres** do hash são enviados à API
3. A API retorna uma lista de hashes que começam com esse prefixo
4. O programa verifica localmente se o hash completo está na lista
5. **A senha nunca é transmitida completa**

## Estrutura do Projeto

```
password-security-tool/
├── 📄 password_checker.py   
├── 📄 requirements.txt      
└── 📄 README.md            
```

## Aviso de Segurança

Esta ferramenta é para **fins educacionais e de conscientização**. 
- Nunca use senhas reais que você ainda utiliza
- A ferramenta é segura (usa hashing), mas sempre tenha cautela
- Use senhas diferentes para cada serviço
- Considere usar um gerenciador de senhas
  

## Autor

**Erick Mateus** 
GitHub: [@Erickmateus10](https://github.com/Erickmateus10)

