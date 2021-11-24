CREATE TABLE cotacao(
    id_cotacao INT PRIMARY KEY AUTO_INCREMENT,
    nome_acao VARCHAR(45),
    cotacao_atual INT,
    hora_cotacao DATETIME
);

SELECT * FROM cotacao;