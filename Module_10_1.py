from time import sleep
import threading
import time
from turtledemo.penrose import start


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            file.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


start_time = time.time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')


threads = []
thread1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
threads.append(thread1)
thread2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
threads.append(thread2)
thread3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
threads.append(thread3)
thread4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))
threads.append(thread4)

for thread in threads:
    thread.start()

end_time = time.time()
print(f'Время выполнения функции и потоков {end_time - start_time} секунд')

for thread in threads:
    thread.join()

end_time = time.time()
print(f'Время выполнения функции и потоков {end_time - start_time} секунд')