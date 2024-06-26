import json

with open("votos_database.json", "r") as file:
    data = json.load(file)

data_list = []
data_list = list(data.values())[0]


data_list2 = list()
for item in data_list:
    data_list2.append(item)

allvotes = list()

for i in range(len(data_list2)):
    allvotes.append(data_list[data_list2[i]]["Voto"])

votosindiv = list()
for i in range(len(data_list2)):
    votosindiv.append(data_list[data_list2[i]])

print("""\n\n\n\n ██████╗████████╗██████╗ ███╗   ███╗
██╔════╝╚══██╔══╝██╔══██╗████╗ ████║
██║        ██║   ██████╔╝██╔████╔██║
██║        ██║   ██╔═══╝ ██║╚██╔╝██║
╚██████╗   ██║   ██║     ██║ ╚═╝ ██║
 ╚═════╝   ╚═╝   ╚═╝     ╚═╝     ╚═╝
                                    """)


while True:
    print("\nVer a contagem de Votos [1]\nVer cada voto (individualmente)[2]\n\nResposta: ")
    ans = int(input(""))

    if ans == 1: 
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("""\n\n\n\n ██████╗████████╗██████╗ ███╗   ███╗
██╔════╝╚══██╔══╝██╔══██╗████╗ ████║
██║        ██║   ██████╔╝██╔████╔██║
██║        ██║   ██╔═══╝ ██║╚██╔╝██║
╚██████╗   ██║   ██║     ██║ ╚═╝ ██║
 ╚═════╝   ╚═╝   ╚═╝     ╚═╝     ╚═╝
                                    """)
        print(f"-----------\nChapa 1: {allvotes.count("Chapa 1")}\nChapa 2: {allvotes.count("Chapa 2")}\n-----------")


    if ans == 2:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("""\n\n\n\n ██████╗████████╗██████╗ ███╗   ███╗
██╔════╝╚══██╔══╝██╔══██╗████╗ ████║
██║        ██║   ██████╔╝██╔████╔██║
██║        ██║   ██╔═══╝ ██║╚██╔╝██║
╚██████╗   ██║   ██║     ██║ ╚═╝ ██║
 ╚═════╝   ╚═╝   ╚═╝     ╚═╝     ╚═╝
                                    """)
        print(f"\nVotos:")
        for voto in votosindiv:
            print(f"{voto}")

    if ans == 99:
        arq = {"votos": {}}
        with open("votos_database.json", "w") as file:
            json.dump(arq, file, indent=4)