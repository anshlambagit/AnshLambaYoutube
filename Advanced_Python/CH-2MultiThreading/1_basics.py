import threading
from concurrent.futures import ThreadPoolExecutor

def transformation(input):

    src = input['src']
    dest = input['dest']

    print(f"Reading from {src}")
    print(f"Transforming.....")
    print(f"Writing data to {dest}")
    return f"Done {src} to {dest}"

array = [
    {"src":"table-1","dest":"table-1"},
    {"src":"table-2","dest":"table-2"},
    {"src":"table-3","dest":"table-3"}
]

with ThreadPoolExecutor(max_workers=3) as executor: 

    my_futures = executor.map(transformation,array)

print(f"The returned values are {list(my_futures)}")