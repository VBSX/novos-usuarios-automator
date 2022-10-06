class usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        
    def filtrar_cpf(self):
        cpf_without_spaces = self.cpf.strip()
        cpf_filter = cpf_without_spaces.replace(".", "").replace("-", "")
        return cpf_filter
    
    
    def filtrar_nome(self):
        nome_modo_titulo = self.nome.title()
        return nome_modo_titulo
    
    def reset_senha(self, senha):
        string = "Senha resetada com sucesso, segue o login:"
        final_string = f"{string}\n	{self.filtrar_nome()}\n		Usuário: CPF\n		Senha: {senha}"
        return final_string
    def novo_usuario(self, senha):
        string = "Usuário criado com sucesso, segue o login:"
        final_string = f"{string}\n	{self.filtrar_nome()}\n		Usuário: CPF\n		Senha: {senha}"
        return final_string  
        
if  __name__ == "__main__":
    nome = "SAMUEL XAVARAL DOS SILVA"
    cpf = "053.014.795-51"
    novo_user_teste = usuario(nome, cpf)
    print(novo_user_teste.reset_senha("adsa#12312"))