import time

#
# def count_down(n):
#     for i in range(n, 0, -1):
#         print(i)
#         time.sleep(1)
#
# count_down(5)
# ---------------------------------
# def slow_function():
#     print("Начало функции")
#     time.sleep(5)
#     print("Конец функции")
#
# print("Начало программы")
# slow_function()
# print("Конец программы")
# ---------------------------------
# ------------- Пример 3:
# import random
# import time
# def long_running_task():
#     for i in range(5):
#         print(f"Выполнение задачи {i}")
#         time.sleep(random.randint(1, 3))
# def main():
#     print("Начало программы")
#     long_running_task()
#     print("Конец программы")
#
# main()

# ---- многопоточность ---Пример 1: ---

import threading
import time

# def worker(num):
#     print(f"Начало работы потока {num}")
#     time.sleep(2)
#     print(f"Конец работы потока {num}")
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print("Все потоки завершили работу")

# Пример 3:////////////////////////////////////////////
# import threading
#
# counter = 0
#
# def increment():
#     global counter
#     for _ in range(1_000_000):
#         counter += 1
#     print(f"Значение счетчика: {counter:_}")
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=increment)
#     threads.append(t)
#     t.start()
#
# for t in threads:
#     t.join()
#
# print(f"Значение счетчика в финале: {counter:_}")

# Многопроцессорный подход****************************************
# # Пример 1:
# import multiprocessing
# import time
# def worker(num):
#     print(f"-----Запущен процесс {num}")
#     time.sleep(3)
#     print(f"Завершён процесс {num}")
#
# if __name__ == '__main__':
#     processes = []
#
#     for i in range(5):
#         p = multiprocessing.Process(target=worker, args=(i,))
#         processes.append(p)
#         p.start()
#     for p in processes:
#         p.join()
#
#     print("Все процессы завершили работу")

# *-*-*-*-**-*-*-*-**-*-*-*-* асинхронный*********-*-*-*-*-*-*-*-**-*-*-*-**-*-*-*-**-*-*-*-*
# # Пример 1:
# import asyncio
# async def print_numbers():
#     for i in range(10):
#         print(i)
#         await asyncio.sleep(1)
# async def print_letters():
#     for letter in ['a', 'b', 'c', 'd', 'e', 'f']:
#         print(letter)
#         await asyncio.sleep(0.5)
#
# async def main():
#     task1 = asyncio.create_task(print_numbers())
#     task2 = asyncio.create_task(print_letters())
#     await task1
#     await task2
#
# asyncio.run(main())
#
# import asyncio
# async def count():
#     print("Начало выполнения")
#     await asyncio.sleep(1)
#     print("Прошла 1 секунда")
#     await asyncio.sleep(2)
#     print("Прошло еще 2 секунды")
#     return "Готово"
# async def main():
#     result = await asyncio.gather(count(), count(), count())
#     print(result)
#
# asyncio.run(main())
# --------------------------------пример 3---------------
# import asyncio
# from pathlib import Path
#
#
# async def process_file(file_path):
#     with open(file_path, 'r', encoding='utf-8') as f:
#         contents = f.read()
#         # do some processing with the file contents
#         print(f'{f.name} содержит {contents[:7]}...')
#
#
# async def main():
#     # dir_path = Path('/path/to/directory')
#     dir_path = Path('.')
#     file_paths = [file_path for file_path in dir_path.iterdir()
#                   if file_path.is_file()]
#     tasks = [asyncio.create_task(process_file(file_path)) for
#              file_path in file_paths]
#
#     await asyncio.gather(*tasks)
#
# if __name__ == '__main__':
#     asyncio.run(main())

# Обычная синхронная загрузка:
# import requests
# import time
#
# urls = ['https://www.google.ru/',
#     'https://gb.ru/',
#     'https://ya.ru/',
#     'https://www.python.org/',
#     'https://habr.com/ru/all/',
#     ]
#
# start_time = time.time()
# for url in urls:
#     response = requests.get(url)
#     filename = 'sync_' + url.replace('https://', '').replace('.','_').replace('/', '') + '.html'
#     with open(filename, "w", encoding='utf-8') as f:
#         f.write(response.text)
#     print(f"Downloaded {url} in {time.time() - start_time:.2f}    seconds")

# ///////////////////////////////Асинхронный подход//////////////////////////
# Пример 1: Асинхронный подход
import asyncio


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(1)


async def print_letters():
    for letter in ["a", "b", "c", "d", "e", "f"]:
        print(letter)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_numbers())
    task2 = asyncio.create_task(print_letters())
    await task1
    await task2


# asyncio.run(main())


# Пример 2:
import asyncio


async def count():
    print("Начало выполнения")
    await asyncio.sleep(1)
    print("Прошла 1 секунда")
    await asyncio.sleep(2)
    print("Прошло еще 2 секунды")
    return "Готово"


async def main():
    result = await asyncio.gather(count(), count(), count())
    print(result)


# asyncio.run(main())

# Пример 3:
import asyncio
from pathlib import Path


async def process_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        contents = f.read()
        # do some processing with the file contents
        print(f"{f.name} содержит {contents[:7]}...")


async def main():
    # dir_path = Path('/path/to/directory')
    dir_path = Path(".")
    file_paths = [file_path for file_path in dir_path.iterdir() if file_path.is_file()]
    tasks = [asyncio.create_task(process_file(file_path)) for file_path in file_paths]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
