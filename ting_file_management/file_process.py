from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        result = instance.search(i)
        if result["nome_do_arquivo"] == path_file:
            return

    content = txt_importer(path_file)
    dict_to_return = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(content),
        "linhas_do_arquivo": content
        }
    instance.enqueue(dict_to_return)
    print(dict_to_return)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
