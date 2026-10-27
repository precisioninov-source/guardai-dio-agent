"""Exemplo local corrigido com consulta parametrizada.

Banco SQLite em memória; não inicia servidor nem persiste dados.
Este exemplo simplifica autenticação e não deve ser usado em produção.
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


def buscar_login(conexao: sqlite3.Connection, login: str) -> bool:
    consulta = "SELECT id FROM usuarios WHERE login = ?"
    return conexao.execute(consulta, (login,)).fetchone() is not None


def main() -> None:
    conexao = abrir_banco_demo()
    login = input("Digite um login fictício (exemplo: aluna.demo): ")
    resultado = buscar_login(conexao, login)
    print("Registro encontrado." if resultado else "Registro não encontrado.")
    conexao.close()


if __name__ == "__main__":
    main()

