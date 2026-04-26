# Lineage Integration

Este repositório contém um projeto de teste para integração com OpenLineage, com foco em validar o envio de eventos de linha de dados e metadados de execução.

## Objetivo

- Testar o envio de eventos OpenLineage via Python.
- Validar estrutura de job, run, datasets de entrada e saída e esquemas de dados.
- Confirmar que o produtor e os namespaces estão sendo enviados corretamente para um servidor OpenLineage local.

## Arquivos principais

- `src/lineage.py`: script principal que cria e emite um evento `RunEvent` para OpenLineage.
- `src/requirements.txt`: dependência do cliente OpenLineage.

## Como usar

1. Configure um servidor OpenLineage local disponível em `http://localhost:5000`.
2. Instale dependências:

```bash
python -m pip install -r src/requirements.txt
```

3. Execute o script:

```bash
python src/lineage.py
```

4. Verifique no servidor OpenLineage se o evento foi recebido com sucesso.

## Estrutura do evento

O script define um evento com:

- `RunState.COMPLETE`
- `runId` único gerado por `uuid.uuid4()`.
- `Job` com namespace `meu_projeto` e nome `job_exemplo_3`.
- Uma dataset de entrada `tabela_entrada` com esquema de colunas.
- Uma dataset de saída `tabela_saida` com esquema de colunas.
- `producer` configurado como `meu_teste_local`.

## Recomendação para evolução

- Adicionar variáveis de ambiente para URL do servidor OpenLineage e producer.
- Incluir tratamento de exceções para falhas na emissão do evento.
- Criar testes automatizados para verificar a construção do evento.
- Expandir o script para ler metadados de uma fonte real e enviar eventos dinâmicos.

## Observações

Este projeto é um ponto de partida simples para testar o OpenLineage. Ele deve ser expandido com configurações parametrizadas e testes para uso em ambientes de integração contínua e pipelines de dados.
