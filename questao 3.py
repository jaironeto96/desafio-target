from datetime import datetime

def calcular_juros_interativo():
    print("\n" + "="*40)
    print("      SISTEMA DE CÁLCULO DE JUROS")
    print("="*40)
    
    try:
        valor_str = input("Digite o valor original do título (R$): ").strip().replace(',', '.')
        valor_original = float(valor_str)
        
        data_vencimento_str = input("Digite a data de vencimento (Formato AAAA-MM-DD ou DD/MM/AAAA): ").strip()
        
    except ValueError:
        print("\n[Erro] Valor original inválido. Use apenas números (ex: 1500.50).")
        return

    data_vencimento = None
    for fmt in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            data_vencimento = datetime.strptime(data_vencimento_str, fmt)
            break
        except ValueError:
            continue
            
    if not data_vencimento:
        print("\n[Erro] Formato de data inválido. Utilize o formato AAAA-MM-DD (ex: 2026-08-15) ou DD/MM/AAAA.")
        return
    
    data_hoje = datetime.now()
    dias_atraso = (data_hoje - data_vencimento).days
    
    print("\n" + "-"*40)
    print("           RESULTADO DO CÁLCULO")
    print("-" * 40)
    print(f"Data de Vencimento: {data_vencimento.strftime('%d/%m/%Y')}")
    print(f"Data Atual:         {data_hoje.strftime('%d/%m/%Y')}")
    
    if dias_atraso <= 0:
        print("\nStatus: O título está em dia ou vence hoje. Não há juros aplicáveis.")
        print(f"Valor a pagar: R$ {valor_original:.2f}")
        print("-" * 40)
        return
    
    taxa_diaria = 0.025
    valor_juros = valor_original * taxa_diaria * dias_atraso
    valor_total = valor_original + valor_juros
    
    print(f"Dias de Atraso:     {dias_atraso} dia(s)")
    print(f"Taxa de Juros:      2.5% ao dia")
    print(f"Valor dos Juros:    R$ {valor_juros:.2f}")
    print(f"Valor Total Atual:  R$ {valor_total:.2f}")
    print("-" * 40)

if __name__ == "__main__":
    calcular_juros_interativo()
