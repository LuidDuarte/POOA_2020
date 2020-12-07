# openClosedPrinciple:
O diretório contém o exercício referente a ferramenta que faz download de títulos de notícias.\
Para sua execução é necessário:
- Python 3
- pip3

Rodar o comando: `pip3 install -r requirements.txt` ou apenas `pip3 install beautifulsoup4` \
Para executar o exemplo: `python3 example.py`

A Classe foi modelada para que, receba qual url e nome do portal o usuário deseja trazer as notícias, bem como quais tipos de notícia o usuário deseja trazer, em um array recebendo ['Nome do tipo', 'nome da classe do html']\
Portanto, o usuário pode receber os resultados como um dicionário chamando o método `return_from_types` como o exemplo a seguir: \ 
```
{
    'Tipo': 'Nome do tipo1',
    'data': {[
        {'Titulo' : 'Titulo da notícia',
        'link' : 'link da notícia'},
        ...
    ]
        ...
    }
}
```
Ou, exportar as inforações como um CSV chamando o método `write_on_csv`, com delimitador e nome de arquivo a sua escolha. \
Por default o delimitador é ";" e o nome é _nome_do_portal_.csv




