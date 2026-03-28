import logging

## Logging Setting

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("ArthmeticApp")

def add(a,b):
    result = a+b
    logger.debug(f"Adding {a}+{b}= {result}")
    return result

def subtract(a,b):
    result = a-b
    logger.debug(f"Subtracting {a}-{b}= {result}")
    return result

def divide(a,b):
    try:
        result = a/b
        logger.debug(f"Dividing {a}/{b}= {result}")
        return result
    except Exception as e:
        logger.error("Division By Zero Error")
        print(e)
        return None

def multiply(a,b):
    result = a*b
    logger.debug(f"Multipling {a}*{b}= {result}")
    return result

def power(a,b):
    result = a**b
    logger.debug(f"{a} to the Power of {b}= {result}")
    return result


add(10,15)
subtract(15,10)
multiply(3,5)
divide(15,5)
power(5,2)
divide(12,0)
