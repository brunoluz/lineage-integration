from openlineage.client.event_v2 import (
    InputDataset,
    OutputDataset,
    RunEvent,
    RunState,
    Job,
    Run,
)
from openlineage.client.facet import SchemaDatasetFacet, SchemaField
import uuid

from datetime import datetime, UTC

from openlineage.client import OpenLineageClient


client = OpenLineageClient(config={
    "transport": {
        "type": "http",
        "url": "http://localhost:5000"
    }
})


run_id = str(uuid.uuid4())

event = RunEvent(
    eventType=RunState.COMPLETE,
    eventTime=datetime.now(UTC).isoformat(),
    run=Run(
        runId=run_id
    ),
    job=Job(
        namespace="meu_projeto",
        name="job_exemplo_3"
    ),
    inputs=[
        InputDataset(
            namespace="local",
            name="tabela_entrada",
            facets={
                "schema": SchemaDatasetFacet(fields=[
                    SchemaField(name="coluna_1", type="string"),
                    SchemaField(name="coluna_2", type="int"),
                ])
            }
        )
    ],
    outputs=[
        OutputDataset(
            namespace="local",
            name="tabela_saida",
            facets={
                "schema": SchemaDatasetFacet(fields=[
                    SchemaField(name="coluna_1", type="string"),
                    SchemaField(name="coluna_2", type="int"),
                ])
            }
        )
    ],
    producer="meu_teste_local"
)

client.emit(event)

print("finished")