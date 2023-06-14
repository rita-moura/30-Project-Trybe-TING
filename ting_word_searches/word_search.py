def exists_word(word, instance):
    counter = 0
    result = []

    for i in range(len(instance)):
        fila = instance.search(i)
        instance_result = {
            "palavra": word,
            "arquivo": fila["nome_do_arquivo"],
            "ocorrencias": [{
                "linha": index + 1
            } for index, linha in enumerate(fila["linhas_do_arquivo"])
                if word.lower() in linha.lower()]
        }
        result.append(instance_result)
        if len(instance_result["ocorrencias"]) == 0:
            counter += 1

    if counter == len(instance):
        return []
    return result


def search_by_word(word, instance):
    counter = 0
    result = []

    for i in range(len(instance)):
        fila = instance.search(i)
        instance_result = {
            "palavra": word,
            "arquivo": fila["nome_do_arquivo"],
            "ocorrencias": [
                {
                    "linha": index + 1,
                    "conteudo": linha
                } for index, linha in enumerate(fila["linhas_do_arquivo"])
                if word.lower() in linha.lower()
            ]
        }
        result.append(instance_result)
        if len(instance_result["ocorrencias"]) == 0:
            counter += 1

    if counter == len(instance):
        return []
    return result
