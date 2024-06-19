print("\n""Olá seja bem vindo ao sistema de planos da vivo. \nPara que possamos ajudá-lo.")

planos = input("\n""Digite seu consumo:")
consumo = int(planos)

if consumo <= 10:
   
    print("\n""O plano mais adequado para você é o: \n---Plano Essencial Fibra - 50Mbps---")

    print("\n""Obrigado e volte sempre!""\n")
    
else: 
    if consumo <= 20:
        print("\n""O plano mais adequado para você é o: \n---Plano Prata Fibra - 100Mbps---")

        print("\n""Obrigado e volte sempre!""\n")

    else: 
        if consumo > 20:
            print("\n""O plano mais adequado para você é o: \n---Plano Premium Fibra - 300Mbps---")

    
            print("\n""Obrigado e volte sempre!""\n")
