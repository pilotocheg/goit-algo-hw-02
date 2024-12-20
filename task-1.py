from queue import Queue

queue = Queue()


class Request:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Request {self.name}"


requests_count = 0


def generate_request():
    global requests_count
    requests_count += 1
    request = Request(f"Заявка {requests_count}")
    queue.put(request)
    print(f"Заявка #{requests_count} створена")


def process_request():
    if queue.empty():
        print("Черга пуста")
    else:
        request = queue.get()
        print(f"{request} оброблена")


def main():
    print("Список дій:")
    print("1. Створити нову заявку")
    print("2. Обробити наступну заявку в черзі")
    print("3. Вийти")

    while True:
        choice = input("Виберіть дію: ")

        if choice == "1":
            generate_request()
        elif choice == "2":
            process_request()
        elif choice == "3":
            break
        else:
            print("Невірний вибір")


if __name__ == "__main__":
    main()
