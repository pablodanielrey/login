import os
import logging
from autobahn.asyncio.wamp import ApplicationRunner

from login.api.wamp import Login

import txaio
txaio.use_asyncio()
txaio.start_logging(level='debug')

def main():
    logging.info('Ejecuando loop')
    runner = ApplicationRunner(
        url=os.environ['CROSSBAR_URL'],
        realm=os.environ['CROSSBAR_REALM']
    )
    runner.run(Login)

if __name__ == '__main__':
    main()
