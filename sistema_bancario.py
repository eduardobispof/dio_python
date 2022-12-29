'''
deposito: deve aparecer no extrato
saque: limite de 3 saques por dia, deve aparecer no extrato
extrato: valores precisam ser mostrato com o formato R$ 1500.45
'''
import time

class SistemaBancario:

    def __init__(self) -> None:
        self.saldo_conta = 0
        self.limite_saque = 500
        self.extrato_conta = list()
        self.cont_saque = 0
        self.LIMITE_QTD_SAQUE = 3
        self.loop = True

        self.menu_inicial()

    def menu_inicial(self) -> None:
        
        while self.loop:
            print("==============CAIXA 001==============")
            print("""
                    [1] - SALDO
                    [2] - SAQUE
                    [3] - DEPOSITO
                    [4] - EXTRATO
                    [0] - SAIR
            """)
            opcao = int(input('DIGITE UMA OPÇÃO...'))

            if opcao != 0:
                
                if opcao == 1:
                    self.saldo()
                elif opcao == 2:
                    self.saque()
                elif opcao == 3:
                    self.deposito()
                elif opcao == 4:
                    self.extrato()
                else:
                    print("OPÇÃO INVÁLIDA")

            else:
                self.loop = False
    
    def verif_volta_menu(self):
        print("""DESEJA REALIZAR OUTRA OPERAÇÃO?
                [1] - SIM
                [2] - NÃO
        """)
        escolha = int(input())
        if escolha == 1:
            print("RETORNANDO AO MENU...")
            time.sleep(1)
            self.menu_inicial()
        else:
            print("SESSÃO ENCERRADA...")
            time.sleep(5)
            self.loop = False

    def add_extrato(self, tipo_operacao: str, valor: float):
        #self.extrato_conta.append({'tipo_operacao': tipo_operacao,'valor': valor})
        self.extrato_conta.append(f"OPERAÇÃO: {tipo_operacao}, VALOR: R${valor}")
    
    def extrato(self):
        if len(self.extrato_conta) > 0:
            for i in self.extrato_conta:
                print(i)
                print("RETORNANDO AO MENU EM 1 MINUTO!")
                time.sleep(60)
                print("RETORNANDO AO MENU...")
                self.menu_inicial()
        else:
            print("NÃO EXISTE EXTRATO PARA SER EXIBIDO")
            print("RETORNANDO AO MENU...")
            time.sleep(5)
            self.menu_inicial()
    def saldo(self):
        print(f"SALDO: R${self.saldo_conta}")
        self.verif_volta_menu()

    def saque(self):
        print("==============CAIXA 001==============")
        print("DIGITE O VALOR QIE DESEJA SACAR: ")
        valor_saque = float(input())
        valor_saque = round(valor_saque, 2)

        if valor_saque > 0 and valor_saque < self.saldo_conta and self.cont_saque < self.LIMITE_QTD_SAQUE:
            
            self.saldo_conta -= valor_saque
            self.cont_saque =+ 1
            
            self.add_extrato('saque', valor_saque)

            print(f"VALOR R${valor_saque} SACADO COM SUCESSO!")
            self.verif_volta_menu()
        else:
            print("VALOR INVALIDO, PFVR REPITA A OPERAÇÃO")
            self.verif_volta_menu()
            
    def deposito(self):
        print("==============CAIXA 001==============")
        print("DIGITE O VALOR QIE DESEJA DEPOSITAR: '")
        valor_deposito = float(input())
        valor_deposito = round(valor_deposito, 2)

        if valor_deposito > 0:
            self.saldo_conta += valor_deposito

            self.add_extrato('DEPOSITO', valor_deposito)
            
            print(f"VALOR R${valor_deposito} DEPOSITADO COM SUCESSO!")
            self.verif_volta_menu()
        else:
            print("VALOR INVALIDO, PFVR REPITA A OPERAÇÃO")
            self.deposito()



def init():
    sistema_bancario = SistemaBancario()

if __name__ == "__main__":
    init()