from departamento_dao import DepartamentoDAO
from funcionario_dao import FuncionarioDAO
from models import Departamento, Funcionario

DB='banco.db'

def exemplo_departamento():
    dao=DepartamentoDAO(DB)
    d=dao.create(Departamento(nome="RH"))
    print("Criado:",d)
    print("Lido:",dao.read(d.id))
    d.nome="RH Atualizado"
    dao.update(d)
    print("Atualizado:",dao.read(d.id))
    dao.delete(d.id)
    print("Após delete:",dao.read(d.id))

def exemplo_funcionario():
    ddao=DepartamentoDAO(DB)
    fdao=FuncionarioDAO(DB)
    d=ddao.create(Departamento(nome="TI"))
    f=fdao.create(Funcionario(nome="João",salario=3000,departamento_id=d.id))
    print("Criado:",f)
    print("Lido:",fdao.read(f.id))
    f.salario=3500
    fdao.update(f)
    print("Atualizado:",fdao.read(f.id))
    fdao.delete(f.id)
    print("Após delete:",fdao.read(f.id))

if __name__=='__main__':
    exemplo_departamento()
    exemplo_funcionario()