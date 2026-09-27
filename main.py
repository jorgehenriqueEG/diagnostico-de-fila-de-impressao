def diagnosticar_fila_impressao(documentos):
    total_documentos = len(documentos)
    total_paginas = sum(doc['paginas'] for doc in documentos)
    tem_erros = any(doc['status'] == 'erro' for doc in documentos)

    if tem_erros:
        diagnostico = "Fila com erros detectados. Verifique a impressora."
    elif total_documentos == 0:
        diagnostico = "Fila de impressão vazia."
    elif total_paginas > 100:
        diagnostico = "Fila muito grande. Considere priorizar documentos."
    else:
        diagnostico = "Fila de impressão normal."

    print(f"Total de documentos: {total_documentos}")
    print(f"Total de páginas: {total_paginas}")
    print(f"Diagnóstico: {diagnostico}")
    return diagnostico

fila_exemplo = [
    {'id': 1, 'usuario': 'joao', 'paginas': 10, 'status': 'pendente'},
    {'id': 2, 'usuario': 'maria', 'paginas': 5, 'status': 'erro'},
    {'id': 3, 'usuario': 'pedro', 'paginas': 20, 'status': 'processando'}
]

diagnosticar_fila_impressao(fila_exemplo)