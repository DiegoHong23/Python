# Computer Shop
PROCESSORS = ['P3', 'P5', 'P7']
PRICE_OF_PROCESSORS = [100, 120, 200]
RAM = ['16', '32']
PRICE_OF_RAM = [75, 150]
STORAGE = ['1', '2']
PRICE_OF_STORAGE = [50,100]
SCREEN = ['19','23']
PRICE_OF_SCREEN = [65,120]
CASE = ['Mini Tower', 'Mid Tower']
PRICE_OF_CASE = [40,70]
USB_PORTS = ['2', '4']
PRICE_OF_PORTS = [10,20]
price = 0

while True:
    print('Which processor do you want?')
    print(PROCESSORS)
    processor = input()
    if processor in PROCESSORS:
        print("good choice")
        print(PRICE_OF_PROCESSORS[PROCESSORS.index(processor)])
        price += PRICE_OF_PROCESSORS[PROCESSORS.index(processor)]
        break
    else: 
        print('invalid')
        continue

while True:
    print('How much RAM do you want?')
    print(RAM)
    ram = input()
    if ram in RAM:
        print("good choice")
        print(PRICE_OF_RAM[RAM.index(ram)])
        price += PRICE_OF_RAM[RAM.index(ram)]
        break
    else: 
        print('invalid')
        continue

while True:
    print('How much storage do you want?')
    print(STORAGE)
    storage = input()
    if storage in STORAGE:
        print("good choice")
        print(PRICE_OF_STORAGE[STORAGE.index(storage)])
        price += PRICE_OF_STORAGE[STORAGE.index(storage)]
        break
    else: 
        print('invalid')
        continue

while True:
    print('Which screen do you want?')
    print(SCREEN)
    screen = input()
    if screen in SCREEN:
        print("good choice")
        print(PRICE_OF_SCREEN[SCREEN.index(screen)])
        price += PRICE_OF_SCREEN[SCREEN.index(screen)]
        break
    else: 
        print('invalid')
        continue
 

while True:
    print('Which case do you want do you want?')
    print(CASE)
    case = input()
    if case in CASE:
        print("good choice")
        print(PRICE_OF_CASE[CASE.index(case)])
        price += PRICE_OF_CASE[CASE.index(case)]
        break
    else: 
        print('invalid')
        continue

while True:
    print('How many ports do you want?')
    print(USB_PORTS)
    ports = input()
    if ports in USB_PORTS:
        print("good choice")
        print(PRICE_OF_PORTS[USB_PORTS.index(ports)])
        price += PRICE_OF_PORTS[USB_PORTS.index(ports)]
        break
    else: 
        print('invalid')
        continue

total_price = price + (price * 20/100)
print("The total price is", total_price)