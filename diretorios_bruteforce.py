import requests

def brute_force(url, diretorios):
    for diretorio in diretorios:
        url_alvo = f"{url}/{diretorio}/"
        resposta = requests.get(url_alvo, timeout=3)
        
        if resposta.status_code == 200:
            print(f"Diretório encontrado: {url_alvo}")
            with open('brute_force.txt', 'a') as file:
                file.write(f"{url_alvo}\n")
        elif 300 <= resposta.status_code < 400:
            print(f"Ocorreu um redirecionamento no diretório: {url_alvo}")
        else:
            pass

if __name__ == "__main__":
    with open("urls.txt", "r") as arquivo_urls:
        urls = arquivo_urls.read().splitlines()

    with open("diretorios.txt", "r") as arquivo_diretorios:
        diretorios = arquivo_diretorios.read().splitlines()
    
    for url in urls:
        print(f"Fazendo brute force em {url}")
        brute_force(url, diretorios)