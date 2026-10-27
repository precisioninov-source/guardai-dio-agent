"""Exemplo local intencionalmente vulnerável para revisão estática.

Banco SQLite em memória; não inicia servidor nem persiste dados.
Use apenas como material didático.
"""

import sqlite3


def abrir_banco_demo() -> sqlite3.Connection:
    conexao = sqlite3.connect(":memory:")
    conexao.execute(
        "CREATE TABLE usuarios (id INTEGER PRIMARY KEY, login TEXT NOT NULL)"
    )
    conexao.execute("INSERT INTO usuarios (login) VALUES (?)", ("aluna.demo",))
    conexao.commit()
    return conexao


def login_vulneravel(conexao: sqlite3.Connection, login: str) -> bool:
    # Vulnerabilidade intencional: a entrada passa a compor a sintaxe SQL.
    consulta = (
        "SELECT id FROM usuarios WHERE login = '" + login + "'"
    )
    return conexao.execute(consulta).fetchone() is not None


def main() -> None:
    conexao = abrir_banco_demo()
    login = input("Digite um login fictício (exemplo: aluna.demo): ")
    resultado = login_vulneravel(conexao, login)
    print("Registro encontrado." if resultado else "Registro não encontrado.")
    conexao.close()


if __name__ == "__main__":
    main()

