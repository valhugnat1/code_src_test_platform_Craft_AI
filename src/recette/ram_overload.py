import argparse
import time
import psutil

def parse_cmd_args():
    """
    Parses command line args
    """
    parser = argparse.ArgumentParser(description='Memory Eating utility for python')
    parser.add_argument('-m', '--memory', type=int, default=-1, help='The amount of memory in gigs to eat', required = True)
    args = parser.parse_args()
    return args


def eat_memory(mem_to_eat):
    """
    Eats memeory
    :param mem_to_eat: The amount of memory to eat in gigs
    """

    MB = 1024 * 1024 
    eat = ""

    memory_usage_percent = 0
    while memory_usage_percent < 95:
        eat = eat + "a" * MB * mem_to_eat
        memory_usage_percent = psutil.virtual_memory().percent
        print(f'Memory Usage: {memory_usage_percent:.2f}%')
        # time.sleep(1)

    for i in range (10):
        
        time.sleep(1)


def main():
    """
    Main sentinel
    """
    mem_to_eat = 1024
    eat_memory(mem_to_eat)
