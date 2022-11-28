import logging

LOG_FORMAT = '%(levelname)s %(asctime)s - %(message)s'
    
# É gerado um arquivo para gravação de erros de execução
logging.basicConfig(filename='app.log', level = logging.DEBUG, filemode='w', format = LOG_FORMAT)
log = logging.getLogger()
log.info('Ola, info')
log.critical('Ola, erro critico')
log.error('Ola, erro')
log.debug('Ola, debug')
log.warning('Ola, warning')

log.level