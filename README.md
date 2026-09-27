# diagnostico-de-fila-de-impressao

## Descrição do Problema

Analisa a fila de impressão de uma impressora corporativa para identificar o status do equipamento. O sistema deve contar o total de documentos, somar as páginas a serem impressas e verificar se há documentos com status de erro na fila.

## Requisitos

* Receber uma lista de dicionários representando os documentos na fila.
* Calcular o total de documentos e a soma das páginas.
* Identificar se existem documentos com status 'erro'.
* Gerar um diagnóstico final baseado nas regras de negócio.

## Exemplo de Uso

Entrada:
[{'id': 1, 'paginas': 10, 'status': 'pendente'}, {'id': 2, 'paginas': 5, 'status': 'erro'}]

Saída: Fila com erros detectados. Verifique a impressora.