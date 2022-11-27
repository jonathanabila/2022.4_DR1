<p align="center">
    <img src="./docs/logo.jpg" align="center" alt="INFNET logo" title="INFNET" width="200">
</p>

<br>

<div align="center">
    <h3>ESCOLA SUPERIOR DE TECNOLOGIA DA INFORMAÇÃO</h3>
    <h3>GRADUAÇÃO EM ENGENHARIA DE SOFTWARE</h3>
    <br>
    <h3>Instituto INFNET - INFNET</h3>
    <br>
    <h4>TESTE DE PERFORMANCE – TP3</h4>
    <h4>DESENVOLVIMENTO DE SOFTWARE ÁGIL E ESCALÁVEL COM MICROSSERVIÇOS</h4>
    <h4>ALUNO: JONATHAN TOLENTINO ABILA</h4>
    <h4>PROFESSOR: LEONARDO SILVA DA GLORIA</h4>
    <br>
</div>

# Índice
- [Índice](#índice)
- [Instruções](#instruções)

# Instruções

## Aplicação
Para executar a aplicação o comando deve ser:

```bash
docker compose up
```

Com isso as aplicações serão iniciadas nas seguintes portas:

- classroom: `http://0.0.0.0:8081/`

## Banco de dados
Não é necessário realizar nenhum comando para a criação das tabelas no banco de dados, já que todo
o processo é controlado pelo docker, entretanto, se quiser forçar o processo pode executar:

```bash
docker compose up XXX
```

Substituindo o XXX pelo nome do migrator:

- classroom -> classroom_migrator
