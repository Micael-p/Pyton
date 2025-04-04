from pathlib import Path
import json
from typing import List, Dict

class Aluno:
    """
    Representa um aluno com nome e nota.
    
    Attributes:
    nome (str): Nome do aluno.
    nota (float): Nota dp aluno.
    """
    def __init__(self, nome: str, nota: float):
        """
        Inicializa uma nova instancia de Aluno.

        Args:
            nome (str): O nome do aluno
            nota (float): A nota do aluno.
        """
        self.nome = nome.strip().title()
        self.nota = float(nota)

    def to_dict(self) -> Dict[str, float]:
        """
        Retorna o aluno como um dicionario com nome e nota.

        Returns:
            dict: um dicionário {nome: nota}.
        """
        return {self.nome: self.nota}
    
    def __str__(self) -> str:
        """
        Representação em string do aluno no formato CSV.

        Returns:
            str: Nome e nota separados por vírgula.
        """
        return f"{self.nome},{self.nota:.1f}"
    
    class GerenciadorAlunos:
        """
        Classe responsável pelo gerenciamento de alunos e persistencia dos dados.

        Attributes:
            csv_path (Path): caminho do arquivo CSV.
            json_path (Path): Caminho do arquivo JSON.
            txt_path (Path): Caminho do arquivo TXT.
            alunos (Dict[str, float]): Dicionario com os dados dos alunos.
        """
        def __init__(self, base_dir: Path):
            """
            Iniciarlizar o gerenciador e carregar os dados existentes.

            args:
                base_dir (Path): Diretorio base onde os arquivos serão armazenados.
            """
            self.csv_path = base_dir / "alunos.csv"
            self.json_path = base_dir / "alunos.json"
            self.txt_path = base_dir / "alunos.txt"
            self.alunos: Dict[str, float] = self._carregar()

            def _carregar(self) -> Dict[str, float]:
                """
                Carregar os dados dos alunos a partir do arquivo CSV, se existir. (_ ==Método protegido ou interno)

                Returns:
                    dict: Dicionario com os dados dos alunos.
                """
                if self.csv_path.exists():
                    try:
                        with open(self.csv_path, "r") as f:
                            return {
                                nome: float(nota)
                                for nome, nota in (linha.strip().split(",") for linha in f)
                            }
                    except FileNotFoundError:
                        print("Arquivo CSV não encontrado.")
                    except ValueError as ve:
                        print(f"Erro ao converter nota para float: {ve}")
                    except OSError as oe:
                        print(f"Erro de sistema ao acessar o arquivo: {oe}")
                return {}
            
            def salvar(self) -> None:
                """
                Salvar os dados dos alunos nos formatos CSV, TXT e JSON.
                """
                try:
                    with open(self.csv_path, "w") as f_csv, open(self.txt_path, "w") as f_txt, open(self.json_path, "w") as f_json:
                        for nome,nota in self.alunos.items():
                            linha = f"{nome},{nota:1f}\n"
                            f_csv.write(linha)
                            f_txt.write(f"{nome} tem nota {nota:.1f}\n")
                            json.dump(self.alunos, f_json, indent=4)

                except Exception as e:
                    print(f"Erro ao salvar os arquivos: {e}")

            def cadastrar(self, aluno: Aluno) -> bool:
                """
                Cadastra ou atualiza um aluno do dicionario e salva os dados.

                Args:
                    aluno (Aluno): Instancia da classe Aluno.

                Returns:
                    bool: True se o cadastro foi bem-sucedido.
                """
                self.alunos[aluno.nome] = aluno.nota
                self.salvar()
                return True
            
            def remover(self, nome: str) -> bool:
                """
                Remove um aluno pelo nome.

                Args:
                    nome (str): Nome do aluno a ser removido.

                Returns:
                    bool: True se o aluno foi removido, False caso contradio.
                """
                if nome in self.alunos:
                    del self.alunos[nome]
                    self.salvar()
                    return True
                return False
            
            def alterar_nota(self, nome: str, nova_nota: float) -> bool:
                """
                Altera a nota de um aluno existente.

                Args:
                    nome (str): Nome do aluno.
                    Nova_nota (float): Nova nota a ser atribuida.
                
                Returns:
                    bool: True se a nota foi alterada, False caso o aluno não existia.
                """
                if nome in self.alunos:
                    self.alunos[nome] = nova_nota
                    self.salvar()
                    return True
                return False
            
            def listar(self) -> List[str]:
                """
                Listar todos os alunos cadastrados.

                Returns:
                    List: Lista de strings no formato "nome,nota".
                """
                return [f"{nome},{nota:.1f}" for nome, nota in self.alunos.items()]
            
            def buscar(self, nome: str) -> str:
                """
                Buscar um aluno pelo nome.

                Args:
                    nome (str): Nome do aluno.
                
                Returns:
                    str: Informação do aluno no formato "nome,nota" ou mensagem de erro.
                """
                if nome in self.alunos:
                    return f"{nome},{self.alunos[nome]:.1f}"
                return "Aluno não encontrado."
            
            if __name__ == "__main__":
                base_dir = Path(__file__).parent
                gerenciador = GerenciadorAlunos(base_dir)

                print("Cadastrando:", gerenciador.cadastrar(Aluno("Micael", 8.0)))
                print("Lendo:", gerenciador.buscar("Micael"))
                print("Lista completa:", gerenciador.listar())
                print("Removendo:", gerenciador.remover("Raphael"))
                print("lista após remoção:", gerenciador.listar())
                print("Novo cadastro:", gerenciador.cadastrar(Aluno("Micael", 8.0)))
                print("Alterar nota:", gerenciador.alterar_nota(Aluno("Micael", 9.0)))
                print("Lista final", gerenciador.Listar())
