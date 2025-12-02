#!/usr/bin/env python3
"""
PASSWORD SECURITY ANALYZER - v1.0
Autor: Erick Mateus
Descrição: Ferramenta para análise de segurança de senhas
"""

import hashlib
import requests
import re
import argparse
from datetime import datetime

def banner():
    print("""
    ╔══════════════════════════════════════════╗
    ║           PASSWORD SECURITY TOOL         ║
    ║            Cybersecurity Tool            ║
    ╚══════════════════════════════════════════╝
    """)

def calcular_forca_senha(senha):
    """Calcula a força da senha baseada em múltiplos critérios"""
    pontuacao = 0
    feedback = []
    
    # Critérios de segurança
    criterios = {
        'min_length': len(senha) >= 8,
        'has_upper': any(c.isupper() for c in senha),
        'has_lower': any(c.islower() for c in senha),
        'has_digit': any(c.isdigit() for c in senha),
        'has_special': bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', senha))
    }
    
    # Pontuação base
    for criterio, atendido in criterios.items():
        if atendido:
            pontuacao += 1
        else:
            if criterio == 'min_length':
                feedback.append("❌ Muito curta (mínimo 8 caracteres)")
            elif criterio == 'has_upper':
                feedback.append("❌ Adicione letras maiúsculas")
            elif criterio == 'has_lower':
                feedback.append("❌ Adicione letras minúsculas") 
            elif criterio == 'has_digit':
                feedback.append("❌ Adicione números")
            elif criterio == 'has_special':
                feedback.append("❌ Adicione caracteres especiais")
    
    # Pontuação extra por comprimento
    if len(senha) >= 12:
        pontuacao += 1
        feedback.append("✅ Boa! Senha longa (12+ caracteres)")
    
    # Classificação
    if pontuacao >= 5:
        nivel = "🔒 FORTE"
    elif pontuacao >= 3:
        nivel = "⚠️  MÉDIA" 
    else:
        nivel = "🔓 FRACA"
    
    return {
        'nivel': nivel,
        'pontuacao': pontuacao,
        'feedback': feedback,
        'criterios_atendidos': sum(criterios.values()),
        'total_criterios': len(criterios)
    }

def verificar_senha_pwned(senha):
    """Verifica se a senha foi vazada usando Have I Been Pwned API"""
    try:
        # Cria hash SHA-1 da senha
        hash_senha = hashlib.sha1(senha.encode('utf-8')).hexdigest().upper()
        prefixo = hash_senha[:5]
        sufixo = hash_senha[5:]
        
        # Consulta a API
        url = f"https://api.pwnedpasswords.com/range/{prefixo}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            # Procura o sufixo na resposta
            for linha in response.text.splitlines():
                hash_sufixo, count = linha.split(':')
                if hash_sufixo == sufixo:
                    return {
                        'vazada': True,
                        'vezes_vazada': int(count),
                        'hash': hash_senha
                    }
            
            return {
                'vazada': False,
                'vezes_vazada': 0,
                'hash': hash_senha
            }
        else:
            return {'erro': 'Falha na consulta à API'}
            
    except Exception as e:
        return {'erro': f'Erro na verificação: {str(e)}'}

def analisar_senha(senha):
    """Análise completa da senha"""
    print(f"\n[+] Analisando senha: {'*' * len(senha)}")
    
    # Verifica força
    resultado_forca = calcular_forca_senha(senha)
    
    print(f"\n📊 ANÁLISE DE FORÇA:")
    print(f"   • Nível: {resultado_forca['nivel']}")
    print(f"   • Pontuação: {resultado_forca['pontuacao']}/6")
    print(f"   • Critérios atendidos: {resultado_forca['criterios_atendidos']}/{resultado_forca['total_criterios']}")
    
    # Feedback detalhado
    if resultado_forca['feedback']:
        print(f"\n💡 RECOMENDAÇÕES:")
        for item in resultado_forca['feedback']:
            print(f"   {item}")
    
    # Verifica se foi vazada
    print(f"\n🔍 VERIFICANDO VAZAMENTOS...")
    resultado_pwned = verificar_senha_pwned(senha)
    
    if 'vazada' in resultado_pwned:
        if resultado_pwned['vazada']:
            print(f"   🔴 PERIGO: Esta senha foi vazada {resultado_pwned['vezes_vazada']:,} vezes!")
            print(f"   ⚠️  RECOMENDA-SE TROCA IMEDIATA!")
        else:
            print(f"   ✅ Esta senha não foi encontrada em vazamentos conhecidos")
    else:
        print(f"   ⚠️  Não foi possível verificar vazamentos: {resultado_pwned.get('erro', 'Erro desconhecido')}")
    
    return {
        'forca': resultado_forca,
        'vazamento': resultado_pwned
    }

def main():
    banner()
    
    parser = argparse.ArgumentParser(description='Analisador de Segurança de Senhas')
    parser.add_argument('--senha', help='Senha para analisar')
    parser.add_argument('--arquivo', help='Arquivo com senhas para analisar')
    
    args = parser.parse_args()
    
    if args.senha:
        analisar_senha(args.senha)
    elif args.arquivo:
        print("[+] Analisando senhas do arquivo...")
        # Implementar leitura de arquivo
    else:
        # Modo interativo MELHORADO
        print("💡 DICA: Use Ctrl+C se digitar errado e quiser recomeçar")
        print("- Recomendado usar Windows Terminal ou VS Code Terminal para melhor experiência")
        
        while True:
            try:
                senha = input("\n🔐 Digite uma senha para analisar (ou 'sair' para encerrar): ")
                if senha.lower() == 'sair':
                    break
                if senha:
                    analisar_senha(senha)
                else:
                    print("Por favor, digite uma senha.")
            except KeyboardInterrupt:
                print("\n\n🔄 Reiniciando...")
                continue

if __name__ == "__main__":
    main()