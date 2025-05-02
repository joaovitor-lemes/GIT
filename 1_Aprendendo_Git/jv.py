import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

# Utilitários para manipulação de tarefas
def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)

def generate_id():
    return int(datetime.now().timestamp() * 1000)

# Funções do menu principal
def show_menu():
    print("\n====== GERENCIADOR DE TAREFAS ======")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Filtrar tarefas")
    print("4. Marcar tarefa como concluída")
    print("5. Remover tarefa")
    print("6. Editar tarefa")
    print("7. Estatísticas")
    print("8. Sair")
    return input("Escolha uma opção: ")

def add_task():
    print("\n--- Adicionar Tarefa ---")
    title = input("Título: ").strip()
    description = input("Descrição: ").strip()
    priority = input("Prioridade (baixa, média, alta): ").strip().lower()
    due_date = input("Data de vencimento (dd/mm/aaaa): ").strip()
    
    try:
        due_date_obj = datetime.strptime(due_date, "%d/%m/%Y")
    except ValueError:
        print("Data inválida. Usando hoje como vencimento.")
        due_date_obj = datetime.today()

    task = {
        "id": generate_id(),
        "title": title,
        "description": description,
        "priority": priority,
        "due_date": due_date_obj.strftime("%Y-%m-%d"),
        "completed": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Tarefa adicionada com sucesso!")

def list_tasks(tasks=None):
    print("\n--- Lista de Tarefas ---")
    tasks = tasks if tasks is not None else load_tasks()
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    for i, task in enumerate(tasks, 1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['title']} (Prioridade: {task['priority']}, Vence: {task['due_date']})")

def filter_tasks():
    tasks = load_tasks()
    print("\n--- Filtrar Tarefas ---")
    print("1. Somente pendentes")
    print("2. Somente concluídas")
    print("3. Prioridade")
    print("4. Vencimento até data")
    print("5. Voltar")
    choice = input("Escolha: ")

    if choice == "1":
        filtered = [t for t in tasks if not t["completed"]]
        list_tasks(filtered)
    elif choice == "2":
        filtered = [t for t in tasks if t["completed"]]
        list_tasks(filtered)
    elif choice == "3":
        prio = input("Prioridade (baixa, média, alta): ").strip().lower()
        filtered = [t for t in tasks if t["priority"] == prio]
        list_tasks(filtered)
    elif choice == "4":
        date_input = input("Data limite (dd/mm/aaaa): ")
        try:
            target = datetime.strptime(date_input, "%d/%m/%Y")
            filtered = [t for t in tasks if datetime.strptime(t["due_date"], "%Y-%m-%d") <= target]
            list_tasks(filtered)
        except ValueError:
            print("Data inválida.")
    else:
        return

def complete_task():
    tasks = load_tasks()
    list_tasks(tasks)
    try:
        index = int(input("Digite o número da tarefa concluída: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            save_tasks(tasks)
            print("Tarefa marcada como concluída.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def delete_task():
    tasks = load_tasks()
    list_tasks(tasks)
    try:
        index = int(input("Digite o número da tarefa a remover: ")) - 1
        if 0 <= index < len(tasks):
            confirm = input(f"Confirma a exclusão de '{tasks[index]['title']}'? (s/n): ").lower()
            if confirm == "s":
                tasks.pop(index)
                save_tasks(tasks)
                print("Tarefa removida.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def edit_task():
    tasks = load_tasks()
    list_tasks(tasks)
    try:
        index = int(input("Digite o número da tarefa a editar: ")) - 1
        if 0 <= index < len(tasks):
            task = tasks[index]
            print(f"Editando '{task['title']}'")

            new_title = input(f"Título [{task['title']}]: ") or task["title"]
            new_desc = input(f"Descrição [{task['description']}]: ") or task["description"]
            new_prio = input(f"Prioridade [{task['priority']}]: ") or task["priority"]
            new_due = input(f"Vencimento [{task['due_date']}]: ") or task["due_date"]

            task["title"] = new_title
            task["description"] = new_desc
            task["priority"] = new_prio

            try:
                datetime.strptime(new_due, "%Y-%m-%d")
                task["due_date"] = new_due
            except ValueError:
                print("Formato de data inválido, mantendo data anterior.")

            save_tasks(tasks)
            print("Tarefa atualizada.")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")

def show_stats():
    tasks = load_tasks()
    total = len(tasks)
    done = sum(1 for t in tasks if t["completed"])
    pending = total - done
    high = sum(1 for t in tasks if t["priority"] == "alta")
    print("\n--- Estatísticas ---")
    print(f"Total: {total}")
    print(f"Concluídas: {done}")
    print(f"Pendentes: {pending}")
    print(f"Tarefas com prioridade ALTA: {high}")

# Loop principal
def main():
    while True:
        choice = show_menu()
        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            filter_tasks()
        elif choice == "4":
            complete_task()
        elif choice == "5":
            delete_task()
        elif choice == "6":
            edit_task()
        elif choice == "7":
            show_stats()
        elif choice == "8":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
