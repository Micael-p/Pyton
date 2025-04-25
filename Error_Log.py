import logging

logging.basicConfig(filename="app.log",level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

    self.conexao.commit()
    log_info("tabelas criadas com sucesso.")
    except sqlite3.IntegrityError as e:
    log_error(f"Erro de integridade ao criar tabelas: {e}")
    raise
    except sqlite3.OperationalError as e:
    log_error(f"Erro de operacional ao criar tabelas: {e}")
    raise
    except sqlite3.DatabaseError as e:
    log_error(f"Erro de banco ao criar tabelas: {e}")
    raise
    except sqlite3.Error as e:
    log_error(f"Erro geral do SQLite ao criar tabelas: {e}")
    raise
