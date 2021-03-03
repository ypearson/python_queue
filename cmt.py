#!/usr/bin/env python3
from queue import Queue
from random import randint
import uuid

SZ=4
NUM_OF_QUEUES=4
DIRECTIONS=['D1','D2', 'D3', 'D4']

direction1 = Queue(maxsize=SZ)
direction2 = Queue(maxsize=SZ)
direction3 = Queue(maxsize=SZ)
direction4 = Queue(maxsize=SZ)

fourStopSigns = [direction1, direction2, direction3, direction4]

def getCarId():
    return str(uuid.uuid4())[:5]

def getCarDirection():
    return randint(1,4);

def carHasArrived(cardId, direction):
    '''
        Fill up the queues with car ID with each direction queue
    '''
    ret = 'ok'
    allFullCount = 0
    for i in range(0,len(fourStopSigns)):
        if fourStopSigns[i].full():
            allFullCount+=1
    if allFullCount == 4:
        ret = 'allFull'
    else:
        if direction == 1:
            if direction1.full():
                ret = 'full'
            else:
                print(f'Car #{cardId} has arrived, going direction 0')
                direction1.put(cardId)
        elif direction == 2:
            if direction2.full():
                ret = 'full'
            else:
                direction2.put(cardId)
                print(f'Car #{cardId} has arrived, going direction 1')
        elif direction == 3:
            if direction3.full():
                ret = 'full'
            else:
                direction3.put(cardId)
                print(f'Car #{cardId} has arrived, going direction 2')
        elif direction == 4:
            if direction4.full():
                ret = 'full'
            else:
                direction4.put(cardId)
                print(f'Car #{cardId} has arrived, going direction 3')
    return ret

def whoGoesNext():
    '''
        Check queue in turn [0->1->2->3] to see who can go next
        Don't stop until all queues are empty
    '''
    i = 0;
    allEmptyCount = 0
    allEmpty = False
    while not allEmpty:
        if not fourStopSigns[i].empty():
            car = fourStopSigns[i].get()
            print(f'Car #{car} going direction {i}')
        else:
            allEmptyCount+=1
        i+=1
        i=i%NUM_OF_QUEUES
        if allEmptyCount ==4:
            print(f'Queues are all empty')
            allEmpty = True

ret = ''
while ret != 'allFull':
    ret = carHasArrived(getCarId(), getCarDirection())
print(f'All queues full!')

whoGoesNext()
