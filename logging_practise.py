import logging
import os


def get_logger(log_path, log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    if os.path.isdir(log_path):
        if log_path[-1] != '/':
            log_path += '/'
        fh = logging.FileHandler(log_path + log_name + '.log')
        fh.setLevel(logging.DEBUG)
        ch = logging.StreamHandler()
        ch.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger
    else:
        return Exception('Path provided is incorrect')


def run():
    logger = get_logger(log_path='C:\Log', log_name='AdamZ_Log')
    logger.info('This is info message')
    logger.debug('This is debug message')



if __name__ == '__main__':
    run()